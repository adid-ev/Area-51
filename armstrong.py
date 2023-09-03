a=""
while(a!="x"):
    n=int(input("Enter a number to check if it is an Armstrong number: "))
    s=0
    t=n
    while(t>0):
        d=t%10
        s+=d**3
        t//=10
    if(n==s):
        print(n,"is an Armstrong number.")
    else:
        print(n,"is not an Armstrong number.")
    a=input("Press x to exit or any other key to continue: ")
    if(a=="x"):
        print("Thank you for using this program!!!")