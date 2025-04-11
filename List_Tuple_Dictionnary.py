#INDEXING IN LIST
# xz=['s','w','e','a','r','a','5','4','6']
# print(xz[::-1])
# print(xz[:4])
import copy

#INDEXING IN TUPLE
# cv=('s','w','e','e','t','h','e','a','r','t')
# print(cv[::-1])
# print(cv[-3:])

#INDEXING IN DICTIONARY
# fy={"sw":5,"ar":46}
# print(fy["sw"])

#CONCATENATION IN LIST
# l=['c','h','a']
# o=['k','k','k']
# v=['a','r','a']
# e=['<3']
# print(l+o+v+e)

#CONCATENATION IN TUPLES
# r=('c','h','o')
# o=('t','t','u')
# h=('k','a','a')
# y=('r','a',':)')
# print(r+o+h+y)

#CONCATENATION DOES NOT WORK IN DICTIONARY

#DUPLICATION IN LIST
# df=['5','4','6']
# print(df*3)

#DUPLICATION IN TUPLE
# nm=('chocobar')
# print(nm*5)

#DUPLICATION IN DICTIONARY DOES NOT WORK

#LENGTH, TYPE IN DICTIONARY, TUPLE, LIST
# we={'A':'SWETHA','B':'SHREE','C':'ARAVINDH'}
# us=('l','i','b','i')
# you=['r','o','h','y']
# print(len(we))
# print(type(we))
# print(len(us))
# print(type(us))
# print(len(you))
# print(type(you))

#ADDING SINGLE ELEMENT TO THE END OF THE LIST - APPEND
# marks=[20,35,46,39]
# marks.append(49)
# print(marks)

#ADDDING A MULTIPLE ELEMENT TO THE END OF THE LIST - EXTEND
# raj=[12,34,56,43,8]
# raj.extend([46,5,78])
# print(raj)

#ADDING A SINGLE ELEMENT AT DESIRED POSITION - INSERT
# vb=[18,7]
# vb.insert(1,46)
# print(vb)

#ADDING SINGLE KEY VALUE PAIR IN DICTIONARY - SETDEFAULT
# io={'A':5,'B':46,'C':8}
# io.setdefault('D',18)
# print(io)

#ADDING MULTIPLE ELEMENT KEY VALUE PAIR IN DICTIONARY - UPDATE
# rt={'Q':1,'W':2,'E':3,'R':4,'T':5,'Y':6}
# fg={'A':0,'S':9,'D':8,'F':7,}
# (fg.update(rt))
# print(fg)
# (rt.update(fg))
# print(rt)

#ADDING ELEMENTS DOES NOT WORKS IN TUPLE, BECAUSE TUPLE IS IMMUTABLE

#DELETE THE ELEMENTS IN LIST BY MENTIONING INDEX VALUES - DEL
# zm=[1,2,3,4]
# del zm[0:3]
# print(zm)

#DELETE THE ELEMENT BUT WE CAN RESTORE THE ELEMENTS BY MENTIONING INDEX VALUE- POP
# al=[3,4,6,8,0]
# al.pop(0)
# print(al)

#DELETE THE ELEMENT BY MENTIONING SPECIFIED VALUE AND NOT INDEX VALUE - REMOVE
# qp=[12,23,34,45,56,67,78,89]
# qp.remove(45)
# print(qp)

#IF THE VALUES PRESENT MULTIPLE TIMES, REMOVE FUNCTION REMOVE ONLY THE FIRST OCCURENCE - COUNT
# a=[1,2,1,3,1,4,5,2,3,1,2,6,5,8]
# cnt=a.count(1)
# print(cnt)
# for x in range(cnt-1):
#     a.remove(1)
#     print(a)

#DELETE ALL THE DATA IN LIST COMPLETELY - CLEAR
# ty=[89,87,65,43,21]
# ty.clear()

#OVERWRITING OR REPLACE THE VALUE IN THE LIST
# hj=[3,4,5,6,67]
# hj[4]=7
# print(hj)

#UPDATE DOES NOT WORK IN TUPLE AND DICTIONARY

#SORT AND REVERSE IN LIST - IT DOES NOT WORKS IN TUPLE AND DICTIONARY
# ui=[45,23,65,22,887,35,55]
# jk=['swetha','varsha','booms','sakthi','sowbi']
# ui.sort()
# jk.sort()
# print(ui)
# print(jk)
# ui.reverse()
# jk.reverse()
# print(ui)
# print(jk)

#COPY FUNCTION IN LIST
# a=[1,2,3,4,5,6]
# b=copy.deepcopy(a)
# print(b)
# c=copy.copy(a)
# print(c)

# LIST FUNCTION TO CONVERT TUPLE INTO LIST AND TUPLE FUNCTION TO CONVERT LIST INTO TUPLE
# tup=(34,56,78,33,88)
# print(list(tup))
# li=[12,56,78,34,55,22]
# print(tuple(li))

#RETURNS KEYS , VALUES AND ITEMS
# ty={'A':5,'S':46}
# print(ty.keys())
# print(ty.values())
# print(ty.items())

# SET FUNCTION - REMOVE DUPLICATES AND KEEP UNIQUE ELEMENTS IN LIST, DICTIONARY, TUPLE
# l=[1,1,2,2,3,3,3,1,23,45,56,4,3,6]
# t=(1,2,3,4,5,12,1,2,3,4,5)
# d={'S':5,'W':46,'E':5}
# print(set(l))
# print(set(t))
# print(set(d))

#SINGLE DIMENSIONAL DATA
data=[1,2,3,4,5,6,7]
print(data[2])
#TWO DIMENSIONAL DATA
data=[10,[20,30],40,50]
print(data[1][1])
#THREE DIMENSIONAL DATA
data=[12,23,[34,56,45,[45,44,89],67],65,87,97,99]
print(data[2][3])
print(data[5])
print(data[2][3][2])
print(data[2][4])