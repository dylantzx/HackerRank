############################# Question ###########################

# https://www.hackerrank.com/challenges/30-sorting/problem

##################################################################

#!/bin/python3

import sys

class bubblesort():
    def __init__(self):
        self.totalSwaps=0
        self.sortedlist = []
        
    def sort(self,a):
        sizeOfArray = len(a)
        for i in range(0,sizeOfArray):
            numOfSwaps = 0
            for j in range(0,sizeOfArray-1):
                if a[j] > a[j+1]:
                    # Swapping takes 3 steps            
                    temp = a[j]
                    a[j] = a[j+1]
                    a[j+1] = temp
                    numOfSwaps +=1
            self.totalSwaps+=numOfSwaps
            
            if numOfSwaps == 0:
                break
        self.sortedlist = a
                
    def display(self):
        print(f"Array is sorted in {self.totalSwaps} swaps.")
        print(f"First Element: {self.sortedlist[0]}")
        print(f"Last Element: {self.sortedlist[-1]}")    

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
bs = bubblesort()
bs.sort(a)
bs.display()
