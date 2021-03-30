# Exercise Three
# Write a simple program that finds the number of digits of a given integer value

def count_digits(value): 
    value = abs(value)
    value = str(value)
    return len(value)

print(count_digits(-908))
