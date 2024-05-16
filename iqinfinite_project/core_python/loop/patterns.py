# Patterns related programs here 
'''
All the pattern related programs are here
'''
# Patterns related programs here : Solution
'''
method : left_right_angle_triangle
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

method : right_right_angle_triangle
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

method : full_pyramid
    *
   ***
  *****
 *******
*********

method : inverted_full_pyramid
*********
 *******
  *****
   ***
    *
'''
class Pattern:
    def __init__(self,no_of_rows):
        self.__no_of_rows = no_of_rows
    def get_rows(self):
        return self.__no_of_rows
    def left_right_angle_triangle(self):
        var_row = self.__no_of_rows
        for i in range(0,var_row):
            for j in range(1,i+1):
                print(j, end=' ')
            print("\n")
    def right_right_angle_triangle(self):
        n = self.__no_of_rows
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print("\n")
    def full_pyramid(self):
        n = self.__no_of_rows
        for i in range(1, n + 1):
            # Print leading spaces
            for j in range(n - i):
                print(" ", end="")
             
            # Print asterisks for the current row
            for k in range(1, 2*i):
                print("*", end="")
            print("\n")
    def inverted_full_pyramid(self):
        n = self.__no_of_rows
        # Outer loop for the number of rows
        for i in range(n, 0, -1):
            # Inner loop for leading spaces in each row
            for j in range(n - i):
                print(" ", end="")
            # Inner loop for printing asterisks in each row
            for k in range(2*i - 1):
                print("*", end="")
            # Move to the next line after each row
            print("\n")
    