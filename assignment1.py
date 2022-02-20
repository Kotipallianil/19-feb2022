def sprime(n):
    for i in range(2,n):
        if n%i==0:
           return False
         return True
t=int(input("enter the numbers:"))
for i in range(t):
        n=int(input("enter the n numbers":))
        c=o
        for i in range(2,n+1):
            if sprime(i):
    if sprime(i):
        c=c+1
print("count of prime numbers are:",c)
