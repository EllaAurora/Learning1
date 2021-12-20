print("welcome to my password validation program")
length= 0
double = False
while double != True:
    while length<=7:
        print("this is my first entry")
        first= input("please enter in a new password: ")
        length = len(first)
        #print(length)
        if length >= 7:
            print("password is too short")
            print("you need to have another go")
            # else:
            #     print("correct length")
            #     print("thank you")
            #     match=0
            #     while match <=2:
            #         #for i in rnage(0,3):
            #         second= input("please re-enter your password: ")
            #         if second ==first:
            #             print("good job, Thanks")
            #             print("password set")
            #             match=3
            #             double= True
            #             else:
            #                 print("passwords not the same")
            #                 match=match+1
            #                 length=0
            #                 print("this is the end of the program")
            #             print("the user is in the system")

