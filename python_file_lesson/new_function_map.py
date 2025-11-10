"""
income = [10, 20, 75]

def double_income(dollars):
  doubled = []
  for x in dollars:
    doubled.append(x * 2)
  return doubled
"""



# new_income = double_income(income)
# print(new_income)

# Triple Each Value
# Write a function that takes a list of numbers and 
# returns a new list with each number multiplied by 3.

def triple_number(numbers):
  tripled = []
  for x in numbers:
    tripled.append(x * 3)
  return tripled

number_list = [10, 20, 30]

print(triple_number(number_list))

## using map_function

incomes = [100, 200 ,300]

def doubled_incomes(euros):
      return euros * 2


new_incomes = list(map(doubled_incomes, incomes ))
print(new_incomes)

## Square the Numbers
# Given a list [2, 4, 6, 8], return a new list with the squares of each number.


number_one = [2,4,6,8]

def number_function(number_square):
   squared = []
   for item in number_square:
      squared.append(item ** 2)
   return squared

print(number_function(number_one))