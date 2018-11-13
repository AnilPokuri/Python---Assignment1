"""
13. Given a string of even length and print the output as string contains last half added with first half of the given string
"""

Input_str = raw_input("Enter a given length string: ")
length = len(Input_str)
print length
num = 0
first = ' '
last = ' '
for ch in Input_str:
    if ((length/2)-1) > num:
        first = first + ch
    else:
        last = last + ch
    num = num + 1

Output_str = last + first

print Input_str
print Output_str 
    
