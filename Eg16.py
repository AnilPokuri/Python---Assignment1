"""
16. Write a program find all even numbers from the given list.
Input_List = [18.8, “Hyd”, 18, 26.9, 19, “BANG”, 26, 33.7, 25, “CHEN”]
Output = [18, 26]
"""

Input_List = [18.8, "HYD", 18, 26.9, 19, "BANG", 26, 33.7, 25, "CHEN"]
Output_List = []
for ele in Input_List:
    if ele!= str(ele) and ele%2 == 0:
        Output_List.append(ele)
        
print Input_List
print Output_List


        
        
     
