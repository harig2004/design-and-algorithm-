def copy(a,b,index=0):
    if index==len(a):
        return b
    else:
        b+=a[index]
        return copy(a,b,index+1)
a="Hello"
b=""
copystr=copy(a,b)
print("Original string:",a)
print("Copied string:",copystr)
