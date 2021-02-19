
############################# Question ###########################

# https://www.hackerrank.com/challenges/30-linked-list/problem

##################################################################


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        # Creates a temporary node to be inserted
        temp_node = Node(data)
        if head is None:
            return temp_node
        curr = head
        # makes the last inserted node as the current node
        while curr.next is not None:
            curr = curr.next
        # link the pointer of the current node to the next node
        curr.next = temp_node
        return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  