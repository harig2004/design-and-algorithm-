def rev(s,index):
    if index<0:
        return
    else:
        print(s[index],end="")
        rev(s,index-1)
string="Hello"
rev(string,len(string) - 1)

