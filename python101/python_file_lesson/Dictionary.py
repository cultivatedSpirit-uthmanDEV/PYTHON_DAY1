## Key and Value in Dictionary

classmates = {'Tony ': 'cool but smells','Emma ': 'sits behind me','lucy ': 'asks too many questions' }

print(classmates)

for k , v in classmates.items():
   print(k + v)

classmates['Tony'] = 'go away'

print(classmates['Tony'])
