#A double linked list is a list with nodes that it has double reference,
#one of them to the previous node and the other to the next node
#finally the list will be like this:
#<-Node-><-Node-><-Node-><-Node->...

#First of all we have to import the Double Node

from DNode import DNode

#create the class of the Double Linked List

class DList():

    def __init__(self):
        
        #At the init method we set the head reference, and the tail reference as None
        #and the size = 0 because the list is empty

        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):

        #overwrite the special method (len) to return the size of the list

        return self.size

    def isEmpty(self):

        #it return a bool, if the list is empty, it will return true, in other case
        #it will return false

        return self.size==0

    def addFirst(self,elem):

        #add a new element at the first of the list (add the element elem if the parameter)

        newNode = DNode(elem)

        #first of all is the list is empty, tail will be the new node like the head
        if self.isEmpty():

            self.tail = newNode
        
        #we link the newnode to the head node, and we link the head node to the 
        #new node too

        else:

            self.head.prev = newNode
            newNode.next = self.head

        #update the reference of the head node
        self.head = newNode

        #increase the size of the list in one
        self.size += 1

    def __str__(self):

        #we made a method to print the Single List like a normal list

        result = ''

        temp = self.head
        if temp == None:
            return result

        while temp is not None:
            result = result + str(temp.elem) +','
            temp = temp.next
        if len(result)>0:
            result=result[:-1]
        return result

    def addLast(self,elem):

        #add an element (elem parameter), at the last position

        newNode = DNode(elem)

        #if the list is empty, the head will be the newNode too

        if self.isEmpty():
            self.head = newNode

        #if the list is not empty, we link the newNode with the tail

        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        #Change tail's reference to newNode
        self.tail = newNode

        self.size += 1

    def removeFirst(self):

        #method to remove the first element of the list

        if self.isEmpty():
            print('ERROR: the list is empty')
            return None
        
        
'it will be continued, i hope tomorrow will be completed'
