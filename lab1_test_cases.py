import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #this test checks to make sure that the maximum value iterative 
        #function is working correctly
        list1 = None
        list2 = [1,2,6,4,5,2,7]
        list3 = [3,9,2,7,2,6,9]
        list4 = []
        #this test case checks that a list of None produces a ValueError
        with self.assertRaises(ValueError):
            max_list_iter(list1)
        #this test case checks that the function returns the max value from a list
        self.assertEqual(max_list_iter(list2), 7)
        #this test case checks that the function still returns the max value when 
        #there are multiple of the same highest value
        self.assertEqual(max_list_iter(list3), 9)
        #this test case checks that an empty list produces None for the output
        self.assertEqual(max_list_iter(list4), None)

    def test_reverse_rec(self):
        #this test checks that the recursive function that reverses a list is
        #working correctly
        list1 = None
        list2 = [1,2,3]
        list2f = [3,2,1]
        list3 = [4,5,3,4,9,2]
        list3f = [2,9,4,3,5,4]
        #this test case checks that a list of None produces a ValueError
        with self.assertRaises(ValueError):
            reverse_rec(list1)
        #this test case checks that the reverse function correctly reverses
        #the list
        self.assertEqual(reverse_rec(list2),list2f)
        #this test case provides another example to make sure that the reverse
        #function correctly reverses the list
        self.assertEqual(reverse_rec(list3),list3f)

    def test_bin_search(self):
        #this test checks to make sure the binary search function is working
        #properly
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        #this test case checks that the function returns the correct index
        #value for the target found in the list
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        #this test case checks that the function still returns the correct
        #index value for the target found at the lower boundary of the list
        self.assertEqual(bin_search(0, low, high, list_val), 0)
        #this test case checks that the function still returns the correct
        #index value for the target found at the upper boundary of the list
        self.assertEqual(bin_search(10, low, high, list_val), 8)
        #this test case checks that the function returns None if the value
        #is not found
        self.assertEqual(bin_search(6, low, high, list_val), None)
        #this test case checks that a ValueError is raised if the list is None
        with self.assertRaises(ValueError):
            bin_search(1,0,5,None)

if __name__ == "__main__":
        unittest.main()