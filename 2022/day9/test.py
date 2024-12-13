import os
import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_move_knots(self):
        test_cases = [
            {'knots': [(1, 2), (1, 1)], 'direction': 'R', 'expected': [(1, 3), (1, 2)]},
            {'knots': [(2, 1), (3, 1)], 'direction': 'D', 'expected': [(1, 1), (2, 1)]},
            {'knots': [(2, 2), (1, 1)], 'direction': 'U', 'expected': [(3, 2), (2, 2)]},
            {'knots': [(2, 2), (1, 1)], 'direction': 'R', 'expected': [(2, 3), (2, 2)]},
            {'knots': [(0, 0), (0, 0)], 'direction': 'R', 'expected': [(0, 1), (0, 0)]},
            {'knots': [(0, 4), (0, 3)], 'direction': 'U', 'expected': [(1, 4), (0, 3)]},
            {'knots': [(4, 4), (3, 4)], 'direction': 'L', 'expected': [(4, 3), (3, 4)]},
            {'knots': [(4, 3), (3, 4)], 'direction': 'L', 'expected': [(4, 2), (4, 3)]},
            {'knots': [(3, 5), (3, 4)], 'direction': 'D', 'expected': [(2, 5), (3, 4)]},
        ]
        for data in test_cases:
            self.assertEqual(solution.move_knots(data['knots'], data['direction']), data['expected'])
    
    def test_is_adjacent(self):
        test_cases = [
            {'knots': [(1, 2), (1, 1)], 'expected': True},
            {'knots': [(2, 1), (3, 1)], 'expected': True},
            {'knots': [(2, 1), (1, 2)], 'expected': True},
            {'knots': [(1, 1), (1, 1)], 'expected': True},
            {'knots': [(1, 3), (1, 1)], 'expected': False},
            {'knots': [(1, 1), (3, 1)], 'expected': False},
            {'knots': [(3, 2), (1, 1)], 'expected': False},
            {'knots': [(2, 3), (1, 1)], 'expected': False},
        ]
        for data in test_cases:
            self.assertEqual(solution.is_adjacent(data['knots']), data['expected'])

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 13)

    def test_follow_head(self):
        test_cases = [
            {'knots': [(0, 1), (0, 0)], 'direction': "R", 'expected': [(0, 1), (0, 0)]},
            {'knots': [(0, 2), (0, 0)], 'direction': "R", 'expected': [(0, 2), (0, 1)]},
            {'knots': [(2, 4), (0, 3)], 'direction': "U", 'expected': [(2, 4), (1, 4)]},
            {'knots': [(3, 1), (4, 2)], 'direction': "D", 'expected': [(3, 1), (4, 2)]},
            {'knots': [(2, 2), (3, 4)], 'direction': "L", 'expected': [(2, 2), (2, 3)]},
        ]
        for data in test_cases:
            self.assertEqual(solution.follow_head(data['knots']), data['expected'])

    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input_2.txt".format(os.path.dirname(__file__))), 36)

if __name__ == '__main__':
    unittest.main()