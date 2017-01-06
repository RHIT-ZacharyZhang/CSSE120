"""
Stage 5: REFACTOR Stage 4 to eliminate the DUPLICATION
         in the Dealer and HumanPlayer classes, as follows:

  -- There is now a  Player  class.

  -- Both the  Dealer  and  HumanPlayer  classes extend
       (aka inherit from) the Player class.

  -- The  Hand  data attribute that was in both the Dealer
       and HumanPlayer classes is now in the  Player  class.

  -- Likewise, the  take_card(Card)  method that was in both the Dealer
       and HumanPlayer classes is now in the  Player  class.

  -- The constructor (__init__) methods for the Dealer and
       HumanPlayer call the constructor method for the Player class.

You can test the above by running the program.
It should print the same as it did in the previous stage.
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


class Player(object):
    def __init__(self):
        self.hand = Hand()

    def take_card(self, card):
        print(type(self))  # for testing
        print('Card is', card)  # stub, for testing


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
