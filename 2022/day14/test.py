import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    def test_build_grid(self):
        grid = solution.build_grid(read.from_file("{}/test_input.txt".format(os.path.dirname(__file__))))
        self.assertTrue((498, 4) in grid)
        self.assertTrue((498, 5) in grid)
        self.assertTrue((498, 6) in grid)
        self.assertTrue((497, 6) in grid)
        self.assertTrue((496, 6) in grid)
    
    def test_calculate_sand(self):
        grid = solution.build_grid(read.from_file("{}/test_input.txt".format(os.path.dirname(__file__))))
        grid = solution.calculate_sand(grid, [], None)
        self.assertTrue((500, 8) in grid)
        grid = solution.calculate_sand(grid, [], None)
        self.assertTrue((499, 8) in grid)
        for x in range(2, 5):
            grid = solution.calculate_sand(grid, [], None)
        self.assertTrue((500, 7) in grid)
        self.assertTrue((498, 8) in grid)
        self.assertTrue((501, 8) in grid)
        for x in range(5, 22):
            grid = solution.calculate_sand(grid, [], None)
        self.assertTrue((500, 2) in grid)
        for x in range(22, 24):
            grid = solution.calculate_sand(grid, [], None)
        self.assertTrue((497, 5) in grid)
        self.assertTrue((495, 8) in grid)
        self.assertEqual(grid, solution.calculate_sand(grid, [493, 503], None))

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 24)
    
    def test_fall_to_bottom(self):
        grid = solution.build_grid(read.from_file("{}/test_input.txt".format(os.path.dirname(__file__))))
        for x in range(93):
            grid = solution.calculate_sand(grid, [], 11)
        self.assertTrue((503, 10) in grid)
    
    def test_stop_flow(self):
        grid = solution.build_grid(read.from_file("{}/test_input.txt".format(os.path.dirname(__file__))))
        for x in range(93):
            grid = solution.calculate_sand(grid, [], 11)
        new_grid = solution.calculate_sand(grid, [], 11)
        self.assertEqual(grid, new_grid)

    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 93)
        
if __name__ == '__main__':
    unittest.main()