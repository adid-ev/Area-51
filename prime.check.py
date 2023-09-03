a=""
while(a!="x"):
    n=int(input("Enter a number to check if it is prime number: "))
    if(n==1):
        print("1 is neither a prime nor a composite number.")
    elif(n==2):
        print("2 is a prime number.")
    else:
        for i in range(2,n):
            if(n%i==0):
                print(n,"is not a prime number.")
                break
        else:
            print(n,"is a prime number.")
    a=input("Press x to exit or any other key to continue: ")
    if(a=="x"):
        print("Thank you for using this program!!!")