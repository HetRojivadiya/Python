list = [1,2,3]

rule = { 12:True,13:False,21:False,23:True,31:True,32:True}

import random

computer = int(random.choice(list))

print("\n1.Snake,2.Water,3.gun\n")
player = int(input("Enter choice : "))
print(f"Player select: {player}")
print(f"Computer select: {computer}")

c = str(player)+str(computer)

key = int(c)
output = rule.get(key)
print(player)
print ("You are winner!") if output == True else print ("Sorry, Computer win this match!") if output == False else print ("Match is Draw!")








