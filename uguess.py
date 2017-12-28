low=0
high=100
guess=50
print('Think of  a number between 0 and 100! \n')
print('Is your secret number'+str(guess)+'?')
while (True):
	ans=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l")
	if ans =='h':
		high=guess
		low=0
		guess=(low+guess)/2
		print('Is your secret number'+str(guess)+'?')
	elif ans == 'l':
		low=guess
		high=100
		guess=(low+guess)/2
		print('Is your secret number'+str(guess)+'?')
	else:
		break
	print('Your secret number is'+str(ans))

		
		


