
#A double linked node, have three parameters, one is the element that
#is saved at memory, and the others two are the references to the other nodes
#one is the reference to the next node and the other is the reference to the previous
#node 

#we create the class of the double node
class DNode():
    #the external parameter to introduce at the init method is the element to save
    def __init__(self,elem):
        #set the previous reference and the next reference as None, beacause they
        #are not enlaced to other nodes
        self.elem = elem
        self.next = None
        self.prev = None
