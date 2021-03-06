"""
Stage 4: In addition to Stages 1 through 3, deals the initial cards
         to the players, as follows:

  -- After the   play_hand()  method does all that it did from the
     previous stages, it now asks the Dealer to deal the two initial
     cards to all of the players (i.e., to both the HumanPlayer
     and the Dealer).  (See details of this  deal()  method below.)

  -- The Dealer class now has:
       -- a  deal(...)   method that takes a list of Players
          and deals 2 cards to each Player by doing the following
          twice for each player in the list:
            -- Deal the top Card from the Deck.  (See details below.)
            -- Tell the player to take the Card.  (See details below.)

  -- The Deck class now has:
      -- a  deal_top_card()  method that removes the top Card from
           the Deck and returns that Card.

  -- The HumanPlayer class now has:
       -- a data attribute (aka instance variable) that is a Hand
            that will contain the player's cards as the player gets them.
       -- a  take_card(Card)  method that takes a Card as its sole argument
            and (at this stage) simply PRINTs that Card on the console.

  -- The Dealer class likewise has a Hand and a   take_card(Card)  method
           that (at this stage) simply PRINTs that Card on the console.

  -- There is a  Hand  class that (at this stage) does nothing.

NOTE: Do you notice some DUPLICATION in the above?
      We will REFACTOR to eliminate it in the NEXT stage.

You can test the above by running the program.
Implementing the above should cause the program to display on the console:
  Playing a hand:
  [The UN-shuffled deck, as per previous stages]
  [The SHUFFLED deck, as per previous stages]
  The top 4 cards from the shuffled Deck, one by one.
  The shuffled deck MINUS the 4 cards that were dealt.
    -- NOTE:  Add a
          self.deck.show_cards()  # for testing
       at the bottom of  play_hand()
       to get this 3rd listing of the Cards in the Deck.
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
    pass


class Dealer(object):
    def __init__(self, deck):
        self.deck = deck
        self.hand = Hand()

    def shuffle(self):
        random.shuffle(self.deck.cards)

    def deal(self, players):
        for _ in range(2):
            for k in range(len(players)):
                card = self.deck.deal_top_card()
                players[k].take_card(card)

    def take_card(self, card):
        print('Card is', card)  # stub, for testing


class HumanPlayer(object):
    def __init__(self):
        self.hand = Hand()

    def take_card(self, card):
        print('Card is', card)  # stub, for testing


class Blackjack(object):
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.human = HumanPlayer()
        self.players = [self.human, self.dealer]

    def play_hand(self):
        print('Playing a hand:')
        self.deck.show_cards()  # for testing

        self.dealer.shuffle()
        self.deck.show_cards()  # for testing

        self.dealer.deal(self.players)
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
