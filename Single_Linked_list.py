#Import the Node to work with it in the list
#The list will be more o less like this:
#   Node->Node->Node->Node->Node
from Single_Node import SNode

class SList():
#Our SList has a head element and tail element, both are references points of the list
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def  __len__(self):
        return self.size
    
    def isEmpty(self):
        #if is empty, size == 0 and it return true, in other case, return False
        return self.size == 0

    def  addFirst(self,elem):
        #we use this method to add an element at the first position of the list
        #NewNode created by SNode class (is a Single Node)
        newNode = SNode(elem)
        #if the list is empty, the head will be the tail too
        if self.isEmpty():
            self.tail = newNode
        
        newNode.next = self.head
        self.head = newNode
        #the size of the list icreases 
        self.size += 1

    def __str__(self):

        #we made a method to print the Single List like a normal list

        result = ''

        temp = self.head
        result =result + str(temp.elem) +','
        
        while temp != self.tail:
            temp = temp.next
            result = result + str(temp.elem) +','
        
        result=result[:-1]
        return result

    def addLast(self,elem):
        #We use this method to add an element at last of the list
        #for that we will use the tail reference

        



test = SList()

test.addFirst(1)

print(test)
print(test.head.elem)
print(test.tail.elem)
print(test.size)