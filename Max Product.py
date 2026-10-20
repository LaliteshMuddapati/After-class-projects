def Sort(List):
    n=len(List)

    for i in range(n):

        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1]=List[j+1], List[j]



List=[]
N=int(input("Enter size of list: "))
print("Start entering elements (only positive integers) of list, each element in a new line: ")
for i in range(N):
    element=int(input(" "))
    List.append(element)



Sort(List)


n=len(List)
Max_product=List[n-1]*List[n-2]

product_list=[List[n-2], List[n-1]]
print("Elements that make up the maximum product: ", product_list)

print("Maximum product is equal to: ", Max_product)