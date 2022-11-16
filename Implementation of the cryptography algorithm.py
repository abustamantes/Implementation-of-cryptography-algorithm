import operator
import numpy as np

#We are working with decimal functions, so the first thing you have to make sure of is to convert binary to decimals

a=np.array([[15,4,6,6],
    [2,9,12,2],
    [5,12,14,2],
    [9,12,2,7],
    [11,13,13,15],
    [1,13,1,3],
    [14,1,12,3], 
    [3,14,0,2],
    [5,3,13,11],
    [12,2,7,4]])


b=np.array([[10,2,15,10],
     [14,0,1,8]]) 

def sbox1(s1):
  s1 = np.select([s1==0,s1==1,s1==2,s1==3,s1==4,s1==5,s1==6,s1==7,s1==8,s1==9,s1==10,s1==11,s1==12,s1==13,s1==14,s1==15], [15,8,1,9,10,4,0,3,2,11,14,12,5,6,7,13], s1)
  return s1
def sbox2(s2):
  s2 = np.select([s2==0,s2==1,s2==2,s2==3,s2==4,s2==5,s2==6,s2==7,s2==8,s2==9,s2==10,s2==11,s2==12,s2==13,s2==14,s2==15], [4,8,5,2,0,9,1,3,15,7,6,14,10,13,11,12], s2)
  return s2


def ciphertext(a,b):
  i=0;j=0;m=0;n=0;
  C1=();C2=();C3=();C4=()
  for m in range(0,len(b)):
    for i in range(0,len(a)): 
      E1=a[i][j+1]^b[m][n]
      E2=a[i][j+3]^b[m][n+2]
      E3=a[i][j]^b[m][n+1]
      E4=a[i][j+2]^b[m][n+3]
      C1=np.append(C1,E1)
      C2=np.append(C2,E2)
      C3=np.append(C3,E3)
      C4=np.append(C4,E4)
  C1 = sbox1(C1)
  C2 = sbox2(C2)
  C3 = sbox1(C3)
  C4 = sbox2(C4)
  Ep=np.stack((C1,C2,C3,C4),axis=1)
  return Ep.astype(int)

def binaryct(Ep):
  rb=[] #Results in binary style
  for i in Ep:
    for j in i:
        j='{0:04b}'.format(j)
        rb.append(j)
  return np.array(rb)[:].reshape(len(Ep),len(Ep[0]))

print(ciphertext(a,b))
print("\n")
print(binaryct(ciphertext(a,b)))