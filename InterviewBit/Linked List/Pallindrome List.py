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
  

    def printList(self):

        temp = self.head 

        while (temp): 
            print(temp.data)
            temp = temp.next    

    def reverse(self):

        current = self.head
        prev = None

        while(current != None):

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

        return self.head


    def check_pallindrome(self):

        while(True):
            p = p.next.next

            if(p.next == None):
                start_second = q.next.next
                break
            if(p == None):
                start_second = q.next
                break

            q = q.next

        q.next = None
        
            
            
        

obj= LinkedList()
obj.append(1)
obj.append(2)
obj.append(3)
print(obj.reverse())
obj.printList()

            
