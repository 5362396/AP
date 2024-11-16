import os


def main():
    print('Głowa i ogon bieżącego katalogu:')
    print(os.path.split(os.getcwd()))

    print('\tKorzeń oraz rozszerzenie ścieżki ../app-2024-w5.pdf')
    print(os.path.splitext('app-2024-w5.pdf'))

    print('\tŚcieżka bezwzględna dla katalogu bieżącego:')
    print(os.path.abspath('.'))

    print('\tŚcieżka bezwzględna dla katalogu nadrzędnego:')
    print(os.path.abspath('..'))


if __name__ == '__main__':
    main()
