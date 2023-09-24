from tkinter import *
import mysql.connector

def adduser():
    
    usrname_info = usrname_verify.get()
    passd_info = passd_verify.get()

# this will delete the entry after login button is pressed
    usrname_login_entry.delete(0, END)
    passd_login_entry.delete(0, END)
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
       )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    sql = "INSERT INTO userTable(UNAME,PASSWD,UTYPE) VALUES (%s,%s,%s)"
    val = (usrname_info,passd_info, 'USER')   
    try:
         cursor.execute(sql,val)
         mydb.commit()
         
    except:
         mydb.rollback()
         # Display messagebox to login   
         messagebox.showinfo("ERROR", "User Already Exists!!")
    mydb.close()
## End of adduser()
     
def user_details():
    global user_details_screen   
    user_details_screen = Toplevel(root)   ###  ????
    user_details_screen.title("Add User")
    user_details_screen.geometry("300x250")
    user_details_screen.iconbitmap(r'ac.ico')
    Label(user_details_screen, text="Please enter User details").pack()
    Label(user_details_screen, text="* indicates value required").pack()
    Label(user_details_screen, text="").pack()
 
    global usrname_verify
    global passd_verify
 
    usrname_verify = StringVar()
    passd_verify = StringVar()
 
    global usrname_login_entry
    global passd_login_entry

    Label(user_details_screen, text="Username * ").pack()
    usrname_login_entry = Entry(user_details_screen, textvariable=usrname_verify)
    usrname_login_entry.pack()
    Label(user_details_screen, text="").pack()
    Label(user_details_screen, text="Password * ").pack()
    passd_login_entry = Entry(user_details_screen, textvariable=passd_verify, show= '*')
    passd_login_entry.pack()
    Label(user_details_screen, text="").pack()
    Button(user_details_screen, text="OK", width=10, height=1, command=adduser).pack()
## End of user_details()

def delete_user():
    global user_delete_screen   
    user_delete_screen = Toplevel(root)   ###  ????
    user_delete_screen.title("Delete User")
    user_delete_screen.geometry("300x250")
    user_delete_screen.iconbitmap(r'ac.ico')
    
    Label(user_delete_screen, text="Please enter Username to delete").pack()
    Label(user_delete_screen, text="* indicates value required").pack()
    Label(user_delete_screen, text="").pack()
    
    global usr_name_verify
    usr_name_verify = StringVar()
    
    Label(user_delete_screen, text="Username * ").pack()
    usrname_entry = Entry(user_delete_screen, textvariable=usr_name_verify)
    usrname_entry.pack()
    Label(user_delete_screen, text="").pack()
    Button(user_delete_screen, text="OK", width=10, height=1, command=del_verify_usr).pack()
### End of delete_user

def del_verify_usr():
### Signature of verify_user (usr, delusr=FALSE)
    if verify_user(usr_name_verify.get(),TRUE):
         messagebox.showinfo("Success", "Operation Successful")
    else:
         messagebox.showinfo("ERROR", "Operation UnSuccessful")
   
    user_delete_screen.destroy()

def edit_user():
    global user_edit_screen   
    user_edit_screen = Toplevel(root)   ###  ????
    user_edit_screen.title("Edit User")
    user_edit_screen.geometry("300x250")
    user_edit_screen.iconbitmap(r'ac.ico')
    
    Label(user_edit_screen, text="Please enter Username to edit").pack()
    Label(user_edit_screen, text="* indicates value required").pack()
    Label(user_edit_screen, text="").pack()
    
    global usr_edit_verify
    usr_edit_verify = StringVar()
    
    Label(user_edit_screen, text="Username * ").pack()
    usrname_entry = Entry(user_edit_screen, textvariable=usr_edit_verify)
    usrname_entry.pack()
    Label(user_edit_screen, text="").pack()
    Button(user_edit_screen, text="OK", width=10, height=1, command=usr_entry_verify_edit).pack()
### End of edit_user()

def usr_entry_verify_edit():
### Signature of verify_user (usr, delusr=FALSE)
    print(usr_edit_verify.get())
    if verify_user(usr_edit_verify.get()):
        change_passwd()
        #messagebox.showinfo("Success", "Operation Successful")
    else:
        unverified_usr()
        messagebox.showinfo("ERROR", "Operation UnSuccessful") 
    #user_edit_screen.destroy()
### End of usr_entry_verify_edit()


def change_passwd():
    
    global passwd_edit_screen
    print("Change password now....Enter New password ...")
    passwd_edit_screen = Toplevel(user_edit_screen)
    passwd_edit_screen.title("Change Password")
    
    passwd_edit_screen.geometry("300x250")
    passwd_edit_screen.iconbitmap(r'ac.ico')
    
    Label(passwd_edit_screen, text="Please enter New Password").pack()
    Label(passwd_edit_screen, text="").pack()
    
    global new_password_usr
    new_password_usr = StringVar()
    
    Label(passwd_edit_screen, text="New Password * ").pack()
    passwd_name_entry = Entry(passwd_edit_screen, textvariable=new_password_usr, show= '*')
    passwd_name_entry.pack()
    Label(passwd_edit_screen, text="").pack()
    
    Label(passwd_edit_screen, text="").pack()
    Button(passwd_edit_screen, text="OK", width=10, height=1, command=old_passwd_edit).pack()
## end of change_passwd()

def old_passwd_edit():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
      )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    
    print("Changing password....for User...",usr_edit_verify.get())
    sql = "UPDATE userTable SET PASSWD = %s  WHERE UNAME = %s AND UTYPE = %s"
    val = (new_password_usr.get(),usr_edit_verify.get(),'USER')
    print("New password: ",new_password_usr.get())
    try:
        cursor.execute(sql,val)
        mydb.commit()
        delete_passwd_edit()
    except mysql.connector.Error:
         mydb.rollback()
         # Display messagebox to login   
         messagebox.showinfo("ERROR", "Can't Update!!!\nUser not found")
    mydb.close()
## End of old_passwd_edit()

def delete_passwd_edit():
    passwd_edit_screen.destroy()
    user_edit_screen.destroy()
    
### End of delete_passwd_edit()

def verify_user (usr, delusr=FALSE):
    print("Inside verify_usr: ",usr, delusr)
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    sql = "SELECT COUNT(*) FROM userTable WHERE UNAME = %s AND UTYPE = %s"
    val = (usr,'USER')
    
    sql1 = "DELETE FROM userTable WHERE UNAME = %s AND UTYPE = %s"
    val1 = (usr,'USER')
    try:
        cursor.execute(sql,val)
        print("try....")
        for x in cursor:
            if x[0] == 1:
                print(x[0])
                if delusr:
                    print("Deleting user.....", usr)
                    cursor.execute(sql1,val1)
                    mydb.commit()
                return TRUE
            else:
                return FALSE
    except mysql.connector.Error:
         mydb.rollback()
         # Display messagebox to login   
         messagebox.showinfo("ERROR", "User not found !!!")
    mydb.close()
### End of verify_user()

def del_aircraft():
    
    global ac_del_screen 
    ac_del_screen = Toplevel(root)   ###  ????
    ac_del_screen.title("Delete Aircraft")
    ac_del_screen.geometry("300x200")
    ac_del_screen.iconbitmap(r'ac.ico')
    
    global a_id
    a_id = StringVar()
    Label(ac_del_screen, text="Aircraft Id").place(x = 60, y = 70)
    ac_id_del_entry = Entry(ac_del_screen, width = 10, textvariable=a_id)
    ac_id_del_entry.place(x = 130, y = 70)
    
    Button(ac_del_screen, text=" DELETE ", height=2, command=del_ac_verify).place(x = 120, y = 120)
## End of del_aircraft()

def del_ac_verify():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
      )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
     
    try:
         sql = "DELETE FROM Aircraft WHERE AC_ID = %s"
         val = (int(a_id.get()),)
         print(val)
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful\n1 row deleted")
    except mysql.connector.Error as e:
         print(e)
         mydb.rollback()
         # Display messagebox to login   
         messagebox.showinfo("ERROR", "Can't Delete\nAircraft ID does not exist")
    mydb.close()
    ac_del_screen.destroy()  
## End of del_ac_verify()

def del_crew():
    
    global crew_delete_screen   
    crew_delete_screen = Toplevel(root)   ###  ????
    crew_delete_screen.title("Delete Crew")
    crew_delete_screen.geometry("300x200")
    crew_delete_screen.iconbitmap(r'ac.ico')
        
    global crew_no
    crew_no = StringVar()
    
    Label(crew_delete_screen, text="Employee ID * ").place(x = 60, y = 70)
    crew_entry = Entry(crew_delete_screen, textvariable=crew_no)
    crew_entry.place(x = 130, y = 70)
    
    Button(crew_delete_screen, text=" DELETE ", height=2, command=del_cu_verify).place(x = 120, y = 120)
##End of del_crew()

def del_cu_verify():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    
    try:
         sql = "DELETE FROM Crew WHERE EMPID = %s"
         val = (crew_no.get(),)
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful\n1 row deleted")
    except mysql.connector.Error:
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Delete\nEmployee ID does not exist")
    mydb.close()
    crew_delete_screen.destroy()
## End of del_cu_verify()

def del_vendor():
    
    global vend_delete_screen   
    vend_delete_screen = Toplevel(root)   ###  ????
    vend_delete_screen.title("Delete Vendor")
    vend_delete_screen.geometry("300x200")
    vend_delete_screen.iconbitmap(r'ac.ico')
    global v_no    
    v_no = StringVar()
    
    Label(vend_delete_screen, text="Vendor ID * ").place(x = 60, y = 70)
    vend_entry = Entry(vend_delete_screen, textvariable=v_no)
    vend_entry.place(x = 130, y = 70)
    
    Button(vend_delete_screen, text=" DELETE ", height=2, command=del_vendor_verify).place(x = 120, y = 120)
##End of del_crew()

def del_vendor_verify():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    
    try:
         sql = "DELETE FROM Vendor WHERE VID = %s"
         val = (v_no.get(),)
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful\n1 row deleted")
    except mysql.connector.Error:
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Delete\nVendor ID does not exist")
    mydb.close()
    vend_delete_screen.destroy()
## End of del_vendor_verify()
def donothing():
    print("")
## End of donothing():    
    
def main_admin_menu_screen():
    global root
    root = Tk()
    menubar = Menu(root)
    root.title("Adminstrator")
    root.geometry('400x300')
    root.iconbitmap(r'ac.ico')
    
    usermenu = Menu(menubar, tearoff=0)
    usermenu.add_command(label="New", command=user_details)
    usermenu.add_command(label="Edit", command=edit_user)
    usermenu.add_command(label="Delete", command=delete_user)

    usermenu.add_separator()

    usermenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="User", menu=usermenu)

    dbmenu = Menu(menubar, tearoff=0)
    dbmenu.add_command(label="Aircraft", command=del_aircraft)
    dbmenu.add_command(label="Crew", command=del_crew)
    dbmenu.add_command(label="Vendor", command=del_vendor)

    menubar.add_cascade(label="Remove", menu=dbmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()
## End of main_admin_menu_screen()