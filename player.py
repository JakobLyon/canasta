import cfg
import cards
import sys

#human player module
class Player():
	
	
	def __init__(self, team):
		self.hand = []
		self.team = team
		self.score = 0

	def draw(self):
		self.hand.append(cfg.gamedeck.draw())

	def firstCheck(self,play):
		return None
	
	def checkPlay(self, play):
		
		return True

	def checkforred3(self,teamboard3s):
		while True:
			found = False
			for three in range(0,self.hand.count(cards.Card('3h'))):
				teamboard3s += 1
				self.hand.append(cfg.gamedeck.draw())
				self.hand.remove(cards.Card('3h'))
				found = True
			for three in range(0,self.hand.count(cards.Card('3d'))):
				teamboard3s += 1
				self.hand.append(cfg.gamedeck.draw())
				self.hand.remove(cards.Card('3d'))
				found = True
			if found == False:
				break
			else:
				print 'Red 3 found, draw a card'
				print 'Your new hand: ', self.hand
		return teamboard3s

	def __repr__(self):
		print(self.hand),
		return ''

#########################################################################################
####										      ###
#########################################################################################

	#return: deck, cfg.discard, teamboard
	def takeTurn(self, teamboard):
		#save hand and cfg.discard in case we need to restore after editing
		odiscard = cfg.discard
		ohand = self.hand

		teamboard3s=teamboard[0]
		#play red 3s and draw
		self.checkforred3(teamboard3s)


		#check if it is possible to take cfg.discard pile, if not, draw 2
		#this code is shit, fix it
		discardlocked = False
		discard2lock = False
		if (cfg.discard[len(cfg.discard)-1] == cards.Card('3c')) | (cfg.discard[len(cfg.discard)-1] == cards.Card('3s')) | (cfg.discard[len(cfg.discard)-1] == cards.Card('2d')) | (cfg.discard[len(cfg.discard)-1] == cards.Card('2h')) | (cfg.discard[len(cfg.discard)-1] == cards.Card('2c')) | (cfg.discard[len(cfg.discard)-1] == cards.Card('3s')):
			discardlocked = True
		elif cfg.discard.count(cards.Card('2h'))>0 | cfg.discard.count(cards.Card('2d'))>0 |cfg.discard.count(cards.Card('2s'))>0 | cfg.discard.count(cards.Card('2c'))>0:
			discard2lock = True

###TURN SETUP FINISHED, PLAYER MAKES DECISIONS HERE###

		#holy shit this is terribly designed and confusing
		"""This loop allows us to kick the player back to the beginning of their turn
		if they make an invalid play. There are two loops inside this. 1: determine if
		they draw or take discard. 2: make their play, cfg.discard, and end turn"""
		tookDiscard = False
		while True:
			'''prompt here to take discard or draw 2, if option is available
			(discardlocked = False)'''
			while True:
				#discard is locked, draw 2
				if discardlocked == True:
					print 'discard is locked. Draw 2 cards.'
					self.draw()
					self.draw()
					break
				#discard is 2locked but not locked, check if we have 2. if not, draw, if we do, give option
				elif discard2lock == True:
					topcount = 0
					for card in self.hand:
						if card.compval(cfg.discard[len(cfg.discard)-1]):
							topcount += 1
					if topcount < 2:
						self.draw()
						self.draw()
						print 'discard is 2 locked and you do not have 2 of the same value. Draw 2 cards.'
						break	
				#we have the option to choose draw or take cfg.discard			
				try:
					print '1. Draw 2'
					print '2. Take discard'
					print '3. Quit game'
					x = input('>> ')
		
					if x == 1:
						self.draw()
						self.draw()
					elif x == 2:
						tookDiscard = True
					elif x == 3:
						sys.exit(0)
				except Exception:
					print 'Unacceptable input'
					print '>> '			
				else:
					break
			if tookDiscard == False:
				print 'Your new hand: ', self
			else:
				print 'You must use this card in your play: ',cfg.discard[len(cfg.discard)-1]

			#prompt here to select cards for our play or pass. if we took the pile(we'll need a boolean to keep track of that) then we need to check if we're actually using it. if not, throw an error that returns us to the beginning of the play.
			while True:
				play = []
				try:
					print '1. Select a card to add to your play'
					print '2. Check if your play is valid'
					print '3. Select a card to discard and end turn'
					print '4. Quit game'
					x = input('>> ')
					if x == 1:
						break
					elif x == 2:
						#checkPlay()
						break
					elif x == 3:
						#discard
						break
					elif x == 4:
						sys.exit(0)
				except Exception:
					print 'Unacceptable input'
					print '>> ' 
		return (teamboard3s,teamboard[1])


	
