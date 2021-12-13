# print("hi")
# print('hi')

# print(5+10)
# print(5*10)
# print(5+10*5) #BODMAS 
# print((5+10)*5)
# print(100/3)
# print(100-3)
# print(100//3) #Round off the Quotient
# print(2*3) #Multiplication
# print(2**3) #PowerOff 2^3

# print(10%3) #REMINDER
# print(100%7)
# print(100%9)
# print(100%2)

# print(2**3+2*3) #8+6
# print((2**3)+2*3)
# print((2**3+2)*3)

#Identifiers = variable= Reference Variable
# doorno = 15
# print(doorno)

#Identifiers Rules No Space Allowed 
#Shouldnot start with Numbers
# tamil1=90
# print(tamil1)
# Tamil_1=90
# print(Tamil_1)
# _TAMIL=90  #private variable is a oops concept
# print(_TAMIL)
# ##ERROR#####
# 2Tamil=90 
# print(2Tamil)

# _math=90 
# print(_math) 

#RULES 
#NO SPECIAL ALLOWED
#NO SPACE 
#UNDERSCORE ALLOWED
#NUMBER ALLOWED BUT SHOULD NOT START WITH It
#CASE Sensitive
#THERE ARE LIST OF RESERVED WORDS
#_,__STARTING -> PRIVATE Variable
#MAGIC METHODS--> __ADD__  FRONT AND BACK UNDERSCORE ALREADY DEFINED IN Python

#python Reserved words
# 33 reserved words
# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#DATATYPES

#simple and dynamically typed
#DUCK TYPING Language
# no =10 #int 
# result = False  #boolean  
#  we never mention datatypes before variable (identifiers) in python 



# Datatypes list  : 14 datatypes

# int
# float
# boolean
# complex
# bytearray
# bytes
# range
# list
# array
# tuple
# dict
# None
# set 
# frozen set 

# n = 10   #10 is pararmeter/argument
# print(type(n))  #print is function/method
# why output is class?
# all datatype is class -we will cover in oops concept

#ID - Address

# n = 10   #10 is pararmeter/argument
# print(type(n))
# print(id(n))

# a = 20   #10 is pararmeter/argument
# print(type(a))
# print(id(a))

#Search for built in function and try it
#id
#len 
#round


#########################     2HOURS COMPLETED  ##############

#INT DATATYPES

#DECIMAL Form
#BINARY Form - 0'S AND 1'S
#OCTAL Form - BASSE 8  0 to 7  start with zero and o
#HEXADECIMAL FORM  start with zero and X

# no = 0B0101
# print(no)

# no1= 0b01001   
# print(no1)


#octal 
# no = 0o776
# print(no)

# no1= 0o765
# print(no1)

#HEXADECIAMAL 

# no = 0X12
# print(no)

# no1= 0XAD
# print(no1)

#if you note all output are normal form that is decimal form

#check inbuild function for conversation

# no1= bin(20)
# print(no1)
# no1= oct(20)
# print(no1)
# no1= hex(20)
# print(no1)

#Float Datatype

#float - . 
#int 

# no = 1.23456789
# print(type(no))

# no = 1.23456789
# print(type(no))

# no = 1.2E3
# print(type(no))

# no = 1.2E7  #Exponential 2POWER 7
# print(type(no))

# COMPLEX

# a+bj

# no = 5+10j
# print((no))
# print(type(no))

# no2 = 5+10j
# total = no+no2
# print((total))
# print(type(total))

# print(no2.real)
# print(no.imag)


#Boolean #Comparison 

# no1 = 10
# no2 = 20
# print(no1>no2)
# print(no1<no2)
# print(no1==no2)
# print(no1!=no2)

# a = True
# print(a)
# print(type(a))

# print(True+True)
# print(True+False)
# print(False+False)

# no1 = "two"
# no2 = "three"
# print(no1>no2)
# print(no1<no2)
# print(no1==no2)
# print(no1!=no2)


#String

# name = "Barath"
# print(name)
# print(id(name))

# name = 'Barath'
# print(name)
# print(id(name))

# name = """ Barath's address is chennai ... he said "hi" """
# print(name)
# name = '''Barath's address is chennai ... he said "hi" '''
# print(name)

# name = '''Kolathur
#           chennai
#         anna nagar
#         tamilnadu '''
# print(name)


# name = "barath"
# city = 'chennai'
# print(name+city)
# print(name,city)  # , will add space  


# name = "barath"
# pin = 600028
# print(name,pin)
# print(name+pin)   # + BOTH SHOULD BE STRING  


#sTRING sLICING
 
# name = "barath"
# print(name[0]) #0 is the index  stars 0 and negative index stat from -1
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[-1])
# print(name[-2])

#Task print last letter and first letter

# name = "barath"
#        #012345
# print(name[0:3])
# print(name[3:])
# print(name[3:5])
# print(name[8:]) #empty 
# print(name[:5])

# a = "HAD LEARNED BASIC KNOWLEDGE OF PYTHON AND ITS FRAMEWORK LIKE DJANGO,FLASK FOR ADVANCEMENT OF SKILLS"
# print(a.title())

# name = 'abcdefghijklmnopqrstuvwxyz'
       #01234567890123456789012345

# print(name[0:5])
# print(name[-1:]) #left to right 
# print(name[5:10])
# print(name[-5:-1]) #Step operator 

#Slicing [::]

# print(name[::])
# print(name[1:10])
# print(name[1:10:2]) #positive index -1 
# print(name[10:2])  #empty set - only left to right 
# print(name[10:2:-1])  #negative index +1 
# print(name[-26:26])
# print(name[26:-1:4])


# name= "123456789"
# name2 = "123456789"

# print(len(name))  #len function doenot count Zero
# val = len(name)
# # print(name[-val:val])

# print(name[val:0:-1]) #to print in reverse #wont work

# print(name[(val-1):0:-1]) #wont work

# print(name[::])
# print(name[::-1]) #to print in reverse
# print(name[0:-5])
# print(name[10:0:-1])
# print(name[::2])


#check whether it is palindrome or not?

# name = "sun"

# print(name)

# name2 = name[::-1]
# print(name2)
# print(name==name2)

# print(name*3)  
# print(name+3) #Error


#TYPE Casting

# no = 99.45  #chaning float to int is type casting

# print(int(no))


#can we able to change name to int? 
#NOOOOOO!!!!

# name = "barath"
# print(int(name))  #VALUEERROR 

# print(float(10))
# print(float(True))
# print(float(False))

# 
# door = "10"

# print(door)
# print(type(door))
# print(int(door))
# print(type(int(door)))



#COMPLEX 

print(complex(10))
print(complex(5.4))
print(complex(True))   #True part
print(complex(False)) #imaginary
print(complex("12"))  
print(complex("12.7"))


