import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
    #update size  
  def dequeue(self):
    item = self.storage.remove_head()
    if item is not None:
      self.size -= 1
    return item
    # update size
  def len(self):
    return self.size
