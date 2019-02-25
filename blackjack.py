import random

suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
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

    def __init__