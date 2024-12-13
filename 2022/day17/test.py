import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    @unittest.skip("skip")
    def test_move_rock_once(self):
        chamber = set([(0,0)])
        rock_current = [[(3, 4), (4, 4), (5, 4), (6, 4)]]
        direction = ">"

        expected = [[(4, 4), (5, 4), (6, 4), (7, 4)]]
        self.assertEqual(solution.move_rock(chamber, rock_current, direction), (chamber, expected))
    
    @unittest.skip("skip")
    def test_move_rock_blocked(self):
        chamber = set([(0,0)])
        test_cases = [
            ([[(4, 2), (5, 2), (6, 2), (7, 2)]], ">"),
            ([[(1, 2), (2, 2), (3, 2), (4, 2)]], "<"),
        ]
        for test in test_cases:
            self.assertEqual(solution.move_rock(chamber, test[0], test[1]), (chamber, test[0]))
    
    @unittest.skip("skip")
    def test_falling_rock(self):
        chamber = set([(0,0)])
        rock_current = [[(3, 4), (4, 4), (5, 4), (6, 4)]]
        direction = ""

        expected = [[(3, 3), (4, 3), (5, 3), (6, 3)]]
        self.assertEqual(solution.move_rock(chamber, rock_current, direction), (chamber, expected))
    
    @unittest.skip("skip")
    def test_stopped_rock(self):
        chamber = set([(0,0)])
        rock_current = [[(3, 1), (4, 1), (5, 1), (6, 1)]]
        direction = ""

        expected_rock = []
        expected_chamber = set([(0,0),(3, 1), (4, 1), (5, 1), (6, 1)])
        self.assertEqual(solution.move_rock(chamber, rock_current, direction), (expected_chamber, expected_rock))
    
    # @unittest.skip("skip")
    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 3068)

if __name__ == '__main__':
    unittest.main()