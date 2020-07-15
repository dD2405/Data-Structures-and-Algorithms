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

    # p jumps once and q twice
    def check_loop(self):
        p = q = self.head

        while(p and q and q.next):
            
            p = p.next
            q = q.next.next

            if(p==q):
                return p

        return None

    def start_loop(self):
        p = q = self.head
        p = self.check_loop()

        while(p != q):
            p = p.next
            q = q.next
        return p.data
        
# Utility function to print the linked list 
    def printList(self):
        temp = self.head 
        while (temp): 
            print(temp.data)
            temp = temp.next

obj = LinkedList()

obj.append(11)
obj.append(8)
obj.append(3)
obj.append(4)

obj.head.next.next.next.next = obj.head.next
print(obj.check_loop())
print(obj.start_loop())
  
  
