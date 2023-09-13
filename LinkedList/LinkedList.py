class Node: # Класс-Узел. Внутри лежит дата и переменная-адрес следующего узла
    def __init__(self,data,next = None) -> None: 
        self.data = data # Дата - число, строка, тдтп
        self.next = next # Next - "ссылка" на следующий

class LinkedList:
    def __init__(self) -> None:
        self.head = None # Голова листа (смотри ниже, как работает)
        #self.size = 0

    def appendToStart(self,data) -> None:
        newNode = Node(data,self.head) # Создаем новую ноду с переданной data
        self.head = newNode # Голова двигается вправо

    def appendToEnd(self,data) -> None:
        currNode = self.head
        while(currNode.next):
            currNode = currNode.next
        newNode = Node(data,None)
        currNode.next = newNode

    def removeFromEnd(self) -> None:
        currNode = self.head
        while(currNode.next.next):
            currNode = currNode.next
        currNode.next = None

    def removeFromValue(self,data) -> None:
        currNode = self.head
        if currNode.data == data:
            currNode.next = currNode.next.next
            self.head = currNode.next
            return
        while(currNode.next.data != data):
            currNode = currNode.next
        print(f'currNode: {currNode.data}')
        currNode.next = currNode.next.next

    def printLList(self) -> None:
        currNode = self.head
        outputArr = []
        while(currNode):
            outputArr.append(currNode.data)
            currNode = currNode.next
        print(outputArr)

newLList = LinkedList()
newLList.appendToStart(2)
newLList.appendToEnd(1)
newLList.appendToStart(5)
newLList.appendToEnd(3)
newLList.appendToStart(7)
# newLList.removeFromEnd()
newLList.removeFromValue(7)


newLList.printLList()

'''
Данный лист работает по такой схеме:
-
0
0-
-0
-0-
--0
--0-
---0
Где 0: self.head, -:Node
'''