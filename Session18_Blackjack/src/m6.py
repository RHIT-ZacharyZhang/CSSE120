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

# Copy your Stage 5 work from m5 into this file.
# Then implement this BY FOLLOWING ALONG IN THE VIDEO.
