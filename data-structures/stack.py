# stack is first in last out
# Push and pop
# peek get access on top item
# clear to remove all stack ele
# undo pops last command
# comands are stored in stack when after executing

# define
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
print(my_stack)

my_stack.pop()
print(my_stack)

# WRAPPER CLASS


class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


# test code for wrapper function
test_stack = Stack()
test_stack.push(10)
test_stack.push(20)
print(test_stack)
print(test_stack.pop())
print(test_stack.peek())
print(test_stack)
