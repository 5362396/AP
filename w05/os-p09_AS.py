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

# (.venv) PS C:\Users\Arek\PycharmProjects\AP\w05> python os-p09_AS.py
# Głowa i ogon bieżącego katalogu:
# ('C:\\Users\\Arek\\PycharmProjects\\AP', 'w05')
#         Korzeń oraz rozszerzenie ścieżki ../app-2024-w5.pdf
# ('app-2024-w5', '.pdf')
#         Ścieżka bezwzględna dla katalogu bieżącego:
# C:\Users\Arek\PycharmProjects\AP\w05
#         Ścieżka bezwzględna dla katalogu nadrzędnego:
# C:\Users\Arek\PycharmProjects\AP
