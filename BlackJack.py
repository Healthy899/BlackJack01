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


class Hand():
	pass

class Chips():
	pass

x = Card('spades','two')
print(x)
y = Deck()
print(y)