"""
12. Write a program find all even number from the given input list and display output as a list format.
"""

Input_List =  []
Output_List = []
for val in range(10):
    val = int(raw_input("Enter an Integer: "))
    Input_List.append(val)
print Input_List
for num in Input_List:
    if num%2 == 0:
        Output_List.append(num)

print Output_List
