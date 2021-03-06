# Creator   : Joshua Navarro
# Date      : 03/7/2019

'''
This is a simple text-based game version of blackjack with betting
'''
import random

# global variables to help create a deck of cards
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

    def change_bet(self,bet):
        '''
        Adjust mutable bet amount
        '''
        self.bet = bet

def take_bet(player_chips):
    '''
    Ask the user for a bet
    Input: Players chips
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
                player_chips.change_bet(bet)
                print(f'Bet accepted.\n')
                break
    
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
    '''
    Display player's hand and dealer hand minus first card
    '''
    print('Dealer hand: ????????, ' + ','.join(map(str,dealer.cards[1:])))
    print('Player hand: ' + ','.join(map(str,player.cards)) + '\n')

def show_all(player,dealer):
    '''
    Display player's and dealer's hands
    '''
    print('Dealer hand: ' + ','.join(map(str,dealer.cards)))
    print('Player hand: ' + ','.join(map(str,player.cards)) + '\n')

def player_busts(player_chips):
    '''
    Player loses chips due to bust
    '''
    player_chips.lose_bet()
    print("Player has busted.\n")

def player_wins(player_chips):
    '''
    Player wins bet
    '''
    player_chips.win_bet()
    print('Player has won!\n')

def dealer_busts():
    '''
    Dealer hand over 21
    '''
    print("Dealer busts.\n")

def dealer_wins(player_chips):
    '''
    Dealer hand better than player hand
    '''
    player_chips.lose_bet()
    print("Dealer has won.\n")

def push():
    '''
    Tie game
    '''
    print("Push.\n")

def replay(player_chips):
    '''
    Ask player if they want to play again if possible
    '''
    if player_chips.total <= 0:
        return False
    while True:
        replay = input("Would you like to play again? Enter Yes or No: ")
        if replay[0].lower() == "y" or replay[0].lower() == "n":
            break
    return replay[0].lower() == 'y'

def main():
    '''
    Full game running with logic
    '''
    # Set up the Player's chips
    player_chips = Chips()
    global playing

    # Print an opening statement
    print("\nWelcome to BlackJack! Goodluck and have fun!\n")

    # Start the game
    while True:
        playing = True
        # Create a deck and shuffle it, player hand, and dealer hand
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        
        # Deal out 2 cards to player and dealer
        hit(deck, player)
        hit(deck, dealer)
        hit(deck, player)
        hit(deck, dealer)

        # Ask the player to bet
        print(f"Player chips: {player_chips.total}")
        take_bet(player_chips)

        # Show cards but not all
        show_some(player, dealer)

        # Start playing blackjack
        while playing:
            # Ask player to hit or stand
            hit_or_stand(deck, player)

            # Show cards but not all
            show_some(player, dealer)

            # If player has busted break out of loop
            if player.value > 21:
                break

        # If player hasn't busted, deal dealer cards until reaches 17
        if player.value <= 21:
            while dealer.value < 17:
                hit(deck, dealer)

            # Show player final cards
            show_all(player, dealer)

            # Play winning scenarios based on final cards
            if dealer.value > 21:
                dealer_busts()
                player_wins(player_chips)
            elif player.value > dealer.value:
                player_wins(player_chips)
            elif player.value == dealer.value:
                push()
            else:
                dealer_wins(player_chips)
        else:
            show_all(player, dealer)
            player_busts(player_chips)

        # Show player remaining chips
        print(f"Player chips: {player_chips.total}")

        # Ask to play agin
        if not replay(player_chips):
            break
    print("Thank you for playing!\n")

if __name__ == '__main__':
	main()