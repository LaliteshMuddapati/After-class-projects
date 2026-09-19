def binarySearch(list, l, r, key):
    while l<=r:
        mid=l+(r-l)//2
        if list[mid]==key:
            return mid
        elif list[mid]<key:
            l=mid+1
        else:
            r=mid-1
    return -1

list=[32, 45, 63, 77, 82]
key=63

print(list)
result=binarySearch(list, 0, len(list)-1, key)
if result!=-1:
    print("Element {} is present at index {}".format(key, result))
else:
    print("Element is not present")
