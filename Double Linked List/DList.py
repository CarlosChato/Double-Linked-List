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

        #method to remove the first element of the list, and return the first element
        #of the list

        if self.isEmpty():
            print('ERROR: the list is empty')
            return None
        
        #if head and tail is equal, tail have to be None

        if self.head == self.tail:
            self.tail = None
        
        #we save the element of head to return it later
        result = self.head.elem

        #change the reference the head for the next node
        self.head = self.head.next

        #if head is different of None, we change the previous reference
        if self.head != None:
            self.head.prev = None
        
        #finally, change the size of the list
        self.size -= 1
        return result

    def removeLast(self):

        #it remove the last element of the list and return it

        #if the list is empty we cant remove an element
        if self.isEmpty():
            print('ERROR: The list is empty')
            return None

        #if head and tail are same, we set  head as None
        if self.head == self.tail:
            self.head = None

        #save the element to return it 
        result = self.tail.elem

        #change the reference of tail
        self.tail = self.tail.prev
        
        #if tail is not None, we have to change the next reference to None
        if self.tail != None:
            self.tail.next = None
        
        self.size -= 1
        
        return result

    def insertAt(self,index:int,elem):

        #insert an element(elem) in the index position

        if index < 0 or index > self.size:
            print('ERROR: index out of range')
            return None

        #index = 0, is the same that addfirst
        if index == 0:
            self.addFirst(elem)

        #index = size, is the same that addLast
        elif index == self.size:
            self.addLast(elem)

        else:
            newNode = DNode(elem)

            aux = self.head
            count = 0

            while count != index:

                aux = aux.next
                count += 1

            #now we are in the position of the newNode

            previous = aux.prev

            #NewNode conected with the previous node
            previous.next = newNode
            newNode.prev = previous

            #NewNode conected with the next node
            newNode.next = aux 
            aux.prev = newNode

            #Increase the size
            self.size+=1

    def getAt(self,index:int):

        #method to return the element at the index position

        if index < 0 or index >= self.size:

            print('ERROR, index out of range')
            return None
        
        count = 0
        #we use an auxiliar node to go to the index position
        aux = self.head
        #loop to go to the index position
        while count != index:
            count += 1
            aux = aux.next

        #return the element of aux
        result = aux.elem

        return result

    def index(self,elem):

        #return the first position if the element, if it does not exit return -1

        #first of all index is the first index position if the element exits, for 
        #this reason, it start as -1. count is the counter of the positions in the
        #list
        index = -1
        count = 0
        aux = self.head

        #we hve to go for all the list
        while aux != None:

            if aux.elem == elem:
                #if the element exists, index has the count value, because
                #is the list position of the element
                index = count
                return index
            
            aux = aux.next
            count += 1
        #the element is not in the list, so it will return index (-1)
        return index


    def removeAt(self,index:int):

        #remove and return the element at the index position
        # 
        #we check if the index is correct 
        if index < 0 or index >= self.size:
            print('ERROR, index out of range')
            return None

        #if the list is empty we cant remove an element
        if self.isEmpty():
            print('ERROR, the list is empty')
            return None

        #if index = 0, is the same that removeFirst
        if index == 0:
            return self.removeFirst()
        
        #if index = size-1 is the same that removeLast
        elif index == self.size-1:
            return self.removeLast()

        else:
            
            #we use a counter to go to the index position
            #aux will be the node of the index position
            count = 0
            aux = self.head

            while count != index:
                count += 1
                aux = aux.next
            
            #we have to use a previous node and the next node of aux
            #to link them and remove aux
            previous = aux.prev
            nextNode = aux.next

            previous.next = nextNode
            nextNode.prev=previous

            self.size -= 1

            return aux.elem


    def clear(self):

        #We set the list without elements, it will be empty
        self.head = None
        self.tail = None
        self.size = 0

    def count(self,elem):

        #it return how many times the list has element

        count = 0
        aux = self.head

        #we have to go for all the list
        while aux != None:
            
            #if aux == elem, count increase in 1
            if aux.elem == elem:
                count += 1

            aux = aux.next
        
        #finally we return count
        return count

    
    def reverse(self):

        #to reverse the list

        aux = self.size//2
        start = self.head
        end = self.tail
        count = 0

        while  count != aux:

            aux_elem = start.elem
            start.elem = end.elem
            end.elem = aux_elem

            end = end.prev
            start = start.next
            count += 1

        

