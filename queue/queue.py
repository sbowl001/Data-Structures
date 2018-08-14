import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    #add one to size
    pass
  
  def dequeue(self):
    self.storage.remove_head()
    #remove one from size
    pass

  def len(self):
    pass
