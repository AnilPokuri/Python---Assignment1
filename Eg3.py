"""
3.Write a program create 3x3 matrix using python. Take all the elements from the user. And also
print the sum of diagonal elements from created matrix.
"""

X = int(raw_input("Enter number of rows in a matrix:"))
Y = int(raw_input("Enter number of columns in a matrix:"))
dia = 0
Input_List = []
for i in range(X):
    Ind_mat = []
    for j in range(Y):
        Ind_mat.append(int(raw_input("Enter the elements for matrix:")))
    print Ind_mat
    Input_List.append(Ind_mat)
print Input_List

for val in range(X):

    for num in range(X):
        if val == num:
            dia = dia + Input_List[val][num]

print dia

        
    
                  
