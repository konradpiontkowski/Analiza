from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class KonfiguracjaBoiska:
    szerokosc: int = 7000  # [cm]
    dlugosc: int = 12000  # [cm]
    szerokosc_pola_karnego: int = 4100  # [cm]
    dlugosc_pola_karnego: int = 2015  # [cm]
    szerokosc_bramki: int = 1832  # [cm]
    dlugosc_bramki: int = 550  # [cm]
    promien_kola_centrowego: int = 915  # [cm]
    odleglosc_od_punktu_karnego: int = 1100  # [cm]

    @property
    def wierzcholki(self) -> List[Tuple[int, int]]:
        return [
            (0, 0),  # 1
            (0, (self.szerokosc - self.szerokosc_pola_karnego) / 2),  # 2
            (0, (self.szerokosc - self.szerokosc_bramki) / 2),  # 3
            (0, (self.szerokosc + self.szerokosc_bramki) / 2),  # 4
            (0, (self.szerokosc + self.szerokosc_pola_karnego) / 2),  # 5
            (0, self.szerokosc),  # 6
            (self.dlugosc_bramki, (self.szerokosc - self.szerokosc_bramki) / 2),  # 7
            (self.dlugosc_bramki, (self.szerokosc + self.szerokosc_bramki) / 2),  # 8
            (self.odleglosc_od_punktu_karnego, self.szerokosc / 2),  # 9
            (self.dlugosc_pola_karnego, (self.szerokosc - self.szerokosc_pola_karnego) / 2),  # 10
            (self.dlugosc_pola_karnego, (self.szerokosc - self.szerokosc_bramki) / 2),  # 11
            (self.dlugosc_pola_karnego, (self.szerokosc + self.szerokosc_bramki) / 2),  # 12
            (self.dlugosc_pola_karnego, (self.szerokosc + self.szerokosc_pola_karnego) / 2),  # 13
            (self.dlugosc / 2, 0),  # 14
            (self.dlugosc / 2, self.szerokosc / 2 - self.promien_kola_centrowego),  # 15
            (self.dlugosc / 2, self.szerokosc / 2 + self.promien_kola_centrowego),  # 16
            (self.dlugosc / 2, self.szerokosc),  # 17
            (
                self.dlugosc - self.dlugosc_pola_karnego,
                (self.szerokosc - self.szerokosc_pola_karnego) / 2
            ),  # 18
            (
                self.dlugosc - self.dlugosc_pola_karnego,
                (self.szerokosc - self.szerokosc_bramki) / 2
            ),  # 19
            (
                self.dlugosc - self.dlugosc_pola_karnego,
                (self.szerokosc + self.szerokosc_bramki) / 2
            ),  # 20
            (
                self.dlugosc - self.dlugosc_pola_karnego,
                (self.szerokosc + self.szerokosc_pola_karnego) / 2
            ),  # 21
            (self.dlugosc - self.odleglosc_od_punktu_karnego, self.szerokosc / 2),  # 22
            (
                self.dlugosc - self.dlugosc_bramki,
                (self.szerokosc - self.szerokosc_bramki) / 2
            ),  # 23
            (
                self.dlugosc - self.dlugosc_bramki,
                (self.szerokosc + self.szerokosc_bramki) / 2
            ),  # 24
            (self.dlugosc, 0),  # 25
            (self.dlugosc, (self.szerokosc - self.szerokosc_pola_karnego) / 2),  # 26
            (self.dlugosc, (self.szerokosc - self.szerokosc_bramki) / 2),  # 27
            (self.dlugosc, (self.szerokosc + self.szerokosc_bramki) / 2),  # 28
            (self.dlugosc, (self.szerokosc + self.szerokosc_pola_karnego) / 2),  # 29
            (self.dlugosc, self.szerokosc),  # 30
            (self.dlugosc / 2 - self.promien_kola_centrowego, self.szerokosc / 2),  # 31
            (self.dlugosc / 2 + self.promien_kola_centrowego, self.szerokosc / 2),  # 32
        ]

    krawedzie: List[Tuple[int, int]] = field(default_factory=lambda: [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (7, 8),
        (10, 11), (11, 12), (12, 13), (14, 15), (15, 16),
        (16, 17), (18, 19), (19, 20), (20, 21), (23, 24),
        (25, 26), (26, 27), (27, 28), (28, 29), (29, 30),
        (1, 14), (2, 10), (3, 7), (4, 8), (5, 13), (6, 17),
        (14, 25), (18, 26), (23, 27), (24, 28), (21, 29), (17, 30)
    ])

    etykiety: List[str] = field(default_factory=lambda: [
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
        "11", "12", "13", "15", "16", "17", "18", "20", "21", "22",
        "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
        "14", "19"
    ])

    kolory: List[str] = field(default_factory=lambda: [
        "#FF1493", "#FF1493", "#FF1493", "#FF1493", "#FF1493", "#FF1493",
        "#FF1493", "#FF1493", "#FF1493", "#FF1493", "#FF1493", "#FF1493",
        "#FF1493", "#00BFFF", "#00BFFF", "#00BFFF", "#00BFFF", "#FF6347",
        "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347",
        "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347", "#FF6347",
        "#00BFFF", "#00BFFF"
    ])
