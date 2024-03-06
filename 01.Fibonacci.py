def fib_iterative(n):
    fib = [0,1]
    for i in range(2,n):
        next=fib[-1]+fib[-2]
        fib.append(next)
    return fib
n=10
fib=fib_iterative(n)
print(fib)

def fib_rec(n1):
    if n1<=1:
        return n1
    else:
        return fib_rec(n1-1)+fib_rec(n1-2)
n1=10
fib1=[]
for j in range(n1):
    fib1.append(fib_rec(j))
print("Fibonacci Series:", fib1)
