class Node:
    def __init__(self, name, parent, size):
        self.name = name
        self.children = []
        self.parent = parent
        self.is_dir = size == 'dir'
        self.size = int(size) if not self.is_dir else None
        