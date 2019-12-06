#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:44:23 2019

@author: student
"""
import sqlite3
import sys

con=sqlite3.connect("mydb1.db")
if con!=None:
    print("connection establish")
else:
    print("not connected")

cursor=con.cursor()

def insertDept():
    id1=int(input("enter id:"))
    dept=input("enter department name:")
    loc=input("name of loaction")
    noe=int(input("no of employees:"))
    cursor.execute("insert into dept values(?,?,?,?)",(id1,dept,loc,noe))
    con.commit()

def displayAll():
    cursor.execute("select * from dept")
    for row in cursor:
        print(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3]))
        
def deleterec():
    aid=int(input("enter id:"))
    cursor.execute("delete from dept where dno=?",(aid,))
    con.commit()  

def updaterec():
    dno=int(input("enter id:"))
    ch=0
    while ch!=3:
        print("1.enter dept:")
        print("2.enter name:")
        print("3.enter location:")
        print("4.press anything to exit")
        ch=int(input("enter your choice:"))
        if ch==2:
            name=input("enter new name:")
            cursor.execute("update dept set name=? where dno=?",(name,dno))
            con.commit()
        elif ch==1:
            dname=input("enter new dept:")
            cursor.execute("update dept set dname=? where dno=?",(dname,dno))
            con.commit()
        elif ch==3:
            loc=input("enter new location:")
            cursor.execute("update dept set location=? where dno=?",(loc,dno))
            con.commit()
def displayDept():
    deptname=input("enter  departname")
    cursor.execute("select * from dept where dname=?",(deptname,))
    for row in cursor:
        print(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3]))
        
def displayIn():
    cursor.execute("select * from dept where location like '%ne%'")
    for row in cursor:
        print(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3]))


      
ans="y"
choice=0
while choice!=7:
    print("**************************")
    print("1.Insert data")
    print("2.delete data")
    print("3.modify data")
    print("4.display data")
    print("5.display by dept")
    print("6.display location")
    print("6.exit")  
    choice=int(input("enter choice"))
    if choice==1:
        insertDept()
    elif choice==2:
        deleterec()
    elif choice==3:
        updaterec()
    elif choice==4:
        displayAll()
    elif choice==5:
        displayDept()
    elif choice==6:
        displayIn()
    else:
        sys.exit(0)