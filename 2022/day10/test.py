import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):
    def test_value_after_cycle(self):
        current_val = 1
        instructions = ['noop', 'addx 3', 'addx -5']
        self.assertEqual(solution.get_value_after_cycles(current_val, 1, instructions), 1)
        self.assertEqual(solution.get_value_after_cycles(current_val, 2, instructions), 1)
        self.assertEqual(solution.get_value_after_cycles(current_val, 3, instructions), 4)
        self.assertEqual(solution.get_value_after_cycles(current_val, 4, instructions), 4)
        self.assertEqual(solution.get_value_after_cycles(current_val, 5, instructions), -1)
    
    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 13140)

    def test_draw_line(self):
        instructions = read.from_file("{}/test_input.txt".format(os.path.dirname(__file__)))
        processed_instructions = []
        for i in instructions:
            if i == 'noop':
                processed_instructions.append(i)
            else:
                processed_instructions.extend(['noop', i])
        sprite = [0, 1, 2]
        self.assertEqual(solution.draw_line(sprite, processed_instructions)[0], '##..##..##..##..##..##..##..##..##..##..')


if __name__ == '__main__':
    unittest.main()