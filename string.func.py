ques="Enter a string : "
def legnth():
    s=input(ques)
    i=0
    for c in s:
        i+=1
    print("The length of the string is ",i,".")
    return i
def upper():
    s=input(ques)
    s=s.upper()
    print("The string in upper case is ",s,".")
    return s
def lower():
    s=input(ques)
    s=s.lower()
    print("The string in lower case is ",s,".")
    return s
def occurence():
    s=input(ques)
    c=input("Enter a character : ")
    i=0
    for x in s:
        if x==c:
            i+=1
    print("The character ",c," occurs ",i," times in the string ",s,".")
def concatenate():
    s=input("Enter first string : ")
    t=input("Enter second string : ")
    s=s+t
    print("The concatenated string is ",s,".")
    return s
def reverse():
    s=input(ques)
    r=[]
    i=-1
    for c in s:
        r.append(s[i])
        i-=1
    print("The reverse of the string is")
    for c in r:
        print(c,end="")
    print("")
def palindrome():
    t=input("Enter a string: ")
    if(t==t[::-1]):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
def panagram():
    s=input("Enter a string: ")
    s=s.lower()
    l=[]
    for c in s:
        if c not in l:
            l.append(c)
    l.sort()
    for d in l:
        if(d==" "):
            l.remove(d)
    if l==['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        print("It is a panagram")
    else:
        print("It is not a panagram")

a=""
while(a!="x"):
    print('''
The following options are provided: 
1. String length
2. String to upper case
3. String to lower case
4. Finding occurence of a character in a string
5. Concatenation of two strings
6. Reversing a string
7. Checking if a string is a palindrome
8. Checking if a string is a pangram
9. Exit
    ''')
    c=int(input("Enter your choice: "))
    if(c==1):
        legnth()
    elif(c==2):
        upper()
    elif(c==3):
        lower()
    elif(c==4):
        occurence()
    elif(c==5):
        concatenate()
    elif(c==6):
        reverse()
    elif(c==7):
        palindrome()
    elif(c==8):
        panagram()
    elif(c==9):
        a="x"
        print("Exiting...")
        print("Thank you for using this program!!!")
    else:
        print("Invalid choice!!!")
        print("Please try again!!!")