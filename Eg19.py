"""
19. Write a program convert the following list to a dictionary. 
X = [(“A”, 65), (“B”, 66), (“C”: 67), (“D”, 68)]
"""

Input_List = [("A", 65), ("B", 66), ("C", 67), ("D", 68)]
dic = {}
Output_List = []
for ele in Input_List:
    Output_List = ele

    dic[Output_List[0]] = Output_List[1:]

print dic     

