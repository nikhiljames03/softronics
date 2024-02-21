class stack:
    def __init__(self):
        self.items =[]
    def is_empty(self):
        return len(self.items)== 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if  not self.is_empty():
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)
    
stack = stack()
stack.push(2)
stack.push(4)
stack.push(6)
print("size: ",stack.size())
print("peek: ",stack.peek())
print("pop :",stack.pop())
print( "size after pop: ",stack.size())
