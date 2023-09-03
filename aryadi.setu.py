#COMPUTER SCIENCE PROJECT CLASS XII , ARYAVARDHAN XII-A ROLL NO.-7 , ADIDEV XII-A ROLL NO.-2
import csv
print('''##############################################################################
==============================================================================
                                ARYADI SETU
                    YOUR PERSONALIZED COVID ASSESSMENT TEST
                        OUR FIGHT AGAINST COVID-19                  
==============================================================================
**All the data you enter  will be stored onto an excel file for further use**
##############################################################################
\n\n
''')
with open("covid.csv",'w', newline='') as cov:
    writer=csv.writer(cov)
    writer.writerow(['NAME','AGE','GENDER','SYMPTOMS','DISEASES','TRAVELLED INTERNATIONALLY','INTERACTION WITH A COVID PATIENT','SOCIAL WORKER'])
def EnteringRecord(records):
    with open("covid.csv",'a', newline='') as cov:
        writer=csv.writer(cov)
        writer.writerow(records)
def SelfAssessmentTest():
    error=0
    n=0
    name=input("\nPlease Enter Your Name : ")
    name=name.upper()
    age=int(input("\nPlease Enter Your Age : "))
    if((age>110)or(age<0)):
        print("INVALID VALUE!!!\nPLEASE RERUN THE TEST")
        error=+1
    elif((age<6)or(age>54)):
        n=1
    gender=input("\nPlease Enter Your Gender : ")
    if gender in ['f','F','female','Female','FEMALE']:
        gender="Female"
    elif gender in ['m','M','male','Male','MALE']:
        gender="Male"
    else:
        print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
        error=+1
    print('''\nGiven Below are the Most Common Symptoms of COVID-19:
(1)Dry Cough
(2)Fever
(3)Difficulty in Breathing
(4)Loss of Senses of Smell and Taste
''')
    k=int(input("\nWhich of the following options apply to you:\n(1)Multiple Symptoms\n(2)Single Symptom\n(3)No Symptom\n\nPlease Select Your Option : "))
    if k not in [1,2,3]:
        print("INVALID VALUE!!!\nPLEASE RERUN THE TEST")
        error=+1
    elif(k==1):
        u=int(input("\nEnter the number of symptoms you have : "))
        if u not in [0,1,2,3,4]:
            print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
            error=+1
        n=n+2*u
        if(u>1):
            symptoms=[]
            for c in range(1,u+1):
                print("Symptom number",c,end=' ')
                s=int(input(": "))
                if(s==1):
                    symptoms.append("Dry Cough")
                elif(s==2):
                    symptoms.append("Fever")
                elif(s==3):
                    symptoms.append("Difficulty in Breathing")
                elif(s==4):
                    symptoms.append("Loss of Senses of Smell and Taste")
                else:
                    print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
                    error=+1
        elif(u==1):
            s=int(input("Enter Your Symptom : "))
            if(s==1):
                symptoms="Dry Cough"
            elif(s==2):
                symptoms="Fever"
            elif(s==3):
                symptoms="Difficulty in Breathing"
            elif(s==4):
                symptoms="Loss of Senses of Smell and Taste"
            else:
                print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
                error=+1
        else:
            symptoms='None'
    elif(k==2):
        n=n+2
        s=int(input("Enter Your Symptom : "))
        if(s==1):
            symptoms="Dry Cough"
        elif(s==2):
            symptoms="Fever"
        elif(s==3):
            symptoms="Difficulty in Breathing"
        elif(s==4):
            symptoms="Loss of Senses of Smell and Taste"
        else:
            print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
            error=+1
    else:
        symptoms='None'
    print('''\nGive Below are some Chronic Diseases:
(1)Diabetes
(2)Hypertension
(3)Heart Disease
(4)Lung Disease
(5)Kidney Disorder
''')
    j=int(input("\nWhich of the following options apply to you:\n(1)Multiple Diseases\n(2)Single Disease\n(3)No Disease\n\nPlease Select Your Option : "))
    if j not in [1,2,3]:
        print("INVALID VALUE!!!\nPLEASE RERUN THE TEST")
        error=+1
    elif(j==1):
        z=int(input("\nEnter the number of diseases you have : "))
        if z not in [0,1,2,3,4]:
            print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
            error=+1
        n=n+2*z 
        if(z>1):
            diseases=[]
            for c in range(1,z+1):
                print("Disease number",c,end=' ')
                d=int(input(": "))
                if(d==1):
                    diseases.append("Diabetes")
                elif(d==2):
                    diseases.append("Hypertension")
                elif(d==3):
                    diseases.append("Heart Disease")
                elif(d==4):
                    diseases.append("Lung Disease")
                elif(d==5):
                    diseases.append("Kidney Disorder")
                else:
                    print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
                    error=+1
        elif(z==1):
            d=int(input("Enter Your Disease : "))
            if(d==1):
                diseases="Diabetes"
            elif(d==2):
                diseases="Hypertension"
            elif(d==3):
                diseases="Heart Disease"
            elif(d==4):
                diseases="Lung Disease"
            elif(d==5):
                diseases="Kidney Disorder"
            else:
                print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
                error=+1
        else:
            diseases='None'
    elif(j==2):
        n=n+2
        d=int(input("Enter Your Disease : "))
        if(d==1):
            diseases="Diabetes"
        elif(d==2):
            diseases="Hypertension"
        elif(d==3):
            diseases="Heart Disease"
        elif(d==4):
            diseases="Lung Disease"
        elif(d==5):
            diseases="Kidney Disorder"
        else:
            print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
            error=+1
    else:
        diseases='None'
    t=input("\nHave You Travelled Internationally in the Last 28-45 Days ? (Yes/No)\nAnswer: ")
    if t in ['n','N','no','No','NO']:
        internationallytravelled="No"
    elif t in ['y','Y','yes','Yes','YES']:
        internationallytravelled="Yes"
        n=n+1
    else:
        print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
        error=+1
    i=input("\nHave You Interacted with a Person who has Tested Positive for COVID-19 ? (Yes/No)\nAnswer: ")
    if i in ['n','N','no','No','NO']:
        interactionwithacovidpatient="No"
    elif i in ['y','Y','yes','Yes','YES']:
        interactionwithacovidpatient="Yes"
        n=n+1
    else:
        print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
        error=+1
    w=input("\nAre You a Social Worker ? (Yes/No)\nAnswer: ")
    if w in ['n','N','no','No','NO']:
        socialworker="No"
    elif w in ['y','Y','yes','Yes','YES']:
        socialworker="Yes"
        n=n+1
    else:
        print("INVALID INPUT!!!\nPLEASE RERUN THE TEST")
        error=+1
    if(error==0):
        records=[name,age,gender,symptoms,diseases,internationallytravelled,interactionwithacovidpatient,socialworker]
        EnteringRecord(records)
        print('''###################################################################################################
===================================================================================================
\nYour Self Assessment Result:''')
        if(n<=2):
            print("YOU ARE AT A LOW RISK. PLEASE REMAIN INSIDE YOUR HOUSE AND FOLLOW ALL NORMS OF SOCIAL DISTANCING!!!")
        elif(n>=5):
            print("YOU ARE AT A HIGH RISK. PLEASE SEEK MEDICAL HELP AND TRY TO AVPOID HUMAN CONTACT!!!")
        else:
            print("YOU ARE AT A MILD RISK. PLEASE FOLLOW ALL THE PRECAUTIONS, AVOID CROWDS AND GATHERINGS!!!")
        print('''
===================================================================================================
###################################################################################################
''')
    else:
        print("\nYOUR DATA HAS NOT BEEN SAVED BECAUSE OF AN ERROR FROM YOUR SIDE!!!\nPLEASE RERUN THE TEST")
def DeletingRecord():
    lines=[]
    name=input("\nPlease Enter a Name to be Deleted with its Record : ")
    with open('covid.csv','r') as cov:
        reader=csv.reader(cov)
        for row in reader:
            lines.append(row)
            for field in row:
                if(field==name):
                    lines.remove(row)
                    p=1
    with open('covid.csv','w') as cov:
        writer=csv.writer(cov)
        writer.writerows(lines)
        if(p==1):
            print("\nYOUR RECORD HAS BEEN DELETED FOR THE NAME",name)
        else:
            print("\nTHE ENTERED NAME IS NOT PRESENT")
        
a='r'
while(a=='r'):
    print("This Self Assement Program provides you with the following options:")
    print('''
\t(1)SELF ASSESS YOURSELF
\t(2)ASSESS MULTIPLE PEOPLE
\t(3)DISPLAY ALL RECORDS
\t(4)DELETE A RECORD
\t(5)DELETE MULTIPLE RECORDS
\t(6)EXIT THE PROGRAM
\n''')
    try:
        q=int(input("Please Enter Your Selection: "))
        if q not in [1,2,3,4,5,6,7]:
            print("\nYOU HAVE ENTERED A WRONG VALUE!!!")
            continue
        elif(q==1):
            SelfAssessmentTest()
        elif(q==2):
            m=int(input("\nEnter the Number of Entries You Want : "))
            for y in range(1,m+1):
                print("\nFor Person",y,':')
                SelfAssessmentTest()
        elif(q==3):
            print()
            with open('covid.csv',"r",newline='\r\n') as cov:
                readCSV = csv.reader(cov, delimiter=',')
                for row in readCSV:
                    print(' | '.join(row))
                    print("==========================================================================================================")
        elif(q==4):
            DeletingRecord()
        elif(q==5):
            l=int(input("\nEnter the Number of Records You Want to Delete : "))
            for o in range(1,l+1):
                print("\nFor Person",o,':')
                DeletingRecord()
        elif(q==6):
            print("\nEXITING...  \nTHANK YOU FOR USING THE PROGRAM!!!")
            break
    except TypeError: print("\nWRONG DATA TYPE ENTERED!!!")
    except: print("\nAN ERROR HAS OCCURED!!!")
