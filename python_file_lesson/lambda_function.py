answer = lambda x: x*7
print(answer(5))

## 

import heapq


grade = [23,25,27,190,290,560]

print(heapq.nlargest(3, grade))

print(heapq.nsmallest(3, grade))


stocks = {
  "GOOG" : 520.54,
  "FB" : 76.45,
  "YHOO" : 39.28,
  "AMZN" : 306.21,
  "AAPL" : 99.76
}

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))





