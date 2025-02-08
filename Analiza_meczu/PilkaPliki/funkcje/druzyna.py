from typing import Generator, Iterable, List, TypeVar

import numpy as np
import supervision as sv
import torch
import umap
from sklearn.cluster import KMeans
from tqdm import tqdm
from transformers import AutoProcessor, SiglipVisionModel

V = TypeVar("V")

SCIEZKA_MODELU_SIGLIP = 'google/siglip-base-patch16-224'


def stworz_paczki(
    sekwencja: Iterable[V], rozmiar_paczki: int
) -> Generator[List[V], None, None]:
    rozmiar_paczki = max(rozmiar_paczki, 1)
    aktualna_paczka = []
    for element in sekwencja:
        if len(aktualna_paczka) == rozmiar_paczki:
            yield aktualna_paczka
            aktualna_paczka = []
        aktualna_paczka.append(element)
    if aktualna_paczka:
        yield aktualna_paczka


class KlasyfikatorDruzyn:
    def __init__(self, urzadzenie: str = 'cpu', rozmiar_paczki: int = 32):
        self.urzadzenie = urzadzenie
        self.rozmiar_paczki = rozmiar_paczki
        self.model_cech = SiglipVisionModel.from_pretrained(
            SCIEZKA_MODELU_SIGLIP).to(urzadzenie)
        self.procesor = AutoProcessor.from_pretrained(SCIEZKA_MODELU_SIGLIP)
        self.reducer = umap.UMAP(n_components=3)
        self.model_klastrujacy = KMeans(n_clusters=2)

    def wyodrebnij_cechy(self, przycinki: List[np.ndarray]) -> np.ndarray:
        przycinki = [sv.cv2_to_pillow(przycinek) for przycinek in przycinki]
        paczki = stworz_paczki(przycinki, self.rozmiar_paczki)
        dane = []
        with torch.no_grad():
            for paczka in tqdm(paczki, desc='Ekstrakcja osadzeń'):
                wektory = self.procesor(
                    images=paczka, return_tensors="pt").to(self.urzadzenie)
                wyniki = self.model_cech(**wektory)
                osadzenia = torch.mean(wyniki.last_hidden_state, dim=1).cpu().numpy()
                dane.append(osadzenia)

        return np.concatenate(dane)

    def dopasuj(self, przycinki: List[np.ndarray]) -> None:
        dane = self.wyodrebnij_cechy(przycinki)
        projekcje = self.reducer.fit_transform(dane)
        self.model_klastrujacy.fit(projekcje)

    def przewiduj(self, przycinki: List[np.ndarray]) -> np.ndarray:
        if len(przycinki) == 0:
            return np.array([])

        dane = self.wyodrebnij_cechy(przycinki)
        projekcje = self.reducer.transform(dane)
        return self.model_klastrujacy.predict(projekcje)
