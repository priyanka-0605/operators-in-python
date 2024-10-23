print("hello world!")
# Operators:are special symbol that carry oyt arithmetic or logical computation
# operator require operands (data) to perform its job
#list of operators:
# Arithmetic operators:
print(3**2)
print(4**0.5)
print(-3**2)
# multiply operator
# if one operand is string and other is number then it will repeat the string
print("ab"*3)
print(3*2)


# addditional operator
x="abc"
y="xyz"
print(x+y)
print(3+2)
print(3-2)
# / is for divide (float)
print(5/2)
# // is for divide(floor)
# it will give floor value
print(5//2)
# MModulus function give reminder 
print(3%2)
print(2%3.0)
# result come as a positive number since denominator operant is a positive number
print(-3%2)
# now result will be in negative number
print(3%-2)
print(-3%-2)


#  RELATIONAL(comparison) OPERATOR:
# always yield true or false as a result ,
print(3>5)
# when truth value converted to int,it becomes 1 or 0
# every non-zero value is considerd as True and zero value is consider as false
x=True
y=int(x)
print(y)
print(int(False))
print(bool(2))
print("ab">"cd")
print('ab'=="ab")
# only!= and ++ can work between complex value
print(3+5j==3+5j)
print(True+5)
print(False+5)
print(5>4>3)
# == check if the content and type is equal in both side or not
print(3+5j==3+5j)
# WHNE CONTENT IS same but type is not it will give false
print(5=="5")
# one is char and other is integer
print('a'==97)
# when char is compare to its unique code then ord() is used
print(ord("a")==97)
# exception only when in == one is int and other is float
print(5==5.0)

# LOGICAL OPERATORS:
# must be written in lowercase only
#   non-zero operand is considered as True , zero will be treated  as false
# "and ","or" is a binary operator ,"not" is a urinary operator

# "and" OPERATOR:
# T and T --> True
print(3!=4 and 10<20)
# T and F --> False
print(3>2 and 3>5)
# F and T --> False
print(3>4 and 5>3)
# second string will be print
print("ram" and "shayam")
print(3 and 4>2)


# "or" OPERATOR
# F or F --> false
# F or T --> true
# T or F --> true
print(4>3 or 3>2)
# first string will be print
print("ram" or "shayam ")

# "not" OPERATOR
# invert the actual result
print(not 4>3)
print( not 5)
print(not 3+4j)
print( not 0+0j)
# empty string will consider as false and non empty string is consider as true
print(not "priyanka")
print(not "")

# bitwise operators:
# operators that work on bits 
# & (and) operator,| (or), ~ (NOT), ^ (XOR) ,>> (RS) rightshift, <<(LS)left shift
print(5&7)
print(5|7)
print(~5)
print(25>>2)


# assignment operators:
# = assignment operatot ,== equal to
x=5
x+=3
x/=2
x=x*3+4
print(x)

# identity operator
# is (returns true if both variable are the same object),is not operator(returns false if both variables ae the same object)
# every variable in python in an object
# objects are dynaically treated 
#objects do not have name but refrence  
print(x is y)
x=5
y=5.0
print(x==y)
print(x is y)

# membership operators:
#  in operator(returns true if a sequence with the specified value is present in the object)
# not in operator(returns false is a sequence with the specified value is present in the object)
x="abc"
# x (variable) should be collection of data we canot assign 
print("a" in x)
print("A "in x)
print("A" not in x)
# error occurs when we asssign x=256 but we can assign string,list ,tuple 
# x=256
# print(5 in x)
x=[1,2,3,4]
print(1 in x)
x="my name is priyanka"
print("my" in x)
