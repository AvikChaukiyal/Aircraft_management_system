from tkinter import *
from tkinter import messagebox
import mysql.connector
from adminmenu import *

# Designing new screen for registration
def register():
 
# The Toplevel widget work pretty much like Frame,
# but it is displayed in a separate, top-level window. 
#Such windows usually have title bars, borders, and other “window decorations”.
# And in argument we have to pass global screen variable
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register Admin")
    register_screen.geometry("300x250")
    register_screen.iconbitmap(r'ac.ico') #set window's icon
 
# set global variables
    global username
    global password
    global username_entry
    global password_entry
    
# Set text variables
    username = StringVar()
    password = StringVar()
 
# Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
# Set username label
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
# Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    
# Set register button, add command = register_user
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
###### End of register()

## Designing New Screen for Login
# define login function
def login():
    global login_screen   
    login_screen = Toplevel(main_screen)
    login_screen.title("Login Admin")
    login_screen.geometry("300x250")
    login_screen.iconbitmap(r'ac.ico') #set window's icon
    
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="* indicates value required").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    login_verification()    
## End of login()

### define login verification function
def login_verification():
    print("working...")
    
## End of login_verification()

### Login Verification process in login_verify()
def login_verify():
#get username and password
 
    username1 = username_verify.get()
    password1 = password_verify.get()
# this will delete the entry after login button is pressed
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
 
#defining verification's conditions 
# Check, if database exist or not. If not then ask user to register
#Else, ask user to login as admin
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
 
# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
    cursor = mydb.cursor()
    
# Show database
    cursor.execute("SHOW DATABASES")    
 
    db=False
    for x in cursor:
      if (x[0] == 'ams2'):
          db=True
    sql =  "SELECT PASSWD FROM userTable WHERE UNAME = %s" 
    val = (username1,)
    if db:  
        cursor.execute("USE ams2")
        cursor.execute(sql,val)
        for x in cursor:
            if password1 == x[0]:
                login_sucess()
            else:
                password_not_recognised()
    else:
        user_not_found()
      
## End of login_verify()

## Designing Login Success Popup
def login_sucess():
 
    global login_success_screen   # make login_success_screen global
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    login_success_screen.iconbitmap(r'ac.ico') #set window's icon
    Label(login_success_screen, text="Login Success").pack()
 
# create OK button
    Button(login_success_screen, text="OK", command=delete_login_success).pack()        
   
## End of login_success()

## Function for deleting the pop-up
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    main_admin_menu_screen()
## Designing Invalid Password Popup
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.iconbitmap(r'ac.ico') #set window's icon
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()    
## End of password_not_recognised()

## function for deleting Invalid password popup
def delete_password_not_recognised():
    password_not_recog_screen.destroy()

## Designing User Not Found Popup
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.iconbitmap(r'ac.ico') #set window's icon
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
## End of user_not_found()

## function for deleting User Not Found popup
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    
## Assigning functions to register i.e., registering users
def register_user():
 
# get username and password
    username_info = username.get()
    password_info = password.get()
 # Check, if database exist or not. If not then create database and table
#Else, ask user to login as admin
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
 
# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
    cursor = mydb.cursor()
    
# Show database
    cursor.execute("SHOW DATABASES")    
 
    db=False
    for x in cursor:
      if (x[0] == 'ams2'):
          db=True
    sql = "INSERT INTO userTable(UNAME,PASSWD,UTYPE) VALUES (%s,%s,%s)"
    val = (username_info,password_info, 'ADMIN')     
    if not db:
        print("Creating Database.....")
# write username and password information into table
        cursor.execute("CREATE DATABASE ams2")
        cursor.execute("USE ams2")
        cursor.execute("CREATE TABLE userTable(UNAME VARCHAR(20) PRIMARY KEY,\
                       PASSWD VARCHAR(20), UTYPE VARCHAR(10))")
        cursor.execute(sql,val)
            
        cursor.execute("CREATE TABLE Aircraft(AC_ID INTEGER PRIMARY KEY,\
                       TYPE VARCHAR(20), SEAT_CAPACITY INTEGER, \
                           FUEL_TANK INTEGER, REQUIRED_FT INTEGER)")
        cursor.execute("CREATE TABLE Crew(EMPID VARCHAR(5) PRIMARY KEY,\
                       ENAME VARCHAR(20), MOBILE_NO VARCHAR(10),\
                           FLIGHT_TIME_HRS INTEGER)")
        cursor.execute("CREATE TABLE Vendor(VID VARCHAR(5) PRIMARY KEY,\
                       VNAME VARCHAR(20), MOBILE_NO VARCHAR(10),\
                           EMAIL VARCHAR(30))")
        try: 
            sql = "CREATE TABLE Assign(AC_ID INTEGER, EMPID VARCHAR(5),PRIMARY KEY(AC_ID, EMPID),\
                 FOREIGN KEY (AC_ID) REFERENCES Aircraft(AC_ID) ON DELETE CASCADE,\
                 FOREIGN KEY (EMPID) REFERENCES Crew(EMPID) ON DELETE CASCADE)"
            cursor.execute(sql)
            
            sql1 = "CREATE TABLE Maintenance(AC_ID INTEGER, VID VARCHAR(5),\
                       CONTRACT_START_DATE DATE, CONTRACT_END_DATE DATE,\
                          LAST_SERVE DATE, PRIMARY KEY(AC_ID, VID),\
                           FOREIGN KEY (AC_ID) REFERENCES Aircraft(AC_ID) ON DELETE CASCADE,\
                               FOREIGN KEY (VID) REFERENCES Vendor(VID) ON DELETE CASCADE)"
            cursor.execute(sql1)
        except mysql.connector.Error as e:
            print("Error : ",e)
        mydb.commit()
# set a label for showing success information on screen 
        messagebox.showinfo("Success","Registration Success!!!\nPlease login to continue")       
        mydb.close()
    else:
     # Display messagebox to login   
         messagebox.showinfo("ERROR", "Admin Already Exists!! \nPlease Login ")
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    register_screen.destroy();
## end of register_user()
    

# Designing Main(First) Screen/ Window
# The screen will have two button login and register

def main_account_screen():
    global main_screen
 
    main_screen = Tk()
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Admin Account Login") # set the title of GUI window
    main_screen.iconbitmap(r'ac.ico') #set window's icon
 
# create a Form label 
    Label(text="Select Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
 
# create Login Button ,  add command = login 
    Button(text="Login", height="2", width="30", command=login).pack() 
    Label(text="").pack() 
 
# create a register button, add command=register in button widget
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop() # start the GUI
 
#main_account_screen() # call the main_account_screen() function
