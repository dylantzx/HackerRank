############################# Question ###########################

# https://www.hackerrank.com/challenges/30-scope/problem

##################################################################

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        self.minNum=100
        self.maxNum=1
        
    # O(n) time complexity
    def computeDifference(self):
        for element in range(len(a)):
            if a[element] > self.maxNum:
                self.maxNum=a[element]
            if a[element] < self.minNum:
                self.minNum=a[element]
        self.maximumDifference = self.maxNum-self.minNum

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)