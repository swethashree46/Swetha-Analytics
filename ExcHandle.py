from logging import exception

#try - except


#############################################################

# print("simple prog with out Exception Handling")
#
# var = "today we are learning EH in python"
# res = var.index('java')
# print("the position of python = " , res)
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
# print("complete")



#############################################################




# print("simple prog with out Exception Handlng")
#
# var = "today we are learning EH in python"
#
# try:
#     res = var.index('java')
#
# except Exception as err:
#     print("lets ignore this error")
#     print("error msg was = ", err)
#     res = "Not Found"
#
# print("the position of python = " , res)
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
# print("complete")
#
#
# a=5
# b='s'
# try:
#     res = a+b
#
# except Exception as err:
#     print(err)
#
#     res = "Operations should be performed on same dataype only"
#     print(res)
# x=4
# t=5
# ans=x+t
# print(ans)

# p=5
# q=0
#
# try:
#     res=p/q
#
# except Exception as err:
#     print("The Error you did",err)
#     print("You should divide any number by zero")
#
# swe=[1,2,3,4,5,6,7,7]
# for a in swe:
#     if(a%2==0):
#         print("Even numbers are = ",a)
#     else:
#         print("Odd numbers are = ",a)
#
#
#
#
#
#
# print("opening file ")
#
# try:
#     fvar = open(r'abc.txt', 'r')
# except Exception as err:
#     fvar = open(r'abc.txt', 'w')
#     print("Created the file")
#
#
# fvar.close()
#
# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
# print("complete")



#EH Example with File concept with data inside
#
# print("opening file ")
#
# try:
#     fvar = opn(r'abc.txt' , 'r')
#
# except Exception as err:
#     print("creating the file abc.txt")
#     fvar = open(r'abc.txt', 'w')
#
# fvar.close()
#
# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")



# EH Example with File concept

#
# print("opening file ")
#
# try:
#     fvar = opn(r'abc.txt' , 'r')
#
# except FileNotFoundError as err:
#     print("creating the file abc.txt")
#     fvar = open(r'abc.txt', 'w')
#
# except NameError as err:
#     print("correcting the func name")
#     fvar = open(r'abc.txt', 'r')
#
# fvar.close()
#
# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")






############################ creating errors ##############################

# assert and raise

### assert statement example to create error
# assert condition , message

# simple example

# mobnum  = str(input("enter the mobile number = "))
# res1 = len(mobnum)
# res2 = mobnum.isdigit()
# # assert condition , message
# assert res1==10 and res2 == True, "hey boss please enter the valid number "
# print("Valid Mobile number")
#
# age = str(input("enter the age = "))
# assert  int(age) >= 22 and int(age) <= 35 , "Age not matched boss"
# print("Valid age")
#
# print("complete")
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")
#
#
#
# flag = 0
# while(True):
#
#     mobnum  = str(input("enter the mobile number = "))
#
#     res1 = len(mobnum)
#     res2 = mobnum.isdigit()
#
#     # assert condition , "error message"
#     try:
#         assert res1==10 and res2 == True, ""
#         flag = 1
#     except AssertionError as err:
#         # print("enter the mobile number again = ")
#         print("Please enter the vaid mobile number remember it can take only 10 digits")
#
#     if(flag == 1):
#         print("success i am goint to next step")
#         break








#  using raise statement

# mobnum  = str(input("enter the mobile number = "))
#
# res1 = len(mobnum)
# res2 = mobnum.isdigit()
#
# # raise category("error msg")
#
# if(res1 != 10 or res2 != True):
#     raise NameError(" enter correct data ")
#
# else:
#     print("Valid mobile number")
#
# print("complete")
#
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")











## assert


# username = "sweet"
# password = "ar@546"
# otp = 3428
#
# userin = str(input("enter the user name = "))
# assert userin == username , "invalid username"
# print("valid user name proceed next ")
#
# pwdin = str(input("enter the password = "))
# assert pwdin == password , "invalid password"
# print("valid password  proceed next ")
#
# otpin = int(input("enter the otp = "))
# assert otpin == otp , "invalid otp"
# print("valid otp  proceed next ")
#
#
# print("welcome to home page")





### raise
### if(cond):
#### raise Ecategory("msg")

# username = "sweet"
# password = "ar@546"
# otp = 3428
#
# userin = str(input("enter the user name = "))
# if(username != userin):
#     raise KeyError("invalid username")
# print("valid user name proceed next ")
#
#
# pwdin = str(input("enter the password = "))
# if(pwdin != password):
#     raise ValueError("invalid password")
# print("valid password  proceed next ")
#
#
# otpin = int(input("enter the otp = "))
# if(otpin != otp):
#     raise ValueError("invalid otp")
# print("valid otp  proceed next ")
#
#
#
# print("welcome to home page")






#assert userin == username and pwdin == password and otpin == otp , "Invalid cread try agaian"



# % >= 60
# back logs == 0
# end duration == 4
# interview == cleared

# perc = int(input("enter the perc = "))
# assert perc >= 60 , "Sorry you dont have enough perc"
# print("percentage is validated")
#
# backlogs = int(input("enter the backlogs = "))
# assert backlogs == 0 , "Sorry you have backlogs"
# print("backlogs is validated")
#
# duration = int(input("enter the eng duration = "))
# assert duration == 4 , "Sorry you dont have enough duration for the course"
# print("duration is validated")
#
# interview = str(input("did u clear the interview = "))
# assert interview == 'yes' , "Sorry  dint clear interview"
# print("interview is validated")
#
# print("welcome to the company XYZ")
#
#
#
#
#
















