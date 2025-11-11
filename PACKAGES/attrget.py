from operator import attrgetter

class User:

  def __init__(self, x, y):
    self.name = x
    self.user_id = y

  def __repr__(self):
    return self.name + ":" + str(self.user_id)
  

users = [
  User('Bucky', 6),
  User('mimi', 43),
  User('nicky', 9),
  User('fizzy', 3),
  User('mic', 4)]

print('----')
for user in sorted(users, key=attrgetter('name')):
  print(user)