def return_int(list):
    "Function adds the list given as a parameter of common ages in college for four years together and returns the sum"
    total_sum = 0
    for i in list:
        total_sum += i
    return total_sum

def return_anything(param_one, param_two):
    "Function takes two parameter and returns the substring from the second parameter to the end of the string given in the first parameter"
    return param_one[param_two:len(param_one)]




# 3 calls for first function
print(return_int([19, 20, 21]))
print(return_int([17, 18, 19]))
print(return_int([20, 21, 22]))
# 3 calls for second function
print(return_anything("Cookie Monster", 7))
print(return_anything("Villanova", 5))
print(return_anything("New Home", 4))