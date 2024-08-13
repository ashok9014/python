def reverse_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    reversed_number = int(reversed_str)
    
    return reversed_number

original_number = 12345
reversed_number = reverse_number(original_number)
print(f"The reverse of {original_number} is {reversed_number}")
