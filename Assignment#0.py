#Create a variable greeting and store a message. Print it.
greeting="Welcome to VS code."
print(greeting)
#Change the value of greeting and print the new message.
greeting=greeting.replace("VS code","AI HUB")
print(greeting)
# Create first_name and last_name, then print full name using f-string.
first_name="isma"
last_name="amjad"
print(f"The full name is {first_name} {last_name}.")
#Print a famous quote with author’s name using f-string.
quote="If you can change your mind, you can change your life"
author="William james"
print(f"\t{quote}\n\t\t\t\t{author}")
#Store a name with extra spaces, strip them, and print clean output.
name="    isma amjad   "
name=name.strip()
print(f"Name without extra spaces is {name}")
# Take a number, add 5, multiply by 2, subtract 3, and print the result.
num=10
result=((num+5)*2)-3
print(f"The result of the number {num} after adding 5, multiplying by 2 and subtracting 3 is {result}")
#Create a and b; print their sum, difference, product, and quotient.
a=12
b=2
print(f"The sum of 2 numbers {a} and {b} is ",a+b)
print(f"The difference of 2 numbers {a} and {b} is ",a-b)
print(f"The product of 2 numbers {a} and {b} is ",a*b)
print(f"The quotient of 2 numbers {a} and {b} is ",a%b)
#Find square and cube of a number using ** operator.
x=5
print(f"The square of the number {x} is:",x**2 )
print("The cube of the number{x} is:",x**3)
#. Add three floating-point numbers and print the total.
f1=23.1
f2=12.3
f3=14.1
add=f1+f2+f3
print(f"The sum of 3 float point numbers {f1},{f2} and {f3} is {add}")
#. Assign x, y, z in one line and print them.
x,y,z=2,3,4
print(f"The values of variables x,y,z are {x}, {y} and {z} respectively.")
# Create a list of 5 favorite fruits and print each one separately.
fruits=["apple","banana","cherry","kiwi","mango"]
for fruit in fruits:
    print(fruit)
#Modify the 2nd item in the list and print the updated list.
fruits[1]="orange"
print(fruits)
#Append a new fruit and insert one at the beginning.
fruits.append("grapes")
fruits.insert("pomegranate")
print(fruits)
# Delete items using del, pop(), and remove().
del fruits[0]
print(f"The fruits after using del function is \n {fruits}")
fruits.pop(2)
print(f"The fruits after using pop function is \n{fruits}")
fruits.remove("mango")
print(f"The fruits after using remove function is \n{fruits}")
#Use sort() and sorted() to sort the list. Show before and after.
list=[1,3,5,6,4,2,33.9,67.0]
print(f"The list before using sort function is \n{list}")
list.sort()
print(f"\nThe list after using sort function is \n{list}")
print(f"\nThe list before using sorted function is \n{list}")
sorted(list)
print(f"\nThe list after using sorted function is \n{list}")
#Create a list of dream travel destinations:
# - Sort alphabetically
# - Reverse the order
# - Count total destinations
destination=["saudi arabia","japan","china","swizerland"]
print(f"the list of destination is \n{destination}")
print(f"the list of deatinations is \n{sorted.destination()}")
print(f"the reverse list of destination is \n{destination[::-1]}")
print(f"the number of destinatins are \n{len(destination)}")
#Start with an empty guest list:
#  - Append 3 guests
#  - Insert 1 at the beginning
#  - Remove one using pop()
#  - Print final list
guests=[]
guests.append("isma")
guests.append("talha")
guests.append("fatimah")
print(f"The guests list after appending 3 guests member is \n{guests}")
guests.insert(0,"rashid")
print(f"\nThe guests list after inserting one new member at the start  is \n{guests}")
guests.pop(1)
print(f"\nThe final list after using pop function is \n{guests}")
# Access the last 3 elements of a list without negative indexing.
num=[23,34,56,77,54,33,21]
l=len(num)
print(f"The last 3 elements of the list are \n{num[l-3:l]}")
#From a list of numbers, print only even numbers.
number=[2,4,5,6,7,8,9,3,1,88,76,55,33,11]
print(f"The even numbers in the list are \n")
for i in number:
  if(i%2==0):
    print(i)
#Print squares of the first 10 natural numbers in a list.
natural_number=[1,2,3,4,5,6,7,8,9,10]
print(f"The of first 10 natural numbers in the list are:\n")
for i in natural_number:
  print(i**2)
#sk the user for 5 favorite movies.
#Store them in a list.
#Print them sorted alphabetically.
movies=[]
for i in range(1,6):
  movie=input(f"{i}. Enter your favorite movie :\n")
  movies.append(movie)
print(f"\nThe movies list without sort is \n{movies}")
print("Movies name in sorted order are:")
print(sorted(movies))
