import os
import unittest
import solution
from node import Node
from read import read

class TestSolution(unittest.TestCase):
    def test_build_tree(self):
        expected_nodes = {
            'a': None,
            'b.txt': 14848514,
            'c.dat': 8504156,
            'd': None,
            'j': 4060174,
            'd.log': 8033020,
            'd.ext': 5626152,
            'k': 7214296
        }
        result = solution.build_tree(read.from_file("{}/test_input.txt".format(os.path.dirname(__file__))))
        self.assertEqual(len(result.children), 4)
        for c in result.children: self.assertEqual(c.size, expected_nodes[c.name])
        self.assertEqual(len(result.children[-1].children), 4)
        for c in result.children[-1].children: self.assertEqual(c.size, expected_nodes[c.name])

    def test_calculate_size(self):
        root = Node('/', None, 'dir')
        a = Node('a', root, 'dir')
        e = Node('e', a, 'dir')
        e.children = [Node('i', e, 584)]
        a.children = [e, Node('f', a, 29116), Node('g', a, 2557), Node('h.lst', a, 62596)]
        d = Node('d', root, 'dir')
        d.children = [Node('j', d, 4060174), Node('d.log', d, 8033020), Node('d.ext', d, 5626152), Node('k', d, 7214296)]
        root.children = [a, Node('b.txt', root, 14848514), Node('c.dat', root, 8504156), d]
        
        expected = {
            584: e,
            94853: a,
            24933642: d,
            48381165: root
        }
        for data in expected:
            self.assertEqual(solution.calculate_size(expected[data]), data)

    def test_get_dirs(self):
        root = Node('/', None, 'dir')
        a = Node('a', root, 'dir')
        e = Node('e', a, 'dir')
        e.children = [Node('i', e, 584)]
        a.children = [e, Node('f', a, 29116), Node('g', a, 2557), Node('h.lst', a, 62596)]
        d = Node('d', root, 'dir')
        d.children = [Node('j', d, 4060174), Node('d.log', d, 8033020), Node('d.ext', d, 5626152), Node('k', d, 7214296)]
        root.children = [a, Node('b.txt', root, 14848514), Node('c.dat', root, 8504156), d]
        
        expected = [e.name, a.name, d.name, root.name]
        for n in solution.get_dirs(root, []):
            self.assertTrue(n.name in expected)

    def test_part1(self):
        self.assertEqual(solution.part1("{}/test_input.txt".format(os.path.dirname(__file__))), 95437)

    def test_part2(self):
        self.assertEqual(solution.part2("{}/test_input.txt".format(os.path.dirname(__file__))), 24933642)

if __name__ == '__main__':
    unittest.main()