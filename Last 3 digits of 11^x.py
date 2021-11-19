# This is a simple program to find the last three digits of 11 raised to any given number.
# The main algorithm that does the work is on line 10

def trim_num(num):
    if len(str(num)) > 3: # no need to trim if the number is 3 or less digits long
        return str(num)[(len(str(num)) - 3):] # trims the number
    return num

def main(exp):
    init_val = str((((exp-1) * (exp))/2) % 10 + (exp % 100) / 10) + str(exp % 10) + "1" # The main algorithm which needs to be cleaned (only the last three digits should be shown)
    return "{}".format(trim_num(init_val))

# To use it, simply copy the code and run the function
