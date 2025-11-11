from operator import itemgetter


users  = [
    {"fname": "AAPL", "lname": 'robert'},
    {"fname": "TSLA", "lname": 'james'},
    {"fname": "GOOG", "lname": 'bucky'},
    {"fname": "AMZN", "lname": 'niied'},
    {"fname": "MSFT", "lname": 'fried'}
]

for x in sorted(users, key=itemgetter('fname')):
  print(x)