
############################# Question ###########################

# https://www.hackerrank.com/challenges/30-nested-logic/problem

##################################################################
# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = list(map(int,input().split()))
expected = list(map(int,input().split()))

if expected[2] == actual[2]:
    if actual[1] > expected[1]:
        fine = 500 * (actual[1] - expected[1])
    elif actual[1] < expected[1]:
        fine = 0
    else:
        if actual[0]>expected[0]:
            fine = 15 * (actual[0] - expected[0])
        else:
            fine = 0
elif expected[2] > actual[2]:
    fine = 0
else:
    fine = 10000
print(fine)
