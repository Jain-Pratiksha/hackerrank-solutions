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
    
    def getHeight(self,root):
        #Write your code here
        if root is not None:
            depth = max(self.getHeight(root.left),self.getHeight(root.right))+1
            #+1 is added because the level starts from 0 but we count it from one
            #eg: level 0, 1, 2 so we count it as 1,2,3 
            return depth
        else: return -1 #because the BST is empty with no root
        #if a root was there then it would return 0 i.e. level 0 and not -1
    
T=int(input())
myTree=Solution()
root=None #root is empty
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
