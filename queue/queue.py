import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    #add item to end of queue
    self.storage.add_to_tail(item)
    self.size += 1
    pass
  
  def dequeue(self):
    #removing from front of queue
    if self.size == 0:
      return None
    removed = self.storage.remove_head()
    self.size -= 1
    return removed

  def len(self):
    return self.size
