class Warrior:
    power = 30

    def __init__(self):
        self.level = 1

    def attack(self):
        print("Boom!")
    
    def info():
        print("Powerful!")

    def retID(self):
        return id(self)
    
    def levelUp(self):
        print("LevelUp!")
        # level += 1 error
        self.level += 1


john = Warrior()
mary = Warrior()

john.attack()
mary.attack()

Warrior.levelup()


# john.info() error!!
Warrior.info()

# id 같게 출력 됨
print(id(john))
print(john.retID())

print(id(mary))
print(mary.retID())

print(Warrior.retID(mary))


print(isinstance(john, Warrior))
number = 7
print(isinstance(number, int))

print(isinstance(number, Warrior))

print(isinstance(7, int))

# 둘다 같은 메모리를 가르키고 있다.
print(id(7))
print(id(number))


print(john.power)
print(mary.power)

john.power += 1

print(john.power)
print(mary.power)
