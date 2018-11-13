"""
10. Write a program join each and every character from the given string with hyphen(-)
Example: 
Input_str = “PYTHON”
Output = P-Y-T-H-O-N
Note: Please Don’t use join () function.
"""
Input_str = "PYTHON"
Output_str = " "
length = len(Input_str)
num = 0
for ele in Input_str:
    if (length-1)!= num:
        Output_str = Output_str + ele + "-"

    else:
        Output_str = Output_str + ele 
    num = num + 1
    
print Output_str 
