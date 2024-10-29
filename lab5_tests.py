import data
import lab5
import unittest
from data import Time
from data import Point
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_part3_1(self):
        time1 = Time(2,32,54)
        time2 = Time(5,12,32)
        result = lab5.time_add(time1, time2)
        check = Time(7, 45, 26)
        self.assertEqual(check, result)

    def test_part3_2(self):
        time1 = Time(8,67,69)
        time2 = Time(4,8,45)
        result = lab5.time_add(time1, time2)
        check = Time(13, 16, 54)
        self.assertEqual(check, result)
    # Part 4
    def test_part4_1(self):
        test = [54,12,4,1,0,-1]
        result = lab5.is_descending(test)
        check = True
        self.assertEqual(check,result)

    def test_part4_2(self):
        test = [12,34,4,112,43,-12]
        result = lab5.is_descending(test)
        check = False
        self.assertEqual(check,result)
    # Part 5
    def test_part5_1(self):
        test = [32,123,53,42,12]
        result = lab5.largest_between(test, -1,3)
        check = 42
        self.assertEqual(check, result)

    def test_part5_2(self):
        test = [32,123,53,42,12]
        result = lab5.largest_between(test, 3,1)
        check = None
        self.assertEqual(check, result)

    def test_part5_3(self):
        test = [32,123,53,42,12]
        result = lab5.largest_between(test, 0,2)
        check = 53
        self.assertEqual(check, result)
    # Part 6
    def test_part6_1(self):
        test = [Point(2,3), Point(21,34), Point(4,1)]
        result = lab5.furthest_from_origin(test)
        check = Point(21,34)
        self.assertEqual(check, result)

    def test_part6_2(self):
        test = [Point(5,4), Point(-11,10), Point(-20,-20)]
        result = lab5.furthest_from_origin(test)
        check = Point(-20,-20)
        self.assertEqual(check, result)




if __name__ == '__main__':
    unittest.main()
