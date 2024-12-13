from read import read
import os
from operator import mul
from functools import reduce

class Monkey:
    def __init__(self, name, items, operation, test):
        self.name = int(name)
        self.items = items
        self.inspect_operation = operation[0]
        self.inspect_value = operation[1]
        self.test_value = test[0]
        self.true_monkey = test[1]
        self.false_monkey = test[2]
        self.inspect_count = 0

    def inspect(self, old):
        self.inspect_count += 1
        if self.inspect_operation == '+':
            return old + int(self.inspect_value)
        elif self.inspect_operation == '*':
            if (self.inspect_value) == 'old':
                return old * old
            else:
                return old * int(self.inspect_value)
        else:
            raise Exception("Invalid operation")
    
    def test(self, item):
        if item % self.test_value == 0:
            return self.true_monkey
        else:
            return self.false_monkey

def create_monkey(input):
    name = input[0].split(' ')[1][0]
    items = [int(i.strip()) for i in input[1].split(':')[1].split(',')]
    [_, _, _, _, operation, value] = input[2].split(' ')
    test_value = int(input[3].split(' ')[-1])
    true_monkey = int(input[4].split(' ')[-1])
    false_monkey = int(input[5].split(' ')[-1])
    return Monkey(name, items, [operation, value], [test_value, true_monkey, false_monkey])

def execute_round(monkeys):
    for m in monkeys:
        for i in m.items:
            print("Monkey {} has item {}".format(m.name, i))
            i = m.inspect(i)
            print("Monkey {} inspects item and gets {}".format(m.name, i))
            i = i // 3
            print("Worry level decreases to {}".format(i))
            to_monkey_name = m.test(i)
            print("Monkey sends item to monkey {}".format(to_monkey_name))
            to_monkey = [t for t in monkeys if t.name == to_monkey_name][0]
            to_monkey.items.append(i)
            print("Monkey {} now has items {}".format(to_monkey_name, to_monkey.items))
        m.items = []
    return monkeys

def part1(path):
    input = read.from_file(path)
    monkeys = [create_monkey(input[i:i+6]) for i in range(0, len(input), 7)]
    for i in range(20):
        print("Round {}".format(i))
        monkeys = execute_round(monkeys)
    monkey_business = [m.inspect_count for m in monkeys]
    return max(monkey_business) * max([m for m in monkey_business if m != max(monkey_business)])

def execute_round_part2(monkeys):
    super_divisor = reduce(mul, [m.test_value for m in monkeys], 1)
    for m in monkeys:
        for i in m.items:
            # monkey inspects
            i = m.inspect(i)
            # calm down
            modulo = i % super_divisor
            i = super_divisor + modulo
            # monkey tests
            to_monkey_name = m.test(i)
            to_monkey = [t for t in monkeys if t.name == to_monkey_name][0]
            
            to_monkey.items.append(i)
        m.items = []
    return monkeys

def part2(path):
    input = read.from_file(path)
    monkeys = [create_monkey(input[i:i+6]) for i in range(0, len(input), 7)]
    for i in range(10000):
        print("Round {}".format(i))
        monkeys = execute_round_part2(monkeys)
    monkey_business = [m.inspect_count for m in monkeys]
    return max(monkey_business) * max([m for m in monkey_business if m != max(monkey_business)])

print(part2("{}/input.txt".format(os.path.dirname(__file__))))