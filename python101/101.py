#DAY_1 
# VIDEO 1 AND 2

print(3+2) # result equals 5

print(3*20) # 60

print(8 + 2 * 10) # python follows bodmas

print ((8 + 2) * 10)#nums in parenthesis are cal. first

print(18//4) # // tells machine to round the remainder

print(5 ** 3) # multiply 5 by 5 in three times

## VARIABLES

tuna = 5
print (tuna + 20) # returned 25
bacon = 15
print(bacon/tuna)
# DAY_2
## VIDEO 3 AND 4
# VIDEO 3
# STRINGS - 
# string, sequence of character
#  encompass with single or double quote
'STRING' # single quote
"keep going" #double quote
#'i don't think she is 18 '# double is required instead
"i don't think she is 18!" # double quote or
'i don\'t think she is 18' # include back slash b4 pseudo string quote
# back slash means special meaning
print(r'C:\owner\desktop\uthman')# r(raw string) cancel the special meaning

# strings can also be stored as a variable just like number
# as well as add together
firstName = "bucky "
firstName + "roberts"

print(firstName + "Roberts")
# strings can also be multiplied
print(firstName * 5)#result buckybuckybuckybucky
#VIDEO 4
# string continues

# how to get each character from a string

user = "Tuna MeFish"
print(user[0]) # computer counts from zero instead of 1

print(user[-1]) # starts counting from the back
print(user[2 : 7])# slice start and stop on 7th without actually slice the 7th
print(user[2:])
print(len('Tuna MeFish')) # len() for length of a string or variable
print(len(user))

#DAY_3
## List - CHARACTERIZED WITH SQUARE BRACKET


players = [23,45,11,7,9]
print(players[2]) # position starts from 0

players[2] = 20 # alteration of value in list
print(players)

print(players + [13,90,46]) #addition of values to 
#an existing list but donot add permanently
print(players)
print(players.append(120))

# list slicing

print(players[:2])
players[:2] = [0,0] ## replace slice value with another
print(players) 

players[:] = []
print(players)

#DAY_4
## if statement

age = 13
if age < 21:
  print("no bear for you")

name = "uthman"

if name is "bucky":
   print("Hey there bucky")
elif name is "lucky":
   print("what's up luzemburg")
elif name is "puncky":
   print("what's up sodiq")
else:
   print('no way home')## returned "no way home"

 ## List and loop

food = ['bacon','tuna','ham','snausages','beef']

for f in food:
   print(f)
   print(len(f))

for f in food[:2]:
    print(f)
    print(len(f))

    ## Arrange  of number _ loop without list
for x in range(10):
   print("bucky is awesome")
for y in range(2,20,2):
   print (y)

   ## while loop

name = 5

'''while name < 10:
 ##  print('i love this')
     name += 1

     ## Break and continue'''

magicNumber = 26

for n in range(101):
   if n is magicNumber:
      print(n,"is the magic number")
      break
   else:
      print(n)

      ## ASSINMENT
'''loop through a 100 and pronoune a num that
is a multiple of 4'''

for v in range(101):
   if  v%4 is 0:
      print(v)

      ## continue
     
numbersTaken =  [2,4,16,5,9,10]
for n in range(1,20):
   if n in numbersTaken:
      continue
   print(n)


   ## Function
   ## contains lines of code that can be called time and 
   # time again

def beef():
   print('python is getting interesting')

beef()

def bitCoin_to_usd(btc):
   amount = btc * 527
   print(amount)


bitCoin_to_usd(3.85)## 3.85usd_
#2028.95btc

## return statement

def allowed_dating_age(my_age):
   girls_age = my_age/2 + 7
   return girls_age

buckys_limit = allowed_dating_age(27)
Bosses_limit = allowed_dating_age(37)
print("Bucky can date girls"
,buckys_limit,"or older")

print("Bucky can date girls",Bosses_limit,"or older")







