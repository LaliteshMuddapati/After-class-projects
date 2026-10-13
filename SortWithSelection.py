List=[]
N=int(input("Enter size of list: "))
print("Start entering elements of list, each element in a new line: ")
for i in range(N):
    element=int(input(" "))
    List.append(element)
 



for i in range(len(List)):
    min_id=i
    for j in range(i+1, len(List)):
        if List[min_id]>List[j]:
            min_id=j

    List[i], List[min_id]=List[min_id], List[i]



print("Sorted array")
for i in range(len(List)):
    print("%d" %List[i], end=" ")