# %%
my_empty_list = []

# %%
import random
def roll_dice():
    return random.randint(1,6)

def get_biggest(a,b):
    if (a>b) :
        return a
    else:
        return b

dice1 =roll_dice()
dice2 = roll_dice()
biggest = get_biggest(dice1,dice2)
#print(random.randint(3, 9))
print("first 1 :" + str(dice1))
print("first 2 :" + str(dice2))

print (biggest)



# %%

#   WARNING: The scripts isort and isort-identify-imports are installed in '/Users/paulstrong/Library/Python/3.8/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#   WARNING: The scripts epylint, pylint, pyreverse and symilar are installed in '/Users/paulstrong/Library/Python/3.8/bin' which is not on PATH.
#   Consider
#    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#  /Applications/Xcode.app/Contents/Developer/usr/bin/python3 /Users/paulstrong/Documents/GitHub/EllaAurora/Learning1/functions.py