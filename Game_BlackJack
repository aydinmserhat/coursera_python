# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        handstr = "Hand Contains"
        for card in self.hand:
            handstr += str(CARD)
        return handstr# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        handvalue = 0
        aces = 0
        for card in self.hand:
            if card.get_rank() == 'A':
                aces += 1
            handvalue += VALUES[card.get_rank()]
        if aces > 0 and (handvalue + 10) <= 21:
            handvalue += 10
        return handvalue    
                
          
    def draw(self, canvas, pos):
        for i in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(i.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(i.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + 73 * self.hand.index(i), pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [] # create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(str(suit),str(rank)))
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        self.card = self.deck[0]
        self.deck.remove(self.card)
        return self.card
    
    def __str__(self):
        # return a string representing the deck
        deckcard = ""
        for cards in self.deck :
            deckcard += str(cards)
        return deckcard    
        
#define event handlers for buttons
def deal():
    global outcome, in_play,  score, player_hand, dealer_hand, my_deck 
    if in_play == True: 
        score = score - 1
    player_hand = Hand()
    dealer_hand = Hand()
    my_deck = Deck()
    my_deck.shuffle()
    player_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card()) 
    outcome = "Hit or Stand ?"
    in_play = True

    # your code goes here

def hit():
    global score, outcome, in_play
    if in_play :
        player_hand.add_card(my_deck.deal_card()) # replace with your code below
        if player_hand.get_value() > 21 :
            outcome = "You Busted !!. New Deal ? "
            score = score - 1
            in_play = False
            return score, outcome, in_play
        else : 
            outcome = "Hit or Stand ?"
        
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, score, in_play
    if in_play :
        if player_hand.get_value() > 21 :
            score = score - 1
            in_play = False
            outcome = "You Busted !!. New Deal ?"
            return score, in_play, outcome # replace with your code below
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(my_deck.deal_card())
            else :
                if dealer_hand.get_value() > 21 :
                    outcome = "Dealer Busted, YOU WIN"
                    score = score + 1
                elif dealer_hand.get_value() >= player_hand.get_value():
                    outcome = "Dealer Win, New Deal ?"
                    score = score - 1
                else :
                    outcome = "**YOU WIN** , New Deal ?"
                    score = score + 1
                    return score, outcome, in_play
        in_play = False
                
                
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas, [0, 100])    
    player_hand.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE)    
    canvas.draw_text(outcome,[50,75],20,"Black")
    canvas.draw_text("Score: "+str(score),[50,50],20,"Black")
    canvas.draw_text("BlackJack",[250,50],35,"Black")
    
    
    # test to make sure that card.draw works, replace with your code below

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
