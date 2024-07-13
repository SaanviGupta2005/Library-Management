# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:14:45 2022

@author: Saanvi Gupta
"""

from traceback import print_last
import pandas as pd
import os



#DISPLAY


def display_menu():
    print("____________________________")
    print("Welcome to Library Management System")
    print("1. Add New Book")
    print("2. View Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Books Issued Status")
    print("7. View Books returned Status")
    print("8. Search Student in Issue")
    print("9. Search Student in Return")
    print("10. Quit")

# ADDING A BOOK

def add_book():
    print("___________")
    print("Add Book Information")
    print("___________")
    Tl = input("Enter Title of Book:")
    au = input("Enter Author of Book:")
    pb = input("Enter Publisher of Book:")
    nc = input("Enter  Number of copies:")
    bn=0
    if not os.path.isfile("D:\\Book1.csv"):
        df = pd.DataFrame(columns = ["Bookno","Title","Author","Publisher","noc"])
        bn=1
        df.loc[bn]=[bn,Tl,au,pb,nc]
    else:
        df=pd.read_csv("D:\\Book1.csv")
        bn=len(df)
        bn=bn+1
        df.loc[bn]=[bn,Tl,au,pb,nc]
    df.to_csv("D:\\Book1.csv",index=False)
    print(df.to_string(index=False))
    print("Data saved successfully")
    input("Press any key to continue")
    return

#VIEWING A BOOK

def view_book():
    print("---Book Record---")
    df=pd.read_csv("D:\\Book1.csv")
    if df.empty==True:
        print_last("No Books Available")
    else:
        print(df.to_string(index=False))
    input("Press any key to continue")

#SEARCHING A BOOK

def search_book():
    print("---Search Book---")
    bn=int(input("Enter Book no. to search:"))
    df=pd.read_csv("D:\\Book1.csv")
    rdf=df[(df['Bookno']==bn)]
    if rdf.empty==True:
        print("This book does not exist")
    else:
        print(rdf.to_string(index=False))
    input("Press any key to continue")


#ISSUE BOOK

def issue_book():
    dfi=pd.DataFrame(columns=['Rollno','Bookno','Copies','IssueData'])
    print("------------------")
    print("Issue Book")
    print("------------------")
    bn=int(input("Enter Book No to be issued: "))
    df=pd.read_csv("D:\\Book1.csv")
    print(df.to_string(index=False))
    if not os.path.isfile('D:\\issue.csv'):
        rc=1
    else:
        dfi=pd.read_csv("D:\\issue.csv")
        rc=len(dfi)
        rc=rc+1
    rdf=df[(df['Bookno']==bn)]

    if rdf.empty==True:
        print("This book does not exist")
    else:
        print(rdf.to_string(index=False))
        c=int(rdf['noc'])
        RN=input("Enter Roll No to whom book to be issued:")
        cop=input("Enter No. of copies to be issued:")
        dt=input("Enter issue date in dd/mm/yy format:")
        c=c-int(cop)
        if c>=0:
            df.loc[rdf.index,'noc']=c
            print(df.to_string(index=False))
            dfi.loc[rc]=[RN,bn,cop,dt]
            dfi.to_csv('D:\\issue.csv',index=False)
            df.to_csv("D:\\Book1.csv",index=False)
            print(dfi.to_string(index=False))
            print("Book issued successfully")
            input("Press any key to continue")
        else:
            print("Insufficient number of books: Can't ISSUE")
            
    return

#RETURN BOOK

def return_book():
    dfr=pd.DataFrame(columns=['Rollno','Bookno','Copies','ReturnDate'])
    print("------------------")
    print("Return Book")
    print("------------------")
    if not os.path.isfile('D:\\return.csv'):
        rc=1
    else:
        dfr=pd.read_csv("D:\\return.csv")
        rc=len(dfr)
        rc=rc+1
    bn=int(input("Enter Book No to be returneD:"))
    df=pd.read_csv("D:\\Book1.csv")
    rdf=df[(df['Bookno']==bn)]
    c=int(rdf['noc'])
    print(rdf.to_string(index=False)) 
    RN=input("Enter Roll no of the Students returning Book:")
    cop=int(input("Enter No of copies to ber returneD:"))
    dt=input("Enter return date in dd/mm/yy format:")
    days=int(input("Enter number of days book kept:"))
    fine=0
    if days>10:
        fine=(days-4)*10*cop
    else:
        fine=0
    c=c+int(cop)
    print("Please pay rent charges of Rs",fine)
    ans=input("Are you sure rent is collected, enter y or n:")
    if ans=="y":
        df.loc[rdf.index,'noc']=c
        print(df.to_string(index=False))
        dfr.loc['rc']=[RN,bn,cop,dt]
        print(dfr.to_string(index=False))
        dfr.to_csv("D:\\return.csv",index=False)
        df.to_csv("D:\\Book1.csv",index=False)
        print("Book Returned successfully")
        input("Press any key to continue")
    else:
        print("Pay the rent first then record will be saved")
    return

#ISSUE BOOK

def view_issuebook():
    if os.path.isfile('D:\\issue.csv'):
        dfi=pd.read_csv("D:\\issue.csv")
        print("Book Issue Status")
        print(dfi.to_string(index=False))
    else:
        print("No Book Issued")
    return

#RETURN BOOK

def view_returnbook():
    if os.path.isfile('D:\\return.csv'):
        dfr=pd.read_csv("D:\\return.csv")
        print("Books Return Status")
        print(dfr.to_string(index=False))
    else:
        print("No Book Issued")
    return


#SEARCHING ROLL NO.

def search_rollno():
    print("---Search Student---")
    rn=int(input("Enter Student no. to search:"))
    dfi=pd.read_csv("D:\\issue.csv")
    rdf=dfi[(dfi['Rollno']==rn)]
    if rdf.empty==True:
        print("This student has not got any book issued")
    else:
        print(rdf.to_string(index=False))
    input("Press any key to continue")

#RETURN ROLL NO.
 
def return_rollno():
    print("---Search student---")
    rn=int(input("Enter Student no. to search:"))
    dfr=pd.read_csv("D:\\return.csv")
    rdf=dfr[(dfr['Rollno']==rn)]
    if rdf.empty == True:
        print("This student has not returned any book")
    else:
        print(rdf.to_string(index=False))
    input("Press any key to continue")




while True:
    display_menu()
    choice=input("Enter your choice:")
    if choice=='1':
        add_book()
    elif choice=='2':
        view_book()
    elif choice=='3':
        search_book()
    elif choice=='4':
        issue_book()
    elif choice=='5':
        return_book()
    elif choice=='6':
        view_issuebook()
    elif choice=='7':
        view_returnbook()
    elif choice=='8':
        search_rollno()
    elif choice=='9':
        return_rollno()
    else:
        break
print("--------------")
print("Thank you for using Library Management System")
print("--------------")
display_menu()
