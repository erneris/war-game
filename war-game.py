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
        self.name = type + " of " + self.suit.capitalize()
    
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

    def war(self):
        cards = []

        while self.player1.deck[0].value == self.player2.deck[0].value:
            card1 = self.player1.deck[0]
            card2 = self.player2.deck[0]
            print(f"Your card {card1} is equal to opponents {card2}, war continues")
            cards.append(card1)
            cards.append(card2)
            self.player2.deck.pop(0)
            self.player1.deck.pop(0)
            self.prompt()


        card1 = self.player1.deck[0]
        card2 = self.player2.deck[0]
        print(f"Your card is {card1.name}")
        print(f"Your opponents card is {card2.name}")

        if card1.value > card2.value:
            for card in cards:
                self.player1.deck.append(card)
            print("You take all of the cards cards and put them to the back of your deck")
            self.prompt()
            self.fight()

        else:
            for card in cards:
                self.player2.deck.append(card)
            print("Your opponent takes all of the cards and puts them to the back of his deck")
            self.prompt()
            self.fight()        

    def fight(self):
        while not self.player1.has_lost and not self.player2.has_lost:
            card1 = self.player1.deck[0]
            card2 = self.player2.deck[0]

            print(f"Your card is {card1.name}")
            print(f"Your opponents card is {card2.name}")

            if card1.value > card2.value:
                print("You take his card and put it to the back of your deck")
                self.player1.deck.append(card2)
                self.player1.deck.append(card1)
                self.player2.deck.pop(0)
                self.player1.deck.pop(0)
                print(f"You have {len(self.player1.deck)} cards left in your deck")
                self.prompt()

            elif card1.value < card2.value:
                print("Your opponent takes your card and puts it to the back of his deck")
                self.player2.deck.append(card1)
                self.player2.deck.append(card2)
                self.player1.deck.pop(0)
                self.player2.deck.pop(0)
                print(f"You have {len(self.player1.deck)} cards left in your deck")
                self.prompt()

            else:
                print("Cards are equal, war starts")
                self.prompt()
                self.war()
            
            if len(self.player1.deck) <= 0:
                self.player1.has_lost = True
            elif len(self.player2.deck) <= 0:
                self.player1.has_lost = True
    
    def prompt(self):
        while True:
            if isinstance(input("Press Enter to continue: "), str):
                clear()
                break

def main():
    clear()
    deck = Deck()
    deck.shuffle_deck()
    game = Game(deck)
    if isinstance(input("Start the game? "), str):
        clear()
        game.fight()

def clear():
    os.system('clear' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    main()