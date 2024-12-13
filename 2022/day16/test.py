import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    def test_parse_input(self):
        expected = {
            "AA": {'flow_rate': 0, 'tunnels': ["DD", "II", "BB"]},
            "BB": {'flow_rate': 13, 'tunnels': ["CC", "AA"]},
            "CC": {'flow_rate': 2, 'tunnels': ["DD", "BB"]},
            "DD": {'flow_rate': 20, 'tunnels': ["CC", "AA", "EE"]},
            "EE": {'flow_rate': 3, 'tunnels': ["FF", "DD"]},
            "FF": {'flow_rate': 0, 'tunnels': ["EE", "GG"]},
            "GG": {'flow_rate': 0, 'tunnels': ["FF", "HH"]},
            "HH": {'flow_rate': 22, 'tunnels': ["GG"]},
            "II": {'flow_rate': 0, 'tunnels': ["AA", "JJ"]},
            "JJ": {'flow_rate': 21, 'tunnels': ["II"]},
        }
        result = solution.parse_input("{}/test_input.txt".format(os.path.dirname(__file__)))
        for test_case in expected:
            self.assertTrue(test_case in result)
            self.assertEqual(result[test_case], expected[test_case])

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 1651)
    
        
if __name__ == '__main__':
    unittest.main()