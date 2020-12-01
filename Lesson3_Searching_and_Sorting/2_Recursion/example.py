def recursive(input):
    # Why less or equal than 0?
    # To avoid input less than 0
    if input <= 0:
        return input
    else:
        print(input)
        output = recursive(input - 1)
        return output

print(recursive(2))
print()
print(recursive(-100))