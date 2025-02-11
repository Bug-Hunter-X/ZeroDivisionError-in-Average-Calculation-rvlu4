def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0 # Handle case where all numbers are zero
    return total / len(numbers)

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_numbers2 = [10, 20, 30, 40, 0] 
average2 = calculate_average(my_numbers2)
print(f"The average is: {average2}")

my_numbers3 = [0,0,0]
average3 = calculate_average(my_numbers3)
print(f"The average is: {average3}") 