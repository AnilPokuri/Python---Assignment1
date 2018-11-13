"""
18. Write a program create a random list of length 10 and print all the elements except the elements which are divisible by 4.
"""
Input_List = []

for ele in range(10):
    ele = raw_input("Enter Random List:")
    print ele

    Input_List.append(ele)

    num = int(ele)
    
    if num%4 == 0:
        
        Input_List.pop()
        
print Input_List
        
