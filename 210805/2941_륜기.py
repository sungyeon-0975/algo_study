word = input()
 

for i in range(len(word)):
    if 'c=' in word:
     word = word.replace('c=','a')     
    
    elif 'c-' in word:
     word = word.replace('c-','a')  

    elif 'dz=' in word:
     word = word.replace('dz=','a')   

    elif 'd-' in word:
     word = word.replace('d-','a')
 
    elif 'lj' in word:
     word = word.replace('lj','a')
    
    elif 'nj' in word:
     word = word.replace('nj','a')
  
    elif 's=' in word:
     word = word.replace('s=','a')
    
    elif 'z=' in word:
     word = word.replace('z=','a')

print(len(word))