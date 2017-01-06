"""
Stage 1: Begins the game, as follows:

  -- main:
       -- constructs a Blackjack object and
       -- asks the Blackjack object to play a hand.

  -- There is a  Blackjack   class that has:
       -- a  play_hand()   method that (at this stage)
            simply prints "Playing a hand:"
       -- 3 data attributes (aka instance variables) that are a:
            -- Deck
            -- Dealer
            -- HumanPlayer
          where Deck, Dealer and HumanPlayer are each a class
          that (in this stage) does nothing.

You can test the above by running the program.
Implementing the above should cause the program to display on the console:
  Playing a hand:
"""


class Deck(object):
    pass


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
