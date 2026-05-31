# Function to print positive numbers from a list
def print_positive_numbers(lst):
    positives = [num for num in lst if num > 0]
    return positives


# Input examples
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Output
print("Output:", ", ".join(map(str, print_positive_numbers(list1))))
print("Output:", print_positive_numbers(list2))