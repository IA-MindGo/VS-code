#Create two variables a = 10 and b = 3.
#Perform and print: addition (+), subtraction (−), multiplication (×), division (/), modulus (%), exponentiation (), and floor division (//).**
a=10
b=3
print(f"Addition of {a} and {b} is {a+b}")
print(f"Subtraction of {a} and {b} is {a-b}")
print(f"Multiplication of {a} and {b} is {a*b}")
print(f"Division of {a} and {b} is {a/b}")
print(f"modulus of {a} and {b} is {a%b}")
print(f"Exponentiation of {a} and {b} is {a**b}")
print(f"Floor division of {a} and {b} is {a//b}")
#Compare a and b using comparison operators: ==, !=, >, <, >=, <=
#Print the result of each comparison.
print(f"{a} == {b} = {a==b}")
print(f"{a} != {b} = {a!=b}")
print(f"{a} > {b} = {a>b}")
print(f"{a} < {b} = {a<b}")
print(f"{a} >= {b} = {a>=b}")
print(f"{a} <= {b} = {a<=b}")
#Create two boolean variables: x = True, y = False.
#Perform and print results of: x and y, x or y, and not x.
x=True
y=False
print(f"{x} and {y} = {x and y}")
print(f"{x} or {y} = {x or y}")
print(f"not {x} = {not x}")
#Create num = 5 and perform assignment operations: +=, -=, *=, /=, %=, **=, //=
#Print the result after each operation.
num=5
num+=5
print(f"The value of num after '+=5' operation is: {num}")
num-=5
print(f"The value of num after '-=5' operation is: {num}")
num*=5
print(f"The value of num after '*=5' operation is: {num}")
num/=5
print(f"The value of num after '/=5' operation is: {num}")
num%=5
print(f"The value of num after '%=5' operation is: {num}")
num**=5
print(f"The value of num after '**=5' operation is: {num}")
num//=5
print(f"The value of num after '//=5' operation is: {num}")
#Create m = 100, n = 100.
#Check if they are the same object using is and is not, and print the result.
m=100
n=100
print(f"Is m={m} and n={n} are the same objects in memory: {m is n }")
print(f"Is m={m} and n={n} are not the same objects in memory: {m is not n }")
#Create a string text = "Python Programming"
#Check if "Python" is in text and if "Java" is not in text.
text="Python progrsmming"
print(f"Is Python in the string: {"Python" in text}")
print(f"Is Java not in the string: {"Java" not in text}")
#Write a Python program to print all keywords using the keyword module.
import keyword
print("List of all keywords in python are:\n",keyword.kwlist)
#Declare: name = "Ali", age = 20, height = 5.9
#Print their values and data types using the type() function.
name="Ali"
age=20
height=5.9
print(f"Name = {name} and {type(name)}")
print(f"Age = {age} and {type(age)}")
print(f"Height = {height} and {type(height)}")
#Write 5 valid variable names (e.g., user_name, x1, _value, TotalAmount, data123)
#Also write 3 invalid ones (as comments): 1name, user-name, class
#Explain why invalid names are not allowed.
print("5 valid variables name are:\n name,\tage1,\t_num,\tis_student,\tHasJob\n")
print("3 invalid variables name are:\n1name:variable cannot start with digit\nuser-name:- can't be used in variables name.\nclass:keywords can't be used as variable name.")
#Create special-naming variables: _hidden = 5, __private = 10, MAX_SIZE = 100
#Print their values.
_hidden=5
__private=10
MAX_SIZE=100
print(f"The value of _hidden is {_hidden}")
print(f"The value of __private is {__private}")
print(f"The value of MAX_SIZE is {MAX_SIZE}")
#Assign values in one line: x = 1, y = 2, z = 3
#Print them.
x,y,z=1,2,3
print(f"The values of x, y and z are {x}, {y} and {z} respectively.")
#Assign same value 0 to a, b, c in one line
#Print them.
a=b=c=0
print(f"a={a}\nb={b}\nc={c}")
#Create temp = 100, print it, delete it using del, then try to print again and observe the error.
temp=100
print(f"temp-{temp}")
del temp
#print(temp)
#Create a string using triple single quotes: '''Hello'''
#Print it.
string='''Hello'''
print(f"string = {string}")
#**Create a multi-line string using triple double quotes:
#"""This is line one.\nThis is line two."""
#Print it.**
multi_line="""This is line one.\n This is line  two."""
print(multi_line)
#**Use type() to check and print the data types of:
#An integer
#A float
#A string
#A boolean**
i=19
f=45.6
s="isma"
b=True
print(f"i={i} and {type(i)}")
print(f"f={f} and {type(f)}")
print(f"s={s} and {type(s)}")
print(f"b={b} and {type(b)}")
#Create score = 85
#Check: score > 50 and score < 100
#Print the result.
score=85
if(score>50 and score<100):
    print(f"Score = {score} and Result = pass")
else:
    print(f"Score = {score} and result = fail")
#Create message = "Welcome to Python"
#Use in and not in to check for the word "Python"
#Print the result.
message="Welcome to Python"
print(f"message = {message}")
print(f"Is Python in message {"Python" in  message}")
print(f"Is Python not in message {"Python" not in message}")
#Write a code block using only comments that explains what your program does.
#declare a variable "message" and assign it a value"Welcome to Python"
#print the value of message 
#print wether Python is in the message 
#print wether Python is not in the message

#create data = 123
#Use id(data) to print its memory address.
data=123
print(f"Value of 'data' is {data} and its memmory address id {id(data)}")