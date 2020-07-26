#We  have to create a node, it will be like a part of a list

class SNode():

#the node only have a external parameter that is the element that it will have
#Only have a memory reference that is the next node
    def __init__(self,e):
        self.elem = e
        self.next = None
        
