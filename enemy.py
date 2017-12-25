class Enemy():
    life = 3
    def attack(self):
        self.life -=1
        print("I am attacked")
    def lives_left(self):
        if self.life <=0:
            print("I am dead")
        else:
            print("I am still alive ,I have "+ str(self.life)+" live(s) left")

enemey1=Enemy()
enemey1.attack()
enemey1.lives_left()
enemey1.attack()
enemey1.lives_left()