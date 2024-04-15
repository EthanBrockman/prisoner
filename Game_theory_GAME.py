import random

Game_History_P1  = []
Game_History_P2 = []
P1_sentence = 0
P2_sentence = 0

class Prisoner:
	def __init__(self, amount_of_games):
		self.amount_of_games = amount_of_games
		
	def game(self, P1_decision, P2_decision):
		global Game_History_P1, Game_History_P2, P1_sentence, P2_sentence
		# This function determines the outcome of the game and records the games history and players sentence
		
		print(P1_decision, P2_decision)
		if P1_decision == 'B' and P2_decision == 'B':
			print(f'They both betray, both get 2 years.\n')
			Game_History_P1.append('B')
			Game_History_P2.append('B')
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
		
	def play_many_games(self):
		#performs mutiple games depending on the amount listed by the user
		for i in range(self.amount_of_games):
			self.game(tit_for_tat(Game_History_P2),randy(Game_History_P1))
class Player:
	def __init__(self):
		pass
	
	
	
def always_betray(game_list):
	# always chooses the betray option
	return('B')
def always_silent(game_list):
	# always chooses the silent option
	return('S')
def tit_for_tat(game_list):
	# will choose silent option unless the enemy chooses to betray. Will betray if they betrayed last round.
	if len(game_list) > 0:
		if game_list[-1] == 'B':
			return('B')
		else:
			return('S')
	else:
		return('S')
def beat_last(game_list):
	# Will choose the option that would beat last round.
	if len(game_list) > 0:
		if game_list[-1] == 'B':
			return('B')
		elif game_list[-1] == 'S':
			return('B')
	else:
		return('S')
def no_mercy(game_list):
	# will choose silent unless betrayed. Will only choose the betray option once betrayed.
	if 'B' in game_list:
		return('B')
	else:
		return('S')
def randy(game_list):
	# randomly chooses an option
	random_number = random.random()
	if random_number <= 0.5:
		return('B')
	elif random_number >= 0.5:
		return('S')
	

	
	
