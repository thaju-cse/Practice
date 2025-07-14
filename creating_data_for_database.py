import random

characters = {0:' ' }
for i in range(ord('a'),ord('z')+1):
    characters [i] = chr(i)
    print(i, chr(i))
for i in range(ord('A'),ord('Z')+1):
    characters [i+26] = chr(i)
    print(i, chr(i))
    
print(random.randint(1,26))
print('for small letters use -> random.randint(97,122) = ', random.randint(97,122))
print('for capital letters use -> random.randint(65,90) = ', random.randint(65,90))
print(', = 44 ',ord(','),'\n  = 32 ', ord(' '))

n = 100
#while n:
 #   length = random.randint(1,20)
  #  for i in range(length):
   #     print(random.random([range(1,100)])) 
