import unittest
from src import GameRunner
from src import Dealer
from src import Player

class TestGameRunner(unittest.TestCase):

	def test_calculate_points_numbers(self):
		cards = [('Clubs', '2'),('Spades', '10')]
		self.assertEqual(GameRunner.GameRunner().calculate_points(cards), 12)


	def test_calculate_points_face(self):
		cards = [('Clubs', '3'),('Spades', 'Queen'),('Diamonds', 'Queen')]
		self.assertEqual(GameRunner.GameRunner().calculate_points(cards), 23)


	def test_determine_winner(self):
		gameRunner = GameRunner.GameRunner()
		dealer = Dealer.Dealer()
		player = Player.Player(500)

		dealer_cards = [('Clubs', '5'), ('Clubs', '6'), ('Clubs', 'Queen')]
		player_cards = [('Clubs', '4'), ('Clubs', '5'), ('Clubs', 'Queen')]

		dealer.cards = dealer_cards
		player.cards = player_cards

		gameRunner.determine_winner(dealer, player, 50)

if __name__ == '__main__':
	unittest.main()
