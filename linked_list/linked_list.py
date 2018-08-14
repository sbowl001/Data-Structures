"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
    #pointer

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
      #set head and tail equal to same Node obj
      self.head = new_node
      self.tail = new_node
    else:
      #set old tails next to new node
      self.tail.set_next = new_node
      tail = new_node

  def remove_head(self):
    #if head doesn't exist
    if self.head == None:
      return None
    else:
    #set head.next = head return head.value
    #if head and tail are same, do something...

  def contains(self, value):
    cur_node = self.head
    while not cur_node == None:
      #if found value, return True
      #update cur_node
      
    #else return False  
    pass

  def get_max(self):
    pass
