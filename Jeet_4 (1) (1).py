import math
l=[]
p=int(input("Enter the plain text:"))
a=int(input("Enter a prime number A:"))
b=int(input("Enter a prime number B other than A:"))

n=a*b
n1=(a-1)*(b-1)
for i in range(1,n1+1):
    if(math.gcd(i,n1)==1 and i!=a and i!=b):
        l.append(i)
print(l)
e=int(input("Select encryption key e from the list:"))
for i in range(1,1000):
    if(((e*i)%n1)==1):
        d=i
        break;
print(d)    
c=(p**e)%n
print("Cipher text to be send to reciever is: {}" .format(c))
t=(c**d)%n
print("Text after decryption is: {}".format(t))
    
        
