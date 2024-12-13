import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    @unittest.skip("skip")
    def test_parse_input(self):
        result = solution.parse_input("{}/test_input.txt".format(os.path.dirname(__file__)))
        self.assertTrue([(2, 18), (-2, 15)] in result)
    
    @unittest.skip("skip")
    def test_calculate_non_beacons(self):
        non_beacons = solution.calculate_non_beacons_by_row([(8, 7), (2, 10)], 7)
        self.assertTrue(-1 in non_beacons)
        self.assertTrue(17 in non_beacons)
        self.assertEqual(len(non_beacons), 19)

        non_beacons = solution.calculate_non_beacons_by_row([(20, 14), (25, 17)], 10)
        self.assertTrue(24 in non_beacons)

    @unittest.skip("skip")
    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__)), 10), 26)
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__)), 9), 25)
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__)), 11), 28)

    def test_find_beacon(self):
        data = solution.parse_input("{}/test_input.txt".format(os.path.dirname(__file__)))
        self.assertEqual(solution.find_beacon(data, 20), (14, 11))
    
    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__)), 20), 56000011)
        
if __name__ == '__main__':
    unittest.main()