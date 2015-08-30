
# A very simple card, rough and dirty. No checking of inputs
class Card(object):

	def __init__(self,value):
		if value[0] != 'X':
			self.value = value[0]
			self.suit = value[1]
		else:
			self.value = 'X'
			self.suit = None

	def __repr__(self):
		if self.value != 'X':
			return str(self.value) + self.suit
		else:
			return self.value

	def compval(self,other):
		if self.value == other.value:
			return True
		else:
			return False

	def __eq__(self, other):
		if (self.value == other.value) & (self.suit == other.suit):
			return True
		return False
