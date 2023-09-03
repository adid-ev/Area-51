a=""
while(a!="x"):
    print('''
Choose the method you want to print the Fibonacci Series by:
1. By the number of terms in the series
2. By the mentioning the limit of the series
3. Exit the program
    ''')
    m=int(input("Enter your favoured method: "))
    if(m==1):
        n=int(input("Enter the number of terms in the series: "))
        print("The Fibonacci Series is: ")
        p=0
        q=1
        print(p)
        print(q)
        for d in range(0,n-2):
            r=p+q
            print(r)
            p=q
            q=r
    elif(m==2):
        n=int(input("Enter the limit of the series: "))
        print("The Fibonacci Series is: ")
        p=0
        q=1
        print(p)
        print(q)
        while(p+q<=n):
            r=p+q
            print(r)
            p=q
            q=r
    elif(m==3):
        a="x"
        print("Thank you for using the program!!!")
    else:
        print("Invalid input!!!")
        print("Please try again!!!")
    
