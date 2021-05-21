# ask user to input the length of their list
input_length = int(input('Enter the length of number list:'))

# initialize an empty list to hold the values
user_list = []

# for range through input length, as the user to input a value and append the value to user_list
for i in range(0, input_length):
    entry = int(input(f'Enter value {i + 1}:'))
    user_list.append(entry)

# print all values in the list that are greater than 20
[print(val) for val in user_list if val > 20]

