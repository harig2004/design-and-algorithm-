def prime(n,i=2):
    if n<=1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)
number=17
if prime(number):
    print("prime number")
else:
    print("is not a prime number")
