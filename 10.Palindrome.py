def Pal(s):
    return s==s[::-1]
s="malayalam"
ans=Pal(s)
if ans:
    print("Yes")
else:
    print("No")
