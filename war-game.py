class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.suit} {self.value}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["hearts", "diamonds", "spades", "clubs"] 
        for suit in suits:
            for value in range(1, 15):
                card = Card(suit, value)
                self.cards.append(card)
    
    def __str__(self):
        return f"{self.cards}"

def main():
    deck = Deck()
    

if __name__ == "__main__":
    main()