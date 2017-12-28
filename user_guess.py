import random
n=int(input("Enter the range within which u want to guess the number: "))
key=random.randrange(0,n)


def check():
    user_input=int(input("Enter your guess: "))
    if user_input == key:
        print("Good Guess Man!!")
    elif user_input > key:
        print("Try a smaller number: ")
        check()
    else:
        print("A Bigger Number: ")
        check()
if key < n//2:
    print("Your answer is in the 1st half,try between {} and {}".format(0,n//2))
    check()
else:
    print("Your answer is in the 2nd half,try between {} and {}".format(n//2,n))
    check()

    
