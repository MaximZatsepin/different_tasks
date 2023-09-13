class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def placeNext(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        currNode = self.head
        while(currNode.next != None):
            currNode = currNode.next
        currNode.next = new_node
    
    def printLList(self) -> None:
        currNode = self.head
        while currNode:
            print(currNode.data)
            currNode = currNode.next


myLlist = LinkedList()
myLlist.placeNext(2)
myLlist.placeNext(3)
myLlist.printLList()