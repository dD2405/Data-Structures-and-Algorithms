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

    def remove_element(self):
        temp  = self.head
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new 
            else: 
                temp = temp.next
        return self.head 
        
    def NodeLength(self):
        n = self.head
        i = 0

        while(n != None):
            n = n.next
            i += 1
        print(i)

    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next


obj= LinkedList()
obj.append(1)
obj.append(1)
obj.append(2)
obj.append(3)
'''obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)
obj.append(3)'''
obj.NodeLength()
obj.remove_element()
obj.printList()
    
