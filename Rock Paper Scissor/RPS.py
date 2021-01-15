import random as rn

opt = ['Rock', 'Paper', 'Scissor']
computer = opt[rn.randint(0, 2)]

player = False
while player == False:
	player = input(" \n Rock, Paper or Scissor ??  ")
	if player.lower() == 'rock':
		if computer == 'Paper':
			print('You lose. Paper can cover your Rock')
		else:
			print("You won. Your Rock can break computer's Scissor")
	elif player.lower() == 'paper':
		if computer == 'Rock':
			print('You won. Your Paper can cover Rock')
		else:
			print('You lose. Scissor can cut your Paper')
	elif player.lower() == 'scissor':
		if computer == 'Rock':
			print('You lose. Rock can break your Scissor')
		else:
			print('You won. Your Scissor can cut Paper')
	elif player == computer:
		print('It\'s a tie')

	player = False
	computer = opt[rn.randint(0, 2)]