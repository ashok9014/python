def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(f"The reverse of '{original_string}' is '{reversed_string}'")
