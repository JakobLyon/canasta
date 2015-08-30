import cards
import deck
import cfg
import player
import sys

debug = 0
#Create all our game utilities: discard pile, players, game fields, and score
#deck and discard pile are created and maintained inside the game loop

#TODO: write a playerAI class and settings so we can make these dynamically
gamestart = 0
player1 = player.Player(1)
player2 = player.Player(2)
player3 = player.Player(1)
player4 = player.Player(2)

#These represents the players fields. They are updated after a players move and used to
#calculate score at the end of a round. The first index represents the number of red 3s.
team1 = (0,[])
team2 = (0,[])

#TODO: consider the game ending situation where the deck is empty

'''
global gamedeck
gamedeck = deck.Deck()
print gamedeck._cards[len(gamedeck._cards)-1]
player1.draw(1)
print player1
player1.draw(2)
print player1
print gamedeck._cards[len(gamedeck._cards)-1]'''
#enter game loop
while True:
	#grab a new deck, deal out to players
	#to deal, the engine draws from the deck and tells the player to draw that card
	cfg.gamedeck = deck.Deck()
	cfg.discard = []
	if gamestart == 4:
		gamestart = 1
	else:
		gamestart += 1

	for deal in range(0,11):
		player1.draw()
		player2.draw()
		player3.draw()
		player4.draw()
	#start the discard pile
	while True:
		if (cfg.gamedeck._cards[cfg.gamedeck.getsizeof()-1] == cards.Card('3h')) | (cfg.gamedeck._cards[cfg.gamedeck.getsizeof()-1] == cards.Card('3d')):
			cfg.gamedeck.shuffle()
		else:
			break
	cfg.discard.append(cfg.gamedeck.draw())	

	if debug == 1:
		print 'Deck after setup:'
		print cfg.gamedeck
		print cfg.gamedeck.getsizeof()
		print 'Initial players hands:'
		print player1
		print player2
		print player3
		print player4

	#enter round loop
	while True:
		#TODO: Establish gameflow here
		if gamestart == 1:
			print 'Player One\'s Turn'
			print 'Your hand: ',player1
			print 'Top of discard: ',cfg.discard[len(cfg.discard)-1]
			team1=player1.takeTurn(team1)
			print cfg.gamedeck
			print cfg.gamedeck.getsizeof()
		elif gamestart == 2:
			player2.takeTurn()
		elif gamestart == 3:
			player3.takeTurn()
		elif gamestart == 4:
			player4.takeTurn()
		

		break
	#TODO: Establish win condition here
	break
