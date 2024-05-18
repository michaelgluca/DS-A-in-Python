from binary_search_tree import *

myTree = BinarySearchTree()


def r_contains(self, value):
    return self.__r_contains(self.root, value)


def __r_contains(self, current_node, value):
    if current_node is None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)
    if value > current_node.value:
        return self.__r_contains(current_node.right, value)


def r_insert(self, value):
    if self.root is None:
        self.root = Node(value)
        self.__r_insert(self.root, value)


def __r_insert(self, current_node, value):
    if current_node is None:
        return Node(value)
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value)
    return current_node


def min_value(self, current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.value


def __delete_node(self, current_node, value):
    if current_node is None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    else:
        if current_node.left is None and current_node.right is None:
            return None
        elif current_node.left is None:
            current_node = current_node.right
        elif current_node.right is None:
            current_node = current_node.left
        else:
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    return current_node


def delete_node(self, value):
    self.root = self.__delete_node(self.root, value)


def invert(self):
    self.root = self.__invert_tree(self.root)


def __invert_tree(self, node):
    if node is None:
        return None

    temp = node.left
    node.left = self.__invert_tree(node.right)
    node.right = self.__invert_tree(temp)

    return node
