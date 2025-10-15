Fw = open('sample.txt','w')
## 'w' stands for write
Fw.write('writing some stuff in my text file\n')
## '\n' means move to the next line
Fw.write('i like bacon\n')
Fw.close()

Fr = open('sample.txt','r')
## 'r' stands for read

text = Fr.read()
print(text)
Fr.close()
