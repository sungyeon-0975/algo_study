


A = int(input())
B = int(input())
C = int(input())

multi = str(A*B*C)

dictn = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

for number in multi:
   dictn[number] += 1

for val in dictn.values():
    print(val)


    