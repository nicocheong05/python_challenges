# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialise next as null
    def __repr__(self):
        return self.data

# Linked list class contains a Node object
class linked_list:
    # Function to initialise head
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,key):
        # store head node
        temp = self.head
        # if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if key was not present in linked list
        if temp == None:
            return
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
    
# start with an empty list
this_list = linked_list()
# creating a node and assigning it to this variable
first_node = Node("a")
# adding this node to the list via the variable
this_list.head = first_node
# creating a second and third node
second_node = Node("b")
third_node = Node("c")
# assigning the second node as the one after the first. Similar process for third node.
first_node.next = second_node
second_node.next = third_node
print(this_list)
