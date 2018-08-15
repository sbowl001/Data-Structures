class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self == None: 
      self = BinarySearchTree( value )
    else: 
      cur_node = self
      done = False
      while not done:
        #Left child
        if cur_node.value >= value: 
          if not cur_node.left == None:
            cur_node = cur_node.left
          else:
            cur_node.left = BinarySearchTree( value )
            done = True
        #Right Child
        elif cur_node.value < value:
          if not cur_node.right == None:
            cur_node = cur_node.right
          else: 
            cur_node.right = BinarySearchTree(value)
            done = True
 

  def contains(self, target):
    cur_node = self
    while cur_node: 
      if target == cur_node.value:
        return True
      elif target < cur_node.value:
        cur_node = cur_node.left
      else: 
        cur_node = cur_node.right
    return False

  

  def get_max(self):
    cur_node = self
    while cur_node.right:
      cur_node = cur_node.right
    return cur_node.value
