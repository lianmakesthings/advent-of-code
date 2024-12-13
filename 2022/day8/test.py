import os
import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_check_visibility(self):
        map = ['30373', '25512', '65332', '33549', '35390']
        expected = {
            (0, 0): True,
            (1, 0): True,
            (1, 1): True,
            (1, 2): True,
            (1, 3): False,
        }
        for coords in expected:
            self.assertEqual(solution.is_visible(map, coords), expected[coords])

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 21)
    
    def test_scenic_score(self):
        map = ['30373', '25512', '65332', '33549', '35390']
        self.assertEqual(solution.calculate_scenic_score(map, (2, 1)), 4)
        self.assertEqual(solution.calculate_scenic_score(map, (2, 3)), 8)
        self.assertEqual(solution.calculate_scenic_score(map, (0, 3)), 0)

    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 8)
if __name__ == '__main__':
    unittest.main()