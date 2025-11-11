item = ['december 30, 2025','bread glove',8.51 ]
print(item[2])
print(item[0])
print(item[1])



## unpacking the list

date ,name, price = ['december 30, 2025','bread glove',8.51 ]
print(name)
print(date)
print(price)


## python cookbook short

def drop_first_last(grades):
  first, *middle, last = grades
  avg = sum(middle)/len(middle)
  print(avg)

drop_first_last([2,2,2,2,2])
drop_first_last([20 ,122,82,42,12])