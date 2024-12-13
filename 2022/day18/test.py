import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    @unittest.skip("skip")
    def test_find_adjacent_cubes(self):
        cube = (1, 1, 1)
        expected = [
            {"cube": (2, 1, 1), "is_adjacent": True},
            {"cube": (3, 1, 1), "is_adjacent": False},
            {"cube": (1, 2, 1), "is_adjacent": True},
            {"cube": (2, 2, 1), "is_adjacent": False},
            {"cube": (1, 1, 1), "is_adjacent": False},
        ]
        all_cubes = [(1, 1, 1), (2, 1, 1), (3, 1, 1), (1, 2, 1), (2, 2, 1)]
        adjacent_cubes = solution.find_adjacent_cubes(cube, all_cubes)
        for test_case in expected:
            self.assertEqual(test_case["cube"] in adjacent_cubes, test_case["is_adjacent"])
    
    @unittest.skip("skip")
    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 64)

    # @unittest.skip("skip")
    def test_find_holes(self):
        cubes = [(2,2,2), (1,2,2), (3,2,2), (2,1,2), (2,3,2), (2,2,1), (2,2,3), (2,2,4), (2,2,6), (1,2,5), (3,2,5), (2,1,5), (2,3,5)]
        expected = [(2, 2, 5)]
        self.assertEqual(solution.find_holes(cubes), expected)

    # @unittest.skip("skip")
    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 58)

if __name__ == '__main__':
    unittest.main()