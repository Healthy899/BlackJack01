# coding can start
import random

suits = ('spades','hearts','clubs','diamonds')
ranks = ('two','three','four','five','six','seven','eight',
		'nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5, 'six':6, 'seven':7, 'eight':8, 
		'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}


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
		while self.value > 21 and self.aces > 1:
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
	while chips.bet == 0 or chips.chips < chips.bet:
		try:
			chips.bet = int(input("Player, take a bet! You can bet 1 - {}".format(chips.chips)))
		except:
			print("Must be a number!")
		else:
			if chips.chips < chips.bet:
				print("Not enough chips")
				continue
			else:
				print("Player bets {}".format(chips.bet))
	return chips.bet
			
		


def take_hit(hand,deck):
	hand.add_card(deck.deal())

def hit_or_stand(hand,deck):
	while hand.value < 21:
		try:
			play = str(input("Do you wish to Hit or Stand? ('h' or 's'"))
		except:
			print("Must be 'h' or 's'")
		else:
			if play[0].lower() == 'h':
				take_hit(hand,deck)
				hand.adjust_for_ace()
				print("Player takes a hit")
				continue
			elif play[0].lower() == 's':
				print("Player Stands!")
				break
			else:
				print("I did not understand that! Try again!")
				continue

def display_some(player_hand,dealer_hand):
	print("Dealer's cards:")
	print("HIDDEN CARD")
	print(dealer_hand.cards[1])
	print('\n')
	print("Player's cards:")
	print(player_hand.cards[0])
	print(player_hand.cards[1])
	print("Your current value is: {}".format(player_hand.value))

def display_all(player_hand,dealer_hand):
	print("Dealer's card:")
	print(dealer_hand.cards[0])
	print(dealer_hand.cards[1])
	print('\n')
	print("Player's cards:")
	print(player_hand.cards[0])
	print(player_hand.cards[1])
	print("Your current value is: {}".format(player_hand.value))

def dealer_turn(hand,deck):
	while dealer_hand.value < 17:
		take_hit(hand,deck)
		hand.adjust_for_ace()



def player_busts(player_hand,chips):
	if player_hand.value > 21:
		chips.value -= chips.bet
	return player_hand.value > 21

	


def dealer_busts(dealer_hand,chips):
	if dealer_hand.value > 21:
		print("Dealer Busts!")
		print("Player Wins!")
		chips.chips += chips.bet
		

def dealer_wins(player_hand,dealer_hand,chips):
	if dealer_hand.value > player_hand.value:
		print("Dealer Wins!")
		chips.value -= chips.bet


def player_wins(player_hand, dealer_hand,chips):
	if player_hand.value > dealer_hand.value:
		print(player_wins)
		chips.value += chips.bet




while True:
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

	# Take a bet:
	take_bet(chips)

	# Adjust for Aces:
	player_hand.adjust_for_ace()

	# Show cards (hid one dealer's card)
	display_some(player_hand,dealer_hand)

	playing = True

	while playing:
		# Prompt player if he wants to Hit or Stand
		hit_or_stand(player_hand,deck)

		# Check is player busts:
		if player_busts(player_hand,chips):
			print("Player Busts!")
			playing = False
		# else dealer's turn:
		else:
			dealer_turn(dealer_hand,deck)
			playing = False

	# Check if dealer busts:
	dealer_busts(dealer_hand,chips)



