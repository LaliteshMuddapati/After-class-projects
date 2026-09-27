def BubbleSort(List):
    n=len(List)

    for i in range(n):

        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1]=List[j+1], List[j]



List=[]
N=int(input("Enter size of list: "))
print("Start entering elements of list, each element in a new line: ")
for i in range(N):
    element=int(input(" "))
    List.append(element)
print(List)    



BubbleSort(List)



print("Sorted list: ")
for i in range(len(List)):
    print("%d" %List[i], end=" ")