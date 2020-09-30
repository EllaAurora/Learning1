# Ella Strong
# date- 30th September 2020
# List manipulation

sportslist=["football","snooker","basketball","netball","tennis","vollyball","cricket","rugby","swimming"]
print(sportslist)

# display a specific point in the list
# we do not count from 0 when indexing from the the back of the list 


sportslist =["football","snooker","basketball"]
sportslist.clear()
print(sportslist)

# You cannot type list2 = list 1, because list 2 will only reference to list 1
sportslist = ["football","snooker","basketball"]
mylist = sportslist.copy()
print(mylist)

list1 = ["d","e","f"]
list2 =[4,5,6]

list3 = list1 + list2
print(list3)
