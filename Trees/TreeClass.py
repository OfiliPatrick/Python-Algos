class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def func(root):
    output = []
    def traverse(root):
        if root == None:
            return None

        if root.left == None and root.right == None:
            output.append(root.val)
            return "Found some leaf nodes"
        
        left = traverse(root.left)
        right = traverse(root.right)

        return left or right

    traverse(root) 
    return output


#      8
#    /   \
#   3    10
#  / \     \
# 1   6    14

tree = Node(8)               
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)

print(func(tree ))


# tree = Node(4)                
# tree.left = Node(2)
# tree.right = Node(7)
# tree.left.left = Node(1)
# tree.left.right = Node(3)
# tree.right.left = Node(6)
# tree.right.right = Node(9)


def permute(s):
  res=[]
  seen={}
  def bt(s,temp):
    if len(temp)==len(s):
      res.append(temp)
    else:
      for i in range(len(s)):
        if not seen.get(i,False):
          temp+=s[i]
          seen[i]=True
          bt(s,temp)
          del seen[i]
          temp = temp[:len(temp)-1]
  bt(s,'')
  return res

             