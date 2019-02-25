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
        pass

    def adjust_for_ace(self):
        pass

def main():
    deck = Deck()
    print(deck)
    deck.shuffle()
    print("\n\nDeck has been shuffled\n")
    print(deck)
    print(deck.deal())
    print(deck)

if __name__ == '__main__':
	main()