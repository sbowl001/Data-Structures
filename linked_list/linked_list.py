"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value #header
    self.next_node = next_node #pointer

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      tail = new_node
    pass

  def remove_head(self):
    #if head == None, return None

    pass

  def contains(self, value):
    cur_node = self.head
    while not cur_node == None:
      # if value == value, return true
        #update cur_node.next
    
    #else return false
      pass

  def get_max(self):
    pass
