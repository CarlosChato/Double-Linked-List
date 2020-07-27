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

        #the size of the list increases 

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
        #We use this method to add an element at last of the list
        #for that we will use the tail reference
        newNode = SNode(elem)

        #List empty, head and tail is the same element

        if self.isEmpty():
            self.head = newNode

        #List not empty, tail.next will be the new node and the new node will be the tail

        else:
            self.tail.next = newNode
        
        self.tail = newNode
        #Size increases  
        self.size += 1

    def removeFirst(self):
        #Method to remove the first element of the list and return
        #the first element of the list

        if self.isEmpty():
            #if the list is empty we cant remove nothing
            print('ERROR: the list is empty')
            return None

        #heal will be head.next and if the new head is None, the list is empty
        #and tail will be None
        
        result = self.head.elem
        self.head =self.head.next

        if self.head == None:
            self.tail = None
        
        self.size-=1

        return result

    def removeLast(self):

        #Method to remove the last element of the list, and return it

        #if the list is empty we cant remove any element
        if self.isEmpty():
            print('ERROR: the list is empty')
            return None

        result = self.tail.elem
        aux = self.head
        #Case we have only one element
        if self.size == 1:
            #Head and tail will be None and the list will be empty
            self.head = None
            self.tail = None
        else:

            #in other case, when the size (len) is different at 1 we search the node
            #which the next will be the tail.

            while aux.next != self.tail:
                aux=aux.next

            #now tail will be the aux node

            aux.next = self.tail.next
            self.tail = aux
        
        self.size -= 1   
        return result     
        

    def insertAt(self,index:int,elem):

        #method to insert an element in an index

        if index < 0 or index > self.size:
            #the index is incorrect
            print('ERROR: index out of range')
            return None
        
        if index == 0:
            #if the index is 0, is the same that add an element at the first position
            self.addFirst(elem)
        
        elif index == self.size:
            #if the index is the same that the size, we add an element at the last position
            
            self.addLast(elem)

        else:
            aux = self.head
            #we start the count at 1, because we need a aux node previous at the site
            #where we will create the new Node
            count = 1
            while count != index:
                aux = aux.next
                count += 1
            #First of all we link the newNode at the list
            newNode = SNode(elem)
            newNode.next = aux.next
            aux.next = newNode
            self.size+=1
    
    def getAt(self,index:int):

        #method to return the element at the index position

        if index <0 or index>=self.size:
            #Incorrects values to the size
            print('ERROR: index out of range')
            return None
        #we use a count to go to the correct index
        count = 0
        aux = self.head

        while count != index:
            count += 1
            aux = aux.next
        #we return the element of aux
        result = aux.elem
        return result

    def index(self,elem):

        #return the first position of the element, if doesnt exist, return -1

        #first of all we set a count as 0, it will be the index count 
        #index, is the value that we will return, the start value is -1
        #because if we dont found the element at the list, we will return -1
        count = 0 
        index = -1
        aux = self.head
        #we need go for all the list, to test all the nodes
        while aux != None:
            #if the element of the node is equal as elem, we change the value of
            #index by count, and we return it
            if aux.elem == elem:
                index=count
                return index
            
            aux = aux.next
            count+=1
        
        #the elements is not at the list, so we return index without changes (-1)
        return index

    def removeAt(self,index):

        #remove and return the element at the index position

        #first of all,we check the index, remember that the index is correct, if 
        #it is between 0 and size-1

        if index < 0 or index >= self.size:
            print('ERROR, index out of range')
            return None
        
        if index==0:
            #if index is 0, is equal at removeFirst
            return self.removeFirst()
        
        elif index==self.size-1:
            #if index is size-1 is equal at removeLast
            return self.removeLast()

        else:
            #we start with count = 1 because, we need the previous node to remove it
            count = 1
            current = self.head
            while count != index:
                current = current.next
                count += 1
            
            #we use a aux node to have the reference of the node that we will remove

            aux = current.next
            #we save the element of the node that we will remove
            result = aux.elem
            #Remove the node changing the references of the nodes
            current.next = aux.next
            self.size -= 1

            return result

    def clear(self):
        
        #we set the list without elem,for that head and tail will be None

        self.head = None
        self.tail = None

    def count(self,elem):

        #return how many elements have the list

        count = 0
        current = self.head

        #current have to go for all the list
        while current != None:
            if current.elem == elem:
                count += 1
            
            current = current.next

        return count

    def getAtNode(self,index):

        #same method that get at, but this return the node and not the element

        if index <0 or index>=self.size:
            #Incorrects values to the size
            print('ERROR: index out of range')
            return None
        #we use a count to go to the correct index
        count = 0
        aux = self.head

        while count != index:
            count += 1
            aux = aux.next
        #we return the element of aux
        
        return aux

    def reverse(self):
        
        #to reverse the order of the list

        start = 0
        last = self.size-1

        while start < last:
            start_node = self.getAtNode(start)
            final_node = self.getAtNode(last)
            aux_elem = start_node.elem
            
            start_node.elem = final_node.elem
            final_node.elem = aux_elem

            start+=1
            last-=1




