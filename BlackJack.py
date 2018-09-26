# coding can start
import random

suits = ('spades','hearts','clubs','diamonds')
ranks = ('two','three','four','five','six','seven','eight',
		'nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5, 'six':6, 'seven':7, 'eight':8, 
		'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}

playing = True


class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank+' of '+self.suit

class Deck():
	def __init__(self):
		self.cards = []
		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit, rank))

	def __str__(self):
		deck_comp = ''
		for card in self.cards:
			deck_comp += '\n'+ card.__str__()
		return deck_comp

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		return self.cards.pop()


class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces >= 1:
			self.value -= 10
			self.aces -= 1

class Chips():
	def __init__(self):
		self.chips = 100
		self.bet = 0

	def win_bet(self):
		self.chips += self.bet

	def lose_bet(self):
		self.chips -= self.bet


def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("Player, take a bet! You can bet 1 - {}  ".format(chips.chips)))
		except ValueError:
			print("Must be a number!")
		else:
			if chips.chips < chips.bet:
				print("Not enough chips")
			else:
				break
			
		


def take_hit(hand,deck):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(hand,deck):
	global playing


	while True:
		hit = input("Would you like to Hit or Stand? Enter 'h' or 's'")

		if hit[0].lower() == 'h':
			take_hit(hand,deck)

		elif hit[0].lower() == 's':
			print("Player Stands. Dealer is playing")
			playing = False

		else:
			print("I did not understand that! Try again!")
			continue
		break


def display_some(player_hand,dealer_hand):
	print('')
	print("Dealer's cards:")
	print("HIDDEN CARD")
	print(dealer_hand.cards[1])
	print('\n')
	print("Player's cards:")
	for card in player_hand.cards:
		print(card)
	print("Your current value is: {}".format(player_hand.value))
	print('')

def display_all(player_hand,dealer_hand):
	print('')
	print("Dealer's card:")
	for card in dealer_hand.cards:
		print(card)
	print("Dealer's value is: {}".format(dealer_hand.value))
	print('\n')
	print("Player's cards:")
	for card in player_hand.cards:
		print(card)
	print("Player's value is: {}".format(player_hand.value))
	print('')

def dealer_turn(hand,deck):
	while dealer_hand.value < 17:
		take_hit(hand,deck)
		hand.adjust_for_ace()



def player_busts(chips):
	chips.lose_bet()
	print("Player Busts!")
	


def dealer_busts(chips):
	print("Dealer Busts!")
	print("Player Wins!")
	chips.win_bet()
		

def dealer_wins(chips):
	print("Dealer Wins!")
	chips.lose_bet()


def player_wins(chips):
	print("Player Wins!")
	chips.win_bet()

def push(chips):
	print("This game is a Tie. PUSH!")
	chips.bet = 0







while True:
	print('\n'*100)
	print('''
Welcome to Black Jack!
Go as close to 21 as possible without going over!
Dealer hits until she reaches 17.
										''')
	# Set up the game:
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	dealer_hand = Hand()
	chips = Chips()

	# Deal 2 cards to the player and dealer:
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Adjust for Aces:
	player_hand.adjust_for_ace()
	dealer_hand.adjust_for_ace()

	# Take a bet:
	take_bet(chips)

	print('\n'*100)
	print("Player bets {}".format(chips.bet))
	# Show cards (hid one dealer's card)
	display_some(player_hand,dealer_hand)


	while playing:
		# Prompt player if he wants to Hit or Stand
		
		hit_or_stand(player_hand, deck)

		print('\n'*100)

		display_some(player_hand, dealer_hand)

		if player_hand.value > 21:
			player_busts(chips)
			playing = False

	if player_hand.value <= 21:

		while dealer_hand.value < 17:
			take_hit(dealer_hand, deck)
			dealer_hand.adjust_for_ace()

		print('\n'*100)
		display_all(player_hand, dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(chips)
			
		else:
			push(chips)

	print('Your current winnings stand at {}'.format(chips.chips))
	x = input("Do you want to play again? y or n?")
	if x[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thanks for playing")
		break



