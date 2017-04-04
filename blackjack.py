class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):

        self.suit = ['Heart','Spade','Diamond','Club']
        self.rank = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        self.deck = []

    def generate(self):

        for i in self.suit:
            for p in self.rank:
                self.deck.append(Card(i,p))

    def print_deck(self):
        for i in self.deck:
            print(i)