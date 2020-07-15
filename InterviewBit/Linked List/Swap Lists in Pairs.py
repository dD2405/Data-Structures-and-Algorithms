# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def append(self, new_data): 
  
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
  
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node

    def swap(self):

        p = self.head
        new_start = p.next

        while(True):

            q = p.next
            temp = q.next
            q.next = p

            if(temp == None or temp.next == None):
                p.next == None
                break

            p.next = temp.next
            p = temp

        return new_start
        

    # Utility function to print the linked list 
    def printList(self):
        temp = self.head 
        while (temp): 
            print(temp.data)
            temp = temp.next

obj = LinkedList()

obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.printList()
print(obj.swap())

