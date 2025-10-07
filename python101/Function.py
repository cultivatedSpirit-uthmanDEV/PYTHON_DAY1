## Function continues

def add_numbers(*args):
  total = 0
  for a in args:
    total += a
  print(total)


add_numbers(3)

### unpacking arguement.

def health_calculator(age, apple_ate,cigs_smoked):
  answer = (100-age) + (apple_ate * 3.5) - (cigs_smoked * 2)
  print(answer)

buckys_data = [27, 20, 0]

health_calculator(buckys_data[0],
buckys_data[1], buckys_data[2])

health_calculator(*buckys_data)

