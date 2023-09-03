t=int(input("No. of test cases: "))
for p in range(1,t+1):
    print(f"\nTest case {p}:")
    n=int(input("Length of array: "))
    k=int(input("No. of rotations: "))
    arr=[]
    for c in range(0,n):
        d=int(input(f"Data at index {c}: "))
        arr.append(d)
    print("Array before rotation:",arr)
    for i in range(0,k):
        temp = arr[n-1]
        for j in range(n-1,0,-1):
            arr[j]=arr[j-1]
        arr[0] = temp
    print("Array after rotation:",arr)