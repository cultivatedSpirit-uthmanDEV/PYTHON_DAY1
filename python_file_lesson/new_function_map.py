income = [10, 20, 75]

def double_income(dollars):
  doubled = []
  for x in dollars:
    doubled.append(x * 2)
  return doubled



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