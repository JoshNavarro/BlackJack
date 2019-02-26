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

    def adjust_for_ace(self):
    	'''
    	Adjust player's value if an ace is in there hand
    	'''
        self.aces += 1
        self.value -= 10

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

def show_all(player,dealer):
    pass

def main():
    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    player1.add_card(deck.deal())
    player1.add_card(deck.deal())
    print('Player1 hand: ' + ','.join(map(str,player1.cards)))
    print('Player1 value: ' + str(player1.value))

if __name__ == '__main__':
	main()