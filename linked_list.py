

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_new_value(self,data):
        if self.head is None:
            

        

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ','
            itr = itr.next
        print(llstr)


ll = LinkedList()
ll.insert_at_begining(12)
ll.insert_at_begining(13)
ll.print()
ll.insert_at_end(14)
ll.print()
