# name
# date-24/9/20
# title-for loops

# while loops forever until xyz happens
# for loops is when we know how many times we want to repeat"for this number of times"

for inerations in range(-10, 20, 3):
    print(inerations)

myscores = []
for x in range(0, 5):
    score = int(input("what was the score?:"))
    myscores.append(score)
print(myscores)

total =0
for x in myscores:
  total = total + x
print("total")
print(total)


# fruits=["apple","banana","cherry"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
