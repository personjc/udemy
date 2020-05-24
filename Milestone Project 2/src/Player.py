class Player:
	
	def __init__(self,chips):
		self.chips = chips
		self.cards = []

	def hold_card(self, card):
		self.cards.append(card)

	def win_chips(self, chips):
		self.chips += chips

	def lose_chips(self, chips):
		self.chips -= chips

	def clear_hand(self):
		self.cards = []