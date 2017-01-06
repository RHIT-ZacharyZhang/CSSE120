"""
Stage 2: In addition to Stage 1, adds a Deck of Cards, as follows:

  -- The  play_hand()  method displays all the Cards in the Deck
       by using the Deck's  show_cards()  method.

  -- The Deck class now has:
       -- a  show_cards()  method that shows all the Cards
            currently in the Deck, in their current order.
       -- a data attribute (aka instance variable) that is a list that
            initially contains the 52 Cards in a standard deck of cards.

  -- There is a  Card  class that has:
       -- data attributes (aka instance variables) for the Card's:
            -- suit_number (1, 2, 3, or 4, for Spade, Heart, Diamond, Club)
            -- pip (1, 2, 3, ... 13, where 1 is Ace, ... 13 is King)
       -- a  __repr__()   method that prints the Card in a reasonable way.

You can test the above by running the program.
Implementing the above should cause the program to display on the console:
  Playing a hand:
  Spade A
  Spade 2
  Spade 3
    ...
  Club Q
  Club K
"""


class Card(object):
    suits = [None, 'Spade', 'Heart', 'Diamond', 'Club']
    pips = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'J', 'Q', 'K']

    def __init__(self, suit, pip):
        self.suit_number = suit
        self.pip_number = pip

    def __repr__(self):
        return Card.suits[self.suit_number] + ' ' + Card.pips[self.pip_number]


class Deck(object):
    def __init__(self):
        self.cards = []
        # Suits are numbered 1 to 4 (and 0 is unused)
        #    for Spade, Heart, Diamond, Club.
        # Cards are numbered 1 to 13 (and 0 is unused)
        #    where 1 is Ace, ... 12 is Queen, 13 is King.
        for j in range(1, 5):
            for k in range(1, 14):
                self.cards.append(Card(j, k))

    def show_cards(self):
        print('The deck currently is:')
        for k in range(len(self.cards)):
            print(self.cards[k])


class Dealer(object):
    pass


class HumanPlayer(object):
    pass


class Blackjack(object):
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.human = HumanPlayer()

    def play_hand(self):
        print('Playing a hand:')
        self.deck.show_cards()  # for testing


def main():
    """ Constructs a Blackjack object and plays a hand """
    game = Blackjack()
    game.play_hand()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
