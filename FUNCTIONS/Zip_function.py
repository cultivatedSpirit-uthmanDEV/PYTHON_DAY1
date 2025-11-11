first = ["adebayo","Titiloye","Wasiu"]
last = ["rashidat","adisa","Uthman"]

name = zip(first, last)

for a,b in name :
  print(a,b)


stocks = {
    'GOOG' : 435,
    'AAPL' : 325,
    'FB' : 54,
    'F' : 45}

  # switch the key and the value

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

