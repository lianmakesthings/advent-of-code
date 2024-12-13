import unittest
from read import read
import solution
import os

class TestSolution(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(24000, solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))))
    
    def test_part2(self):
        self.assertEqual(45000, solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))))

if __name__ == '__main__':
    unittest.main()