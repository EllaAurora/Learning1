import unittest

def HelloToYou(name):
  return "Hello " + name

def CalculateAreaRect(width,height):
  return width*height

class TestStringMethods(unittest.TestCase):

    def test_HelloToYou(self):
        self.assertEqual(HelloToYou("Ella"), "Hello Ella")

    def test_RectangleCalc(self):
        self.assertEqual(CalculateAreaRect(5,4), 20)
        
if __name__ == '__main__':
    unittest.main()