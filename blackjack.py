import random

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    '''
    A class to hold the suit and rank of a given card
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    '''
    A class to hold 52 card objects to create a standard deck of cards
    '''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        return ','.join(map(str,self.deck))

    def shuffle(self):
        '''
        Shuffle the current deck of cards
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        Deal one card out from top of deck (index 0)
        '''
        return self.deck.pop(0)

class Hand():
    '''
    A class to hold each player's cards in hand
    '''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        '''
        Add a single card to the players hand
        '''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        '''
        Adjust player's value if an ace is in there hand
        '''
        self.value -= 10
        self.aces -= 1

class Chips():
    '''
    A class to acount for a player's starting chips, bets, and ongoing winnings
    '''
    def __init__(self):
        self.total = 100 # Change this value for starting value or take a user input
        self.bet = 0

    def win_bet(self):
        '''
        Adjust player total chips if bet is one
        '''
        self.total += self.bet

    def lose_bet(self):
        '''
        Adjust player total chips if bet is lost
        '''
        self.total -= self.bet

def take_bet(player_chips):
    '''
    Ask the user for a bet
    Input: Players chips
    Output: Bet amount
    '''
    # Check to see if user input is a number
    while True:
        try:
            bet = int(input("Place your bet: "))
        except:
            print("Please enter a number.")
            continue
        else:
            # Check that player total does not exceed bet amount
            if bet > player_chips.total:
                print(f"Amount cannot be covered. Total chips: {player_chips.total}")
                continue
            else:
                print(f'Bet accepted.')
                break
    return bet
    
def hit(deck,hand):
    '''
    Add card to player/dealer hand
    Input: current deck and player hand
    '''
    # Deal one card off the deck
    card = deck.deal()
    # Add card to hand
    hand.add_card(card)
    # Check if card was an Ace
    if hand.aces > 0 and hand.value > 21:
        hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    '''
    Ask player if they want to hit or stand
    '''
    global playing

    while True:
        try:
            choice = int(input("Hit (1) or Stand (2): "))
        except:
            continue
        else:
            if choice not in (1,2):
                continue
            else:
                break
    if choice == 1:
        hit(deck, hand)
    else:
        playing = False

def show_some(player, dealer):
    pass

def show_all(player,dealer):
    pass

def main():
    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    
    hit(deck, player1)
    hit(deck, player1)
    hit(deck, player1)
    hit(deck, player1)
    print('Player1 hand: ' + ','.join(map(str,player1.cards)))
    print('Player1 value: ' + str(player1.value))
'''
    player1_chips = Chips()
    bet = take_bet(player1_chips)
'''
if __name__ == '__main__':
	main()