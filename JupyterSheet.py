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
my_string.replace('a', '?')

# %%
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

# %%
