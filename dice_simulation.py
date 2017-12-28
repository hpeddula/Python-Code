import random
def user():
    user_input=input("Would you like to roll a  die,Please Enter Y/N:")
    if user_input == 'Y':
       number()
       user()
    else:
        print("It's Ok!!")
def number():
    n=random.randrange(1,6)
    print(n)
user()
