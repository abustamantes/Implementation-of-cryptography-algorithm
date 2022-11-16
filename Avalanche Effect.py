import operator
import numpy as np


AI=np.array([[15,4,6,6],
    [2,9,12,2],
    [5,12,14,2],
    [9,12,2,7],
    [11,13,13,15],
    [1,13,1,3],
    [14,1,12,3], 
    [3,14,0,2],
    [5,3,13,11],
    [12,2,7,4]])

AII=np.array([[10,2,15,10],
     [14,0,1,8]]) 

def changing_bits(g,b,i1):
  return b[:g]+i1+b[g+1:]  

def zipping(c):
  return [i + j for i, j in zip(([i + j for i, j in zip(c[::2], c[1::2])][::2]), ([i + j for i, j in zip(c[::2], c[1::2])][1::2]))]

def avalanche_effect(AI,AII):
  counter=0;q=0
  for q in range(0,len(AI)):#10 times for the plain text
    x=AI[q]
    b=[format(i, '04b') for i in x]
    b="".join(b)
    ma=0;na=0;p=1
    for ma in range(0,len(AII)):#2 times for the keys
      g=0
      for i in b:#Changing each bit of the 16 bit plain text
        if i=="1":
          i1=i.replace("1","0")
        else:
            i1=i.replace("0","1")
        c=changing_bits(g,b,i1) # Creating 16 new plain text for each original plain text(AI)
        g = g + 1
        c = zipping(c)     
        c=[int(s, base=2) for s in c]
        c=np.array(c)
        Ea1 = c[1] ^ AII[ma][na]
        Ea2 = c[3] ^ AII[ma][na + 2]
        Ea3 = c[0]^ AII[ma][na + 1]
        Ea4 = c[2]^ AII[ma][na + 3]
        Epa=[Ea1,Ea2,Ea3,Ea4]
        Ea1 = sbox1(Ea1)
        Ea2 = sbox2(Ea2)
        Ea3 = sbox1(Ea3)
        Ea4 = sbox2(Ea4)
        Epa=np.stack((Ea1,Ea2,Ea3,Ea4))
        if p <=16:
          x2=ciphertext(AI,AII)[q]
          b2=[format(i, '04b') for i in x2]
          b2="".join(b2)
        else:
          x2=ciphertext(AI,AII)[q+10]
          b2=[format(i, '04b') for i in x2]
          b2="".join(b2)
        x3=Epa
        b3=[format(i, '04b') for i in x3]
        b3="".join(b3)
        p=p+1
        for x,y in zip(b2,b3):
          if x!=y:
            counter=counter+1 #Counting the bits that have changed
  return counter


print(avalanche_effect(AI,AII))
print("The avalanche effect is:" + str((avalanche_effect(AI,AII)/(16*16*2*10))*100) +"%")
