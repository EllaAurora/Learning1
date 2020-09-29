# code comments
#this window is called IDLE.

#what does IDLE stand for? What is an IDLE?
# IDE?

# and IDLE Is a place where you can code
# is python the only IDLE?
def NameGame():
    replay=False
    while replay == False: 
        # this is using a varibale to store the users name
        nameis=input("what is your name?:")
        # this is doing...
        print("welcome",nameis,".It's lovely to meet you.")
        # the bit where it says int is an integer input
        levels = 0
        level_over=False
        while level_over==False:
        levels = int(input(" Your game has 1453 levels. how many have you done?:"))
        if levels >1453 or levels<0
           print("unacceptable. Your number must be between 0 and 1453 
        else:
            print("acceptable value entered")
            level_over=True
                 




        print("you have completed",round (levels/1453*100),"percent of the game")
        playagain =input("would you like to play again?:")
        if playagain == "yes" or playagain =="Yes" or playagain == "YES" or playagain == "y" or playagaiin == "Y":
            print("ok")
        else:
            print("end of game")
            replay=True
            print("good bye")

NameGame()
