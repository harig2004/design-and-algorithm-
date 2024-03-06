def compute_hcf(x,y):
    if x>y:
        s=y
    else:
        s=x
    for i in range(1,s+1):
        if((x%i==0) and (y%i==0)):
            hcf=i 
    return hcf
num1=54 
num2=24
