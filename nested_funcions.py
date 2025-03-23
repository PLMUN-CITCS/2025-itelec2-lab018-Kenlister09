def square (num):
  """Return the square of the given number."""
  return num * num # Or nume ** 2

def sum_of_squares(numbers):
  """Return the sum of the squares of the numbers in the list"""
  total = 0
  for n in numbers:
    total += square(n) # call the square function and add to total
return total
numbers_list = [2, 3, 4]
result = sum_of_squares(numbers_list)
print(f"the sum of squares is: {result}")
