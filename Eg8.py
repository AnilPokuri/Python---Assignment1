"""
8.Write a program change the given input list by  doing rotate left.
Ex: input [4, 5, 6, 7] output [5, 6, 7, 4]
"""
List = [4,5,6,7]
Z = len(List)
print Z
for num in range(Z):
    x = List[0]
    y = List[Z-1]
    List[0] = y
    List[Z-1] = x
    Z = Z - 1
print List 
    
