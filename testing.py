import unittest
from files import *
"""To insert give filename as 3rdyear.json and then random details with key less than 32 char"""

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(insert())
    def test2(self):
        self.assertEqual(read('3rdyear.json','17CS134') ,True )
    def test3(self):
        self.assertEqual(delete('3rdyear.json','17CS237') ,'Key has been deleted' )
    def test4(self):
        self.assertTrue(objsize(1000))
if __name__ == '__main__': 
    unittest.main() 