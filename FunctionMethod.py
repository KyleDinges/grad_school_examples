# create print_even function that accepts two values
def print_even(val_1, val_2):

    # define function that divides value by 2 and if the remainder is 0, print the value, else do nothing
    def check_even(val):
        if val % 2 == 0:
            print(val)
        else:
            pass
    # create a list to iterate over with the input parameters to print_even()
    input = [val_1, val_2]

    # use a for loop to iterate over the input values and call check_val() on each
    for val in input:
        check_even(val)

