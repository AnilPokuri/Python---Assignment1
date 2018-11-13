"""
7. Write a program find the maximum number from the given input list
Input_list = [82, 62, 61, 54, 71, 89, 75, 73]
"""

Input_list = [82, 62, 61, 54, 71, 89, 75, 73]
i = 0
for j in Input_list:
    if i >= j:
        print i
    else:
        i = j
        print j
    
    
