############################# Question ###########################

# https://www.hackerrank.com/challenges/30-review-loop/problem

##################################################################

# Enter your code here. Read input from STDIN. Print output to STDOUT

count = int(input().strip())
for i in range(count):
    inp = input()
    print(f"{inp[::2]} {inp[1::2]}")
