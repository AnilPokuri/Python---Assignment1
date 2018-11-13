"""
11. Write a program take 10 input strings of different lengths from the user and store all the strings into a list and display only odd length strings are the output in a list format.
"""
List1 = []
num = 0
List2 = []

for str1 in range(10):
    str1 = raw_input("Enter a string: ")
    List1.append(str1)
    num = len(str1)
    if num%2 != 0:
        List2.append(str1)

print List1
print List2
