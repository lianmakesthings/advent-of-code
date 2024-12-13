import os
import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_part1(self):
        test_cases = {
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
            "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
            "nppdvjthqldpwncqszvftbrmjlhg": 6,
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11
        }
        for case in test_cases:
            self.assertEqual(solution.part1(case), test_cases[case])

    def test_part2(self):
        test_cases = {
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
            "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
            "nppdvjthqldpwncqszvftbrmjlhg": 23,
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26
        }
        for case in test_cases:
            self.assertEqual(solution.part2(case), test_cases[case])

if __name__ == '__main__':
    unittest.main()