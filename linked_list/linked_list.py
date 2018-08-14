"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

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
    if self.head == None:
      self.head = self.tail = Node(value)
    else:
      new_node = Node(value)
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head == self.tail and self.head is not None:
      value = self.head.value
      self.head = self.tail = None
      return value
    else:
      current_head = self.head
      self.head = self.head.get_next()
      value = current_head.get_value()
      current_head = None
      return value

  def contains(self, value):
    if self.head is None:
      return False

    current_node = self.head

    while current_node is not None:
      if current_node.get_value() == value:
        return True
      current_node = current_node.get_next()

    return False

  def get_max(self):
    if self.head is None:
      return None

    current_node = self.head
    max_value = current_node.get_value()

    while current_node is not None:
      if current_node.get_value() > max_value:
        max_value = current_node.get_value()
      current_node = current_node.get_next()

    return max_value
