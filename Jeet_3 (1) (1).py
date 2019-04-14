p=int(input("Enter the prime number p:"))
q=int(input("Enter the prime number q:"))

a=int(input("Enter the secret key of A:"))
b=int(input("Enter the secret key of B:"))

s1=(q**a) % p
s2=(q**b) % p
print("Calculated number after selecting secret number A gives {} and B gives {}. ".format(s1,s2))
r=(s2**a) % p
s=(s1**b) % p

if r==s:
    print("They can communicate on a common secret key {}" .format(r))
else:
    print("They can not communicate as A shares a key{} and B shares a key {}" .format(r,s))

