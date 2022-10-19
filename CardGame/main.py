import random


class Rank:
    def __init__(self, rank):
        self.curr_rank = rank


class Suit:
    def __init__(self, suit):
        self.curr_suit = suit


class Card:
    def __init__(self, card_rank, card_suit):
        self.card_rank = Rank(card_rank)
        self.card_suit = Suit(card_suit)

    def __str__(self):
        return 'Card: {}, {}'.format(self.card_rank.curr_rank, self.card_suit.curr_suit)


class Set:
    card_set = None

    def __init__(self):
        self.card_set = []

        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for rank in ranks:

                new_card = Card(suit, rank)
                self.add(new_card)
                print("Created: {} of {}".format(rank, suit))

    def print_self(self):

        for card_set in self.card_set:
            print(card_set)

    def add(self, card_set):
        self.card_set.append(card_set)

    def shuffle(self):
        random.shuffle(self.card_set)

    def get_card(self):
        self.card_set.pop()


set = Set()
set.print_self()
set.shuffle()
set.print_self()
print("\n")
set.get_card()
set.print_self()
