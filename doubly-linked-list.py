class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.length = 0

    def get(self, index: int) -> int:
        curr = self.__head
        count = 0 
        diff = self.length - 1
      
        if index > diff:
            return -1
        
        while curr:
            print(curr.val)
            if count == index:
                break
            
            count += 1
        
            curr = curr.next
            
        return curr.val
    
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        self.length += 1
        
        if self.__head is None:
            self.__head = node
            self.__tail = node
            return
        
        node.next =  self.__head
        self.__head.prev = node
        self.__head = node

    def addAtTail(self, val: int) -> None:
        self.length += 1
        node = Node(val)
        
        if self.__tail is None:
            self.__head = node
            self.__tail = node
            return
         
        node.prev = self.__tail
        self.__tail.next = node
        self.__tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        
        self.length += 1
        curr = self.__head
        count = 0 
        prev = curr
        
        while curr:
            if count == index:
                break
            count += 1
            prev = curr
            curr = curr.next
            
        node = Node(val)
        node.next = curr
        node.prev = curr.prev
        curr.prev = node
        prev.next = node
          
                  
    def deleteAtIndex(self, index: int) -> None:
        curr = self.__head
        prev = curr
        count = 0
        
        while curr:
            if count == index:
                break
            count += 1
            prev = curr
            curr = curr.next
        
        if curr is None:
            return
        
        self.length -= 1
        
        if self.length == 0:
            self.__head = None
            self.__tail = None
            return 
          
        if curr == self.__head:
            self.__head =  curr.next
        
        if curr == self.__tail:
            self.__tail = curr.prev
        
        prev.next = curr.next
        curr.prev = prev
   
