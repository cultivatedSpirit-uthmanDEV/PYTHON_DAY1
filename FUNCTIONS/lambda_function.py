answer = lambda x: x*7
print(answer(5))

## 

import heapq


grade = [23,25,27,190,290,560]

print(heapq.nlargest(3, grade))

print(heapq.nsmallest(3, grade))


import heapq

stocks = [
    {"name": "AAPL", "price": 520.54},
    {"name": "TSLA", "price": 76.45},
    {"name": "GOOG", "price": 39.28},
    {"name": "AMZN", "price": 306.21},
    {"name": "MSFT", "price": 99.76}
]

cheapest_two = heapq.nsmallest(2, stocks, key=lambda stock: stock["price"])
print(cheapest_two)




