#print("Hello world...")

#1
# to check version use ---- python --version
# to upgrade python use ---- python --upgrade

#2
# Program to addition of three variable

# a=10
# b=20
# c=30
#
# print(a+b+c)

#3
# addition of two variable
# a=10
# b=30
# print(a+b)

#minus
# a=100
# b=50
# print(a-b)

#*
# a=30
# b=3
# print(a*b)

#-+
# a=20
# b=40
# c=60
# print(a+b-c)

#4
#code to find id of variable, char and value

# a=5
# a=5
# 10
# a="Ankit" - case sensitive
# b="ankit" - case sensitive
# print(id(a))
# print(id(a))
# print(id(10))
# print(id(a))
# print(id(b))
# print(id(a))

#5
# identifier
# defination :- The name in a python is called identifier
#  varible name
#   module name
#  def   function name (function creates with def keyword)
#  class name

# rules
# alpha.b
# 1 - 9 range
# variable not start with digit

#examples of identifier if valid or not
# 132a=10
# print(123a) - invalid

# ab10=20
# print(ab10) - valid

# _60=20
# print(_60) - valid

# _a=31
# print(_a) - valid

# %a=12
# print(%a) - invalid

# a4444=10
# print(a4444) - valid

#6
# Python is case sensitve language
# example:
# A=20
# a=20
# print(a)
#
#6.1
# _a=10 ---- if variable start with (_) then its called privet
# __a=20 ----- if variable start with (__) then its called strongly privet

#7


# import keyword
# d=keyword.kwlist
# print(d)

"""
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
#  'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise'
#  'return', 'try', 'while', 'with', 'yield']
"""

# print(False - True)

#code to find id of variable, char and value

# a=5
# 10
# # print(id(a))
# print(id(10))
# print(id(a))

# stack memory store char LIKE(a, b c means chars)
# Python heap space store value ex (10, 15)

# id is inbuilt functionality

#datatypes:-----

# use "type" inbuild functionalty to check data type

# 1) int
# b=40
# print(type(b))

# 2) flote
# d=1.9
# print(type(d))

# 3) complex
# b=4.5+10.1j
# print(type(b))
# print(b.real)
# print(b.imag)

# b=4.5-10.1j
# print(type(b))
# print(b.real)
# print(b.imag)

# b=4.5*10.1j
# print(type(b))
# print(b.real)
# print(b.imag)

# 4) bool

# a=True
# b=False
# print(type(a))
# print(type(b))
#
# print(a+b)
#
# # 5) string

# multiple line string can be with ("""abc""")

# immutable ---- not able to change
# mutable - can change


# 6) bytes
# bytes data type range should be 0 - 256 (means 0 to 255)

# list is data type but array is not data type
# array contains same dt value
# list contains multiple data type value


# -----------------------------------------x------------------------------------------------

# conversion of data type into another data type

# Type casting

# int float string complex bool

# 1) convert into int

# 1.1) to string

# a=20
# print(a)
# print(type(a))
# a1=str(a)
# print(a1)
# print(type(a1))

#1.2 flote to int

# a=20.5
# print(a)
# print(type(a))
# a1=int(a)
# print(a1)
# print(type(a1))

# #1.3 complex to int
# a=10+20j
# print(a)
# print(type(a))
# a1=int(a)
# print(a1)
# print(type(a1))

# complex to int data type will not be able to convert. error will shown on terminal

# #1.4 string to int

# a="10"
# print(a)
# print(type(a))
# a1=int(a)
# print(a1)
# print(type(a1))

# rule:
# chars will not convert
# only whole number convert

#1.4 bool to int
# a=True
# print(a)
# print(type(a))
# a1=int(a)
# print(a1)
# print(type(a1))

# 2) convert into flote

# 2.1 int

# a=20
# print(a)
# print(type(a))
# a1=float(a)
# print(a1)
# print(type(a1))

# 2.2 bool

# a=True
# print(a)
# print(type(a))
# a1=float(a)
# print(a1)
# print(type(a1))

# # 2.3 str
#
# a="10.5"
# print(a)
# print(type(a))
# a1=float(a)
# print(a1)
# print(type(a1))

# 2.3 complex
#
# a=20+5j
# print(a)
# print(type(a))
# a1=float(a)
# print(a1)
# print(type(a1))
#
# This will not able to convert

#3) convert from int, flote, bool, complex to string

# 3.1 int to str with three variables

# c=20
# d=5
# e=5
# print(c,d,e)
# c2=str(c+d+e)
# print(c2)
# print(type(c2))

# Output== 30 in str

# # 3.2 flote to str
#
# d=20.5
# print(d)
# print(type(d))
# d2=str(d)
# print(d2)
# print(type(d2))

# Output== 20.5 in str

# 3.3 bool to str
# b=False
# print(b)
# print(type(b))
# b2=str(b)
# print(b2)
# print(type(b2))

# Output== False in str

# # 3.4 complex to str
#
# n=25+5j
# print(n)
# print(type(n))
# n2=str(n)
# print(n2)
# print(type(n2))

# Output== 20+5j in str

# new code

# a=20
# b=10
# c=30.5
# d=complex(a+b,c)
# print(d)
# output==30+30.5j

# 4) convert into bool

# 4.1 int

# b=20
# print(b)
# print(type(b))
# b2=bool(b)
# print(b2)
# print(type(b2))


# 4.2 str

# b="0"
# print(b)
# print(type(b))
# b2=bool(b)
# print(b2)
# print(type(b2))

# # 4.3 flote
#
# b=0.0
# print(b)
# print(type(b))
# b2=bool(b)
# print(b2)
# print(type(b2))

# 4.4 complex

# b=20+5j
# print(b)
# print(type(b))
# b2=bool(b)
# print(b2)
# print(type(b2))

# 5 convert into complex

# # 5.1 int
#
# b=20
# print(b)
# print(type(b))
# b2=complex(b)
# print(b2)
# print(type(b2))

# # 5.2 str
# #
# b="20"
# print(b)
# print(type(b))
# b2=complex(b)
# print(b2)
# print(type(b2))
#
# # 5.3 bool
#
# b=True
# print(b)
# print(type(b))
# b2=complex(b)
# print(b2)
# print(type(b2))
#
# # # 5.3 flote
#
# b=50.5
# print(b)
# print(type(b))
# b2=complex(b)
# print(b2)
# print(type(b2))

# new
# a=20
# b=10
# c=30.5
# d=complex(a+b,c)
# print(d)

# a=20
# b=30
# c=20
# d=str(a+b+c)
# print(d)

# a=2
# b="ANkit"
# print(a*b)
#
# a=20
# b=2
# print(a//b)

# print(2**5)

# a=20
# b=30
# c=(str(a)+str(b))
# print(c)
# print(20**2**2)

# a=20
# b=2
# c=float(a)**float(b)
# print(c)
#
# a="how are you ?p["
# print(a)


# a=str(input("enter your name"))
# # print(s)


# Operators symbols

#Opertors is a symbol that perform certain operation

# + - * /

# Aritmetic operator

# + (concatanetion)
# Rules:=== 1st and 2nd both the value of variable should be in string data type
#
# - (minus)
#
# * (multi --- repeat)
# Rules:===== 1) one value of variable should be in string data type and
# second value of varibale should be in int data type
#
# 2) If both the value of variable are same then multiplication will perform
#
# 3) If one value is string and one value is int then repetation of string value will perform
#
# / (division)  ====
# Rules:==== / slash operator always perform floting point aritmetic hence it
# will return flote value
#
# // (flore devision) ====
# Rules:===== // slash operator (flore division)
# can perform both flote and int, if argument are int type then result is int
# type, if atleast one argument is flote type then result is flote type

# % Modulas
# % Modulas will shown output is in reminder (Ex: 10%3 (3x3=9) (remaning 1 is remainder))

# ** Exponent operator / Power operator
# Optput will shown in belwo format
# Ex===
# 1) print(10**3)
# 2) 10 x 10 x 10 = 1000 (The output is 1000)


# Program of + (concatenation)

# a=20
# b=30
# c=str(a)+str(b)
# print(c)
#
# #programm of - (minus)
# c=30
# b=10
# print(c-b)

# program of * (Repetation)

# h="Ankit"
# n=4
# print(h*n)

# Program of / division

# r=10
# h=2
# print(r/h)

# program of // flore division

# t=10
# a=2
# print(t//a)

# program of % Modulas

# o=10
# t=4
# print(o%t)

# Program of ** Exponent / power operator
#
# f=10
# t=3
# print(f**t)

# a="1"
# print(ord("10"))

# Relational opertor

# To assigne the value

# symbols
# <
# >
# >=
# <=

# Relational operator output will be on Bool data type (true or false)

# a=20
# b=30
# c=80
# n=50
# print(a+b<c+n)

# a=20
# b=50
# print(b<a)

# r=4.5
# s=4.6
# print(r>s)

# f=30
# s=30
# print(f<=s)

# ank="pro"
# enter="value"
# print(ank>enter)
# print(ord("p"))
# print(ord("v"))

# equality operator
# To check the output value

# symbols

# ==
# !=

# q=30
# w=-30
# print(q==w)
#
# a=20
# b=30
# c=80
# n=50
# print(a+b==c+n)

# t=00
# q=0
# print(t!=q)

# logical operator
# logic

# And
# or
# Not

# And
# If all the value are same then output will be true
#If only single value false then output will be false

# Or
# If all the value are same then output will be False
#If only single value true then output will be true

# Not
# This will reverse the output

# ankit=20 > 30
# ank=40 > 35
# c=ankit and ank
# print(c)

# i=10 < 20
# o=50 < 60
# print(i and o)

# b=70 > 40
# g=67 < 33

# print(b or g)

# t=33 > 33
# q=67 < 33

# print(t or q)

# a= not 10>20
# b= not  10<30
# print(a)
# print(b)

# f=20
# d=40
# c=float(f)
# e=float(d)
# print(c>e)
#
# f=20
# d=40
# c=str(f)
# e=str(d)
# print(c!=e)

# f=20>30
# d=40<30
# e=100 > 20
# print(f<d)
# print(d>e)
# print(f and d or e)


# a=10>5
# v=20>100
# c=20>5
# f=30>20
# h=50>30
# y=a and v, c or f,h
# print(y)

# a=20
# b=30
# f=55
# r=30
# c=str(a)+str(b)
# j=str(f)+str(r)
# print(c)
# print(j)
# print(c>j)
#
# data=input("Click any button and enter on terminal to show the value")
# c=10
# f=30
# f(input(c>f))
# print(f)
#
#
#
#
# name=input("what is your name")
# print("hello, " + name )


# a=1
# c=(bool(a))
# d=(str(c))
# print("Value is, " + d)


# num1=input("enter the number: ")
# num2=input("enter the number: ")
# c=int(num1)
# d=int(num2)
# r=num1<num2
# print(r)

# / Identity operator: is, is not (To check if value is stored in python memory or not)
# Output will be on bool dt

# / Membership operator: in,   not in ((To check if specific value under variable is there or not)
# Output will be on bool dt


# Ternary operator::: if else part


# n=int(input("Enter first number: "))
# g-n
# s=n
# for i in range(4):
# n=int(input("Enter next number: "))
# if n>g:
# g=n
# if n<s:
# s-n
# print()
# print("Largest number is: ",g)

# numbers = [5, 2, 8, 1, 9]
# largest = numbers [0]
# smallest = numbers [0]
#
# for numbers in numbers:
#     if numbers > largest:
#         largest = numbers
#     elif numbers < smallest:
#         smallest = numbers
#
# print("Largest numbers:", largest)
# print("Smallest numbers:", smallest)

# num1 = (input("enter the value"))
# num2 = (input("enter the value"))
# largest = num1
# smallest = num2
#
# for num1 in num2:
#     if num1 > largest:
#         largest = num2
#     elif num1 < smallest:
#         smallest = num2
#
# print("Largest numbers:", largest)
# print("Smallest numbers:", smallest)


# a=int(input("first: "))
# b=int(input("secon: "))
# c=int(input("third: "))
# if a<c:
#     print("smallest is",a)
# else:
#     print:("smallest is",b)
#
# else:
#      if b<c:
#          print('smallest is',b)
#      else:
#          print("smallest is", c)

#
#created 3 variable of input with flote dt:
# user1=float(input('Enter first value: '))
# user2=float(input(' Enter second value: '))
# user3=float(input('Enter third value: '))
# #defined variables below:
# n1=user1
# n2=user2


# n3=user3
# #applied (min) to show smallest value:
# Small = min(n1,n2,n3)
# print('Smallest value is',+ Small)

# Flow control

# conditional : if elif else
# transfer : break pass continue
#itrative  : for while
# Python vertual machine follows interprative

# The execution of flow is line by line and the execution of the compliler it proced the all code and gives output at once time


# #3 input variables
# value1=(input("First value: "))
# value2=(input("second value: "))
# value3=(input("third value: "))
# v1=float(value1)
# v2=float(value2)
# v3=float(value3)
# if(v1<v2 or v1<v3):
#     small=v1
# elif(v2<v1 or v2<v3):
#     small=v2
# else:
#     small=v3
#     print(small)

# created 3 variable
# user1=int(input('Enter first value: '))
# user2=int(input(' Enter second value: '))
# user3=int(input('Enter third value: '))
# #variables:
# n1=user1
# n2=user2
# n3=user3
# if n1<n2 or n1<n3:
#     small = n1
# elif n2<n1 or n2<n3:
#     small = n2
# else:
#     small = n3
# print("Your lowest value is", + small)


# # 3 variables of input
# user1=int(input('Enter first value: '))
# user2=int(input(' Enter second value: '))
# user3=int(input('Enter third value: '))
# if user1<user2 or user1<user3:
#     small = user1
# elif user2<user1 or user2<user3:
#     small = user2
# else:
#     small = user3
# print("Your lowest value is", + small)

# 3 variables of input
# user1=int(input('Enter first value: '))
# user2=int(input(' Enter second value: '))
# user3=int(input('Enter third value: '))
# if user1<user2 and user1<user3:
#     print("Your small value is:", user1)
# elif user2<user1 and user2<user3:
#     print("Your small value is:", user2)
# else:
#     print("Your small value is:", user3)


# brand = input("enter your brand:")
# if (brand == "redbull"):
#     print("Tanujas brand")
# elif (brand == "fizz"):
#     print("Meghas brand")
# elif (brand == "Thumsup"):
#     print("Ankits brand")
# elif (brand == "oldmonk"):
#     print("Ayush brand")
# elif (brand == "Bislery"):
#     print("Mukund brand")
# elif (brand == "pepsi"):
#     print("pradip brand")
# elif (brand == "budwiser"):
#     print("pranav brand")
# else:
#     print("mrunals brand")

# Menu_of_food=input("select your menu:")
#
# if (Menu_of_food == "masala dosa"):
#     print("Your masala dosa is ready to serve")
# elif (Menu_of_food == "Sambar vada"):
#     print("Your sambar vada is ready to serve")
# elif (Menu_of_food == "aloo bonda"):
#     print("Your aloo bonda is ready to serve")
#
# else:
#     print("Sorry this food is not available right now or try after some time")

# Menu_of_food=input("select your menu:")
#
# if (Menu_of_food == "masala dosa"):
#     print("Your masala dosa is ready to serve")
# if (Menu_of_food == "Sambar vada"):
#     print("Your sambar vada is ready to serve")
# if (Menu_of_food == "aloo bonda"):
#     print("Your aloo bonda is ready to serve")
#
# else:
#     print("Sorry this food is not available right now or try after some time")

# a=input("What would you like to drink:")
# print("Here is your", a)
# food=input("select your food:")
#
# if (food == "masala dosa"):
#     print("Your masala dosa is ready to serve")
# elif (food == "Sambar vada"):
#     print("Your sambar vada is ready to serve")
# elif (food == "aloo bonda"):
#     print("Your aloo bonda is ready to serve")
#
# else:
#     print("Sorry this food is not available right now or try after some time")

# # All foods are available
# Drink=input("What would you like to drink:")
# print("Here is your", Drink)
# Food=input("what would you like to eat:")
# print("Here is your", Food)
# print("Wait for few minutes to ready")
# print("Enjoy!!")

# t=int(input("Enter your full name:"))
# a=int(input("Enter your age for driving licence:"))
# if a>17:
#     print("Ready to apply")
# else:
#     print("Not ready to apply")

#itrative
#Defination === If we want to execute some action for every element present in sequence

# d=[8,20,40,34,10,0,6, "Mrunal"]
# for a in d:
#     if a % 5==00:
#       print(a)


# d=[1,2,3,4,5,6,7,8,9,10]
# a=int(input("Enter your number:"))
# for r in d:
#
#     print(a*r)

# num1=input("enter the number: ")
# num2=input("enter the number: ")
# c=int(num1)
# d=int(num2)
# r=num1<num2
# print(r)

# d="Ankit"
# for r in d:
#
#     print(end=r)


# d="Ankit"
# for r in d:
#     print(r * 4)

# s="Ankit"
# for r in s:
#     print(end=r * 4)

# d=[1,2,3,4,5,6,7,8,9,10]
# a=int(input("Enter your number:"))
# for r in d:
#
#     print(a*r)

# d=range(1,11)
# a=int(input("Enter your number:"))
# for r in d:
#
#     print(a*r)


# while loop

# Code will stop if value is false
# If value is true then loop will be infinite

# practice:

# x=30
# while x>10:
#     x=x-1
#     print(x)

# x=30
# m=int(input("Enter the value"))
# while x>m:
#     x=x-1
#     print(x)

# x=int(input("Enter 1st value:"))
# m=int(input("Enter 2nd value:"))
# while x>m:
#     x=x-1
#     print(x)

# x=int(input("Enter 1st value:"))
# m=int(input("Enter 2nd value:"))
# g=int(input("Enter 2nd value:"))
# t=int(input("Enter 2nd value:"))
# while x>m and g>t:
#     x=x-1
#     print(x)


# Transfer statement

# n=[100,200,300,400]
# for i in n:
#     if i==100:
#         continue
#     print(i)
#     if i==300:
#         continue
#     print(i)
#
# n=[100,200,300,400]
# for i in n:
#     if i==300:
#         continue
#     print(i)

# n="Ankit"
# for i in n:
#     if i=="k":
#         continue
#     print(end=i)


# v="pythonpractice"
# t="aeiouAEIOU"
# for i in v:
#     if i in t:
#         print(end=i)
#     pass


# x=30
# while x>10:
#     x=x-1
#     print(x)

# x=30
# m=int(input("Enter the value"))
# while x>m:
#     x=x-1
#     print(x)

# x=int(input("Enter 1st value:"))
# m=int(input("Enter 2nd value:"))
# while x>m:
#     x=x-1
#     print(x)

# x=int(input("Enter 1st value:"))
# m=int(input("Enter 2nd value:"))
# g=int(input("Enter 2nd value:"))
# t=int(input("Enter 2nd value:"))
# while x>m and g>t:
#     x=x-1
#     print(x)


# Transfer statement

# n=[100,200,300,400]
# for i in n:
#     if i==100:
#         continue
#     print(i)
#     if i==300:
#         continue
#     print(i)
#
# n=[100,200,300,400]
# for i in n:
#     if i==300:
#         continue
#     print(i)

# n="Ankit"
# for i in n:
#     if i=="k":
#         continue
#     print(end=i)

# (""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  ""
#  "sfdsfdsfdsf"
#  "ddddddddddddddddsdsadasdasdsadsdasdsadsadsad")


# a=[1,2,3,4,5]
# print(a[::-1])


# n=input("enter main str:")
# t=input("enter sub str:")
# for t in n:
#     if t==n:
#         print("very good")
#     else:

#         print("not good")




#///////////////////////////////////////////////

# u1 = int(input("Enter the first value:"))
# u2= int(input("Enter the second value:"))
# if u2 == u1:
#     print("Value is equal")
# else:
#     print("value is not equal")
# #
# # #//////////////////////////////////////////////////
# #
# e = (input("Enter the first value:"))
# t = (input("Enter the second value:"))
# if t > e:
#     print("Value is greater")
# else:
#     print("value is smaller")
#////////////////////////////////////////////////////

# u1 = int(input("Enter the first value:"))
# u2= int(input("Enter the second value:"))
# if u2 == u1:
#     print("Value is equal")
# else:
#     print("value is not equal")
#
# # #//////////////////////////////////////////////////////
# #
# u1 = (input("Enter the first char:"))
# u2= (input("Enter the second char:"))
# if u2 > u1:
#     print("very good")
# else:
#     print("not good")
#
# #///////////////////////////////////////////////////
# u1 = (input("Enter the main string:"))
# u2= (input("Enter the sub:"))
# if u2 != u1:
#     print("not equal")
# else:
#     print("equal")


# #//////////////////
# u1 = (input("Enter the main string:"))
# u2= (input("Enter the sub:"))
# if u2 <= u1:
#     print("good")
# else:
#     print("not good")

# #//////////////////
# u1 = (input("Enter the main string:"))
# u2= (input("Enter the sub:"))
# if u2 >= u1:
#     print("good")
# else:
#     print("not good")


# u1 = (input("Enter 1st:"))
# u2 = (input("Enter 2nd:"))
# u3 = (input("Enter 3rd:"))
# u4 = (input("Enter 4th:"))
#
# if u2 == u1:
#     print("True")
# else:
#     print("false")
# if u3 == u2:
#     print("True")
# else:
#     print("false")
# if u4 == u3:
#     print("True")
# else:
#     print("false")



# s="ankit"
# print(s.find("a"))


# string

# Concatenation with slicing
# count will be minus 1 in slicing

# Concatenation

# an=1234
# ss=5678
# dr=str(an)
# dt=str(ss)
# print(dr[0:2]+dt[0:1])
# #///////////////////////////////////////////////////
#
# # Repetition with if else
#
# a=input("Enter the 1st string")
# s=int(input("Enter the value"))
# b=input("Enter the 2nd string ")
# n=int(input("Enter the value"))
#
# print(a*s, "and", b*n)
# if a == b:
#     print("equal")
# else:
#     print("Not equal")
#
# #Membership
#
# n="Ankit"
# for i in n:
#     if i==n[1]:
#         continue
#     print(end=i)
# #////////////////////////
#
# # strip: lstrip: rstrip
# #///////////////////////////////////////1
# Ank="Backend dev    ****@#$    "
# print(Ank.rstrip(" *@#$"))
#
# #///////////////////////////////////////////2
# b="                 $Endgame"
# print(b.lstrip("    $"))
#
# #////////////////////////////////////////////3
# n="                 ndtv                     "
# print(n.strip("    "))
#
#
# # Find and index
# #///////////////////////////// 1
# j="Anknitt"
# print(j.find("A"))
#
# #////////////////////////// 2
# t="PythonPPythonn"
# print(t.rfind("PP"))
#
# #///////////////////////////// 3
# y="       *pythonpython"
# print(y.rindex("p"))
# t=y.lstrip(" *")
# print(t.rindex("p"))
#
# #///////////////////////////// 4
# # rfind random code
# a="Endgameendgame"
# b="Endgameendgame"
# x=a.rfind("m")
# y=b.rfind("g")
# print(x+y)

# string
# replace()///////////////////////////

# g="hpboss new"
# f= "gross"
# print(g.replace("hpboss","gross"))

# # count ()
# n="triptripy"
# print(n.count("p"))

# # split()
# # h="draganddrop"
# # t="drag"
# # y="drop"
# # print(h.split(t))
# # print(h.split(y))

# join()

# f="trip", "to", "goa"
#
#
#
# d="&".join(f)
# print(d)

# n="i want to play games"
# t=(n.replace("games", "other"))
# h=(n.replace("i", "you"))
# print(t+h)


# g="inter", "Now"
# print("@".join(g))
#
# p="BEdevlopers"
# print(p.split("BE"))

# ank="Avengers"
# u=(ank.replace("Ave", "rev"))
# print(u)

#replace
# i="Glean maxwell"
# y=i.replace("Glean", "Crick")
# print(y)

#join
# i="Glean maxwell", "Trple"
# print("@".i,join)

# #split
# s="Endgame"
# print(s.split("E"))

#count
# n= "ebcabcabcbc"
# print(n.count("a"))

#Cases///////////////////////////////////////////////////////
#upper() ---- to convert small latters to capital
#lower() ---- to convert capital to small latters
#swapcase() - upper to lower and lower to upper , it will reverse
# title() - it will capital first latter of all words
#capitalize() - it will capital first latter of first word in string

# startswith() == it will starting (Bool output)
# endswith() == it will ending (Bool output)

# to check character in string

# isalnam() - to check if string data contain alpha amd number
# isalpha() -  to check if string data contain alpha
# isdigit() -  to check if string data contain digit
# islower() - to check if string data contain lowercase
# isupper() - to check if string data contain uppercase
# istitle() - to check if string data contain title
# isspace() - to check if string data contain spaces

# a="python devs"
# print(a.islower())
#
# b="python devs"
# print(b.isalpha())
#
# c="python devs"
# print(c.isalnum())
#
# d="python devs"
# print(d.isupper())
#
# d=" python devs"
# print(d.isspace())
#
# e=" python devs"
# print(e.istitle())
#
# f=" python devs"
# print(e.isdigit())

# name=input("Enter your full name:")
# mobile=input("Enter your valid mobile number:")
#
# if name.isalpha() or name.isspace():
#     print("Correct")
# else:
#     print("Invalid")
# if mobile.isdigit():
#         print("correct")
# else:
#         print("Invalid")

# phone=input("Enter mobile no:")
# name=input("Enter first name:")
# if len(phone) !=10:
#     print(phone,":Invalid")
# else:
#     print(phone,":Valid")
# if name.istitle() and name.isalpha():
#     print(name,":Correct")
# else:
#     print(name,":Invalid")

# format in string
# 1
# menu= "wada pav"
# addon = "Nothing"
# print("my menu is {} and addon is {}".format(menu,addon))






# r="a1b2c3"
# print(r[0:6:2]+r[1:6:2])

# r="a1b2c3"
# for i in r:
#     if i in "abc":
#         print(i)


#/////////////////////////////////////////////////////////////////////////////////////////////////////

# list
# list is mutable (changable)
# duplicate data allowed
#hetro - more than one data type can stroed in list

# list :

# s=[1,1.2,"mrunal"]
# # print(type(s))
#
# s1=[1,2,3,"python"]
# print(s1[3][4])

# insertion order is preserved
# duplicate data allowed

# s="python"
# print(s[0])

# [], hetro, ,duplicate are allowed, insertion order is preserved, dynamic,mutable,indexing slicing
# comma
# d=[1,2,3,4,100.34,1]   ==> dynamic   change in  mutable

# ===list===

# s=[]
# s1=[1,2,3,4,5]

# s=eval(input("enter your list"))
# print(s)
# print(s[1])

# list()   range

# s=list(range(2,21,2))
# print(s)
# d="ashwiniandmegha009"
# s1=list(d)
# print(s1)

# split

# s="mrunal@is@django@developer"
# s1=s.split("l")
# print(s1)
# #
# s2=list(s)
# print(s2)


# s1=["python",1,2,4]
#
# s="python"

# range
# append list

# list is a mutable   change
# immutable non change


# indexing

# s=[1,2,3,4,6]
# print(s)
# s[0]=100
# print(s)

# s=[10,3,7,90,12,56,2,4]
# codezs
# 8:46 PM
# list     len
# length
#
# # len
# s=[1,2,3,4,5,6,8,"python"]
# print(len(s))

# 2)count
# s=[1,1,2,3,4,5,6,0]
# print(s.count(0))

# 3)index
#
# s=[1,3,2,4,5,6,1,2]
# print(s.index("mru"))

# ===
# append: ===> add

# append:  value/data/ element   add   ==> list  ==> end of the list

# s=[]
# s.append("mrunal")
# s.append("ankit")
# s.append(6.7)
# print(s)

#
# s1=[1,2,4,5]
# s1.append("python")
# print(s1)

# s=[10,3,7,90,12,56,2,4]
# for i in s:
#     if i%2 !=0:
#         print(i)
#////////////////////////////////////////////////////////////////////////////////////////////


# method 1

# a=[1,1,"python",1,2,3,4,5,5,5]
# print(a[2][2])

# method 2
# b=eval(input("Enter the value"))
# print(s)
# print(s[1])

#method
# s=list(1)
# print(s)

# ank=[10,3,7,90,12,56,2,4]
# for i in ank:
#     if i % 2 !=0:
#         print(i)

# ank=[10,3,7,90,12,56,2,4]
# u=0
# t=0
# while i < len(ank):
#     if num%2!=0:
#         u+=num
#         t+=1
#         print(u)

# value replaced

# a=[1,2,3]
# a[1]=100
# print(a)

# b=[10,12,13]
# b.append("an")
# print(b)
#
# c=[10,12,13]
# c.insert(1,100)
# print(c)

# an=[20,22,23,2,4,5,6,]
# t=(an[0:7:2])
# print(t)


# Method 1

# r="a1b2c3"
# print(r[0:6:2]+r[1:6:2])
#
# #//////////////////////////////////////////////
#
#Method 2
# t="a1b2c3"
# el=[]
# for i in t:
#     if i.isalpha():
#         el.append(str(i))
#         print(end=i)
# for i in t:
#     if i.isdigit():
#         el.append(int(i))
#         print(end=i)

# t="a1b2c3"
# for i in t:
#     if i in "abcdefghijklmnopqrstuvwxyz":
#         print(i)
# for i in t:
#     if i in "1234567890":
#         print(i)

# t="a1b2c3"
# # print()
# # name = "mrunal"
# # age= 29
# # city =  'sangadi'
#
#
# print("my name is {} and my age is {}".format(age,name))
# # print("my name is {1} and my age is {0} and my city name is {2}".format(age,name,city))
# # print("my name is {n} and my age is {a} and my city name is {c}".format(a=age,n=name,c=city))


# y=[1,2,3]
# y[2]=10
# print(y)

# s=[]
# s.append([1,2,3,4,5,6,])
# print(s)

# ////////////////////////////////////////////////////

# remove()

# remove function will remove specific element from stdlib_list
# if there is duplicate data then it will remove first element of duplicate
# if element is not in list then shows value error


# a=[1,2,3,4,5,6]
# a.remove(4)
# print(a)
#
# a=[1,2,3,4,4,4,4,5,6]
# a.remove(4)
# print(a)
#
# a=[1,2,3,4,5,6]
# a.remove(10)
# print(a)

# pop()
# in pop last element from list will remove and removed element will shown in output
# we can remove specific element using index number

# t=[1,2,3,4,5,6,7]
# t.pop()
# print(t)
#
# t=[1,2,3,4,5,6,7]
# t.pop(5)
# print(t)

# reverse()
# it will reverse the elements under list

# a=[10,20,30]
# a.reverse()
# print(a)

# a=[10,20,30]
# a.reverse()
# print(a)

# sort()
# sort() will manage the oreder into accedning order from list

# a=[20,10,5,70,2]
# a.sort()
# print(a)

# for decending use sort()first then use reverse()
# method 1
# a=[20,10,5,70,2]
# a.sort()
# a.reverse()
# print(a)

# method 2
# a=[20,10,5,70,2]
# a.sort(reverse=True)
# print(a)

# alise and cloning== shalow copy and deep copy

# nested list
# list comparison
# list compresstion
# clear()

# extend()
# One list extend to another list

# r=[1,2,3,4,5]
# r1=[3,2,1,]
# r.extend(r1)
# print(r1)

# a=[]
# b=[1,2,3,4,5,]
# a.extend(b)
# a.append("ankit")
# print(a)
# for i in a:
#     if i in ["ankit"]:
#         print(i)

# a=eval(input("value"))
# b=eval(input("enter"))
# a.append(b)
# print(a)
# if a in [2]:
#     print(a)

# s=(1,2,3,[1,2,3])
# print(s)
# s[3][1]=20
# print(s)


# s=list(range(2,21,2))
# print(s)

# a=[i for i in range(2,21,2)]
# print(a)

# a=[i*3 for i in range(1,11)]
# print(a)

# s=[1,2,3,4,5,6,7,8,9,10]
# ss=[i for i in s if i%2==0]
# print(ss)

# s=[1,2,1,1,3,3]
# s1=set(s)
# print(s1)

# a=(10,20,30)
# b=10
# c=30
# d=10
#
# mm=a
# print(mm)

# a=(1,2,3,4,5)
# 1(a)=t
# print(t)

# a="abc123"
# if a.isalnum():
#     print("yes")

# codezs
# 8:15 PM
# # union: it return all element from both set  (|)
#
# a={1,2,3,4}
# b={3,4,5,6}
#
# print(a.union(b))
# print(b.union(a))
#
# print("===>",a|b)
# print("===>",b|a)
# codezs
# 8:19 PM
# # intersection :   it return common element from set  (&)
#
#
# print(a.intersection(b))
# print(b.intersection(a))
# print(a&b)
# print(b&a)
# codezs
# 8:23 PM
# # difference  (-): a.difference(b)
# # print(b.difference(a))
# # print(b-a)
# codezs
# 8:28 PM
# # symmentric_difference  (^)
#
# print(a.symmetric_difference(b))
# print(a^b)
# codezs
# 8:37 PM
# # set   comprehension
# m={2,3,4,5,2}
# s={x*x for x in m}
# print(s)
# ryq-bvob-bjs

# codezs
# 8:16 PM
# import json
# d1 = {'python': 95, 'java': 94, 'c++': 90}
#
# json_data = json.dumps(d1)    dict   ==> json
# print(json_data)
# dict_data = json.loads(json_data)     json ==> dict
# print(dict_data)
# ryq-bvob-bjs

# a=[1,2,3,3]
# a[20]
# print(a)

# a={"a":1,"b":2,"c":3}
# b=list(a)
# print(b)
# c=dict(b)
# print(c)

# functions of string data type
# len()
# count()
# replace()
# split()
# join()
# upper()
# lower()
# swapcase()
# titl()
# capitalize()
# startswith()
# endswith()
# isalnum()
# isalpha()
# isdigit()
# islower()
# isupper()
# istitle()
# isspace()
# index()
# rindex()
# find()
# rfind()
# strip()
# lstrip()
# rstrip)()
# format()
#
# # functions of list data type
# split()
# len()
# count()
# index()
# append()
# insert()
# extend()
# remove()
# pop()
# reverse()
# sort()
# sort(reverse=True)
# clear()
#
# # functions of list data type
# len()
# count()
# index()
# sorted()
# min()
# max()
#
# # functions of set data type
# add()
# update()
# copy()
# pop()
# remove()
# discard()
# clear()
# union()
# intersection()
# difference()
# symmetric_difference()
#
# # functions of dict data type
# del d[key]
# clear()
# dict()
# len()
# get()
# pop()
# popitem()
# keys()
# values()
# items()
# copy()
# setdefault()
# update()

# i=("ankit     ")
# print(len(i))
# if len(i) == 10 :
#     print("valid")

# e="ankitmanapure"
# print(e.endswith("r"))

# a={"a":1,"b":2,"c":3}
# print(a.pop("a"))
# print(a)

# a={i:i*2 for i in range(1,11)}
# print(a)
# print(type(a))

# b=int(input("Enter value:"))
# v=[i*b for i in range(1,11)]
# print(v)

# s="qwertyuiop sdad sdfsdf"
# print(s.count("q"))
# n=s.replace("q","Q")
# print(n)
# print(n.split("e"))
# print(n.join("  "))
# print(n.upper())
# print(n.lower())
# print(n.title())
# print(n.capitalize())
# print(n.swapcase())
# print(n.startswith("qW"))
# print(n.endswith("sdf"))
# print(n.isalnum())
# print(n.isalpha())
# print(n.isdigit())
# print(n.islower())
# print(n.isupper())
# print(n.istitle())
# print(n.isspace())

# print("{} 's salary is {} and his age is {}".format("ankit","10000","22"))
# print("{0} 's salary is {1} and his age is {2}".format("ankit","10000","22"))
# print("{x} 's salary is {y} and his age is {z}".format(z="22",y="22222",x="ankit"))

# list
# a=[10,20,30,40,50,60,20]
# print(len(a))
# print(a.count(20))
# a.insert(1,100)
# print(a)
# a.append(10000)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# # a.clear()
# # print(a)

# a=(10,20,30,40,50,60,70,80,90,100)
# print(min(a))
# print(max(a))
# a1=sorted(a,reverse=True)
# print(a1)
# print(sorted(a,reverse=True))
# c={1,2,3,4,5,6,7,8,98,0}
# c.add(40)
# c.update(c,range(8,15))
# print(c)
# for a in c:
#     if a in c:
#         print("yes",a,c)

# random
# nn = dict(k1 = 20, k2 = 30, k3 = 40)
# print(type(nn))
# print(nn)

# def call(name):
#     if name == "mrunal":
#         print("hello sir")
#     if name == "ayush":
#         print("good boy")
# call("mrunal")
# call("ayush")

# def a():
#     c="ankit"
#     if c in "   ":
#         print("ok")

# def a(x):
#     print(x*x)
# a(5)

# def a(x):
#     return (x*x)
# c=a(5)
# print(c)

# def a(*s):
#     print(s)
#     print(type(s))
#     b=list(s)
#     print(type(b))
#     b.append(10)
#     print(b)
#     s=tuple(b)
# a(20)

# 4)variable length arguments==> *s     output ==> tuple
# we can call this function by passing any number of arguments including zero number and output shown in tuple



# parameter arg   fix: a   a,b    a,v,c   x,c,v,b

# def wish(*s):
#     print(s)
# wish(1,3,4,5,6,7,8,9,7,4,3,4)
# wish(1)
# wish()
#
# # s=()
# # print(type(s))

# variable  length argument   and variable length keyword argument


# variable length keyword argument     output is in dict

# def wish(**d):
#     print(d)
#     print
# ========
# 3.default argument

# def world(name="mrunal"):
#     print(name)
# world()
# world("pranay")
# you can use positional argument and keyword argument at same time:
# yes

# position value  (10,20)
# keyword value (name="tanuja")

# def new(name,msg):
#     print(name,"----------",msg)
# new("gm",msg="mrunal")
# codezs
# 20:58
# 1) positional arguments==>

# these are the arguments passed to function in correct position order
#
# def wish(a,b):
#     print(a+b)
# wish(1,2)
# wish(10,20)

# 2)keyword arguments ==>  we can passed arguments value by keyword:


# def wish(name,msg):
#     print(name,"----------",msg)
# wish(name="mrunal",msg="gm")
# wish(msg="gm",name="mrunal")
# jdjhsdhdsjkf


# Return///////////////////////////
# def aa():
#     return "Ankit"
# g=aa()
# print(g)

# positional argument
# keyword argument
# default argument
# variable length argument

# positional argument///////////////////////
# def wish(a,b):
#     print(a+b)
# wish(1,2)
# wish(10,20)

# keyword argument/////////////////////////////
# def wish(name,msg):
#     print(name,"----------",msg)
# wish(name="mrunal",msg="gm")
# wish(msg="gm",name="mrunal")

# default argument
# def world(name="mrunal"):
#     print(name)
# world()

# variable length keyword argument////////////////////////////

# def wish(**d):
#     print(d)
# wish(a=20,b=30,c=40)


# variable length argument//////////////////////

# def wish(*d):
#     print(d)
# wish(20,30,40)

# def o():
#     # f=input("select that:")
#     # t=input("select that")
#     # if f > t:
#     #     print("Yes")
# o()



# s=[1,2,3,4,5,6]
# s.append(dict(r=10,f=30))
# print(s)
# t="ankit"
# i=[10,]
# if i in s:
#     print(s)
# i.append(s.copy())
# print(i)
# i.sort(reverse=True)

# cube of a list and dict
# list
# a=[1,2,3,4,5]
# m=[]
# j=[i for i in a if m.append(i**3)]
# print(m)
#
# # dict
# a={1,2,3,4,5}
# k={i:i*i*i for i in a}
# print(k)

# addition
# a=[1,2,3,4,5]
# x=0
# for i in a:
#     x += i
# else:
#     print(x)
#
#
# # print second top value from list
# d=[20,5,10,1,100]
# g=[d.sort(reverse=True), d.pop(0)]
# print(max(d))
#
#


# addition
# a=[1,2,3,4,5]
# x=[0]
# for i in a:
#     x[0] += i
# print(x)
#
#
# # # print only special chars
# f= "abc&%"
# for i in f:
#     if i in "!@#$%^&*()_+=-{}[];':,./<>?":
#         print(end=i)
#
# print abcd1234
# a = "4d3c2b1a"
# n = [i for i in a if i.isalpha()]
# j = [i for i in a if i.isdigit()]
# n.sort()
# j.sort()
# print(n+j)
# k=str(n+j)
# print(k)
# u=k.replace("'",'')
# y=u.replace(",",'')
# print(y)



# print second top value from list
# d=[20,5,10,1,100]
# g=[d.sort(reverse=True), d.pop(0)]
# print(max(d))



# # cube of a list and dict
# # list
# a=[1,2,3,4,5]
# m=[]
# j=[i for i in a if m.append(i**3)]
# print(m)
#
# # dict
# a={1,2,3,4,5}
# k={i:i*i*i for i in a}
# print(k)

# """it will be like x=i then x+i"""
# a=[1,2,3,4,5]
# x=[0]
# for i in a:
#     x[0] += i
# else:
#     print(x)


# a=[1,2,3,4,5]
# s=0
# i=0
# while i < len(a):
#     s+=a[i]
#     i+=1
#     print(s)

















# addition of list using index number

# a=[1,2,3,4,5]
# x=[0]
# for i in a:
#     x[0] += i
# print(x)

# s=lambda a,b,c:a if a>b and a>c else b  if b>a and b>c else c
# print(s(40,20,30))

# y=lambda a,b:a*b
# print(y(10,10))


# codezs
# 7:26 PM
# # factorial
#
# def factorial(n):
#     if n==0:
#         result = 1
#     else:
#         result=n*factorial(n-1)
#     return result
# d=factorial(6)
# print(d)
# codezs
# 7:40 PM
# filter(functionname,seq name)
#
# sequance :  list   tuple  string
# l=[1,2,3,4,5,6,7,89,90]

# def wish(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# l=[1,2,3,4,5,6,7,89,90]
# l1=list(filter(wish,l))
# print(l1)
#
# l2=list(filter(lambda x:x%2==0,l))
# print(l2)
# codezs
# 7:54 PM
# def wish(w):
#     return w**3
#
# l=[1,2,3,4]
# # l2=list(map(wish,l))
# # print(l2)

# l2=list(map(lambda x:x**3,l))
# print(l2)

# def wish(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,7,89,90]
# l1=list(filter(wish,l))
# print(l1)


# l=[1,2,3,4,5,6,7,89,90]
# l2=list(map(lambda x:x**3,l))
# print(l2)


# def ank1(add):
#     def inner1(x,y):
#         if y==5:
#             print(x*y)
#         else:
#             add(x,y)
#     return inner1
# @ank1
# def add(x,y):
#     print(x+y)
# add(2,6)











# generators  : generators is function which is responsible to generate seq of value  we can write generator function as a ordinary function but
# instead of return it use  yield.


# def wish():
#     yield "a"
#     yield "b"
#     yield "c"
# s=wish()
# print(type(s))
# print(next(s))
# print(next(s))
# print(next(s))

# def countdown(num):
#     while (num>0):
#         yield num
#         num=num-1
# b=countdown(8)
# for i in b:
#     print(i)

# def first(num):
#     n=1
#     while n<=num:
# def first(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
# value=first(10)
# for i in value:
#     print(i)










# def ank1(add):
#     def inner1(x,y):
#         if y==5:
#             print(x*y)
#         else:
#             add(x,y)
#     return inner1
# @ank1
# def add(x,y):
#     print(x+y)
# add(2,6)

# def wish():
#     yield "a"
#     yield "b"
#     yield "c"
# t=[]
# s=wish()
# t.append(next(s))
# t.append(next(s))
# t.append(next(s))
# print(t)


# def countdown(num):
#     while (num>0):
#         yield num
#         num=num-1
# n=[]
# b=countdown(8)
# for i in b:
#     print(i+2)
# n.append(i)
# print(n)

# random81
# def code1(get):
#     def inner1(a,b):
#         if b<a:
#             print(a/b)
#         else:
#             get(a,b)
#     return inner1
# @code1
# def get(a,b):
#     print(a*b)
# get(10,5)
# get(5,10)

# def a1():
#     yield 10*2
#     yield 20*2
#     yield 30*2
#     yield 40*2
# a2=a1()
# y=[i for i in a2]
# print(y)

# def a1(q,w):
#     if q<w:
#         print("yes")
#     else:
#         print("no")
#         yield
#     if q>w:
#         print("ok")
#     else:
#         print("no")
#
# n=a1(q=int(input("Enter the first value:")),w=int(input("Enter second value:")))
# for i in n:
#     print(i)


# from math import *
# print(factorial(3))

# def name(get):
#     def inner(a,b):
#         if b<a:
#             print(a/b)
#         else:
#             get(a,b)
#     return inner
# @name
#
# def get(a,b):
#     print(a*b)
# get(10,5)

# def name(get):
#     def inner(a,b):
#         if b<a:
#             print(a/b)
#         else:
#             get(a,b)
#     return inner
# @name
#
# def get(a,b):
#     print(a*b)
# get(10,5)


# def table():
#     t=list(range(2,21,2))
#     yield t
#     t = list(range(3, 31, 3))
#     yield t
# f=table()
# print(next(f))
# print(next(f))

# def table():
#     t=int(input("Enter the number:"))
#     y=[1,2,3,4,5,6,7,8,9,10]
#     if t in y:
#         print("yes value is there")
#     else:
#         print("No, value is not there")
#     yield
# f=table()
# print(next(f))

# from math import *
# print(factorial(3))


# random81
# def code1(func):
#     def inner1(a,b):
#         if b<a:
#             print(a/b)
#         else:
#             func(a,b)
#     return inner1
# @code1
# def func(a,b):
#     print(a*b)
# func(10,5)
# func(5,10)

# import math
# def arg():
#     p=dict(
#            square_of_1=1,
#            square_of_2=2,
#            square_of_3=3,
#            square_of_4=4,
#            square_of_5=5,
#            square_of_6=6
#            )
#     u=p
#     h=p
#     for i in h.values():
#         y=math.factorial(i)
#         for z in u.keys():
#             print(z,y)
#
# arg()

# class Wish:
#     def __init__(x):
#         x.a=10
#         x.b=20
#
#     def mrunal(x):
#         print(x.a)
#
#     def pranay(x):
#         print(x.b+x.a)
#
# s=Wish()
# s.mrunal()
# s.pranay()


# class Wish:
#     def __init__(x):
#         x.a=10
#         x.b=20
#
#     def mrunal(x):
#         if x.a>x.b:
#             print(("greter"))
#         else:
#             print("Not greter")
#
#     def pranay(x):
#         d=x.a
#         y=x.b
#         print(d+y)
#
# s=Wish()
# s.mrunal()
# s.pranay()

# class Wish:
#     def __init__(x):
#         x.a=10
#         x.b=20
#
#     def mrunal(x):
#         print(x.a)
#
#     def pranay(x):
#         print(x.b+x.a)
#
# s=Wish()
# s.mrunal()
# s.pranay()


# def crate():
#     player_info=dict(name="ankit",
#                      Health=100,
#                      gun="akm",
#                      map="USA",
#                      survive_time=30,
#                      )
#     y=player_info.keys()
#     print(y)
# crate()


# t=[1,2,3,5,6]
# t.sort(reverse=True)
# y=t[0]+t[1]
# print(y)

# x_top2=[1,20,50,90,30,100,200,25,76]
# y=[x_top2.sort(reverse=True), x_top2.pop(0)]
# print(max(x_top2))

# u=lambda a,b:a+b
# print(u(5,5))

# def add():
#     u = lambda a, b: a + b
#     print(u(5,5))
# # add()
#
# # def add():
# #     u = lambda a, b: a + b
# #     print(u(5,5))
# # add()
#
# a=10
# b=2
# print(a//b)