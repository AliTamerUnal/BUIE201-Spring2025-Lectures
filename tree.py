class TreeItem:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    # operator overloading functions
    def __lt__(self, other):
        return self._data < other._data
    def __gt__(self, other):
        return self._data > other._data
    def __eq__(self, other):
        return self._data == other._data

    def left(self):
        return self._left

    def right(self):
        return self._right

    def update(self, data = None, left = None, right = None):
        if data is not None:
            self._data = data
        if left is not None:
            self._left = left
        if right is not None:
            self._right = right

    def print(self, level):
        print (level * "    ", self._data)

class Tree:
    def __init__(self):
        self._root = None

    def _insert_tree_item(self, new_tree_item, root):        
        if root is None:
            self._root = new_tree_item
        else:
            if new_tree_item < root: # calls new_tree_item.__lt__(root)
                if root.left() is None:
                    root.update(left = new_tree_item)
                else:
                    self._insert_tree_item(new_tree_item, root.left())
            else:
                if root.right() is None:
                    root.update(right = new_tree_item)
                else:
                    self._insert_tree_item(new_tree_item, root.right())

    def insert(self, new_data):
        new_tree_item = TreeItem(new_data)
        self._insert_tree_item(new_tree_item, self._root)
    
    def _print_sub_tree(self, root, level):  
        if root is None:
            return
        
        self._print_sub_tree(root.right(), level + 1)
        root.print(level)
        self._print_sub_tree(root.left(), level + 1)

    def print(self):      
        if self._root is None:
            return

        self._print_sub_tree(self._root, 1)


t = Tree()
t.insert(6)
t.insert(3)
t.insert(4)
t.insert(8)
t.insert(7)

t.print()