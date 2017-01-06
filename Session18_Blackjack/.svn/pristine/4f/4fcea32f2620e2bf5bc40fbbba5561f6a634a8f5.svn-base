"""
Stage 6: Enhance the Player and Hand classes so that the
         Hand really contains the Card that the Player receives
         from the Dealer, as follows:

  -- After the  play_hand()  method causes the cards to be dealt,
       it calls a   show_hands()  method that (at this stage) prints
       the Hand for the Dealer and the Hand for the HumanPlayer.

  -- The Hand class now has:
       -- a data attribute that will be a list of Cards in the Hand.
            (When a Hand is constructed, this list is initialized
            to the empty list.)
       -- a  __repr__()   method that prints the Hand in a reasonable way.

  -- The Player class'  take_card(Card)  method no longer prints the Card.
       Instead, it appends the Card to the list of Cards
       in the Player's Hand.

You can test the above by running the program.
If you wish, you can comment-out some or all of the Deck-printing
from previous stages.  In any case, the last thing printed should be:
  -- the HumanPlayer's Hand
  -- the Dealer's Hand
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

    def deal_top_card(self):
        card = self.cards[0]
        del self.cards[0]
        return card


class Hand(object):
    def __init__(self):
        self.cards = []

    def __repr__(self):
        s = 'Hand:'
        for k in range(len(self.cards)):
            s = s + ' ' + str(self.cards[k])
        return s


class Player(object):
    def __init__(self):
        self.hand = Hand()

    def take_card(self, card):
        self.hand.cards.append(card)
#         print(type(self))  # for testing
#         print('Card is', card)  # stub, for testing


class Dealer(Player):
    def __init__(self, deck):
        super().__init__()
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck.cards)

    def deal(self, players):
        for _ in range(2):
            for k in range(len(players)):
                card = self.deck.deal_top_card()
                players[k].take_card(card)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()


class Blackjack(object):
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.human = HumanPlayer()
        self.players = [self.human, self.dealer]

    def show_hands(self):
        for k in range(len(self.players)):
            print(type(self.players[k]))  # for testing
            print(self.players[k].hand)

    def play_hand(self):
        print('Playing a hand:')
        self.deck.show_cards()  # for testing

        self.dealer.shuffle()
        self.deck.show_cards()  # for testing

        self.dealer.deal(self.players)
        self.deck.show_cards()  # for testing

        self.show_hands()


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
