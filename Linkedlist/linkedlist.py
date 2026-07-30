print("Hello world")

#Doubly linked list
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next =None 
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    #Insert at the head
    def insert_head(self,val):
        new_node =Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 

    #Append at the end        
    def append_node(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current =current.next 
            current.next = new_node
            new_node.prev = current 

    #Insert at the position         
    def insert_at_pos(self,val,position):
        new_node = Node(val)
        if position == 0:
            if self.head :
                new_node.next = self.head
                self.head.prev = new_node 
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                return 
            temp=temp.next
        if temp is None:
            return 
        new_node.next = temp.next 
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node





def insert_at_head(self,head,val):
    node_1 = Node(val)
    if head:
        if head.prev is None:
            node_1.next = head
            head.prev = node_1

    return node_1

def insert_at_singlyy_head(self,val,head):
    new_node=Node(val)
    if head is None:
        return new_node
    new_node.next = head 
    return new_node
def delete_head_of_ll(self,val,head):
    if head is None:
        return None
    head = head.next
    if head is not None:
        head.prev = None
    return head


def reverse_a_doubly_linked_list(self,head):
    if head is None:
        return None
    temp = head
    prev = None
    while temp:
        temp.next ,temp.prev = temp.prev , temp.next
        prev = temp
        temp = temp.prev
    return prev