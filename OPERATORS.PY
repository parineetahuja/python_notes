'''question 1 -

x = "100"
y="200"

a=int(x)
b=float(y)
print(x+y)

question 2 -'''
'''
x,y="120","python"

print(y)'''
'''
 question 3 -''' 
'''
x="data"
y=list(x)

print(5*x)'''

#question 4 -

#print (12/12)
'''
x=12
y=12
z=x/y
print(type(z))'''
'''
x=120.789

y=str(x)
print(len(y))'''

#-----------------------------------------------------------  
'''Operators :- types of operators 
-----------------------------------------------------------
1. Airthmatic operators
2. Assingment operators 
3. comperison operators
4. logical operators 
5. Identity operators
6. Membership operators
7. Bitwise operators
--------------------------------------------------------------
1. Airthmatic operators
--------------------------------------------------------------

+ : Addition
-:  Substraction
*:  Multiplication
/:  divison
%:  module:- it shows the reminder
**: exponentation:- it is used to add the power on number.
//: floor divison :- it show the value before the decimal.
'''
'''
module question 1)
x=45
y=20
print("modules:-" ,x%y)

print("the reminder of",x,"and",y,"is:-",x%y)'''
'''
exponentation question 2
x=5
y=3
print(x*y)
print(x**y)'''
'''
floor division question 3
x = 19
y= 5
print(x//y)'''

#question 4

#print(19%4)-3
'''
question 5

print(1.3//1)- if we divide with decimal number it will always 
give decimal number'''

#Question 6

#print(45//8.5)-5.0

#question 7

'''x = 13
y = 7
z = x%y
print(type(z))
'''

'''
Question 8
x=2
print(x**4)'''
'''
----------------------------------------------------------
2. ASSIGNMENT OPERATORS:- 
= :- ASSIGN OR
!=:NOT EQUALS TO                
== :- EQUALS TO                
+= :   (X=X+1)                       
-=:     (X=X-1)
*=:     (X=X*1)
/=:     (X=X/1)'''
'''
 1.  x=45
   y=45
   
   print(x==y)'''

"""
x=100
y=200

print(x==y)
print(x!=y)
"""

#plus equals to (+= or x=x+1)
'''
x=50
y=x+5
print(y)

x+=5
x+=10
print(x)
x=x+10'''

'''-----------------------------------------------------
3. comperison operators:-
-----------------------------------------------------

> : greater than 
< :less than
>=:greater than equalts to
<=:less than equals to
==:equals to
!=:not ewuals to 

'''

#1.

'''
x=45
y=10
print(x>y)
print(x<=y)

x=100
y=100
print(x==y)
print(x>=y)

'''
#-------------------------------------------------
# IF_ELSE STATEMENT
#-------------------------------------------------

# if_else :- it is used to divide the data in differnet 
           #  differnet category.
'''
write a python progrm to show the number if number is greater
than 10 then print yes else print no '''


'''x=8

if x>10:
  print("yes")
else:
    print("no")

x=100

if x>50:
   print("yes it is greater than 50")
else:
   print("it is not greater than 50") 

'''
# write a python program to check the no is even or odd


'''x = 15 

if x%2==0:
  print("even number")
else:
  print("odd number")  
'''

# write a python program to check the number is odd 
'''
x = 19 

if x%2==1:
   print(x)'''

 # check the number is divisible of 9 or not 
'''
x = 40


if x%9==0:
   print("divisible of 9")
else:
  ("not divisble")'''

  # user input :- it is a input where you enter the values in 
                  #output screen 
'''
  x = int(input("enter any number :-"))
  print(x)
  
  if x%2==0:
     print("even number")
  else:
     print("odd number") '''  
'''
# write a python program with help of user input and show the 
number is greter than 200 then print "yes greater than 200 "
else print "less than 200"'''

'''
x= int(input("enter any number "))
print(x)
if x>=200:
  print("yes greater than 200")
else:
  print("less than 200")'''

# check the text is equal to delhi then print yes else print 
#no
'''
x=str(input("enter any text :-")) 
if x=="delhi":
   print("yes")
else:
  print("no")    
'''

#write a python program to show the state and capital according
#to user input
'''
  x = "bihar"
  x=str(input("enter the state name :-"))
  if x=="bihar":
     print("patna") 
  else:
    print("other") ''' 

 # LOGICAL OPERATORS
 # AND :-IT RETURN TRUE WHEN BOTH CONDITION ARE TRUE
 # OR :- IT RETURN TRUE WHEN AT LEAST ONE CONDITION IS TRUE
 #NOT :-ITS REVERSE THE OUTPUT OF(AND OR)  
"""
x = 15 
y = 10

print(x>10 and y>5) """


'''
x=15
y=10

if x>10 and y>5:
  print("both condition are true")
else:
 print("wrong condition")  

 write a python program to check the number is between 20
 to 30 than print "yes" else print "no"'''
'''
x= 25

if x>20 and x<30:
  print("yes")
else:
  print("no")   '''

  # write a python program to check if number is divisble of 10
  #or 5 then print yes else print no
'''
x=int(input("enter number:-"))
if x%10==0 or x%5==0:
    print("yes")
  else:  
    print("no")   '''
'''
---------------------------------------------------
MEMBERSHIP OPERATORS :- 
---------------------------------------------------'''
'''
x ="science"
print("i"in x)
print("I"in x)
print("z"not in x)
print("s"not in x)'''

#x=[24,4,5,6,7,8,10]

#check 24 in list or not
# check 10 in list

# write a program with the help of user input to print
#if name contain a or i then print "yes" else print no

'''
x=str(input("enter name :-"))
if "i" in x or "a" in x:
    print("yes")
else:
  print("no") '''

  # x= sunday ,monday,tuesday,wednesday
  # if sunday in x then print present 
  # else print not present 

'''x =str(input("enter weekday"))
if x in "sunday":
    print("present")
else:
  print("absent")   
'''

# writea python program to show the grade

x=int(input("grade"))
if x>=90:
    print("a")
elif x>=80:
  print("A")
elif x>=70:
  print("b")
elif x>=60:
  print("c")
elif x>=50:
  print("d")
else:
  print("fail")         
