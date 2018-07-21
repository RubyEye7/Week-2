import random
def d2():
    print(random.randint(1,2))
def d3():
    print(random.randint(1,3))
def d4():
    print(random.randint(1,4))
def d6():
    print(random.randint(1,6))
def d8():
    print(random.randint(1,8))
def d10():
    print(random.randint(1,10))
def d12():
    print(random.randint(1,12))
def d20():
    print(random.randint(1,20))
def d100():
    print(random.randint(1,100))
def d120():
    print(random.randint(1,120))

def Dice():
    true = True
    while true:
        DiceChoice = input("Enter the type of dice you would like to use: ")
        if DiceChoice == "d2":
            d2()
        elif DiceChoice == "d3":
            d3()
        elif DiceChoice == "d4":
            d4()
        elif DiceChoice == "d6":
            d6()
        elif DiceChoice == "d8":
            d8()
        elif DiceChoice == "d10":
            d10()
        elif DiceChoice == "d12":
            d12()
        elif DiceChoice == "d20":
            d20()
        elif DiceChoice == "d100":
            d100()
        elif DiceChoice == "d120":
            d120()
        elif DiceChoice == "end":
            true = False

Dice()            
