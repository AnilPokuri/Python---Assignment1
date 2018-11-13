"""
6. WAP print all duplicated values in descending order from the given input list. 
Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
"""


Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
length = len(Input_list)
Duplicate_elements = []
num = 0
for i in Input_list:
    num = num + 1
    for j in Input_list[num:-1]:
        if i == j:
            Duplicate_elements.append(i)
Duplicate_elements.reverse()

print Input_list
print Duplicate_elements 
        
