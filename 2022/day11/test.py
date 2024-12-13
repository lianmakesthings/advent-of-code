import os
import unittest
import solution
from read import read

class TestSolution(unittest.TestCase):

    def test_monkey(self):
        input = read.from_file("{}/test_input.txt".format(os.path.dirname(__file__)))
        excepted = [
            {'index': 0, 'name': 0, 'items': [79, 98], 'inspect': 19, 'test': 23, 'true_monkey': 2, 'false_monkey': 3},
            {'index': 7, 'name': 1, 'items': [54, 65, 75, 74], 'inspect': 7, 'test': 19, 'true_monkey': 2, 'false_monkey': 0},
            {'index': 14, 'name': 2, 'items': [79, 60, 97], 'inspect': 1, 'test': 13, 'true_monkey': 1, 'false_monkey': 3},
            {'index': 21, 'name': 3, 'items': [74], 'inspect': 4, 'test': 17, 'true_monkey': 0, 'false_monkey': 1},
            ]
        for data in excepted:
            monkey = solution.create_monkey(input[data['index']:data['index']+6])
            self.assertEqual(monkey.name, data['name'])
            self.assertEqual(monkey.items, data['items'])
            self.assertEqual(monkey.inspect(1), data['inspect'])
            self.assertEqual(monkey.test(data['test']), data['true_monkey'])
            self.assertEqual(monkey.test(data['test']+1), data['false_monkey'])

    def test_round(self):
        input = read.from_file("{}/test_input.txt".format(os.path.dirname(__file__)))
        monkeys = [solution.create_monkey(input[i:i+6]) for i in range(0, len(input), 7)]
        monkeys = solution.execute_round(monkeys)
        self.assertEqual(monkeys[0].items, [20, 23, 27, 26])
        self.assertEqual(monkeys[1].items, [2080, 25, 167, 207, 401, 1046])
        self.assertEqual(monkeys[2].items, [])
        self.assertEqual(monkeys[3].items, [])

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 10605)
    
    def test_round_part2(self):
        input = read.from_file("{}/test_input.txt".format(os.path.dirname(__file__)))
        monkeys = [solution.create_monkey(input[i:i+6]) for i in range(0, len(input), 7)]
        monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 2)
        self.assertEqual(monkeys[1].inspect_count, 4)
        self.assertEqual(monkeys[2].inspect_count, 3)
        self.assertEqual(monkeys[3].inspect_count, 6)

        for i in range(1, 20):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 99)
        self.assertEqual(monkeys[1].inspect_count, 97)
        self.assertEqual(monkeys[2].inspect_count, 8)
        self.assertEqual(monkeys[3].inspect_count, 103)

        for i in range(20, 1000):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 5204)
        self.assertEqual(monkeys[1].inspect_count, 4792)
        self.assertEqual(monkeys[2].inspect_count, 199)
        self.assertEqual(monkeys[3].inspect_count, 5192)

        for i in range(1000, 2000):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 10419)
        self.assertEqual(monkeys[1].inspect_count, 9577)
        self.assertEqual(monkeys[2].inspect_count, 392)
        self.assertEqual(monkeys[3].inspect_count, 10391)

        for i in range(2000, 3000):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 15638)
        self.assertEqual(monkeys[1].inspect_count, 14358)
        self.assertEqual(monkeys[2].inspect_count, 587)
        self.assertEqual(monkeys[3].inspect_count, 15593)

        for i in range(3000, 4000):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 20858)
        self.assertEqual(monkeys[1].inspect_count, 19138)
        self.assertEqual(monkeys[2].inspect_count, 780)
        self.assertEqual(monkeys[3].inspect_count, 20797)

        for i in range(4000, 5000):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 26075)
        self.assertEqual(monkeys[1].inspect_count, 23921)
        self.assertEqual(monkeys[2].inspect_count, 974)
        self.assertEqual(monkeys[3].inspect_count, 26000)

        for i in range(5000, 10000):
            monkeys = solution.execute_round_part2(monkeys)
        self.assertEqual(monkeys[0].inspect_count, 52166)
        self.assertEqual(monkeys[1].inspect_count, 47830)
        self.assertEqual(monkeys[2].inspect_count, 1938)
        self.assertEqual(monkeys[3].inspect_count, 52013)

    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 2713310158)

if __name__ == '__main__':
    unittest.main()