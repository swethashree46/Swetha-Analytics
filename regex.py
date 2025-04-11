# import re
#
# var = "my mobile nums are 7411694426 and 9986019197abcd"
#
# temp = var.split(' ')
# print(temp)
#
# for x in temp:
#     if(len(x) == 10 and x.isdigit()):
#         print(x)

















import re

# var = "today python is easy to learn i love python and python rocks"

# res = re.match('today', var)
# print(res)

# res = re.search('python', var)
# print(res)

# res = re.findall('python', var)
# print(res)

# res = re.sub('python', 'java', var)
# print(res)






# regex examples

# var = "my mobile nums are 7411694426 and 9986019197abcd and 9986019193 and 9816167888xyz"
# # # # ten digits
# pat = '[0-9]{10}'
# res = re.findall(pat,var)
# print(res)



### example with file proj








## ecplaining the students the real time example of getting the mobile nums from text fil

# fvar = open(r'regexinput.txt', 'r')
# data = fvar.read()
# fvar.close()
#
# patn = '[A-Z][a-z]{1,}'
# patm = '[0-9]{10}'
# patp = '[A-Z]{3,}'
# patd = '[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}'
#
# names = re.findall(patn,data)
# mobile = re.findall(patm,data)
# places = re.findall(patp,data)
# dates = re.findall(patd,data)
#
#
# print("Names = ", names)
# print("mobile = ", mobile)
# print("places = ", places)
# print("dates = ", dates)
#
#









# var = "my fav dest places are SINGAPORE and MALDIVES and LOSVEGAS and BALI and GOA"
# pat = '[A-Z]{3,}'
# res = re.findall(pat,var)
# print(res)







#
# var = """
# KEERTHANA id is ABC1234
# ANU id is XYZ9875
# MAINAK id is PQE4545
# """
#
# patn = '[A-Z]{3,}'
# pate = '[A-Z]{3}[0-9]{4}'
#
# names = re.findall(patn,var)
# empid = re.findall(pate,var)
#
# print(names)
# print(empid)





## regex program with file

# fvar = open(r'regexinput.txt', 'r')
# data = fvar.read()
# fvar.close()
#
# print(data)
#
# patn = '[A-Z][a-z]{1,}'
# patp = '[A-Z]{3,}'
# patm = '[0-9]{10}'
# patd = '[0-9]{2}[/][0-9]{2}[/][0-9]{4}'
#
# names = re.findall(patn,data)
# places = re.findall(patp,data)
# mob = re.findall(patm,data)
# dobs = re.findall(patd,data)
#
# print("Names = ", names)
# print("Places = ", places)
# print("Mobile = ", mob)
# print("Dobs = ", dobs)
#







var = """
Mahesh likes CHICKEN
Prakash likes BIRYANI
Resmi likes JAMOON
"""

patn = '[A-Z][a-z]{1,}'
patf = '[A-Z]{2,}'

names = re.findall(patn, var)
food = re.findall(patf, var)

print(names)
print(food)






















var = """
India ip address is 192.3.4.67
Australia ip address is 23.123.5.4
Canada ip address is 165.211.90.43 and 1.45.78.122
"""

patc = '[A-Z][a-z]{1,}'
patip = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'

countries = re.findall(patc, var)
ips = re.findall(patip,var)

print(countries)
print(ips)










# var = """
# 16.09.2000 and email is chethanasonami16092000@gmail.com
# 26/11/1994 and email is dipalioj1234@reddiff123.com
# 26-04-2000 and email is JayaShreeBharaThi10@yahoo.com
# 26:04:2000 and email is JayaShreeBharaThi10@yahoo.com
# """
#
# patd = '[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}'
# pate = '[a-zA-Z0-9]{1,}[@][a-zA-Z0-9]{1,}[.]com'
#
# dates = re.findall(patd,var)
# emails = re.findall(pate, var)
#
# print(dates)
# print(emails)



# file example to format uneven spaces
# import re
#
# fvar = open(r'data.txt', 'r')
# info = fvar.read()
# fvar.close()
#
# print(info)
# pat = '[ ]{1,}'
#
#
# res = re.sub(pat, ' ', info)
#
# print("\n ================================================== \n")
# # print(res)
#
#
# res2 = re.sub('\n', '' , res)
# print(res2)
#
# fvar = open(r'formatted.txt', 'w')
# fvar.write(res2)
# fvar.close()



#####$another file example

# fvar = open(r'ajay.txt', 'r')
# adata = fvar.read()
# fvar.close()

# adata_formatted = adata.replace('9986019197', '7411694426')
# print(adata_formatted)

# adata_formatted = re.sub('[0-9]{10}', '7411694426', adata)
# print(adata_formatted)





# var = """
# Reshma                         your slangis            good
# North      Karnataka        has a    fastest        speaking        slang.
# I        am from     bangalore    mine is a       broken     mixed   one
# """
#
# pat = '[ ]{1,}'
#
# print(var, "\n")
# res = re.sub(pat,' ', var)
# print(res)
#






















# password Validation function

# pwd = str(input("enter the password = "))
#
# caps = len(re.findall('[A-Z]', pwd))
# lows = len(re.findall('[a-z]', pwd))
# digs = len(re.findall('[0-9]', pwd))
# spec = len(re.findall('[^A-Za-z0-9]', pwd))
# pwdlen = len(pwd)
#
# if(caps > 0 and lows > 0 and digs > 0 and spec > 0 and pwdlen >= 8):
#     print("Valid Password")
# else:
#     print("Invalid password")
#
# print("caps = " , caps)
# print("lower = " , lows)
# print("digits = " , digs)
# print("special char = " , spec)
# print("pwd len -  ", pwdlen)
#
#
#
#
#

#
# #
# var = """
# hello  $$$$ %%%% * ( )))           all            how
# are you        $$$$ %%%% * ( )))         hope
# all are   $$$$ %%%% * ( )))      revising            python
# """
# print("\n ================================== \n")
#
# op = re.sub(r'[^A-Za-z0-9]{1,}', '' , var)
# print(op)
#




#
#
# var = "my mobile nums are 7411694426 and 9986019197abcd"
# res = re.sub('[0-9]{10}', 'MOBILENUM', var)
# print(res)
