import random 

# reply = input('Do you want to play again? Y for yes and N for no: \n ')
reply = 'Y'

def roll_dice(): 
	global reply
	mini = 1
	maxi = 6
	dice = random.randint(mini,maxi)
	print(dice)

	reply = input('Do you want to play again? Y for yes and N for no:\n')

while reply == 'Y' or reply == 'y':
	roll_dice()
	

