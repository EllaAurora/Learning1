import unittest
import math

# Right angled triangle with sides a, b, c
# 
#
#     A
#      |\
#      | \
#  a   |  \
#      |   \   c
#      |_   \
#      |_|___\
#     B       C
#         b
#  AB = a
#  BC = b  
#  AC = c = hypotenuse 

       
# https://www.tutorialspoint.com/python/number_sqrt.htm
# https://www.includehelp.com/python/calculate-square-of-a-given-number.aspx
# https://www.mathsisfun.com/pythagoras.html


def CalcASq(c,b):
  return c*c -b*b
def CalcCSq(a,b): return a*a + b*b

def CalculateC(a,b) :

    cSq = CalcCSq(a,b)
    return math.sqrt(cSq)

def CalculateC_Short(a,b) :   
    return math.sqrt(a*a + b*b)

def CalculateA(c,b) :
    return math.sqrt(c*c - b*b)

def CalculateAShorter(c,b) :
    return math.sqrt(c**2 - b**2)

def CalculateAShorter2(c,b) :
    return (c**2 - b**2)**0.5

def CalculateA(c,a) :
    return math.sqrt(c*c - a*a)

def myfunc(alist):
    return len(alist)


class TestPythogoreansCalculations(unittest.TestCase):

    def test_CalcCSq(self):
        self.assertEqual(CalcCSq(3,4), 25)

    def test_CalcASq(self):
        self.assertEqual(CalcASq(5,3), 16)

    def test_CalcA(self):
        self.assertEqual(CalculateA(5,3), 4)
    
    def test_CalculateA(self):
        AC = c =5
        AB = a = 3
        BC = b  = CalculateAShorter2(c,a)
        expected_b = 4
        self.assertEqual(b, expected_b)

        
if __name__ == '__main__':
    unittest.main()




# z = math.sqrt(25)
# x = CalculateC(3,4)

# print("sqrt of 25 is " + str(z))
# print("Lenghth hypotenuse of a=3 b=4 c=" + str(x))



# C:\Users\ellaa_52\AppData\Roaming\Python\Python37\Scripts' which is not on PATH.
#The scripts iptest.exe, iptest3.exe, ipython.exe and ipython3.exe are installed in 'C:\Users\ellaa_52\AppData\Roaming\Python\Python37\Scripts' which is not on PATH.