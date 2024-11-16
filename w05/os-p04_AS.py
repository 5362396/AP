import os
import sys
import time


def main():
    # Jeżeli nie podano pliku, to używamy pliku źródłowego niniejszego programu
    if len(sys.argv) == 1:
        pliki = [__file__]
    else:
        pliki = sys.argv[1:]

    for nazwa_pliku in pliki:
        if not os.path.exists(nazwa_pliku):
            print('Plik nie istnieje!')
            continue

        stat_info = os.stat(nazwa_pliku)

        print(f'os.stat({nazwa_pliku})')
        print(f'\tRozmiar: {stat_info.st_size}')
        print(f'\tUprawnienia: {oct(stat_info.st_mode)}')
        print(f'\tWłaściciel: użytkownik o numerze uid = {stat_info.st_uid}')
        print(f'\tUrządzenie: {stat_info.st_dev}')
        print(f'\tOstatnio modyfikowany: {time.ctime(stat_info.st_mtime)}')


if __name__ == '__main__':
    main()
