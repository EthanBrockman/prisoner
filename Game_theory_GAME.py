import random

writing_file = open('game_data', 'w')
Game_History_P1  = []
Game_History_P2 = []
P1_sentence = 0
P2_sentence = 0

class Prisoner:
	def __init__(self, amount_of_games):
		self.amount_of_games = amount_of_games
		
	def game(self, P1_decision, P2_decision):
		global Game_History_P1, Game_History_P2, P1_sentence, P2_sentence
		print(P1_decision, P2_decision)
		# This function determines the outcome of the game and records the games history and players sentence
		if P1_decision == 'B' and P2_decision == 'B':
			print(f'They both betray, both get 2 years.\n')
			writing_file.write(f'They both betray, both get 2 years.\n')
			Game_History_P1.append('B')
			Game_History_P2.append('B')
			P1_sentence += 2
			P2_sentence += 2
		elif P1_decision == 'B' and P2_decision == 'S':
			print(f'Prisoner 1 faces no charge, prisoner 2 gets 3 years\n')
			writing_file.write(f'Prisoner 1 faces no charge, prisoner 2 gets 3 years\n')
			Game_History_P1.append('B')
			Game_History_P2.append('S')
			P2_sentence += 3
		elif P1_decision == 'S' and P2_decision == 'B':
			print(f'Prisoner 2 faces no charge, prisoner 1 gets 3 years\n')
			writing_file.write(f'Prisoner 2 faces no charge, prisoner 1 gets 3 years\n')
			Game_History_P1.append('S')
			Game_History_P2.append('B')
			P1_sentence += 3
		elif P1_decision == 'S' and P2_decision == 'S':
			print(f'They both stay silent, both get 1 year\n')
			writing_file.write(f'They both stay silent, both get 1 year\n')
			Game_History_P1.append('S')
			Game_History_P2.append('S')
			P1_sentence += 1
			P2_sentence += 1
		else:
			print('there is an error')
	def play_many_games(self, P1, P2):
		# performs mutiple games depending on the amount listed by the user
		for i in range(self.amount_of_games):
			self.game(P1.player_choice(), P2.player_choice())
		print('View game_data.txt to see how many years you will serve and the game history')
			
class Player:
	def __init__(self, choice, player_number):
		self.choice = choice
		self.player_number = player_number
	
	def player_choice(self):
		# returns the choice of the player with the game history of the other player
		global Game_History_P1, Game_History_P2
		if self.player_number == 1:
			if self.choice == 1:
				return(always_betray(Game_History_P2))
			elif self.choice == 2:
				return(always_silent(Game_History_P2))
			elif self.choice == 3:
				return(tit_for_tat(Game_History_P2))
			elif self.choice == 4:
				return(beat_last(Game_History_P2))
			elif self.choice == 5:
				return(no_mercy(Game_History_P2))
			elif self.choice == 6:
				return(randy(Game_History_P2))
		elif self.player_number == 2:
			if self.choice == 1:
				return(always_betray(Game_History_P1))
			elif self.choice == 2:
				return(always_silent(Game_History_P1))
			elif self.choice == 3:
				return(tit_for_tat(Game_History_P1))
			elif self.choice == 4:
				return(beat_last(Game_History_P1))
			elif self.choice == 5:
				return(no_mercy(Game_History_P1))
			elif self.choice == 6:
				return(randy(Game_History_P1))
		
	
		
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

def sentence1():
	# returns player 1's sentence
	global P1_sentence
	return(P1_sentence)
	
def sentence2():
	#returns player 2's sentence
	global P2_sentence
	return(P2_sentence)

