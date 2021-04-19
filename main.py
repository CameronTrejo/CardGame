
from Card import Card
from Minion import Minion

def main():
    
    deck = []
    
    acornBearer = Minion('Acorn Bearer', 1, 2, 1)
    deck.append(acornBearer)

    sigilOfSilence = Card('Sigil of Silence', 0)
    deck.append(sigilOfSilence)

    imprisonedFelmaw = Minion('Imprisoned Felmaw', 2, 5, 4)
    deck.append(imprisonedFelmaw)

    nagrandSlam = Card('Nagrand Slam', 10)
    deck.append(nagrandSlam)
    
    for card in deck:
        card.printCard()
        print('\n')

if __name__ == '__main__':
    main()