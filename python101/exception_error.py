## syntax error and exception

tuna = int(input("what's your fav number?\n"))
print(tuna)


while True:
   try:
      number = int(input("what's ur favourite number?\n"))
      print(18/number)
      break
   except ValueError:
      print("Make sure to enter a number")
   except:
      print("Don't pick Zero")
   finally:
      print("loop is complete")