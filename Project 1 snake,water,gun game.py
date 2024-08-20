#We all played snake,water,gun game in our childhood.if you haven't,google the rules of this game and write a python program capital of playing this game with the user.
import random
'''
1 for snake 
-1 for water 
0 for gun
'''
computer = random.choice([1,-1,0])
youstr = input("Enter your choice:  ")
youDict = {"s":1 , "w": -1 , "g": 0}
reverseDict = {1: "snake" , -1: "water", 0:"gun"}
you=youDict[youstr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Draw")
else:
    # if(computer==1 and you==-1):   same program but he is  a multiple line code 
    #     print("You win!")
    # elif(computer==1 and you==0):
    #     print("You lose!")
    # elif(computer==-1 and you==0):
    #     print("You win!")
    # elif(you==1 and computer==-1):
    #     print("You win!")
    # elif(you==1 and computer==0):
    #     print("you lose!")
    # elif(you==-1 and computer==0):
    #     print("You win!")
    # else:
    #     print("Something entered wrong")
    
    if((computer - you)==-1 or (computer -you)==-2): # same program but 4 line code
       print("You win")
    else:
        print("You lose")