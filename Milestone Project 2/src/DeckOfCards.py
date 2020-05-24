import random

class DeckOfCards:

#Collection of Cards - Suit, rank
	def __init__(self):
		self.cards = [[('Clubs', 'Ace'), False],	
				 [('Clubs', '2'), False],
				 [('Clubs', '3'), False],
				 [('Clubs', '4'), False],
				 [('Clubs', '5'), False],
				 [('Clubs', '6'), False],
				 [('Clubs', '7'), False],
				 [('Clubs', '8'), False],
				 [('Clubs', '9'), False],
				 [('Clubs', '10'), False],
				 [('Clubs', 'Jack'), False],
				 [('Clubs', 'Queen'), False],
				 [('Clubs', 'King'), False],
				 [('Spades', 'Ace'), False],	
				 [('Spades', '2'), False],
				 [('Spades', '3'), False],
				 [('Spades', '4'), False],
				 [('Spades', '5'), False],
				 [('Spades', '6'), False],
				 [('Spades', '7'), False],
				 [('Spades', '8'), False],
				 [('Spades', '9'), False],
				 [('Spades', '10'), False],
				 [('Spades', 'Jack'), False],
				 [('Spades', 'Queen'), False],
				 [('Spades', 'King'), False],
				 [('Diamonds', 'Ace'), False],	
				 [('Diamonds', '2'), False],
				 [('Diamonds', '3'), False],
				 [('Diamonds', '4'), False],
				 [('Diamonds', '5'), False],
				 [('Diamonds', '6'), False],
				 [('Diamonds', '7'), False],
				 [('Diamonds', '8'), False],
				 [('Diamonds', '9'), False],
				 [('Diamonds', '10'), False],
				 [('Diamonds', 'Jack'), False],
				 [('Diamonds', 'Queen'), False],
				 [('Diamonds', 'King'), False],
				 [('Hearts', 'Ace'), False],	
				 [('Hearts', '2'), False],
				 [('Hearts', '3'), False],
				 [('Hearts', '4'), False],
				 [('Hearts', '5'), False],
				 [('Hearts', '6'), False],
				 [('Hearts', '7'), False],
				 [('Hearts', '8'), False],
				 [('Hearts', '9'), False],
				 [('Hearts', '10'), False],
				 [('Hearts', 'Jack'), False],
				 [('Hearts', 'Queen'), False],
				 [('Hearts', 'King'), False]]

	#Draw Cards
	def draw_card(self):
		
		while True:
			index = random.randrange(0,51)
			if self.cards[index][1] == False:
				self.cards[index][1] = True
				return self.cards[index]
			else:
				continue