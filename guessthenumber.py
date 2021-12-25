import random
numf = []
numv = []
print("Hi gamer, Tell me your nickname")
name = input()
print("Hi, " + name + ". Welcome to the Guess Number")
print("Choose an Option!: ")
print("1) Easy Level / 2) Middle Level / 3) Hard Level  / 4) Exit")
opt = int(input())
if (opt == 1):
    RandomNumber = random.randrange(0,10)
    print("Welcome to the Easy Level")
    attemps = 1
    while attemps <= 3:
        number = int(input("Tell me a number between 1 and 10, you have 3 attemps and this is your try: " + str(attemps) + ": "))
        if(number <= 10):
            if(number == RandomNumber):
                numv.append(number)
                print("You got It!")
                print("You failed this numbers: " + str(numf) + ". And you guess this number with  " + str(numv))
                break
            elif(number < RandomNumber): 
                print("The number is higher")
                numf.append(number)
            elif(number > RandomNumber):
                print("The number is lower")
                numf.append(number)
            attemps += 1
        elif(number > 10 and number <= 50):
            print("That number is not valid for this level. Better go to the Middle Level")
        elif(number > 50):
            print("That number is not valid for this level. Better go to the Hard Level")
elif(opt == 2):
    RandomNumber = random.randrange(0,50)
    print("Welcome to the Middle Level")
    attemps = 1
    while attemps <= 5:
        number = int(input("Tell me a number between 1 and 50, you have 5 attemps and this is your try: " + str(attemps) + ": "))
        if(number <= 50):
            if(number == RandomNumber):
                numv.append(number)
                print("You got It!")
                print("You failed this numbers: " + str(numf) + ". And you guess this number with  " + str(numv))
                break
            elif(number < RandomNumber): 
                print("The number is higher")
                numf.append(number)
            elif(number > RandomNumber):
                print("The number is lower")
                numf.append(number)
            attemps += 1
        elif(number > 50):
            print("That number is not valid for this level. Better go to the Hard Level")
elif(opt == 3):
    RandomNumber = random.randrange(0,100)
    print("Welcome to the Hard Level")
    attemps = 1
    while attemps <= 8:
        number = int(input("Tell me a number between 1 and 10, you have 3 attemps and this is your try: " + str(attemps) + ": "))
        if(number <= 100):
            if(number == RandomNumber):
                print("You got It!")
                numv.append(number)
                print("You failed this numbers: " + str(numf) + ". And you guess this number with  " + str(numv))
                break
            elif(number < RandomNumber): 
                print("The number is higher")
                numf.append(number)
            elif(number > RandomNumber):
                print("The number is lower")
                numf.append(number)
            attemps += 1
        elif(number > 100):
            print("The number is higher than 100")
elif(opt == 4):
    print("Bye Bye")
else:
    print("Rewrite the number")