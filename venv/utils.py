###
#
# Module Exercise
# find max number and display to another module
# ##

def find_max():
    numbers = [2, 14, 55, 8, 10, 12, 20]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return  max
