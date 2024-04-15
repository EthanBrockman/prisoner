from project_game_test import *

print(f'Game Theory is the study of strategy of rational agents and the strategies they use.\n')
print('You are going to be playing a type of Game Theory game called Prisoners Dilemma.')
print('In this game two criminals are arrested, they can either stay silent and maintain')
print('cooperation or betray the other with the promise of being let go if you do so.')
print(f'\nScoring rules:  B = betray  S = Silent\n1.(BB) If both betray each prisoner serves 2 years\n2.(SS) If both stay silent they will both serve 1 year.\n3.(BS) If one betrays and one stays silent the player who betrayed will be let go and the player who stayed silent will serve 3 years')
print(f'\nWhich strategy would you like to use?\n1. Always betray\n2. Always silent\n3. Tit for tat\n4. Beat last round\n5. No mercy\n6. Random choice\n')

amount_of_games = int(input("Enter the number of games: "))
P1_strategy = int(input("Enter the strategy for player 1: "))
P2_strategy = int(input("Enter the strategy for player 2: "))
player1 = Player(P1_strategy, 1)
player2 = Player(P2_strategy, 2)
prisoner1 = Prisoner(amount_of_games)
prisoner1.play_many_games(player1, player2)
