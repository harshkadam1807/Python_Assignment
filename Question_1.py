def conversion_currency(num):
    # Convert the number to a string
    num_string = str(num)

    # Determine the position to insert commas
    length = len(num_string)
    comma_positions = [i for i in range(length - 1, 0, -2)]

    # Insert commas at appropriate positions
    for position in comma_positions:
        num_string = num_string[:position] + ',' + num_string[position:]

    return num_string

input_num = 504678
currency_notation = conversion_currency(input_num)
print("Input:", input_num)
print("Output:", currency_notation)