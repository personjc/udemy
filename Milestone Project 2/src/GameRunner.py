from DeckOfCards import DeckOfCards
from Player import Player
from Dealer import Dealer

class GameRunner:

	def __init__(self):
		pass

	def starting_chips():
		return int(input('Please enter starting chips amount: '))

	def calculate_points(self, cards):
		total = 0
		for card in cards:
			try:
				total += int(card[1])
			except:
				total += 10

		return total

	def determine_winner(self, dealer, player, bet):
		dealer_total = self.calculate_points(dealer.cards)
		player_total = self.calculate_points(player.cards)

		print('Player Total: ' + str(player_total))
		print('Dealer Total: ' + str(dealer_total))

		if player_total > 21:
			self.player_lost(player, bet)
		elif dealer_total > 21:
			self.player_won(player, bet)	
		elif dealer_total == player_total:
			self.player_tie(player)
		elif dealer_total > player_total:
			self.player_lost(player, bet)		
		elif dealer_total < player_total:
			self.player_won(player, bet)	

		print('Your new chip total is: ' + str(player.chips))

	def player_lost(self, player, bet):
		print('You lost! Dealer takes the cd chips :(')
		player.chips -= bet

	def  player_won(self, player, bet):
		print('You won!')
		player.chips += bet

	def  player_tie(self, player):
		print('You tied! Keep your bet.')

	def run():
		player1 = Player(starting_chips())
		dealer = Dealer()
		deck = DeckOfCards()
		keep_playing = True
		bust = False

		while keep_playing:
			#Place bets
			bet = int(input('Please enter amount to bet: '))

			#Draw Dealer Cards
			card = deck.draw_card()
			print('Dealer card: ' + str(card[0]))
			dealer.draw_card(card[0])
			dealer.draw_card(deck.draw_card()[0])

			#Draw Player Cards
			card = deck.draw_card()
			print('Player card #1: ' + str(card[0]))
			player1.hold_card(card[0])
			card = deck.draw_card()
			print('Player card #2: ' + str(card[0]))
			player1.hold_card(card[0])

			#TODO - turn player turn into a method
			#Player's turn
			player_turn = True
			while player_turn:
				choice = input("Would you like to 'Stay' (S) or 'Hit' (H)?")
				if choice.lower() == 'h':
					card = deck.draw_card()
					print('Card drawn' + str(card[0]))
					player1.hold_card([0])
					if calculate_points(player1.cards) > 21:
						print('You busted! Point Total: ' + str(calculate_points(player1.cards)))
						bust = True
						break
					else:
						continue
				elif choice.lower() == 's':
					break
				else:
					print("Please enter a valid input")

			#Show Dealer's full hand
			print('Dealer cards: ')
			for card in dealer.cards:
				print(str(card))

			#Draw Dealer cards to beat player
			while calculate_points(dealer.cards) < calculate_points(player1.cards) and bust == False:
				card = deck.draw_card()
				print('Dealer draws: ' + str(card[0]))
				dealer.draw_card(card[0])

			#Determine Winner
			determine_winner(dealer, player1, bet)

			choice = input('Keep playing (y/n)?')

			if choice.lower() == 'y':
				continue
			elif choice.lower() == 'n':
				keep_playing = False
			else:
				keep_playing = False


	if __name__ == '__main__':
		run()	


		


