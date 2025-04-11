#FOR LOOP
#EXAMPLE 1
#PRINTING ALL THE VALUES IN LIST USING FOR LOOP
# swetha=[5,46]
# count=0
# for x in swetha:
#     print(x)
#     count+=1
#     print("Swetha contains ",count)

#EXAMPLE 2
#FOR LOOP WITH CONDITION
# shree=[1,2,3,4,5,6,7,8,9,10]
# count=0
# for x in shree:
#     if(x%2==0):
#         print(x)
#         count+=1
#         print("The even numbers are ",count)

#EXAMPLE 3
#PRINT THE VALUE WITHOUT CONDITION
# sweet=[1,2,3]
# for x in sweet:
#     print(x*2)

#EXAMPLE 4
#PRINT STRING USING FOR LOOP
# parts=['Heart','Blood','Lungs','Brain','Eyes']
# for x in parts:
#     print(x)

#EXAMPLE 5
#GETTING INPUT AND PRINT VALUES USING FOR LOOP
# marks=list(input("Enter your mark "))
# for x in marks:
#     print(x)

#EXAMPLE 6
#PRINTING VALUES BY ASSIGNING RANGE
# for s in range(1,4):
#     print(s)

#EXAMPLE 7
#PRINTING VALUES USING RANGE WITH CONDITION
count=0
for a in range(1,11):
    if(a%5==0):
        count+=1
        print(a)
        print(count)

#WHILE LOOP
#EXAMPLE 1
#INFINITE LOOP
# num=[1,2,3,4,5]
# while(num!=0):
#     print(num)

#EXAMPLE 2
#SIMPLE PROGRAM
# s=5
# while(s>0):
#     print("SWETHA LOVES ARAVINDH")
#     s-=1

#EXAMPLE 3
#IF CONDITION
# ar=1
# while(ar<=10):
#     if(ar%3==0):
#         print(ar)
#     ar+=1

#BREAK
#EXAMPLE 1
#FOR LOOP
# sw=[1,2,3,4,5,6,7,8]
# for a in sw:
#     if(a>5):
#         break
#     print(a)

#EXAMPLE 2
#WHILE LOOP
# j=3
# while(j>0):
#     if(j=1):
#         break
#     print(j)
#     j-=1

#CONTINUE
#EXAMPLE 1
#FOR LOOP
# for w in range(2,8):
#     if(w==5):
#         continue
#     print(w)

#EXAMPLE 2
#WHILE LOOP
# y=5
# while(y>0):
#     if(y==3):
#         continue
#     print(y)
#     y=y-1

#PASS
#EXAMPLE 1
#FOR LOOP
# love=['SWETHA','ARAVINDH','HEART']
# for s in love:
#     if(s=='HEART'):
#         pass
#     print(s)

#EXAMPLE 2
#WHILE LOOP
# l=46
# while(l>=41):
#     if(l==43):
#         pass
#     print(l)
#     l-=1

#LETTER GUESSING GAME
# myletter='s'
# count=0
# while(True):
#     guess=str(input("Enter a letter "))
#     count+=1
#     if(myletter==guess):
#         print("WOW! YOU GUESSED IT RIGHT",count)
#         break
#     else:
#         print("Good try")







