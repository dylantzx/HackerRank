############################# Question ###########################

# https://www.hackerrank.com/challenges/30-queues-stacks/problem

##################################################################

import sys
from collections import deque

class Solution:
    # Write your code here
    # deque provides an O(1) time complexity for append and pop operations
    def __init__(self):
        self.q = deque()
        self.s = deque()
    
    def pushCharacter(self,letter):
        self.s.append(letter)
    
    def enqueueCharacter(self,letter):
        self.q.append(letter)
    
    def popCharacter(self):
        return self.s.pop()
    
    def dequeueCharacter(self):
        return self.q.popleft()
    
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    