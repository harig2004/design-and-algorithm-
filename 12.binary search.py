def bin(arr,find):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==find:
            return mid
        elif arr[mid]<find:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[2,3,4,10,40]
find=10
result=bin(arr,find)
if result!=-1:
    print(result)
else:
    print("Element is not present in array")
