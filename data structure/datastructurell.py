# intialise a node with data and nextnode
class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

# create a class for linked list
class Linkedlist:
    def __init__(self): 
        self.head=None
    def is_empty(self):   # check the linkedlist is empty
        return self.head is None
    def append(self,data): # add element at the end of the linked list
        new_node = Node(data)
        if self.is_empty(): #if it's an empty linked list set head to the new node
            self.head =new_node
        else:
            current_node = self.head #point to the head node
            while current_node.next_node:
                current_node = current_node.next_node #add elements if the  link is not empty
            current_node.next_node=new_node
    def display(self):
        elements =[]
        current_node = self.head
        while current_node:
            elements.append(current_node.data) #store all the nodes in a list
            current_node = current_node.next_node 
        print(" ->".join(map(str,elements)))


my_linkedlist= Linkedlist()

n = int(input("enter a range of number:"))
for i in range(1,n+1):
    x = int(input("enter a number:"))
    my_linkedlist.append(x)


print("linked list:")
my_linkedlist.display()