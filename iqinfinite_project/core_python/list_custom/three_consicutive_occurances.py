class ThreeConsecutiveOccurances:
    def __init__(self, var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def three_consicutive_occurances(self):
        var_list = self.__var_list
        arr = var_list
        size = len(var_list)
        r = []
        for i in range(size - 2):
 
            # checking the conditions
            if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
         
                # printing the element as the 
                # conditions are satisfied 
                r.append(arr[i])
        return r