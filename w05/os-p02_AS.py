import os
import sys


def main():
    if len(sys.argv) < 2:
        print('Użycie: python3 os-p02_AS.py plik1 plik2 ...')
        sys.exit(1)

    for filepath in sys.argv[1:]:
        if not os.path.exists(filepath):
            print('Plik nie istnieje!')
            continue

        print('Testowanie pliku', filepath)
        print('Plik istnieje:', os.access(filepath, os.F_OK))
        print('Plik można czytać:', os.access(filepath, os.R_OK))
        print('Plik jest zapisywalny:', os.access(filepath, os.W_OK))
        print('Plik jest wykonywalny:', os.access(filepath, os.X_OK))


if __name__ == '__main__':
    main()
