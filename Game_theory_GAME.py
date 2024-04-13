class Prisoner:
	def __init__(self, amount_of_games):
		self.amount_of_games = amount_of_games
		
	def game(self, P1_decision, P2_decision):
		if P1_decision == 'B' and P2_decision == 'B':
			print(f'They both betray, both get 2 years.\n')
			Game_History_P1.append('B')
			Game_History_P1.append('B')
			P1_sentence += 2
			P2_sentence += 2
		elif P1_decision == 'B' and P2_decision == 'S':
			print(f'Prisoner 1 is faces no charge, prisoner 2 gets 3 years\n')
			Game_History_P1.append('B')
			Game_History_P2.append('S')
			P2_sentence += 3
		elif P1_decision == 'S' and P2_decision == 'B':
			print(f'Prisoner 2 is faces no charge, prisoner 1 gets 3 years\n')
			Game_History_P1.append('S')
			Game_History_P2.append('B')
			P1_sentence += 3
		elif P1_decision == 'S' and P2_decision == 'S':
			print(f'They both stay silent, both get 1 year\n')
			Game_History_P1.append('S')
			Game_History_P2.append('S')
			P1_sentence += 1
			P2_sentence += 1
		else:
			print('there is an error')
class Player:
	def __init__(self):
		pass
	
	
	
def always_betray(game_list):
	pass
def always_silent(game_list):
	pass
def tit_for_tat(game_list):
	pass
def beat_last(game_list):
	pass
def no_mercy(game_list):
	pass
def randy(game_list):
	pass

	
	
Game_History_P1  = []
Game_History_P2 = []
P1_sentence = 0
P2_sentence = 0



example_game = Prisoner(10)
example_game.play_many_games()
print(Game_History_P1)
