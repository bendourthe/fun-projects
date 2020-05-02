# LIBRARIES IMPORT

import random

# DEFINE GLOBAL VARIABLES

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# DEFINE GAME CLASSES

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += '\n' + card.__str__()
        return 'The deck has: ' + deck

    def __len__(self):
        return len(self.deck)

    def __type__(self):
        return type(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        # Track aces in hand
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value < 21 and self.aces:
            self.values -= 10
            self.aces -= 1

class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# DEPENDENCIES

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips. You have: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        hit_stand = input('Hit or Stand? Enter h or s   ')
        if hit_stand[0].lower() == 'h':
            hit(deck,hand)
        elif hit_stand[0].lower() == 's':
            print("Player Stands -> Dealer's turn")
            playing = False
        else:
            print('Sorry, I did not understand that. Please enter h or s ONLY')
            continue
        break

def show_some(player,dealer):

    print("\nDEALER'S HAND (one card hidden!)")
    print(dealer.cards[1])
    print("\nPLAYER'S HAND")
    for card in player.cards:
        print(card)
    print('Total value -> ', player.value)

def show_all(player,dealer):

    print("\nDEALER'S HAND")
    for card in dealer.cards:
        print(card)
    print('Total value -> ', dealer.value)
    print("\nPLAYER'S HAND")
    for card in player.cards:
        print(card)
    print('Total value -> ', player.value)

def player_busts(player, dealer, chips):
    print('Player BUSTS!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Player WINS! Dealer BUSTS!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer WINS!')
    chips.lose_bet()

def push(player, dealer):
    print('PUSH -> Player and Dealer tie')

# GAME

round_num = 1

while True:
    # Print an opening statement
    if round_num == 1:
        print('WELCOME TO A NEW GAME OF BLACK JACK')

    # Print current round
    print('\nROUND #', round_num)

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    if round_num == 1:
        player_chips = Chips()
    round_num += 1

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print('\nPlayer total chips are: {}'.format(player_chips.total))

    # Ask to play again
    new_game = input("Would you like to play again? Enter y or n: ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nTHANK YOU FOR PLAYING")
        break
