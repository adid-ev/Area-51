a=""
while(a!="x"):
    n=int(input("Enter a number to display it\'s factorial: "))
    if(n<0):
        print("Factorial of a negative number is not possible.\nRetry!")
    elif(n==0):
        print("Facotrial of 0 = 1")
    else:
        f=1
        for c in range(1,n+1):
            f=f*c
        print("Factorial of",n,"=",f)
    a=input("Enter any key to continue or press 'x' to exit: ")
    if(a=="x"):
        print("Thank you for using this program!!!")
        break