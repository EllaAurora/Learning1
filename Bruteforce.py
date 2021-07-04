#Ella Strong
#30/06/2021
#Brute Force

import time

attempts = 0
password = "password"


for i in range(5):
    userInput = input("please enter your password: ")
    if userInput == password:
        print("Welcome to Twitter HQ")
        break
       


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
            print("not locked out")
        else:
            print("please try again")
    print("loop exited")
print("exiting")