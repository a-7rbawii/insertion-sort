def InsSort(myList):
    UBound = len(myList)

    for i in range(1,UBound):
        NextItem = myList[i]
        position = i - 1

        while position>=0 and myList[position]>NextItem:
            myList[position+1] = myList[position]
            position = position - 1
        myList[position+1] = NextItem


myList = []
n = int(input("Enter number of elements in the List:\n"))
for j in range(0,n):
    element = int(input("Input element:\n"))
    myList.append(element)
print("The unsorted array is "+str(myList))

InsSort(myList)

print("The sorted array is "+str(myList))