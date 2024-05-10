import random, os

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self._value = value
        type = ""
        if value == 14:
            type = "Ace"
        elif value == 13:
            type = "King"
        elif value == 12:
            type = "Queen"
        elif value == 11:
            type = "Jack"
        else:
            type = str(self._value)
        self.name = type + " of " + self.suit
    
    @property
    def value(self):
        return self._value
    
    def __repr__(self):
        return f"{self.suit} {self._value}"
    
    def __str__(self):
        return f"{self.name}"

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
        cards_for_one_player = len(self.cards) // 2
        self.deck1 = self.cards[:cards_for_one_player]
        self.deck2 = self.cards[cards_for_one_player:]
        return self.deck1, self.deck2

    def __str__(self):
        return f"{self.cards}"

class Player:
    def __init__(self):
        self.deck = []
        self.has_lost = False

class Game:
    def __init__(self, deck):
        self.player1 = Player()
        self.player2 = Player()
        deck.split_deck()
        self.player1.deck, self.player2.deck = deck.split_deck()

    def fight(self):
        while not self.player1.has_lost and not self.player2.has_lost:
            card1 = self.player1.deck[0].value
            card2 = self.player2.deck[0].value
            if card1 > card2:
                self.player1.deck.append(card2)
                self.player2.deck.pop(0)

    def show_deck(self):
        clear()
        print("Your deck is: ")
        for card in self.player2.deck:
            print(card)
            

def main():
    deck = Deck()
    deck.shuffle_deck()
    game = Game(deck)
    if input("Start the game? "):
        game.show_deck()
        game.fight()

def clear():
    os.system('clear' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    main()