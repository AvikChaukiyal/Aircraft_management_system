from tkinter import *
import mysql.connector
from usermenu import *

## Designing New Screen for Login
# define login function
def login():
    global login_screen   
    login_screen = Toplevel(user_main_screen)
    login_screen.title("User Login")
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
    cursor.execute("USE ams2")
    
    try:
        sql= "SELECT PASSWD FROM userTable WHERE UNAME = %s AND UTYPE = %s"
        val = (username1,'USER')
        cursor.execute(sql,val)
        for x in cursor:
            if password1 == x[0]:
                login_sucess()
            else:
                password_not_recognised()
    except mysql.connector.Error:
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
    user_main_screen.destroy()
    main_user_menu_screen()

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
    
def main_user_account_screen():
    global user_main_screen
    user_main_screen = Tk()
    user_main_screen.wm_state('iconic')
    login()
    user_main_screen.mainloop() # start the GUI
 
#main_account_screen() # call the main_account_screen() function
