import os

miesiace = {
    'wiosna': ['marzec', 'kwiecień', 'maj'],
    'lato': ['czerwiec', 'lipiec', 'sierpień'],
    'jesien': ['wrzesień', 'październik', 'listopad'],
    'zima': ['grudzień', 'styczeń', 'luty']
}

for pora, nazwy in miesiace.items():
    os.makedirs(f'PoryRoku/{pora}', exist_ok=True)
    for miesiac in nazwy:
        os.makedirs(f'PoryRoku/{pora}/{miesiac}', exist_ok=True)

os.chmod('PoryRoku', 0o700)
