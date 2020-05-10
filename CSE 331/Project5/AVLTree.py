import random as r

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.height == other.height

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result
            
    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """
        Inserts a value into the AVL tree while keeping balance
        :param node: root of the subtree where val is being inserted
        :param value: value of the node being inserted
        """
        if self.root is None:
            insert_node = Node(value)
            self.root = insert_node
            self.size = self.size + 1
        else:
            if node is not None:
                if value < node.value:
                    if node.left is None:
                        insert_node = Node(value)
                        node.left = insert_node
                        insert_node.parent = node
                        self.size = self.size + 1
                    else:
                        self.insert(node.left, value)
                elif value == node.value:
                    return
                else:
                    if node.right is None:
                        insert_node = Node(value)
                        node.right = insert_node
                        insert_node.parent = node
                        self.size = self.size + 1
                    else:
                        self.insert(node.right, value)
        if node is not None:
            self.rebalance(node)

    def remove(self, node, value):
        """
        Takes in a value to remove from the tree
        :param node: root of the (sub)tree the node will be removed from
        :param value: value to remove from the tree
        :return: root of the subtree
        """
        if node is None:
            return
        if node.value == value:
            if node.right is None and node.left is None:
                if node.parent is None:
                    self.root = None
                elif node.parent.left == node:
                    node.parent.left = None
                    node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
                else:
                    node.parent.right = None
                    node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
            elif node.right is not None and node.left is None:
                if node.parent is None:
                    self.root = node.right
                elif node.parent.left == node:
                    node.parent.left = node.right
                    node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
                else:
                    node.parent.right = node.right
                    node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
            elif node.left is not None and node.right is None:
                if node.parent is None:
                    self.root = node.left
                elif node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                max_node = self.max(node.left)
                if max_node.parent is not node:
                    max_node.parent.right = max_node.left
                    max_node.parent = node.parent
                    max_node.left = node.left
                    max_node.right = node.right
                    node.left.parent = max_node
                    node.right.parent = max_node
                else:
                    max_node.parent = node.parent
                    max_node.right = node.right
                    node.right.parent = max_node
                if node.parent is None:
                    self.root = max_node
                    max_node.height = max(self.height(max_node.left), self.height(max_node.right)) + 1
                elif node.parent.left == node:
                    node.parent.left = max_node
                    max_node.height = max(self.height(max_node.left), self.height(max_node.right)) + 1
                    node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
                else:
                    node.parent.right = max_node
                    max_node.height = max(self.height(max_node.left), self.height(max_node.right)) + 1
                    node.parent.height = max(self.height(node.parent.left), self.height(node.parent.right)) + 1
            self.size = self.size - 1
            return self.root
        elif node.value < value:
            self.remove(node.right,value)
        else:
            self.remove(node.left, value)
        if node is not None:
            return self.rebalance(node)

    def search(self, node, value):
        """
        Uses value and seaches for the node that applies
        :param value: value of node to find
        :param node: node of subtree root
        :return: node with the given value if found, else returns the potential parent node
        """
        cur = node
        if cur is not None:
            while cur is not None:
                if value == cur.value:
                    return cur
                elif value < cur.value:
                    if cur.left is None:
                        return cur
                    cur = cur.left
                else:
                    if cur.right is None:
                        return cur
                    cur = cur.right
        else:
            return None

    def inorder(self, node):
        """
        gives generator object of tree using the traversal method
        :param node: node to start traversal
        :return:generator object of the tree traversed
        """
        if node is None:
            return

        if node.left is not None:
            yield from self.inorder(node.left)

        yield node

        if node.right is not None:
            yield from self.inorder(node.right)

    def preorder(self, node):
        """
        gives generator object of tree using the traversal method
        :param node: node to start traversal
        :return:generator object of the tree traversed
        """
        if node is None:
            return

        yield node

        if node.left is not None:
            yield from self.preorder(node.left)

        if node.right is not None:
            yield from self.preorder(node.right)

    def postorder(self, node):
        """
        gives generator object of tree using the traversal method
        :param node: node to start traversal
        :return:generator object of the tree traversed
        """
        if node is None:
            return

        if node.left is not None:
            yield from self.postorder(node.left)

        if node.right is not None:
            yield from self.postorder(node.right)

        yield node

    def breadth_first(self, node):
        """
        gives generator object of tree using the traversal method
        :param node: node to start traversal
        :return:generator object of the tree traversed
        """

        if node is None:
            return
        queue = [self.root]
        while queue:
            yield queue[0]
            cur = queue[0]
            queue = queue[1:]
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

    def depth(self, value):
        """
        Finds depth of a node with a given value
        :param value: value of node to find depth of
        :return:  depth of the node
        """
        if self.root is None:
            return -1
        depth = 0
        if self.search(self.root, value).value == value:
            node = self.search(self.root, value)
            while node != self.root:
                node = node.parent
                depth += 1
            return depth
        else:
            return -1

    def height(self, node):
        """
        Finds height of subtree
        :param node: root of subtree to find height up
        :return: height of subtree
        """
        if node is None:
            return -1
        return node.height

    def min(self, node):
        """
        minimum of the tree rooted at the given node
        :param node: subtree root to find min of
        :return: min of subtree
        """
        if node is None or node.left is None:
            return node
        left_min = self.min(node.left)
        return left_min

    def max(self, node):
        """
        max of the tree rooted at the given node
        :param node: subtree root to find max of
        :return: max of subtree
        """
        if node is None or node.right is None:
            return node
        right_max = self.max(node.right)
        return right_max

    def get_size(self):
        """
        finds size of tree
        :return: size of tree
        """
        return self.size

    def get_balance(self, node):
        """
        Determines balance of the tree at subtree
        :param node: root of subtree to find balance of
        :return: balance factor
        """
        right = -1
        if node.right is not None:
            right = node.right.height
        left = -1
        if node.left is not None:
            left = node.left.height
        return left - right

    def left_rotate(self, root):
        """
        Preforms a left rotate operation
        :param root: root of subtree where rotaion occurs
        :return: root of new subtree
        """
        RLchild = root.right.left
        if root.parent is not None:
            if root.parent.left == root:
                root.parent.left = root.right
                if root.right is not None:
                    root.right.parent = root.parent
                # update height
            elif root.parent.right == root:
                # set parents left child to root.left
                root.parent.right = root.right
                if root.right is not None:
                    root.right.parent = root.parent
           # root.right.parent.height = max(self.height(root.right.parent.left), self.height(root.right.parent.right)) + 1
        else:
            self.root = root.right
            self.root.parent = None
        # set root.lefts, right child node as root
        root.right.left = root
        if root is not None:
            root.parent = root.right
        # set roots left cgild as LRchild
        root.right = RLchild
        if RLchild is not None:
            RLchild.parent = root
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        if root.parent is not None:
            root.parent.height = max(self.height(root.parent.left), self.height(root.parent.right)) + 1
        if root.parent.parent is not None:
            root.parent.parent.height = max(self.height(root.parent.parent.left), self.height(root.parent.parent.right)) + 1

        # if root.right is not None:
        #    root.right.height = max(self.height(root.right.left), self.height(root.right.right)) + 1

        return root.parent

    def right_rotate(self, root):
        """
        Preforms a right rotate operation
        :param root: root of subtree where rotaion occurs
        :return: root of new subtree
        """
        LRchild = root.left.right
        if root.parent is not None:
            if root.parent.left == root:
                root.parent.left = root.left
                if root.left is not None:
                    root.left.parent = root.parent
                #update height
            elif root.parent.right == root:
                # set parents left child to root.left
                root.parent.right = root.left
                if root.left is not None:
                    root.left.parent = root.parent
                # update height
            root.left.parent.height = max(self.height(root.left.parent.left),
                                           self.height(root.left.parent.right)) + 1
        else:
            self.root = root.left
            self.root.parent = None
        #set root.lefts, right child node as root
        root.left.right = root
        if root is not None:
            root.parent = root.left
        #set roots left cgild as LRchild
        root.left = LRchild
        if LRchild is not None:
            LRchild.parent = root

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        if root.left is not None:
            root.left.height = max(self.height(root.left.left), self.height(root.left.right)) + 1

        return root.parent

    def rebalance(self, node):
        """
        Acts to balance of the tree at subtree
        :param node: root of subtree to balance
        :return: root of new subtree
        """
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        if self.get_balance(node) == -2:
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
            return self.left_rotate(node)
        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
            return self.right_rotate(node)

def sum_update(root, total):
    """
     replace the keys in the tree with the sum of the keys and orders them
    :param root: root of subtree where action is occuring
    :param total: current total of visited nodes
    :return: total sum at node
    """
    if root is None:
        return

    if root.right is not None:
        total = sum_update(root.right, total)

    total = total + root.value
    root.value = total

    if root.left is not None:
        total = sum_update(root.left, total)
    if root.parent is not None:
        return total
    else:
        swap_branch(root)
def swap_branch(cur):
    """
    Swaps branch
    :param cur: root of subtree where action is occuring
    """

    if cur is None:
        return
    if cur.left is not None:
        swap_branch(cur.left)
    if cur.right is not None:
        swap_branch(cur.right)
    temp = cur.left
    cur.left = cur.right
    cur.right = temp


