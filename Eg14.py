""" 14. WAP replace each string from the given list with the same string which is repeated with length of the string. 
Example: 
Input = [“A”, “AB”, “ABC”, “ABCD”]
Output = [“A”, “ABAB”,          “ABCABCABC”,“ABCDABCDABCDABCD”]
"""


Input = ["A", "AB", "ABC", "ABCD"]
val  = 0
Output = []
for ele in Input:
    I = ""
    num = len(ele)
    for x in range(num):
        I = I + ele
    Output.append(I)

    val = val + 1

print Input
print Output 
