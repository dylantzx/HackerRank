############################# Question ###########################

# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

##################################################################

# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input())
list_of_queries = [input().split() for i in range(count)]
phonebook = {name:number for name,number in list_of_queries}
while True:
    try:
        check_name = input()
        if check_name in phonebook:
            print(f"{check_name}={phonebook[check_name]}")
        else:
            print("Not found")
    except:
        break