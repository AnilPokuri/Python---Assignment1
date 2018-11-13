"""
20. Write a program reverse each string from the given list and finally reverse a list.
"""



Input_List = [raw_input("Enter a List: ")]
Output_List = [] 


for ele in Input_List:
    string = " "
    len = len(ele)

    for ch in range(len):
      string = string + ele[len-1]
      len = len - 1

    print string

    Output_List.append(string)

print Input_List
print Output_List 
  
      
    
