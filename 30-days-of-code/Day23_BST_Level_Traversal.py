import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        #Way 1
##        queue = [root]
##        while len(queue) is not 0:
##            current_val = queue[0] #reading first level i.e. level 0
##            queue = queue[1:]
##            print(str(current_val.data)+ " ",end="")
##            
##            if current_val.left is not None:
##                queue.append(current_val.left)
##            if current_val.right is not None:
##                queue.append(current_val.right)

        #Way 2
        node_val = list()
        node_val.append(root)
        nodes_traversed = []

        while len(node_val)>0:
            node = node_val.pop(0)
            if node.left is not None:
                node_val.append(node.left)
            if node.right is not None:
                node_val.append(node.right)
            nodes_traversed.append(node.data)
        print(*nodes_traversed)
                
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
