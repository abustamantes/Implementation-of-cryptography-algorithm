import numpy as np

#Results for the encryption
ct=([[ 8, 14,  3,  9],
 [ 5, 12, 12,  7],
 [11, 12,  2,  2],
 [11,  6,  6, 10],
 [ 2, 5, 10, 11],
 [ 2, 11,  8, 15],
 [10, 11, 15,  7],
 [12, 12,  7, 12],
 [ 0,  1,  2, 11],
 [ 3,  7, 14,  6],
 [ 4,  9,  1, 14],
 [ 2,  8,  4,  2],
 [ 6,  8, 13,  7],
 [ 6,  0, 10, 12],
 [ 5, 10,  6, 13],
 [ 5,  4,  7,  5],
 [15,  4, 14,  2],
 [13,  8,  8, 10],
 [ 1, 15, 13, 13],
 [ 9,  3, 15,  8]])

#Key
AII=np.array([[10,2,15,10],
     [14,0,1,8]])

#Seed
AIII=np.array([9,7,2,15])

def reverse_sbox1(s1):
  s1 = np.select([s1==0,s1==1,s1==2,s1==3,s1==4,s1==5,s1==6,s1==7,s1==8,s1==9,s1==10,s1==11,s1==12,s1==13,s1==14,s1==15], [6,2,8,7,5,12,13,14,1,3,4,9,11,15,10,0], s1)
  return s1
def reverse_sbox2(s2):
  s2 = np.select([s2==0,s2==1,s2==2,s2==3,s2==4,s2==5,s2==6,s2==7,s2==8,s2==9,s2==10,s2==11,s2==12,s2==13,s2==14,s2==15], [4,6,3,7,0,2,10,9,1,5,12,14,15,13,11,8], s2)
  return s2
def reverse_sbox3(s3):
  s3 = np.select([s3==0,s3==1,s3==2,s3==3,s3==4,s3==5,s3==6,s3==7,s3==8,s3==9,s3==10,s3==11,s3==12,s3==13,s3==14,s3==15], [15,8,0,10,5,1,12,6,4,13,14,3,7,2,9,11], s3)
  return s3
def reverse_sbox4(s4):
  s4 = np.select([s4==0,s4==1,s4==2,s4==3,s4==4,s4==5,s4==6,s4==7,s4==8,s4==9,s4==10,s4==11,s4==12,s4==13,s4==14,s4==15], [8,11,13,10,9,0,4,15,6,5,1,14,3,12,7,2], s4)
  return s4

def binaryct(Ep):
  rb=[] #Results in binary style
  for i in Ep:
    for j in i:
        j='{0:04b}'.format(j)
        rb.append(j)
  return np.array(rb)[:].reshape(len(Ep),len(Ep[0]))

def decryption(ct,b,c):
    ct=np.transpose(ct)
    ct[0] = reverse_sbox1(ct[0])
    ct[1] = reverse_sbox2(ct[1])
    ct[2] = reverse_sbox3(ct[2])
    ct[3] = reverse_sbox4(ct[3])
    ct=np.transpose(ct)
   
    i=0;m=0;n=0
    for i in range(0,len(ct)):
        if i<10:
            for m in range(0,len(b)-1):        
                ptext1=ct[i][2]^b[m][n+1]^c[1]
                ptext2=ct[i][0]^b[m][n]^c[3]
                ptext3=ct[i][3]^b[m][n+3]^c[0]
                ptext4=ct[i][1]^b[m][n+2]^c[2]
                ct[i,0]=ptext1
                ct[i,1]=ptext2
                ct[i,2]=ptext3
                ct[i,3]=ptext4
        else:
            for m in range(1,len(b)):        
                ptext1=ct[i][2]^b[m][n+1]^c[1]
                ptext2=ct[i][0]^b[m][n]^c[3]
                ptext3=ct[i][3]^b[m][n+3]^c[0]
                ptext4=ct[i][1]^b[m][n+2]^c[2]
                ct[i,0]=ptext1
                ct[i,1]=ptext2
                ct[i,2]=ptext3
                ct[i,3]=ptext4
    return ct
   
decrypted=decryption(ct,AII,AIII)
print(decrypted)
print()
print(binaryct(decrypted))
