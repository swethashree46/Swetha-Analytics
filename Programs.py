# tickets=[546001,
#          546002,
#          546003,
#          546004,
#          546005,
#          546006,
#          546007,
#          546008,
#          546009,
#          546010]
# import random
# random.shuffle(tickets)
# print("WELCOME TO LOTTERY GAME")
# z=str(input("ARE YOU READY FOR FIRST PRIZE?  "))
# if(z=="YES"):
#     f=random.choice(tickets)
#     print("THE FIRST PRIZE WINNER IS--  ",f)
#     tickets.remove(f)
# else:
#     print("THANK YOU!")
#
# y=str(input("ARE YOU READY FOR SECOND PRIZE?  "))
# random.shuffle(tickets)
# if(y=="YES"):
#
#     s=random.choice(tickets)
#     print("THE SECOND PRICE WINNER IS--  ",s)
#     tickets.remove(s)
#
# else:
#     print("THANK YOU!")
#
# x=str(input("ARE YOU READY FOR THIRD PRIZE?  "))
# random.shuffle(tickets)
# if(x=="YES"):
#
#     t=random.choice(tickets)
#     print("THE THIRD PRIZE WINNER IS--  ",t)
#     print("THE END")
#     tickets.remove(t)
# else:
#     print("THANK YOU!")


#SNAKE AND LADDERS GAME

#position = the position of a player
#count= the count of dice rolled to reach destiny
#dice= the random number between 1 and 6

# import random
# from collections.abc import dict_keys
#
# position=0
# count=0
#
# while(position<=100):
#     dice=random.randrange(1,7)
#     position=position+dice
#     count+=1
#
#     if(position==100):
#         print("Your position is", position)
#         print("Great Girl, You reached the Destiny")
#         print("You Won")
#         break
#
#     if(position>100):
#         position=position-dice
#         print("Your position is",position)
#         print("Its okay, Don't Give up!")
#
#     elif(position==5):
#         print("Your position is", position)
#         position=46
#         print("Your Goodness!,You stepped into a ladder and get into 46")
#
#     elif(position==7):
#         print("Your position is", position)
#         position=15
#         print("Your Goodness!,You stepped into a ladder and get into 15")
#
#     elif(position==12):
#         print("Your position is", position)
#         position=32
#         print("Your Goodness!,You stepped into a ladder and get into 32")
#
#     elif(position==18):
#         print("Your position is", position)
#         position=2
#         print("Sad of you!,You got bitten by Snake and get down into 8")
#
#     elif(position==23):
#         print("Your position is", position)
#         position=51
#         print("Your Goodness!,You stepped into a ladder and get into 51")
#
#     elif(position==26):
#         print("Your position is", position)
#         position=11
#         print("Sad of you!,You got bitten by Snake and get down into 11")
#
#     elif(position==37):
#         print("Your position is", position)
#         position=62
#         print("Your Goodness!,You stepped into a ladder and get into 62")
#
#     elif(position==42):
#         print("Your position is", position)
#         position=78
#         print("Your Goodness!,You stepped into a ladder and get into 78")
#
#     elif(position==48):
#         print("Your position is", position)
#         position=29
#         print("Sad of you!,You got bitten by Snake and get down into 29")
#
#     elif(position==53):
#         print("Your position is", position)
#         position=44
#         print("Sad of you!,You got bitten by Snake and get down into 44")
#
#     elif(position==61):
#         print("Your position is", position)
#         position=16
#         print("Sad of you!,You got bitten by Snake and get down into 16")
#
#     elif(position==69):
#         print("Your position is", position)
#         position=86
#         print("Your Goodness!,You stepped into a ladder and get into 86")
#
#     elif(position==75):
#         print("Your position is", position)
#         position=94
#         print("Your Goodness!,You stepped into a ladder and get into 94")
#
#     elif(position==77):
#         print("Your position is", position)
#         position=55
#         print("Sad of you!,You got bitten by Snake and get down into 55")
#
#     elif(position==85):
#         print("Your position is", position)
#         position=96
#         print("Your Goodness!,You stepped into a ladder and get into 96")
#
#     elif(position==89):
#         print("Your position is", position)
#         position=67
#         print("Sad of you!,You got bitten by Snake and get down into 67")
#
#     elif(position==92):
#         print("Your position is", position)
#         position=2
#         print("Sad of you!,You got bitten by Snake and get down into 2")
#
# print("GAME OVER!!!")
# print("No of times the dice rolled is ",count)


#FIBONACI SERIES

# ar=int(input("Enter loop count"))
# first=0
# second=1
# print("",first)
# print("",second)
#
# while(ar>0):
#     res=first+second
#     print("",res)
#     first=second
#     second=res
#     ar-=1




