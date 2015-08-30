import cards
import random

#Create a Canasta deck. This means two standard decks with jokers put together.


RANKS = '23456789TJQKA'
SUITS = 'dhsc'
#SUITS = u'\u2660'u'\u2665'u'\u2666'u'\u2663'


class Deck(object):
	
	def __init__(self):
		self._cards = []
		for rank in RANKS:
			for suit in SUITS:
				self._cards.append(cards.Card((rank,suit)))
		for rank in RANKS:
			for suit in SUITS:
				self._cards.append(cards.Card((rank,suit)))
		for x in range(0,4):		
			self._cards.append(cards.Card('X'))
		random.shuffle(self._cards)
	
	'''def draw(self, num):
		if num == 1:
			return self._cards.pop()
		else:
			return self._cards.pop(), self._cards.pop()
	'''

	def draw(self):
		return self._cards.pop()	

	def shuffle(self):
		random.shuffle(self._cards)

	#print shit out
	def getsizeof(self):
		return len(self._cards)

	def __repr__(self):
		print(self._cards),
		return ''
