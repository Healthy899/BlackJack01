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

x = Card('spades','two')
print(x)
y = Deck()
y.shuffle()
print(y)
h = Hand()
deal_card = y.deal()
print("The card that has been dealt is:")
print(deal_card)
h.add_card(deal_card)
print('The Value is:')
print(h.value)