from collections import deque

my_stack =deque()

my_stack.append("item1")
my_stack.append("item2")
my_stack.append("item3")

item = my_stack.pop()
print("deque : ",item)

