import random

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
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def split_deck(self):
        print(self.cards)
        cards_for_one_player = len(self.cards) // 2
        deck1 = self.cards[:cards_for_one_player]
        deck2 = self.cards[cards_for_one_player:]
        return deck1, deck2

    def __str__(self):
        return f"{self.cards}"

class Player:
    def __init__(self):
        self.deck = []
        has_lost = False

class Game:
    def __init__(self, deck):
        self.player1 = Player()
        self.player2 = Player()
        self.player1.deck, self.player2.deck = deck.split_deck()
        print(self.player1.deck, self.player2.deck)

def main():
    deck = Deck()
    deck.shuffle_deck()
    game = Game(deck)

    

    

if __name__ == "__main__":
    main()