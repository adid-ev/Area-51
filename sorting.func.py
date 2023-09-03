def BubbleSort():
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if(List[j]>List[j+1]):
                (List[j], List[j+1]) = (List[j+1], List[j])

def InsertionSort():
    for i in range(1, n):
        temp = List[i]
        prev = i-1
        while((prev>=0) and (temp < List[prev])):
            List[prev + 1] = List[prev]
            prev = prev-1
        List[prev + 1] = temp 

def QuickSort(List, low, high):
    def partition(List, low, high):
        pivot = List[high]
        i = low - 1
        for j in range(low, high):
            if(List[j] <= pivot):
                i = i + 1
                print("i =",i,"List =", List)
                (List[i], List[j]) = (List[j], List[i])
        (List[i + 1], List[high]) = (List[high], List[i + 1])
        return i+1
    if(low < high):
        pi = partition(List, low, high)
        QuickSort(List, low, pi - 1)
        QuickSort(List, pi + 1, high)  

def MergeSort(List):
    def Merge(a, b):
        FinalList = []
        while((a != []) and (b != [])):
            if(a[0] > b[0]):
                FinalList.append(b[0])
                del b[0]
            else:
                FinalList.append(a[0])
                del a[0]
        while(a != []):
            FinalList.append(a[0])
            del a[0]
        while(b != []):
            FinalList.append(b[0])
            del b[0]
        return FinalList
    length = len(List)
    if(length == 1):
        return List
    mid = length//2
    preList = List[:mid]
    postList = List[mid:]
    preList = MergeSort(preList)
    postList = MergeSort(postList)
    return Merge(preList, postList)

def SelectionSort(List):
    for i in range(0, n-1):
        min = i
        for j in range(min+1, n):
            if(List[j]<List[min]):
                min = j
        if(min != i):
            (List[i],List[min]) = (List[min], List[i])
    return 0

def HeapSort(List):
    def Heapify(List, N, i):
        left = 2 * i + 1
        right = left + 1
        print(i)
        if((left <= N) and (List[left] > List[i])):
            max = left
        else:
            max = i
        if((right < N) and (List[right] > List[max])):
            max = right
        if(max != i):
            (List[i], List[max]) = (List[max], List[i])
            Heapify(List, max)
    def BuildMaxHeap(List):
        for i in range(N//2, -1, -1):
            Heapify(List, i)
    N = len(List)
    BuildMaxHeap(List)
    for i in range(N-1, 0, -1):
        (List[i], List[1]) = (List[1], List[i])
        
        Heapify(List, i, 0)

n=int(input("Enter length of list: "))
List = []
for i in range(1, n+1):
    element = int(input(f"Enter element {i}: "))
    List.append(element)

print('''
The following sorting options are provided: 
1. Bubble sort
2. Insertion Sort
3. Quick Sort
4. Merge Sort
5. Selection Sort
6. Heap Sort
    ''')
choice = int(input("Enter your choice: "))
if(choice == 1):
    BubbleSort()
    print(List)
elif(choice == 2):
    InsertionSort()
    print(List)
elif(choice == 3):
    QuickSort(List, 0, n-1)
    print(List)
elif(choice == 4):
    MergeSort(List)
    print(List)
elif(choice == 5):
    SelectionSort(List)
    print(List)
elif(choice == 6):
    HeapSort(List)
    print(List)