# Display numbers from -10 to -1 using for loop
'''
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
'''
# Display numbers from -10 to -1 using for loop : solution
class DisplayNegativeTenToNegativeOne:
    def display_negative_ten_to_negative_one(self):
        start = -10
        end = -1
        for i in range(start,end+1):
            print(f"\033[92m{i}\033[97m")