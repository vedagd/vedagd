class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextvnextal = None
 
class LinkedList:
    def __init__(self):
        self.headval = None
 
example = LinkedList()
example.headval = Node(23)
e2 = Node(90)
e3 = Node(90)
example.headval.nextval
e2.nextval = e3