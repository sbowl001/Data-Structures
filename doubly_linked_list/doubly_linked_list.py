class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    pass

  def insert_before(self, value):
    pass

  def delete(self):
    pass

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    #create new_node, ListNode
    #if head does not exits
    #head and tail = new_node

    #else 
      #head.prev = new_node
      #new_node.next = head
      #update head head = new_node
    pass

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
