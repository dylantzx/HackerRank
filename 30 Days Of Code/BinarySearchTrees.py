############################# Question ###########################

# https://www.hackerrank.com/challenges/30-binary-search-trees/problem

##################################################################

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
        if root == None:
            # print("No children")
            # return -1 because there there are numberOfEdges = numberOfNodes - 1
            return -1
        # print(">>",root.data)
        
        ### Compares left and right children recursively by backtracking ###
        # Eg. Given a Tree: 3 2 5 1 4 6 7
        # 3 -> 2 -> 1 -> 2 -> 3 
        # at 1, returns 1 + Max(-1,-1) = 0
        # at 2, returns 1 + Max(0,-1) = 1
        # at 3, returns 1 + Max(1, *recurse into right branch*)
        # 5 -> 4 -> 5
        # at 4, returns 1 + Max(-1,-1) = 0
        # at 5, returns 1 + Max(0, *recurse into right branch*)
        # 6
        # at 6, returns 1 + Max(-1, *recurse into right branch*)
        # 7
        # at 7, returns 1 + Max(-1, -1) = 0
        # Backtracks to 6
        # at 6, returns 1 + Max(-1, 0) = 1
        # Backtracks to 5
        # at 5, returns 1 + Max(0, 1) = 2
        # Backtracks to 3 (root)
        # at 5, returns 1 + Max(1, 2) = 3
    
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       