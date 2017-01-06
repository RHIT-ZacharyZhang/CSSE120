"""
Stage 3: In addition to Stages 1 and 2, shuffles the Deck, as follows:

  -- After the   play_hand()  method displays all the (unshuffled) Cards
       on the console (per Stage 2), the  play_hand()  method then
       asks the Dealer to shuffle the Deck.  Then, just for testing,
       the  play_hand() method again displays all the Cards (now shuffled).

  -- The Dealer class now has:
       -- a  shuffle()  method that shuffles the Deck.
            Note:  The  random  class has a  shuffle()  method
            that can shuffle any LIST.  That is,
               random.shuffle(  BLAH )
            will shuffle BLAH as long as BLAH is a LIST.
       -- a data attribute (aka instance variable) for the Deck
            that the Blackjack object constructed.

You can test the above by running the program.
Implementing the above should cause the program to display on the console:
  Playing a hand:
  Spade A
  Spade 2
  Spade 3
    ...
  Club Q
  Club K
    And then the same 52 cards, but in a random order.
"""

import random


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
    def __init__(self, deck):
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck.cards)


class HumanPlayer(object):
    pass


class Blackjack(object):
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.human = HumanPlayer()

    def play_hand(self):
        print('Playing a hand:')
        self.deck.show_cards()  # for testing

        self.dealer.shuffle()
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
