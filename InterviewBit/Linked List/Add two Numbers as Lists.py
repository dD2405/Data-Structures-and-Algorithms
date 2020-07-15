# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.val = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data) 
 
        if self.head is None:
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node

    def reverse(self):
        current = self.head
        prev = None

        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

        return self.head

    def add_numbers(self,A,B):

        C = Node(0)
        temp = C
        carry ,rem ,div ,add = 0,0,0,0
        
        while(A != None and B != None):

            if carry != 0:
                add = A.val + B.val + carry
                div = add//10
            else:
                add = A.val + B.val 
                div = add//10 

            if div != 0:
                remainder = add%10
                carry = div
                C.val = remainder

            else:
                C.val = add 
                C = C.next

            if A is not None:
                A = A.next
            if B is not None: 
                B = B.next

        return C.next

    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next

            
A = LinkedList()

A.append(2)
A.append(4)
A.append(3)

B = LinkedList()

B.append(5)
B.append(6)
B.append(4)

obj = LinkedList()

obj.add_numbers(A.head,B.head)

obj.printList()

            
            
