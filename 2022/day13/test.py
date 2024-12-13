import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    def test_is_in_order(self):
        test_cases = [
            {'input': [[1,1,3,1,1], [1,1,5,1,1]], 'expected': True},
            {'input': [[[1],[2,3,4]], [[1],4]], 'expected': True},
            {'input': [[9], [[8,7,6]]], 'expected': False},
            {'input': [[[4,4],4,4], [[4,4],4,4,4]], 'expected': True},
            {'input': [[7,7,7,7], [7,7,7]], 'expected': False},
            {'input': [[], [3]], 'expected': True},
            {'input': [[[[]]], [[]]], 'expected': False},
            {'input': [[1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]], 'expected': False},
            ]
        for test_case in test_cases:
            self.assertEqual(solution.is_in_order(test_case['input'][0], test_case['input'][1]), test_case['expected'])

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 13)

    def test_bubble_sort(self):
        expected = [[], [[]], [[[]]], [1,1,3,1,1], [1,1,5,1,1], [[1],[2,3,4]], [1,[2,[3,[4,[5,6,0]]]],8,9], [1,[2,[3,[4,[5,6,7]]]],8,9], [[1],4], [3], [[4,4],4,4], [[4,4],4,4,4], [7,7,7], [7,7,7,7], [[8,7,6]], [9]]
        input = [[1,1,3,1,1], [1,1,5,1,1], [[1],[2,3,4]], [[1],4], [9], [[8,7,6]], [[4,4],4,4], [[4,4],4,4,4], [7,7,7,7], [7,7,7], [], [3], [[[]]], [[]], [1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]]
        self.assertEqual(solution.bubble_sort(input), expected)

    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 140)
if __name__ == '__main__':
    unittest.main()