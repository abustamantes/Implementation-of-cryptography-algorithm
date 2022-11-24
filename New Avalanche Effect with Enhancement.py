import numpy as np

#We are working with decimal functions, so the first thing you have to make sure of is to convert binary to decimals
#Plain text
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

#Key
AII=np.array([[10,2,15,10],
     [14,0,1,8]])

#Seed
AIII=np.array([9,7,2,15])

def sbox1(s1):
  s1 = np.select([s1==0,s1==1,s1==2,s1==3,s1==4,s1==5,s1==6,s1==7,s1==8,s1==9,s1==10,s1==11,s1==12,s1==13,s1==14,s1==15], [15,8,1,9,10,4,0,3,2,11,14,12,5,6,7,13], s1)
  return s1
def sbox2(s2):
  s2 = np.select([s2==0,s2==1,s2==2,s2==3,s2==4,s2==5,s2==6,s2==7,s2==8,s2==9,s2==10,s2==11,s2==12,s2==13,s2==14,s2==15], [4,8,5,2,0,9,1,3,15,7,6,14,10,13,11,12], s2)
  return s2
def sbox3(s3):
  s3 = np.select([s3==0,s3==1,s3==2,s3==3,s3==4,s3==5,s3==6,s3==7,s3==8,s3==9,s3==10,s3==11,s3==12,s3==13,s3==14,s3==15], [2,5,13,11,8,4,7,12,1,14,3,15,6,9,10,0], s3)
  return s3
def sbox4(s4):
  s4 = np.select([s4==0,s4==1,s4==2,s4==3,s4==4,s4==5,s4==6,s4==7,s4==8,s4==9,s4==10,s4==11,s4==12,s4==13,s4==14,s4==15], [5,10,15,12,6,9,8,14,0,4,3,1,13,2,11,7], s4)
  return s4

def ciphertext(a,b,c):
  i=0;j=0;m=0;n=0
  C1=();C2=();C3=();C4=()
  for m in range(0,len(b)):
    for i in range(0,len(a)):
        E1=a[i][j+1]^c[3]^b[m][n]
        E2=a[i][j+3]^c[2]^b[m][n+2]
        E3=a[i][j]^c[1]^b[m][n+1]
        E4=a[i][j+2]^c[0]^b[m][n+3]
        
        C1=np.append(C1,E1)
        C2=np.append(C2,E2)
        C3=np.append(C3,E3)
        C4=np.append(C4,E4)
  C1 = sbox1(C1)
  C2 = sbox2(C2)
  C3 = sbox3(C3)
  C4 = sbox4(C4)
  Ep=np.stack((C1,C2,C3,C4),axis=1)
  return Ep.astype(int)

def binaryct(Ep):
  rb=[] #Results in binary style
  for i in Ep:
    for j in i:
        j='{0:04b}'.format(j)
        rb.append(j)
  return np.array(rb)[:].reshape(len(Ep),len(Ep[0]))
ct=ciphertext(AI,AII,AIII)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("Now, we are going to calculate the new avalanche effect")

def changing_bits(g,b,i1):
  return b[:g]+i1+b[g+1:]  

def zipping(c):
  return [i + j for i, j in zip(([i + j for i, j in zip(c[::2], c[1::2])][::2]), ([i + j for i, j in zip(c[::2], c[1::2])][1::2]))]

def avalanche_effect(AI,AII,AIII):
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
        Ea1 = c[1] ^AIII[3]^ AII[ma][na]
        Ea2 = c[3] ^AIII[2]^ AII[ma][na + 2]
        Ea3 = c[0]^AIII[1]^ AII[ma][na + 1]
        Ea4 = c[2]^AIII[0]^ AII[ma][na + 3]
        Epa=[Ea1,Ea2,Ea3,Ea4]
        Ea1 = sbox1(Ea1)
        Ea2 = sbox2(Ea2)
        Ea3 = sbox3(Ea3)
        Ea4 = sbox4(Ea4)
        Epa=np.stack((Ea1,Ea2,Ea3,Ea4))
        if p <=16:
          x2=ciphertext(AI,AII,AIII)[q]
          b2=[format(i, '04b') for i in x2]
          b2="".join(b2)
        else:
          x2=ciphertext(AI,AII,AIII)[q+10]
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


print(f"The total of bits that have changed is: {avalanche_effect(AI,AII,AIII)}")
print("The avalanche effect is:" + str((avalanche_effect(AI,AII,AIII)/(16*16*2*10))*100) +"%")