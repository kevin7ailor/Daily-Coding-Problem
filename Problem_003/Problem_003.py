class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Codec:

  def serialize(self, root):
    serial = []
    
    def dfs(node):
      if not node:
        serial.append("None")
        return

      serial.append(str(node.val))
      dfs(node.left)
      dfs(node.right)
    dfs(root)
    return ",".join(serial)

  def deserialize(self, serialString):
    values = serialString.split(",")
    self.i = 0

    def dfs():
      if values[self.i] == "None":
        self.i += 1
        return None
      node = Node(values[self.i])
      self.i += 1
      node.left = dfs()
      node.right = dfs()
      return node
    return dfs()

if __name__ == '__main__':
  node = Node('root', Node('left', Node('left.left')), Node('right'))
  ser = Codec()
  des = Codec()
  
  assert des.deserialize(ser.serialize(node)).left.left.val == 'left.left'