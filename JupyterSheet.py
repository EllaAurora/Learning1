# %%
print("hello")

# %%
print("Ella \n Strong")

# %%
print("Good Morning Ella \n Strong333")


# %%
my_string = 'python is my favourite programming language!'

# %%
my_string


# %%
type(my_string)

# %%
len(my_string)

# %%
my_string = ('python is my favourite programming language!'
             ' hhhhhfgdd')
my_string

# %%
help(str.replace)

# %%
my_string = "ella"
my_string.replace('a', '?')

# %%
my_string = "the weather is hot"
my_string.replace("is", "will be")

# %%
my_empty_list = []

# %%
my_empty_list = []

# %%

list_of_ints = [1, 2, 6, 7]
# https://github.com/jerry-git/learn-python3
# %%
my_list = ['Python', 'is', 'still', 'cool']
print(my_list[0])
print(my_list[3])

# %%
my_list = ['Python', 'is', 'still', 'cool']
print(my_list[4])

# %%
favFoods = ['banana', 'ice cream', 'cheese', 'chocolate', 'pizza']
print(favFoods)

# %%
help(list.append)


# %%
favFoods.append('nachos')
print(favFoods)

# %%
# NUMBERS
#    1         2          3        4          5
# INDExS
#    0        1           2          3       4
# an index starts with 0!!

['banana', 'ice cream', 'cheese', 'chocolate', 'pizza']
favFoods[3]

# %%
favFoods.insert(1, "jam")
print(favFoods)


# %%

favFoods.remove("cheese")
print(favFoods)

# %%
# favFoods.remove(1)
favFoods = ['banana', 'ice cream', 'cheese', 'chocolate', 'pizza']
del favFoods[2]
print(favFoods)

# %%
# if statement
age = 14
if (age > 18):
    print("snap")
else:
    print("no snap")

# %%
languages = ['Java', 'C++', 'Go', 'Python', 'JavaScript']
if 'Python' in languages:
    print('Python is there!')
# %%
languages = ['Java', 'C++', 'Go', 'JavaScript']
if 'Python' in languages:
    print('Python is there!')
else:
    print("python isnt there")

# %%                                      1st           2nd
#                                        first        second
computerGames = ["minecraft", "marble","Candy Crush","Candy Crush"]
computerGames.remove("Candy Crush")
print(computerGames)

# %%
computerGames = ["minecraft", "marble","Candy Crush"]
del computerGames[2]
print(computerGames)

# %%
computerGames = ["minecraft", "marble","Candy Crush"]
computerGames.append("run 3")
print(computerGames)

# %%
computerGames = ["minecraft", "marble","Candy Crush"]
computerGames.insert(1,"run 3")
print(computerGames)


# %%
computerGames = ["minecraft", "marble","Candy Crush"]
computerGames[0] ="minecraft 2"
print(computerGames)

# %%
colours = ["Blue","greenn","purple","red"]
colours[1] ="green"
print(colours)

# %%
colours = ["Blue","greenn","purple","red"]
colours.insert(2,"brown")
print(colours)

# %%
colours = ["Blue","greenn","purple","red"]
colours.append("Black")
print(colours)

# %%
colours = ["Blue","greenn","purple","red"]
length = len(colours)
print(length)


# %%

numbers = [23,545,223,45,22,66]
length = max(numbers)
print(length)

# %%
numbers = [23,545,223,45,22,66]
length = min(numbers)
print(length)


# %%
numbers = [23,545,223,45,22,66]
length = sorted(numbers,reverse=True)
print(length)



# %%
numbers = [23,545,223,45,22,66]
length = sorted(numbers,reverse=False)
print(length)

# %%
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)
# %%
for i in range(20):
    print(i)
# %%
for x in range(2,30,3):
    print(x)
# %%
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias my_functionn")

# %%
def my_hello(name):
    print("hello " + name )

my_hello("Emil")
my_hello("Tobias my_functionn")

# %%
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
    print("end of fruits loop")
print("end of adj loop")  

# https://www.justlearnpython.com/docs/exercises/beginner-exercises-python/
# https://www.w3schools.com/python/exercise.asp?filename=exercise_numbers1
# %%
print("Hello world")

# %%
name=input("whats your name")
print("hello "+name)
# %%
a= int(input("a=?"))
b=int(input("b=?"))
c = a+b
print("a+b="+ str(c))

# %% get even 1 to 100
for i in range(1,101):
    if (i%2) == 1:
      continue
    else:
      print(i)
# %%
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

# %% while loops
print("starting")
i = 1
while i < 6:
  print(i)
  i += 1
print("Ending")
# %% take 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# %%
x = 5
x = float(x)
# %%
x = 5.5
x = int(x)
# %%
def my_function():
  print("Hello from a function")
my_function()
# %%
def my_function(fname,lname):
    print(fname)
my_function("Ella","Strong")
# %%
def my_function(fname,lname): # def says this is a function declaration
    print(fname+" "+lname)
my_function("Ella","Strong") # calling the function with 2 parameters
# %%
def my_function(x):
    return x + 5
my_function(10)
# %%
def my_function(x):
    return x + 5
answer =my_function(10)
print("function answer: "+ str(answer))
# %%
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("purple","blue","red","black")
# %%
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
my_function("Emil", "Tobias", "Linus")
# %%
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# %% Print the second item in the fruits list. https://www.w3schools.com/python/exercise.asp?filename=exercise_lists1
fruits = ["apple","banana","cherry"]
print(fruits[1])
# %% Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple","banana","cherry"]
fruits[0] = "kiwi"
print(fruits)
# %%
#   item   |  first |  second  |   third
#  index   |  0     |   1      |   2
fruits = [ "apple",  "banana",   "cherry"]
print(fruits[1])

# %%
fruits = ["apple", "banana", "cherry"]
fruits.append ("orange")
fruits

# %%
#   item   |  first |  second  |   third
#  index   |  0     |   1      |   2

#                 |
#                 |
# insert          \/
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
fruits
# %%
#   item   |  first |  second  |   third
#  index   |  0     |   1      |   2
# negative indexing
#          |  -3     |   -2           -1                <---

#
#                 |
#                 |
# insert          \/
fruits = ["apple", "banana", "cherry"]
fruits[-2]
# %% Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits[2:5]
# %% Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
len(fruits)
# %% Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
# %% Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
      print("5 and 10 is not equal")
# %% Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

# %%
a = 50
b = 10
if a > b:
  print("Hello World")
# %%
a = 50
b = 10
if a != b:
  print("Hello World")
# %%
a = 10
b = 10
if a == b:
  print("Yes")
else:
  print("No")
# %%
a = 50
b = 10
if a == b:
  print("1")
elif  a > b:
  print("2")
else:
  print("3")
# %%
a = 50
b = 10
c = 50
d = 10
if a == b and c == d:
  print("Hello")
# %%
if a == b or c == d:
  print("Hello")

# %%
if 5 > 2: print("Five is greater than two!")
if 5 > 2: 
    print("Five is greater than two!")

# %%
if 5 > 2:
  print("Yes")
else:
  print("No")
print("Yes") if 5 > 2 else print("No")

# %%
count =5
# %%
x = range(6)
for n in x:
  print(n)
# %%
for n in range(0,3):
  print(n)

# %%

import time

attempts = 0
password = "password"


#for i in range(0,3):
userInput = input("please enter your password")
if userInput == password and attempts <4:
    print("Welcome to Twitter HQ")
    attempts=0


else:
    print("incorrect password")
    attempts = attempts+1
    if attempts == 3:
        print("too many tries")
        print("locked out for 10 seconds")
        attempts = 0
        for x in range(0,10):
            print(x)
            time.sleep(0.2)
    else:
        print("please try again")
        print("loop exited")
# %%



# %%
import random
z = [1,2,3,4,5,8]
print("initialised",z)
random.shuffle(z)
print ("shuffled",z)

z2=sorted(z)
print("sorted",z2)

#  %% while loops
i=0
while (i<5):
  print(i)
  i=i+1




# %%


