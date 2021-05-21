# ask user for input integer then convert to int
input_int = input('Enter integer:')
input_int = int(input_int)

# check for remainder when dividing by 2. If 0, print EVEN, else print ODD
if input_int % 2 == 0:
    print('EVEN')
else:
    print('ODD')