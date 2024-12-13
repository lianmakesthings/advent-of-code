from node import Node
from read import read
import os

def build_tree(input):
    root = Node('/', None, 'dir')
    current_node = root
    input = input[1:]
    for line in input:
        print(line)
        if line.startswith('$'): 
            if line.startswith('$ cd '):
                if line.endswith('..'):
                    current_node = current_node.parent
                    print('moving pointer to node', current_node.name)
                else:
                    node_name = line.split(" ")[-1]
                    node = [node for node in current_node.children if node.name == node_name]
                    current_node = node[0] if len(node) > 0 else Node(node_name, current_node, 'dir')
                    print('moving pointer to node', current_node.name)
        else:
            [size, name] = line.split(" ")
            child = Node(name, current_node, size)
            current_node.children.append(child)
            print("adding child {} to node {}".format(child.name, current_node.name))
        
    return root

def calculate_size(node):
    sum = 0
    print("node {} has children {}".format(node.name, [child.name for child in node.children]))
    for child in node.children:
        print("looking up size of child {} for node {}".format(child.name, node.name))
        if child.size: 
            sum += child.size
        else: 
            child.size = calculate_size(child)
            sum += child.size
        print("child {} has size {}".format(child.name, child.size))
    node.size = sum
    return sum

def get_dirs(node, dirs):
    for child in node.children:
        print("checking child {} for node {}".format(child.name, node.name))
        if child.is_dir: dirs.append(child)
        get_dirs(child, dirs)
    return dirs

def part1(filename):
    input = read.from_file(filename)
    root = build_tree(input)
    calculate_size(root)
    dirs = get_dirs(root, [])
    return sum([n.size for n in dirs if n.size < 100000])

def part2(filename):
    input = read.from_file(filename)
    root = build_tree(input)
    calculate_size(root)
    required_space = 30000000 - (70000000 - root.size)
    smallest_dir = root
    for dir in get_dirs(root, []):
        if dir.size >= required_space and dir.size < smallest_dir.size: smallest_dir = dir
    return smallest_dir.size

print(part2("{}/input.txt".format(os.path.dirname(__file__))))