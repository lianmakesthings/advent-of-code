import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    
    def test_build_map(self):
        map = solution.build_map(read.from_file("{}/test_input.txt".format(os.path.dirname(__file__))))
        self.assertTrue(map['grid'][(0, 0)] == 0)
        self.assertTrue(map['grid'][(2, 5)] == 25)
        self.assertTrue(map['grid'][(1, 1)] == 1)
        self.assertTrue(map['grid'][(4, 7)] == 8)

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 31)
    
    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 29)

if __name__ == '__main__':
    unittest.main()