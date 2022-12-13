import os
import pickle as pk
from datetime import date,datetime
import random
import json


#4 LINES GAP BTW TWO FUNCTIONS
now = datetime.now()
today = date.today()# datetime object containing current date and time
dt_string=now.strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S
dt_stringLessAccurate=today.strftime("%d/%m/%y")          #dd/mm/YY 



'''
d1= Ealier date
d2= Later date
'''
def GetDiffDate(d1,d2):
     days1=int(d1[:2])+int(d1[3:5])*30+int(d1[6:8])*365
     days2=int(d2[:2])+int(d2[3:5])*30+int(d2[6:8])*365
     return days2-day1



def ConactNoCheck(ContactNo):
     while 1:
          if len(str(ContactNo))!=10:
               print("\nEntered conact number does not exist..")
               print("Contact number must have 10 digits...\n")
               ContactNo=input("Please Enter correct Contact Number:")
               
          else:
               break          
     return ContactNo     



def  AccNameCheck(AccName):
    
    while 1:

        if any(char.isdigit() for char in AccName):
           print("Please Enter a valid name...")
           AccName=input("Enter Account Name:")
           continue
        
        elif any(char in ['!','@','#','$','%','&','*','(',')','-','_','=','+','/','~','`',"\\","|","]","}","[","{","\'","\"",";",":",".",">",",","<","/","?"] for char in AccName ):
            print("Please Enter a valid name...")
            AccName=input("Enter Account Name:")
            continue

        if len(AccName)<4:
            print("Please Enter a valid name...")
            AccName=input("Enter Account Name:")
            continue
        
        elif len(AccName)>20:
            print("Please Enter a valid name...")
            AccName=input("Enter Account Name:")
            continue  
          
        else:
            break
  
    return AccName  
        



def PasswordCheck(password):
    
    while 1:
        
        if len(password)<6:
            print("Entered Password is too short, it must be more than 6 characters...")
            password=input("Create a better password:")
            continue
        
        elif len(password)>20:
            print("Entered Password is too long, it must be less than 20 characters...")
            password=input("Create a better password:")
            continue
        
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least 1 digit...")
            password=input("Create a better password:")
            continue
        
        elif not any(char.islower() for char in password):
            print("Password must contain at least one lowercase character...")
            password=input("Create a better password:")
            continue

        elif not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase character...")
            password=input("Create a better password:")
            continue

        elif not any(char in ['!','@','#','$','%','&','*','(',')','-','_','=','+','/','~','`',"\\","|","]","}","[","{","\'","\"",";",":",".",">",",","<","/","?"] for char in password):
            print("Password must contain at least one special character...")
            password=input("Create a better password:")
            continue

        else:
            print("Password created successfully...")
            break
    return password




def EditProfile(AccType,AccNo):

    print(AccType)
    print(AccNo)
      
    if AccType=='1':
        with open("SavingsAccFile.dat","rb") as infile:
            with open("tempSavingsAccFile.dat","wb")as outfile:
                  try:
                   while 1:    
                    acc=pk.load(infile)
                    if acc['AccNo']==AccNo:
                        while 1:
                            print("""                             Pleaase select what you want to edit:
                                                                     (1)Change password
                                                                     (2)Change Name
                                                                     (3)Change mobile number
                                                                       \n""")
                            Option=input("Enter Option :")
                            
                            if Option=='1':
                                password=input("Enter new password :")
                                password=PasswordCheck(password)
                                print("Confirm password change from",acc['Password'],"to",password,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option :")
                                if Confirmation1 in 'Yy':
                                    print("Password Changing...")
                                    acc['Password']=password
                                    print("Password chaged succesfully..")
                                    with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Password changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Password change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('SavingsAccTransaction.dat')
                                    os.rename('temp.dat','SavingsAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Password change failed...")
                                    with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attemt was ma change password on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('SavingsAccTransaction.dat')
                                    os.rename('temp.dat','SavingsAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            pk.dump(acc,outfile)
                                            print("Account updating...")
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break

                            if Option=='2':
                                name=input("Enter new account name :")
                                print("Confirm account name change from",acc['AccName'],"to",name,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option :")
                                if Confirmation1 in 'Yy':
                                    print("Changing Account name...")
                                    acc['AccName']=name
                                    print("Account name chaged succesfully..")
                                    with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Account name changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Account name change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('SavingsAccTransaction.dat')
                                    os.rename('temp.dat','SavingsAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR  UPDATED ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Account name change failed...")
                                    with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to change the acount name on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('SavingsAccTransaction.dat')
                                    os.rename('temp.dat','SavingsAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            pk.dump(acc,outfile)
                                            print("Account updating...")
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break        
                            if Option=='3':
                                ContactNo=input("enter new contact number:")
                                print("Confirm Contact number change from",acc['ContactNo'],"to",ContactNo,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Contact number...")
                                    acc['ContactNo']=ContactNo
                                    print("Contact number chaged succesfully..")
                                    with open("SavingsAccTransaction.dat","rb") as fin:
                                      with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Contact number changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Contact number change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('SavingsAccTransaction.dat')
                                    os.rename('temp.dat','SavingsAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Contact number changing failed...")
                                    with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to change the contact number on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('SavingsAccTransaction.dat')
                                    os.rename('temp.dat','SavingsAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            pk.dump(acc,outfile)
                                            print("Account updating...")
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break      
                    else:
                        pk.dump(acc,outfile)                    
                  except:
                        print("CHECKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK") #testing
                        pass                      
        os.remove('SavingsAccFile.dat')
        os.rename('tempSavingsAccFile.dat','SavingsAccFile.dat')




    elif AccType=='2':
            
        with open("FDAccFile.dat","rb") as infile:
            with open("tempFDAccFile.dat","wb")as outfile:
                  try:
                   while 1:    
                    acc=pk.load(infile)
                    if acc['AccNo']==AccNo:
                        while 1:
                            print("""                             Pleaase select what you want to edit:
                                                                     (1)Change password
                                                                     (2)Change Name
                                                                     (3)Change mobile number
                                                                       """)
                            Option=input("Enter Option:")
                            
                            if Option=='1':
                                password=input("enter new password:")
                                password=PasswordCheck(password)
                                print("Confirm password change from",acc['Password'],"to",password,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Password Changing...")
                                    acc['Password']=password
                                    print("Password chaged succesfully..")
                                    with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Password changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Password change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('FDAccTransaction.dat')
                                    os.rename('temp.dat','FDAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Password change failed...")
                                    with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt to change password was made on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('FDAccTransaction.dat')
                                    os.rename('temp.dat','FDAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break

                            if Option=='2':
                                name=input("enter new account name:")
                                print("Confirm account name change from",acc['AccName'],"to",name,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Account name...")
                                    acc['AccName']=name
                                    print("Account name chaged succesfully..")
                                    with open("FDTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Account name changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Account name change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('FDAccTransaction.dat')
                                    os.rename('temp.dat','FDAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR  UPDATED ACCOUNT INFO:")
                                            c
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Account name change failed...")
                                    with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to change the account number on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('FDAccTransaction.dat')
                                    os.rename('temp.dat','FDAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break        
                            if Option=='3':
                                ContactNo=input("enter new contact number:")
                                print("Confirm Contact number change from",acc['ContactNo'],"to",ContactNo,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Contact number...")
                                    ContactNo=acc['ContactNo']
                                    print("Contact number chaged succesfully..")
                                    with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Contact number changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Contact number change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('FDAccTransaction.dat')
                                    os.rename('temp.dat','FDAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Contact number changing failed...")
                                    with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt to change the contact number was made on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('FDAccTransaction.dat')
                                    os.rename('temp.dat','FDAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break      
                    else:
                        pk.dump(acc,outfile)                    
                  except:
                        pass                      
        os.remove('FDAccFile.dat')
        os.rename('tempFDAccFile.dat','FDAccFile.dat')



    elif AccType=='3':
        with open("RDAccFile.dat","rb") as infile:
            with open("tempRDAccFile.dat","wb")as outfile:
                  try:
                   while 1:    
                    acc=pk.load(infile)
                    if acc['AccNo']==AccNo:
                        while 1:
                            print("""                             Pleaase select what you want to edit:
                                                                     (1)Change password
                                                                     (2)Change Name
                                                                     (3)Change mobile number
                                                                       """)
                            Option=input("Enter Option:")
                            
                            if Option=='1':
                                password=input("enter new password:")
                                password=PasswordCheck(password)
                                print("Confirm password change from",acc['Password'],"to",password,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Password Changing...")
                                    acc['Password']=password
                                    print("Password chaged succesfully..")
                                    with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Password changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Password change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('RDAccTransaction.dat')
                                    os.rename('temp.dat','RDAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Password change failed...")
                                    with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt to change password was made on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('RDAccTransaction.dat')
                                    os.rename('temp.dat','RDAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break

                            if Option=='2':
                                name=input("enter new account name:")
                                print("Confirm account name change from",acc['AccName'],"to",name,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Account name...")
                                    acc['AccName']=name
                                    print("Account name chaged succesfully..")
                                    with open("RDTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Account name changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Account name change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('RDAccTransaction.dat')
                                    os.rename('temp.dat','RDAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR  UPDATED ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Account name change failed...")
                                    with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to change the account number on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('RDAccTransaction.dat')
                                    os.rename('temp.dat','RDAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break        
                            if Option=='3':
                                ContactNo=input("enter new contact number:")
                                print("Confirm Contact number change from",acc['ContactNo'],"to",ContactNo,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Contact number...")
                                    ContactNo=acc['ContactNo']
                                    print("Contact number chaged succesfully..")
                                    with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Contact number changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Contact number change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('RDAccTransaction.dat')
                                    os.rename('temp.dat','RDAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Contact number changing failed...")
                                    with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt to change the contact number was made on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('RDAccTransaction.dat')
                                    os.rename('temp.dat','RDAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break      
                    else:
                        pk.dump(acc,outfile)                    
                  except:
                        pass                      
        os.remove('RDAccFile.dat')
        os.rename('tempRDAccFile.dat','RDAccFile.dat')



    elif AccType=='4':
        with open("CurrentAccFile.dat","rb") as infile:
            with open("tempCurrentAccFile.dat","wb")as outfile:
                  try:
                   while 1:    
                    acc=pk.load(infile)
                    if acc['AccNo']==AccNo:
                        while 1:
                            print("""                             Pleaase select what you want to edit:
                                                                     (1)Change password
                                                                     (2)Change Name
                                                                     (3)Change mobile number
                                                                       """)
                            Option=input("Enter Option:")
                            
                            if Option=='1':
                                password=input("enter new password:")
                                password=PasswordCheck(password)
                                print("Confirm password change from",acc['Password'],"to",password,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Password Changing...")
                                    acc['Password']=password
                                    print("Password chaged succesfully..")
                                    with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Password changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Password change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('CurrentAccTransaction.dat')
                                    os.rename('temp.dat','CurrentAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Password change failed...")
                                    with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt to change password was made on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('CurrentAccTransaction.dat')
                                    os.rename('temp.dat','CurrentAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break

                            if Option=='2':
                                name=input("enter new account name:")
                                print("Confirm account name change from",acc['AccName'],"to",name,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Account name...")
                                    acc['AccName']=name
                                    print("Account name chaged succesfully..")
                                    with open("CurrentTransaction.dat","rb") as fin:
                                      with open("temp.dat","wb")as fout:
                                         try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Account name changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Account name change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                         except:
                                             pass
                                    os.remove('CurrentAccTransaction.dat')
                                    os.rename('temp.dat','CurrentAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR  UPDATED ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Account name change failed...")
                                    with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to change the account number on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('CurrentAccTransaction.dat')
                                    os.rename('temp.dat','CurrentAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break        
                            if Option=='3':
                                ContactNo=input("enter new contact number:")
                                print("Confirm Contact number change from",acc['ContactNo'],"to",ContactNo,"?")
                                print("Enter Y/y to confirm changes or anything else to exit")
                                Confirmation1=input("Enter option:")
                                if Confirmation1 in 'Yy':
                                    print("Changing Contact number...")
                                    ContactNo=acc['ContactNo']
                                    print("Contact number chaged succesfully..")
                                    with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Contact number changed on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Contact number change recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('CurrentAccTransaction.dat')
                                    os.rename('temp.dat','CurrentAccTransaction.dat')
                                    print("Do you wanat to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Account updating...")
                                            pk.dump(acc,outfile)
                                            print("Account updated successfully...")
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break
                                else:
                                    print("Contact number changing failed...")
                                    with open("CurrentAccTransaction.dat","rb") as fin:
                                      with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt to change the contact number was made on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                    os.remove('CurrentAccTransaction.dat')
                                    os.rename('temp.dat','CurrentAccTransaction.dat')
                                    print("Do you want to edit more?")
                                    print("Enter Y/y to confirm changes or anything else to exit")
                                    Confirmation2=input("Enter option:")
                                    if Confirmation2 in 'Yy':
                                            continue
                                    else:
                                            print("YOUR ACCOUNT INFO:")
                                            print(json.dumps(acc,indent=2))
                                            print("Exiting to main menu...")
                                            for i in range(4): print()
                                            print("********************************************************************************************************************************************************************")
                                            break      
                    else:
                        pk.dump(acc,outfile)                    
                  except:
                        pass                      
        os.remove('CurrentAccFile.dat')
        os.rename('tempCurrentAccFile.dat','CurrentAccFile.dat')

    
def CheckBalance(AccType,AccNo):
    
    if AccType=='1':
        with open("SavingsAccFile.dat","rb") as fin:
            while 1:
                acc=pk.load(fin)
                if acc['AccNo']==AccNo:
                    print("The balance remaining in the account: $",acc['CurrentAmount'],"\n",sep="")
                    print("Returning to main menu...")
                    for i in range(4): print()
                    print("********************************************************************************************************************************************************************")
                    break
                    
    if AccType=='2':
        with open("FDAccFile.dat","rb") as fin:
            while 1:
                acc=pk.load(fin)
                if acc['AccNo']==AccNo:
                    print("The balance remaining in the account: $",acc['CurrentAmount'],"\n",sep="")
                    print("Returning to main menu...")
                    for i in range(4): print()
                    print("********************************************************************************************************************************************************************")
                    break

    if AccType=='3':
        with open("RDAccFile.dat","rb") as fin:
            while 1:
                acc=pk.load(fin)
                if acc['AccNo']==AccNo:
                    print("The balance remaining in the account: $",acc['CurrentAmount'],"\n",sep="")
                    print("Returning to main menu...")
                    for i in range(4): print()
                    print("********************************************************************************************************************************************************************")
                    break

    if AccType=='4':
        with open("CurrentAccFile.dat","rb") as fin:
            while 1:
                acc=pk.load(fin)
                if acc['AccNo']==AccNo:
                    print("The balance remaining in the account: $",acc['CurrentAmount'],"\n",sep="")
                    print("Returning to main menu...")
                    for i in range(4): print()
                    print("********************************************************************************************************************************************************************")
                    break






def ViewTransactionHistory(AccType,AccNo):

    if  AccType=='1':
        with open("SavingsAccTransaction.dat","rb") as fin:
          try:   
            while 1:
                acc=pk.load(fin)
                if acc[0]==AccNo:
                    print("\n\nTRANSACTION HISTORY\n")
                    for EachTransaction in acc:
                        print(EachTransaction)
          except:              
            print("Returning to main menu...")
            for i in range(4): print()
            print("********************************************************************************************************************************************************************")

            
    elif  AccType=='2':
        print(AccNo) #testing
        with open("FDAccTransaction.dat","rb") as fin:
          try:   
            while 1:
                acc=pk.load(fin)
                if acc[0]==AccNo:
                    print("\n\nTRANSACTION HISTORY\n")
                    for EachTransaction in acc:
                        print(EachTransaction)
          except:              
            print("Returning to main menu...")
            for i in range(4): print()
            print("********************************************************************************************************************************************************************")

    elif  AccType=='3':
        with open("RDAccTransaction.dat","rb") as fin:
          try:   
            while 1:
                acc=pk.load(fin)
                if acc[0]==AccNo:
                    print("\n\nTRANSACTION HISTORY\n")
                    for EachTransaction in acc:
                        print(EachTransaction)
          except:              
            print("Returning to main menu...")
            for i in range(4): print()
            print("********************************************************************************************************************************************************************")

            
    elif  AccType=='4':
        with open("CurrentAccTransaction.dat","rb") as fin:
          try:   
            while 1:
                acc=pk.load(fin)
                if acc[0]==AccNo:
                    print("\n\nTRANSACTION HISTORY\n")
                    for EachTransaction in acc:
                        print(EachTransaction)
          except:              
            print("Returning to main menu...")
            for i in range(4): print()
            print("********************************************************************************************************************************************************************")





    
def PerformTransaction(AccType,AccNo):
    if AccType=='1':
        with open("SavingsAccFile.dat","rb") as infile:
            with open("temp1.dat","wb")as outfile:
                while True:
                  try:  
                     acc=pk.load(infile)
                     if acc['AccNo']==AccNo:
                         
                         print("""                                    You can make the following operations:

                                                            (1)make a deposite
                                                            (2)make a withdrawal
                                            You can only make a limited transaction on the same day\n\n""")
                         Option=input("Entered option :")
                         if Option=='1':
                             Deposite=int(input("\nEnter the amount you want to deposite :"))
                             print("Amount Depositing...")
                             acc['CurrentAmount']=acc['CurrentAmount']+Deposite
                             print("YOUR ACCOUNT INFO")
                             print(json.dumps(acc,indent=2))
                             print("Do you want to confirm the changes?(Y/N)")
                             Confirmation=input("Entered option :")
                             if Confirmation in 'Yy':
                                 print("Amount depositing...")
                                 pk.dump(acc,outfile)
                                 print("Ammount deposited succesfully...")
                                 with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been deposited on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass            
                                 os.remove('SavingsAccTransaction.dat')
                                 os.rename('temp2.dat','SavingsAccTransaction.dat')
                                 print("Entering back to main menu...")
                                 
                             else:
                                 acc['CurrentAmount']=acc['CurrentAmount']-Deposite
                                 print("Amount depostion failed...")
                                 with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been  attempted to be deposited on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                 os.remove('SavingsAccTransaction.dat')
                                 os.rename('temp2.dat','SavingsAccTransaction.dat')
                                 print("Entering back to main menu...")

                             
                         if Option=='2':
                             Withdrawal=int(input("\nEnter the ammount you want to withdraw :"))
                             if Withdrawal<acc['CurrentAmount']:
                                 print("Amount withdrawing...")
                                 acc['CurrentAmount']=acc['CurrentAmount']-Withdrawal
                                 print("YOUR ACCOUNT INFO")
                                 print(json.dumps(acc,indent=2))
                                 print("Do you want to confirm the changes?(Y/N)")
                                 Confirmation=input("Entered option :")
                                 if Confirmation in 'Yy':
                                     print("Amount withdrawing...")
                                     pk.dump(acc,outfile)
                                     print("Ammount withdrawn succesfully...")
                                     with open("SavingsAccTransaction.dat","rb") as fin:
                                       with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been withdrawn on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass
                                     os.remove('SavingsAccTransaction.dat')
                                     os.rename('temp.dat','SavingsAccTransaction.dat')      
                                     print("Entering into main menu...")
                                     
                                 else:
                                     acc['CurrentAmount']=acc['CurrentAmount']+Withdrawal
                                     print("Amount withdrawal failed...")
                                     with open("SavingsAccTransaction.dat","rb") as fin:
                                         with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               break           
                                     os.remove('SavingsAccTransaction.dat')
                                     os.rename('temp.dat','SavingsAccTransaction.dat')
                                     print("Entering back to main menu...")
                             else:
                                 print("Transaction not possible as account balance is maxed out...")
                                 with open("SavingsAccTransaction.dat","rb") as fin:
                                         with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               pass          
                                 os.remove('SavingsAccTransaction.dat')
                                 os.rename('temp.dat','SavingsAccTransaction.dat')
                                 print("Entering into main menu...")
                   
                     else:
                        pk.dump(acc,outfile)
                         
                  except:
                       break
        os.remove('SavingsAccFile.dat')
        os.rename('temp1.dat','SavingsAccFile.dat')


    if AccType=='2':
        with open("FDAccFile.dat","rb") as infile:
            with open("temp1.dat","wb")as outfile:
                while True:
                  try:  
                     acc=pk.load(infile)
                     if acc['AccNo']==AccNo:
                         
                         print("""                              You can make the following operations:

                                                            (1)make a deposite
                                                            (2)make a withdrawal
                                            But making a withdrawal that is on a date befoer the agreed period of time
                                            would almost nullify the interest rates.A withdrawal from fixed deposited
                                            is suggested to be only be made if absolutely neccesary .""")
                         Option=input("Entered option :")
                         if Option=='1':
                             Deposite=int(input("\nEnter the amount you want to deposite :"))
                             print("Amount Depositing...")
                             acc['CurrentAmount']=acc['CurrentAmount']+Deposite
                             print("YOUR ACCOUNT INFO")
                             print(json.dumps(acc,indent=2))
                             print("Do you want to confirm the changes?(Y/N)")
                             Confirmation=input("Entered option :")
                             if Confirmation in 'Yy':
                                 print("Amount depositing...")
                                 pk.dump(acc,outfile)
                                 print("Ammount deposited succesfully...")
                                 with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been deposited on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass             
                                 os.remove('FDAccTransaction.dat')
                                 os.rename('temp2.dat','FDAccTransaction.dat')
                                 print("Entering back to main menu...")
                                 
                             else:
                                 acc['CurrentAmount']=acc['CurrentAmount']-Deposite
                                 print("Amount depostion failed...")
                                 with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been  attempted to be deposited on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                 os.remove('FDAccTransaction.dat')
                                 os.rename('temp2.dat','FDAccTransaction.dat')
                                 print("Entering back to main menu...")

                             
                         if Option=='2':
                             DurationInDays=GetDiffDate(acc['SimplifiedDate'],dt_stringLessAccurate)
                             DurationInMonths=DurationInDays//30
                             if acc['AgreedDuration']< DurationInMonths: 
                                 Withdrawal=int(input("\nEnter the ammount you want to withdraw :"))
                                 if Withdrawal<acc['CurrentAmount']:
                                     print("Amount withdrawing...")
                                     acc['CurrentAmount']=acc['CurrentAmount']-Withdrawal
                                     print("YOUR ACCOUNT INFO")
                                     print(json.dumps(acc,indent=2))
                                     print("Do you want to confirm the changes?(Y/N)")
                                     Confirmation=input("Entered option :")
                                     if Confirmation in 'Yy':
                                         print("Amount withdrawing...")
                                         pk.dump(acc,outfile)
                                         print("Ammount withdrawn succesfully...")
                                         with open("FDAccTransaction.dat","rb") as fin:
                                           with open("temp2.dat","wb")as fout:
                                            try: 
                                                 while 1:
                                                     AccTransaction=pk.load(fin)
                                                     if AccTransaction[0]==AccNo:
                                                         TransactionOccuredNow="$"+str(Withdrawal)+" has been withdrawn on "+str(dt_string)
                                                         AccTransaction.append(TransactionOccuredNow)
                                                         print("Transaction recorded...")
                                                         pk.dump(AccTransaction,fout)
                                                     else:
                                                         pk.dump(AccTransaction,fout)
                                            except:
                                                  pass
                                         os.remove('FDAccTransaction.dat')
                                         os.rename('temp.dat','FDTransaction.dat')      
                                         print("Entering back to main menu...")
                                         
                                     else:
                                         acc['CurrentAmount']=acc['CurrentAmount']+Withdrawal
                                         print("Amount withdrawal failed...")
                                         with open("FDAccTransaction.dat","rb") as fin:
                                             with open("temp2.dat","wb")as fout:
                                                try: 
                                                   while 1:
                                                     AccTransaction=pk.load(fin)
                                                     if AccTransaction[0]==AccNo:
                                                         TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                         AccTransaction.append(TransactionOccuredNow)
                                                         print("Transaction recorded...")
                                                         pk.dump(AccTransaction,fout)
                                                     else:
                                                         pk.dump(AccTransaction,fout)
                                                except:
                                                   pass           
                                         os.remove('FDAccTransaction.dat')
                                         os.rename('temp.dat','FDAccTransaction.dat')
                                         print("Entering back to main menu...")
                                 else:
                                     print("Transaction not possible as account balance is maxed out...")
                                     with open("FDAccTransaction.dat","rb") as fin:
                                         with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               pass           
                                     os.remove('FDAccTransaction.dat')
                                     os.rename('temp.dat','FDAccTransaction.dat')
                                     print("Entering into main menu...")
                             
                             else:
                                 print("The agreead duration was ",acc['AgreedDuration']," so a withdrawal at ",DurationInMonths," is not advised")
                                 print("The intresest promised will be nullified")
                                 print("Do you wish to proceed with the withdrawal?(Y/n")
                                 Option=input("Enter option :")
                                 if Option in 'Yy':
                                     Withdrawal=int(input("\nEnter the ammount you want to withdraw :"))
                                     if Withdrawal<acc['CurrentAmount']:
                                         print("Amount withdrawing...")
                                         acc['CurrentAmount']=acc['CurrentAmount']-Withdrawal
                                         print("YOUR ACCOUNT INFO")
                                         print(json.dumps(acc,indent=2))
                                         print("Do you want to confirm the changes?(Y/N)")
                                         Confirmation=input("Entered option :")
                                         if Confirmation in 'Yy':
                                             print("Amount withdrawing...")
                                             pk.dump(acc,outfile)
                                             print("Ammount withdrawn succesfully...")
                                             with open("SavingsAccTransaction.dat","rb") as fin:
                                               with open("temp2.dat","wb")as fout:
                                                try: 
                                                     while 1:
                                                         AccTransaction=pk.load(fin)
                                                         if AccTransaction[0]==AccNo:
                                                             TransactionOccuredNow="$"+str(Withdrawal)+" has been withdrawn on "+str(dt_string)
                                                             AccTransaction.append(TransactionOccuredNow)
                                                             print("Transaction recorded...")
                                                             pk.dump(AccTransaction,fout)
                                                         else:
                                                             pk.dump(AccTransaction,fout)
                                                except:
                                                      pass
                                             os.remove('SavingsAccTransaction.dat')
                                             os.rename('temp.dat','SavingsAccTransaction.dat')      
                                             print("Entering back to main menu...")
                                         
                                         else:
                                             acc['CurrentAmount']=acc['CurrentAmount']+Withdrawal
                                             print("Amount withdrawal failed...")
                                             with open("SavingsAccTransaction.dat","rb") as fin:
                                                 with open("temp2.dat","wb")as fout:
                                                    try: 
                                                       while 1:
                                                         AccTransaction=pk.load(fin)
                                                         if AccTransaction[0]==AccNo:
                                                             TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                             AccTransaction.append(TransactionOccuredNow)
                                                             print("Transaction recorded...")
                                                             pk.dump(AccTransaction,fout)
                                                         else:
                                                             pk.dump(AccTransaction,fout)
                                                    except:
                                                       pass           
                                             os.remove('SavingsAccTransaction.dat')
                                             os.rename('temp.dat','SavingsAccTransaction.dat')
                                             print("Entering back to main menu...")
                                     else:
                                         print("Transaction not possible as account balance is maxed out...")
                                         with open("SavingsAccTransaction.dat","rb") as fin:
                                             with open("temp2.dat","wb")as fout:
                                                try: 
                                                   while 1:
                                                     AccTransaction=pk.load(fin)
                                                     if AccTransaction[0]==AccNo:
                                                         TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                         AccTransaction.append(TransactionOccuredNow)
                                                         print("Transaction recorded...")
                                                         pk.dump(AccTransaction,fout)
                                                     else:
                                                         pk.dump(AccTransaction,fout)
                                                except:
                                                   pass           
                                         os.remove('SavingsAccTransaction.dat')
                                         os.rename('temp.dat','SavingsAccTransaction.dat')
                                         print("Entering into main menu...")
                                     
                                 else:
                                     print("Amount withdrawal failed...")
                                     print("Exiting to main menu")
                            
                     else:
                        pk.dump(acc,outfile)
                         
                  except:
                       break
        os.remove('SavingsAccFile.dat')
        os.rename('temp1.dat','SavingsAccFile.dat')
    if AccType=='3':
        with open("RDAccFile.dat","rb") as infile:
            with open("temp1.dat","wb")as outfile:
                while True:
                  try:  
                     acc=pk.load(infile)
                     if acc['AccNo']==AccNo:
                         
                         print("""                   You can make the following operations:
                                                            (1)make a deposite
                                                            (2)make a withdrawal
                                            You can only make a limited transaction on the same day\n\n""")
                         Option=input("Entered option :")
                         if Option=='1':
                             Deposite=int(input("\nEnter the amount you want to deposite :"))
                             print("Amount Depositing...")
                             acc['CurrentAmount']=acc['CurrentAmount']+Deposite
                             print("YOUR ACCOUNT INFO")
                             print(json.dumps(acc,indent=2))
                             print("Do you want to confirm the changes?(Y/N)")
                             Confirmation=input("Entered option :")
                             if Confirmation in 'Yy':
                                 print("Amount depositing...")
                                 pk.dump(acc,outfile)
                                 print("Ammount deposited succesfully...")
                                 with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been deposited on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass             
                                 os.remove('RDAccTransaction.dat')
                                 os.rename('temp2.dat','RDAccTransaction.dat')
                                 print("Entering back to main menu...")
                                 
                             else:
                                 acc['CurrentAmount']=acc['CurrentAmount']-Deposite
                                 print("Amount depostion failed...")
                                 with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been  attempted to be deposited on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                 os.remove('RDAccTransaction.dat')
                                 os.rename('temp2.dat','RDAccTransaction.dat')
                                 print("Entering back to main menu...")

                             
                         if Option=='2':
                             Withdrawal=int(input("\nEnter the ammount you want to withdraw :"))
                             if Withdrawal<acc['CurrentAmount']:
                                 print("Amount withdrawing...")
                                 acc['CurrentAmount']=acc['CurrentAmount']-Withdrawal
                                 print("YOUR ACCOUNT INFO")
                                 print(json.dumps(acc,indent=2))
                                 print("Do you want to confirm the changes?(Y/N)")
                                 Confirmation=input("Entered option :")
                                 if Confirmation in 'Yy':
                                     print("Amount withdrawing...")
                                     pk.dump(acc,outfile)
                                     print("Ammount withdrawn succesfully...")
                                     with open("RDAccTransaction.dat","rb") as fin:
                                       with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been withdrawn on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass
                                     os.remove('RDAccTransaction.dat')
                                     os.rename('temp.dat','RDAccTransaction.dat')      
                                     print("Entering back to main menu...")
                                     
                                 else:
                                     acc['CurrentAmount']=acc['CurrentAmount']+Withdrawal
                                     print("Amount withdrawal failed...")
                                     with open("RDTransaction.dat","rb") as fin:
                                         with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               pass           
                                     os.remove('RDAccTransaction.dat')
                                     os.rename('temp.dat','RDAccTransaction.dat')
                                     print("Entering back to main menu...")
                             else:
                                 print("Transaction not possible as account balance is maxed out...")
                                 with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               pass           
                                 os.remove('SavingsAccTransaction.dat')
                                 os.rename('temp.dat','SavingsAccTransaction.dat')
                                 print("Entering into main menu...")
                   
                     else:
                        pk.dump(acc,outfile)
                         
                  except:
                       break
        os.remove('RDAccFile.dat')
        os.rename('temp1.dat','RDAccFile.dat')


    if AccType=='4':
        with open("CurrentAccFile.dat","rb") as infile:
            with open("temp1.dat","wb")as outfile:
                while True:
                  try:  
                     acc=pk.load(infile)
                     if acc['AccNo']==AccNo:
                         
                         print("""                   You can make the following operations:
                                                            (1)make a deposite
                                                            (2)make a withdrawal
                                            You can make a unlimited transaction on the same day\n\n""")
                         Option=input("Entered option :")
                         if Option=='1':
                             Deposite=int(input("\nEnter the amount you want to deposite :"))
                             print("Amount Depositing...")
                             acc['CurrentAmount']=acc['CurrentAmount']+Deposite
                             print("YOUR ACCOUNT INFO")
                             print(json.dumps(acc,indent=2))
                             print("Do you want to confirm the changes?(Y/N)")
                             Confirmation=input("Entered option :")
                             if Confirmation in 'Yy':
                                 print("Amount depositing...")
                                 pk.dump(acc,outfile)
                                 print("Ammount deposited succesfully...")
                                 with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been deposited on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass             
                                 os.remove('CurrentAccTransaction.dat')
                                 os.rename('temp2.dat','CurrentAccTransaction.dat')
                                 print("Entering back to main menu...")
                                 
                             else:
                                 acc['CurrentAmount']=acc['CurrentAmount']-Deposite
                                 print("Amount depostion failed...")
                                 with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Deposite)+" has been  attempted to be deposited on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                                 os.remove('CurrentAccTransaction.dat')
                                 os.rename('temp2.dat','CurrentAccTransaction.dat')
                                 print("Entering back to main menu...")

                             
                         if Option=='2':
                             Withdrawal=int(input("\nEnter the ammount you want to withdraw :"))
                             if Withdrawal<acc['CurrentAmount']:
                                 print("Amount withdrawing...")
                                 acc['CurrentAmount']=acc['CurrentAmount']-Withdrawal
                                 print("YOUR ACCOUNT INFO")
                                 print(json.dumps(acc,indent=2))
                                 print("Do you want to confirm the changes?(Y/N)")
                                 Confirmation=input("Entered option :")
                                 if Confirmation in 'Yy':
                                     print("Amount withdrawing...")
                                     pk.dump(acc,outfile)
                                     print("Ammount withdrawn succesfully...")
                                     with open("CurrentAccTransaction.dat","rb") as fin:
                                       with open("temp2.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been withdrawn on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                              pass
                                     os.remove('CurrentAccTransaction.dat')
                                     os.rename('temp.dat','CurrentAccTransaction.dat')
                                     print("Entering back to main menu...")
                                            
                                 else:
                                     acc['CurrentAmount']=acc['CurrentAmount']+Withdrawal
                                     print("Amount withdrawal failed...")
                                     with open("CurrentAccTransaction.dat","rb") as fin:
                                         with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               pass           
                                     os.remove('CurrentAccTransaction.dat')
                                     os.rename('temp.dat','CurrentAccTransaction.dat')
                                     print("Entering back to main menu...")
                             else:
                                 print("Transaction not possible as account balance is maxed out...")
                                 with open("SavingsAccTransaction.dat","rb") as fin:
                                         with open("temp2.dat","wb")as fout:
                                            try: 
                                               while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="$"+str(Withdrawal)+" has been  attempted to be withdrawn on "+str(dt_string)+" but failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Transaction recorded...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                            except:
                                               pass           
                                 os.remove('SavingsAccTransaction.dat')
                                 os.rename('temp.dat','SavingsAccTransaction.dat')
                                 print("Entering into main menu...")
                   
                     else:
                        pk.dump(acc,outfile)
                         
                  except:
                       break
        os.remove('CurrentAccFile.dat')
        os.rename('temp1.dat','CurrentAccFile.dat')

    



 

def UserProfile(AccType,AccNo):
    
    #testing if there is any problem with the parameters recieved
    print("AccNo: ",AccNo)
    print("AccType: ",AccType)
    
    if AccType=='1':
        file=open("SavingsAccFile.dat","rb")
        while True:
                acc=pk.load(file)
                if acc['AccNo']==AccNo:
                    print("YOUR ACCOUNT INFO:")
                    print(json.dumps(acc,indent=2)) 
                    print("""                               Please enter the key to perform the corresponding action:

                                                        (1)Edit Profile
                                                        (2)Check Balance
                                                        (3)Perform Transaction
                                                        (4)View Transaction History
                                                        (5)Log Out\n\n""")
                    choice=input("Enter Option :")
                    if choice in '1':
                        file.close() 
                        EditProfile(AccType,AccNo)
                        break
                    elif choice in '2':
                        file.close()
                        CheckBalance(AccType,AccNo)
                        break
                    elif choice in '3':
                        file.close()
                        PerformTransaction(AccType,AccNo)
                        break
                    elif choice in '4':
                        file.close()  
                        ViewTransactionHistory(AccType,AccNo)
                        break
                    elif choice in '5':
                        file.close()
                        print("Logging out...")
                        print("Returning to main menu...")
                        for i in range(4): print()
                        print("********************************************************************************************************************************************************************")
                        break


    if AccType=='2':
            file= open("FDAccFile.dat","rb")
            while True:
                acc=pk.load(file)
                if acc['AccNo']==AccNo:
                    print("YOUR ACCOUNT INFO:")
                    print(json.dumps(acc,indent=2)) 
                    print("""                               Please enter the key to perform the corresponding action:

                                                        (1)Edit Profile
                                                        (2)Check Balance
                                                        (3)Perform Transaction
                                                        (4)View Transaction History
                                                        (5)Log Out\n\n""")
                    choice=input("Enter Option :")
                    if choice in '1':
                        file.close() 
                        EditProfile(AccType,AccNo)
                        break
                    elif choice in '2':
                        file.close() 
                        CheckBalance(AccType,AccNo)
                        break
                    elif choice in '3':
                        PerformTransaction(AccType,AccNo)
                        break
                    elif choice in '4':
                        file.close() 
                        ViewTransactionHistory(AccType,AccNo)
                        break
                    elif choice in '5':
                        file.close() 
                        print("Logging out...")
                        print("Returning to main menu...")
                        break
                    
                    
    if AccType=='3':
            file=open("RDAccFile.dat","rb")
            while True:
                acc=pk.load(file)
                if acc['AccNo']==AccNo:
                    print("YOUR ACCOUNT INFO:")
                    print(json.dumps(acc,indent=2)) 
                    print("""                               Please enter the key to perform the corresponding action:

                                                        (1)Edit Profile
                                                        (2)Check Balance
                                                        (3)Perform Transaction
                                                        (4)View Transaction History
                                                        (5)Log Out\n\n""")
                    choice=input("Enter Option :")
                    if choice in '1':
                        file.close() 
                        EditProfile(AccType,AccNo)
                        break
                    elif choice in '2':
                        file.close() 
                        CheckBalance(AccType,AccNo)
                        break
                    elif choice in '3':
                        file.close() 
                        PerformTransaction(AccType,AccNo)
                        break
                    elif choice in '4':
                        file.close() 
                        ViewTransactionHistory(AccType,AccNo)
                        break
                    elif choice in '5':
                        file.close()
                        print("Logging out...")
                        print("Returning to main menu...")
                        break
                 
    if AccType=='4':
            file=open("CurrentAccFile.dat","rb")
            while True:
                acc=pk.load(file)
                if acc['AccNo']==AccNo:
                    print("YOUR ACCOUNT INFO:")
                    print(json.dumps(acc,indent=2)) 
                    print("""                               Please enter the key to perform the corresponding action:

                                                        (1)Edit Profile
                                                        (2)Check Balance
                                                        (3)Perform Transaction
                                                        (4)View Transaction History
                                                        (5)Log Out\n\n""")
                    choice=input("Enter Option :")
                    if choice in '1':
                        file.close() 
                        EditProfile(AccType,AccNo)
                        break
                    elif choice in '2':
                        file.close() 
                        CheckBalance(AccType,AccNo)
                        break
                    elif choice in '3':
                        file.close() 
                        PerformTransaction(AccType,AccNo)
                        break
                    elif choice in '4':
                        file.close()
                        ViewTransactionHistory(AccType,AccNo)
                        break
                    elif choice in '5':
                        file.close()  
                        print("Logging out...")
                        print("Returning to main menu...")
                        break                   



def LoginProfile():
    
    print("""
                                                         Enter the type of your bank account:
                                                         
                                                                   (1)Savings Account
                                                                   (2)Fixed Deposite account
                                                                   (3)Recurring Deposite account
                                                                   (4)Current Account
           \n\n""")
    Option=input("Enter option:")                                                           
    if Option=='1':
        print("Entering into Savings Accounts Database...")
        AccNo=int(input("Enter your Account number: "))
        print("Searching for the account ...")
        filein=open('SavingsAccFile.dat','rb')
        try:
                while True:
                    acc=pk.load(filein)
                    if acc['AccNo']==AccNo:
                        print("Account found..!")
                        password=input("Enter password :")
                        if password==acc['Password']:
                            print("Logging into ur account...")
                            with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Logged onto the bank account on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('SavingsAccTransaction.dat')
                            os.rename('temp.dat','SavingsAccTransaction.dat')
                            filein.close()
                            UserProfile(Option,acc['AccNo'])
                            break
                        else:
                            print("Wrong Password...")
                            print("Account Login Denied...")
                            with open("SavingsAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to login to the bank account on "+str(dt_string)+" but login failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('SavingsAccTransaction.dat')
                            os.rename('temp.dat','SavingsAccTransaction.dat')
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")
                            filein.close()
                            break
                         
        except EOFError:
                filein.close()
                print("Account does not exist...")
                print("Do you wish to create an account?")
                choice=input("Enter (y/n): ")
                if choice in 'Yy':
                            CreateSavingsAcc()
                else:
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")

                           
    elif Option=='2':
        print("Entering into Fixed Deposit Accounts Database...")
        AccNo=int(input("Enter your Account number: "))
        print("Searching for the account info...")
        filein=open('FDAccFile.dat','rb')
        try:
                while True:
                    acc=pk.load(filein)
                    if acc['AccNo']==AccNo:
                        print("Account found..!")
                        password=input("Enter password :")
                        if password==acc['Password']:
                            print("Logging into ur account...")
                            with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Logged onto the bank account on ", str(dt_stringLess)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('FDAccTransaction.dat')
                            os.rename('temp.dat','FDAccTransaction.dat')
                            filein.close()
                            UserProfile(Option,acc['AccNo'])
                            break   
                        else:
                            print("Wrong Password...")
                            print("Account Login Denied...")
                            with open("FDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to login to the bank account on "+str(dt_stringLess)+" but login failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('FDAccTransaction.dat')
                            os.rename('temp.dat','FDAccTransaction.dat')
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")
                            filein.close()
                            break
        except EOFError:
                    filein.close()
                    print("Account does not exist...")
                    print("Do you wish to create an account?")
                    choice=input("Enter (y/n): ")
                    if choice in 'Yy':
                            CreateFDAcc()
                    else:
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")


    elif Option=='3':
        print("Entering into Recurring Deposit Accounts Database...")
        AccNo=int(input("Enter your Account number: "))
        print("Searching for the account info...")
        filein=open('RDAccFile.dat','rb')
        try:
                while True:
                    acc=pk.load(filein)
                    if acc['AccNo']==AccNo:
                        print("Account found..!")
                        password=input("Enter password :")
                        if password==acc['Password']:
                            print("Logging into ur account...")
                            with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Logged onto the bank account on "+str(dt_stringLessAccurate)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('RDAccTransaction.dat')
                            os.rename('temp.dat','RDAccTransaction.dat')
                            filein.close()
                            UserProfile(Option,acc['AccNo'])
                            break
                        else:
                            print("Wrong Password...")
                            print("Account Login Denied...")
                            with open("RDAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to login to the bank account on "+str(dt_stringLessAccurate)+" but login failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('RDAccTransaction.dat')
                            os.rename('temp.dat','RDAccTransaction.dat')
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")
                            filein.close()
                            break
        except EOFError:
                    filein.close()
                    print("Account does not exist...")
                    print("Do you wish to create an account?")
                    choice=input("Enter (y/n): ")
                    if choice in 'Yy':
                            CreateRDAcc()
                    else:
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")
            
    


    elif Option=='4':
         
        print("Entering into Current Deposit Accounts Database...")
        AccNo=int(input("Enter your Account number: "))
        print("Searching for the account info...")
        filein=open('CurrentAccFile.dat','rb')
        try:
                while True:
                    acc=pk.load(filein)
                    if acc['AccNo']==AccNo:
                        print("Account found..!")
                        password=input("Enter password :")
                        if password==acc['Password']:
                            print("Logging into ur account...")
                            with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="Logged onto the bank account on "+str(dt_string)
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('CurrentAccTransaction.dat')
                            os.rename('temp.dat','CurrentAccTransaction.dat')
                            filein.close()
                            UserProfile(Option,acc['AccNo'])
                            break
                        else:
                            print("Wrong Password...")
                            print("Account Login Denied...")
                            with open("CurrentAccTransaction.dat","rb") as fin:
                                     with open("temp.dat","wb")as fout:
                                        try: 
                                             while 1:
                                                 AccTransaction=pk.load(fin)
                                                 if AccTransaction[0]==AccNo:
                                                     TransactionOccuredNow="An attempt was made to login to the bank account on "+str(dt_string)+" but login failed"
                                                     AccTransaction.append(TransactionOccuredNow)
                                                     print("Login attempt recorded to Transaction history...")
                                                     pk.dump(AccTransaction,fout)
                                                 else:
                                                     pk.dump(AccTransaction,fout)
                                        except:
                                             pass
                            os.remove('CurrentAccTransaction.dat')
                            os.rename('temp.dat','CurrentAccTransaction.dat')
                            print("Returning to main menu...")
                            for i in range(4): print()
                            print("******************************************************************************************************************************************************************************************")
                            filein.close()
                            break
        except :
                filein.close()
                print("Account does not exist...")
                print("Do you wish to create an account?")
                choice=input("Enter (y/n): ")
                if choice in 'Yy':
                         CreateCurrentAcc()
                else:
                         print("Returning to main menu...")
                         for i in range(4): print()
                         print("******************************************************************************************************************************************************************************************")


     




def CreateSavingsAcc():
    print("Proceeding to create a savings account...\n\n")
    print("""\t\tIn the Savings account, the user can withdaw and deposit money whenever they feel free to
             there is no restriction set in the amount that can be deposited or withdrawn but there is
             a limit on the number of transaction that can take place.We provide interest rates that are
             fair and entirely dependednt on the period of time the amount is kept in the bank.

                  TIME PERIOD                  INTEREST RATES
                  
                Upto 2 weeks                       Nil
                2 weeks  - 3 months                3%
                3 months - 6 months                4%
                6 months - 1 year                  5%
                1 year   - 2 years                 5.2%
                more than 2 years                  5.5%\n\n""")
    with open("SavingsAccFile.dat","ab") as fout1:                                                      # A binary file for storing each of the Savings Account as a dictionary 
        acc={}       


        print("""    
          Create a strong password that satisfies the following condition:
              #Has more than 6 but less than 20 characters
              #Has at least one digit
              #Has at least one upperccase alphabet
              #Has at least one lowercase alphaber
              #Contains at least one of the any special characters\n""")
        acc['Password']=input("Create a password:")
        acc['Password']=PasswordCheck(acc['Password'])                                                  # Calling a function to help user to create a strong password 


        print("\nAccount name should be valid and should be as given in any of the public records. It should not contain numbers or special characters.\n")  
        acc['AccName']=input("Enter the name of account holder: ")
        acc['AccName']=AccNameCheck(acc['AccName'])
        print("Your Account name has been saved as: ",acc['AccName'])

        
        acc['AccNo']=int(random.random()*pow(10,10))
        print("Your account no:",acc['AccNo'])
        
         
        print("\nIinitial deposition must be at least $1000 \n")
        while 1:
          try:
             acc['InitialAmount']=int(input("Enter the amount to be deposited in the account:"))
             if acc['InitialAmount']<1000:
                   print("Iinitial deposition must be at least $1000...")
                   continue
             else:
                   break
          except:
               print("Please enter valid input...")
               print("Expected a number as input...")
               continue        
        print("Your account has been updated with $",acc['InitialAmount'])


        acc['Date']=dt_string                                 #Precise date with seconds and hour 
        acc['SimplifiedDate']=dt_stringLessAccurate           #less precise date, in order to reduce
                                                              #the complexity of the code for finding duration for interest
        print("Date on which account was created:",dt_string)
       
        acc['CurrentAmount']=acc['InitialAmount']

        acc['ContactNo']=int(input("Enter your mobile number: +91"))
        acc['ContactNo']=ConactNoCheck(acc['ContactNo']) 

        pk.dump(acc,fout1)
        print("Account successfully created...")
        print("Account info: ")
        print(json.dumps(acc,indent=2))
        print("Returning to main menu...")

        with open("SavingsAccTransaction.dat","ab") as fout2:                                           # Creating a Transcation Histroy file in order to keep track of all the transactions that happens in the account
            AccTransactionHistory=[acc['AccNo']]
            pk.dump(AccTransactionHistory,fout2)
        for i in range(4): print()    
        print("******************************************************************************************************************************************************************************************")    
        



def CreateFDAcc():
    print("Proceeding to create a Fixed Deposit account...\n\n")
    print("""\t\tIn the Fixed Deposit account, or FD for short, the user can deposit a sum whenever when they feel they are upto it
             and can store the amount in the bank for an agreed amount of time.During this agreed amount of time, they will be get
             an interest at rates higher than they would in a saving account but they can not withdraw the sum deposited.

                  TIME PERIOD                  INTEREST RATES
                  
                Upto 2 weeks                      Nil
                2 weeks  - 3 months                4%
                3 months - 6 months                6%
                6 months - 1 year                  8%
                more than 1 year                   8.2%\n\n\n""")
    with open("FDAccFile.dat","ab") as fout1:
        acc={}       

        print("""    
          Create a strong password that satisfies the following condition:
              #Has more than 6 but less than 20 characters
              #Has at least one digit
              #Has at least one upperccase alphabet
              #Has at least one lowercase alphaber
              #Contains at least one of the any special characters\n""")  
        acc['Password']=input("Create a password:")
        acc['Password']=PasswordCheck(acc['Password'])

        print("\n\nAccount name should be valid and should be as given in any of the public records. It should not contain numbers or special characters.\n\n")
        acc['AccName']=input("Enter the name of account holder: ")
        acc['AccName']=AccNameCheck(acc['AccName'])
        print("Your Account name has been saved as: ",acc['AccName'])
        
        acc['AccNo']=int(random.random()*pow(10,10))
        print("Your account no:",acc['AccNo'])
         
        print("\nIinitial deposition must be at least $1000 \n")
        while 1:
          try:
             acc['InitialAmount']=int(input("Enter the amount to be deposited in the account:"))
             if acc['InitialAmount']<1000:
                   print("Iinitial deposition must be at least $1000...")
                   continue
             else:
                   break
          except:
               print("Please enter valid input...")
               print("Expected a number as input...")
               continue        
        print("Your account has been updated with $",acc['InitialAmount'])

        acc['Date']=dt_string                                 #Precise date with seconds and hour 
        acc['SimplifiedDate']=dt_stringLessAccurate           #less precise date, in order to reduce
                                                              #the complexity of the code for finding duration         
        print("Date on which account was created:",dt_string)

        acc['AgreedDuration']=int(input("Enter how many months the amount is agreed to be there in the bank: "))

        acc['ContactNo']=int(input("Enter your mobile number: +91"))
        acc['ContactNo']=ConactNoCheck(acc['ContactNo'])
       
        acc['CurrentAmount']=acc['InitialAmount']

        pk.dump(acc,fout1)
        print("Account successfully created...")
        print("Account info: ")
        print(json.dumps(acc,indent=2))
        print("Returning to main menu...")

        with open("FDAccTransaction.dat","ab") as fout2:
            AccTransactionHistory=[acc['AccNo']]
            pk.dump(AccTransactionHistory,fout2)


        with open("FDAccTransaction.dat","rb") as fout2:  #Testing
             try:
                  content=pk.load(fout2)
                  print(content)
                  
             except:
                  pass
        for i in range(4): print()    
        print("******************************************************************************************************************************************************************************************")
        


def CreateRDAcc():
     print("Proceeding to create a Recurring Deposit account...")
     
     with open("RDAccFile.dat","ab") as fout1:
        acc={}       

        print("""    
          Create a strong password that satisfies the following condition:
              #Has more than 6 but less than 20 characters
              #Has at least one digit
              #Has at least one upperccase alphabet
              #Has at least one lowercase alphaber
              #Contains at least one of the any special characters\n""")  
        acc['Password']=input("Create a password:")
        acc['Password']=PasswordCheck(acc['Password'])


        print("\n\nAccount name should be valid and should be as given in any of the public records. It should not contain numbers or special characters.\n\n")
        acc['AccName']=input("Enter the name of account holder: ")
        acc['AccName']=AccNameCheck(acc['AccName'])
        print("Your Account name has been saved as: ",acc['AccName'])

        
        acc['AccNo']=int(random.random()*pow(10,10))
        print("Your account no:",acc['AccNo'])

        acc['ContactNo']=int(input("Enter your mobile number: +91"))
        acc['ContactNo']=ConactNoCheck(acc['ContactNo'])

         
        print("\nIinitial deposition must be at least $1000 \n")
        while 1:
          try:
             acc['InitialAmount']=int(input("Enter the amount to be deposited in the account:"))
             if acc['InitialAmount']<1000:
                   print("Iinitial deposition must be at least $1000...")
                   continue
             else:
                   break
          except:
               print("Please enter valid input...")
               print("Expected a number as input...")
               continue        
        print("Your account has been updated with $",acc['InitialAmount'])


        acc['Date']=dt_string                                 #Precise date with seconds and hour 
        acc['SimplifiedDate']=dt_stringLessAccurate           #less precise date, in order to reduce
                                                              #the complexity of the code for finding duration
        print("Date on which account was created:",dt_string)

        acc['AgreedDuration']=int(input("Enter how many months the amount is agreed to be there in the bank: "))
       
        acc['CurrentAmount']=acc['InitialAmount']

        pk.dump(acc,fout1)
        print("Account successfully created...")
        print("Account info: ")
        print(json.dumps(acc,indent=2))
        print("Returning to main menu...")

        with open("RDAccTransaction.dat","ab") as fout2:
            AccTransactionHistory=[acc['AccNo']]
            pk.dump(AccTransactionHistory,fout2)
        for i in range(4): print()    
        print("******************************************************************************************************************************************************************************************")    






def CreateCurrentAcc():
     print("""\t\t\tCurrent account is mainly targeted towards the buisnessmen who need to have many transaction in a single day
\t\t\tbut for the sum they store they do not get any interest.It greatly facilitates the mordern bussiness world.\n\n\n""")
     print("Proceeding to create a Current account...")
     
     with open("CurrentAccFile.dat","ab") as fout1:
        acc={}       

        print("""    
          Create a strong password that satisfies the following condition:
              #Has more than 6 but less than 20 characters
              #Has at least one digit
              #Has at least one upperccase alphabet
              #Has at least one lowercase alphaber
              #Contains at least one of the any special characters\n""")  
        acc['Password']=input("Create a password:")
        acc['Password']=PasswordCheck(acc['Password'])


        print("\n\nAccount name should be valid and should be as given in any of the public records. It should not contain numbers or special characters.\n\n")
        acc['AccName']=input("Enter the name of account holder: ")
        acc['AccName']=AccNameCheck(acc['AccName'])
        print("Your Account name has been saved as: ",acc['AccName'])

        
        acc['AccNo']=int(random.random()*pow(10,10))
        print("Your account no:",acc['AccNo'])

         
        print("\nIinitial deposition must be at least $1000 \n")
        while 1:
          try:
             acc['InitialAmount']=int(input("Enter the amount to be deposited in the account:"))
             if acc['InitialAmount']<1000:
                   print("Iinitial deposition must be at least $1000...")
                   continue
             else:
                   break
          except:
               print("Please enter valid input...")
               print("Expected a number as input...")
               continue        
        print("Your account has been updated with $",acc['InitialAmount'])

        
        acc['Date']=dt_string                                 #Precise date with seconds and hour 
        acc['SimplifiedDate']=dt_stringLessAccurate           #less precise date, in order to reduce
                                                              #the complexity of the code for finding duration
        print("Date on which account was created:",dt_string)

        acc['ContactNo']=int(input("Enter your mobile number: +91"))
        acc['ContactNo']=ConactNoCheck(acc['ContactNo'])         
       
        acc['CurrentAmount']=acc['InitialAmount']

        pk.dump(acc,fout1)
        print("Account successfully created...")
        print("Account info: ")
        print(json.dumps(acc,indent=2))
        print("Returning to main menu...")

        with open("CurrentAccTransaction.dat","ab") as fout2:
            AccTransactionHistory=[acc['AccNo']]
            pk.dump(AccTransactionHistory,fout2)
        for i in range(4): print()  
        print("******************************************************************************************************************************************************************************************")     




print()


print("                                                                                           JARVIS BANKING")
print("                                                                                 Trascending Banking Managements")

for i in range(3): print()

print("""
                                                                  JARVIS Banking was created as part of a group project
                                                                  between 4 aspiring young IT enthusiasist.This project is
                                                                  a miniaturized version of a practical banking management
                                                                  that



                                                             We ,here at Jarvis Banking , provides 4 different types of Bank account:                                                        
                                                                                                                                                      
                                                                               *Savings Account                                                                                                                               
                                                                                                                                                                                     
                                                                               *Fixed Deposit Account(FD)                                                                                                                                
                                                                                                                                                                                   
                                                                               *Reccuring Deposit Account(RD)
                                                                                                                                                                                      
                                                                               *Current Account


*******************************************************************************************************************************************************************************************""")



while 1:
    for i in range(4): print()
    print("                                                                                   MAIN MENU                                \n\n")
    print("                                                                                  (a)Login                                      ")
    print("                                                                                  (b)Create an account                          ")
    print("                                                                                  (c)About Us                                   ")
    print("                                                                                  (d)Help                                       ")
    print("                                                                                  (e)Quit                                   \n\n")
    print()
    print("Enter the corresponding key in order to select the option")
    Option=input("Enter option :")
    print()
    

    
    if Option in 'Aa':
        print("Option Selected to login into account....\n")
        print("Enter Y/y to continue or N/n to return to main menu: ")
        Confirmation=input("Enter Option :")
        if Confirmation not in 'Yy':
            print("\nExiting Account login")
            print("Returning to main menu...\n")
            for i in range(4): print()
            print("******************************************************************************************************************************************************************************************")
            continue
        print("Proceeding to logging in...")
        for i in range(4): print()
        LoginProfile()

       

    elif  Option in 'Bb':
        print("Option Selected to Create an account....\n")
        print("Enter Y/y to continue or N/n to return to main menu: ")
        Confirmation=input("Enter Option :")
        if Confirmation not in 'Yy':
            print("\nExiting Account creation")
            print("Returning to main menu...\n")
            for i in range(4): print()
            print("******************************************************************************************************************************************************************************************")
            continue
        print("Proceeding to create an account...\n")
        print("""                                                             Please select the type of bank account you wish to open:\n\n
                                                                                  (1)Savings Account
                                                                                  (2)Fixed Deposit Account
                                                                                  (3)Recurring Deposit Account
                                                                                  (4)Current Account\n""")
        AccReqToCreate=input("Enter Option :")
        for i in range(4): print()
        if AccReqToCreate in '1':
            CreateSavingsAcc()
            continue
        elif AccReqToCreate in '2':
            CreateFDAcc()
            continue
        elif AccReqToCreate in '3':
            CreateRDAcc()
            continue
        elif AccReqToCreate in '4':
            CreateCurrentAcc()
            continue
        else:
            print("""Entered key is invalid, Returning to the main menu...""")
            for i in range(4): print()
            print("**************************************************************************************************************************************************************************************************")
            continue



    elif Option in 'Cc':
        print("""                                                                \t\t\t  ABOUT US
                                                        The idea  of banking management to be the selection for school project
                                                        was first popped up in the head of a student named Joshua of XII C. It
                                                        appeared to be a good complimentation to the bot which was the central
                                                        idea that the project revolved on.The project was set into motion on 21st
                                                        of August on sunny afternoon google meet where the minds shared idea.
                                                        Joshua himself leadered the whole group and took upon himself the task of
                                                        appointments that the bot would remind the user of where, Nikhil focused on
                                                        other functions that can be added to the bot.Nabil designed the bot from scrath
                                                        and Niranjan designed the banking aspect of the program.The project got
                                                        completed on 19th of September.""")
        for i in range(4): print()
        print("Returning to main menu...")
        for i in range(4): print()
        print("*********************************************************************************************************************************************************************************")
        continue   



    elif Option in 'Dd':
        print("""please press the corresponding keys:
                             (a)---->logging into your bank account
                             (b)---->Creating a new bank account
                             (c)---->About the developers and the team behind the project
                             (d)---->For Help
                             (f)---->exiting the program""")
        print()
        print("Returning to main menu...")
        for i in range(4): print()
        print("*********************************************************************************************************************************************************************************")
        continue
    

        
    elif Option in 'Ee':
        print("Exiting the program...")
        print("THANK YOU for using JARVIS BANKING")
        for i in range(4): print()
        print("***************************************************************************************************************************************************************************************")
        break



    else:
        print("Entered key is invalid, please press the corresponding keys:")
        print("                     (a)---->logging into your bank account")
        print("                     (b)---->Creating a new bank ccount")
        print("                     (c)---->About the developers and the team behind the project")
        print("                     (d)---->For Help")
        print("                     (f)---->exiting the program")
        print()
        print("Returning to main menu...")
        for i in range(4): print()
        print("********************************************************************************************************************************************************************")
    
