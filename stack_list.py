class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()
  
def reverse_string(string):
    stack = Stack()
    reverse_string = ""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reverse_string += stack.pop()
    return reverse_string

def sort_stack(stack):
    additional_stack = Stack()
 
    while not stack.is_empty():
        temp = stack.pop()
 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
 
        additional_stack.push(temp)
 
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop()) 
