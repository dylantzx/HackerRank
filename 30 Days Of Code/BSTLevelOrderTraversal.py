############################# Question ###########################

# https://www.hackerrank.com/challenges/30-binary-trees/problem

##################################################################

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
        # Create a queue using a list
        queue = [root]
        queueData = []
        
        while queue:
            toVisit = queue.pop(0)
            queueData.append(toVisit.data)
            if toVisit.left != None:
                queue.append(toVisit.left) 
            if toVisit.right != None:
                queue.append(toVisit.right)
        print(*queueData)        
        
        
            
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
