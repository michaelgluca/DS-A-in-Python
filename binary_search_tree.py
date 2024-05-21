class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def bfs(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid_bst(self):
        # Get node values of the binary search tree in ascending order
        node_values = self.dfs_in_order()
        # Iterate through the node values using a for loop
        for i in range(1, len(node_values)):
            # Check if each node value is greater than the previous node value
            if node_values[i] <= node_values[i - 1]:
                # If node values are not sorted in ascending order, the binary
                # search tree is not valid, so return False
                return False
        # If all node values are sorted in ascending order, the binary search tree
        # is a valid binary search tree, so return True
        return True


def kth_smallest(self, k):
    # create a stack to hold nodes
    stack = []
    # start at the root of the tree
    temp = self.root

    while stack or temp:
        # traverse to the leftmost node
        while temp:
            # add the node to the stack
            stack.append(temp)
            temp = temp.left

        # pop the last node added to the stack
        temp = stack.pop()
        k -= 1
        # if kth smallest element is found, return the value
        if k == 0:
            return temp.value

        # move to the right child of the node
        temp = temp.right

        # if k is greater than the number of nodes in the tree, return None
    return None
