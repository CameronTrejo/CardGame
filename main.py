
from Card import Card
from Minion import Minion

def main():
    acornBearer = Minion('Acorn Bearer', 1, 2, 1)
    sigilOfSilence = Card('Sigil of Silence', 0)

    acornBearer.printCard()
    sigilOfSilence.printCard()


if __name__ == '__main__':
    main()