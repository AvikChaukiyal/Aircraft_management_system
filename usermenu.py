from tkinter import *
import mysql.connector
import datetime 

def addaircraft():

    global ac_details_screen 
    ac_details_screen = Toplevel(root)   ###  ????
    ac_details_screen.title("Add Aircraft")
    ac_details_screen.geometry("400x400")
    ac_details_screen.iconbitmap(r'ac.ico')
    
    Label(ac_details_screen, text="Please enter Aircraft details", font=('Times',12,'bold','italic')).place(x = 120, y = 10)
    Label(ac_details_screen, text="* indicates value required", font=('Times',12, 'bold','italic')).place(x = 120, y = 30)
 
    global aid
    global actype
    global ac_capacity 
    global ac_fuel
    global ac_ft_req    
    
    aid = StringVar()
    actype = StringVar()
    ac_capacity = StringVar()
    ac_fuel = StringVar()
    ac_ft_req = StringVar()
 
    Label(ac_details_screen, text="ID * ").place(x = 20, y = 80)
    ac_id_entry = Entry(ac_details_screen, width = 10, textvariable=aid)
    ac_id_entry.place(x = 80, y = 80)

    Label(ac_details_screen, text="Type").place(x = 200, y = 80)
    ac_type_entry = Entry(ac_details_screen, textvariable=actype)
    ac_type_entry.place(x = 240, y = 80)

    Label(ac_details_screen, text="Seating\nCapacity").place(x = 15, y = 150)
    ac_cap_entry = Entry(ac_details_screen, width = 10, textvariable=ac_capacity)
    ac_cap_entry.place(x = 80, y = 160)

    Label(ac_details_screen, text="Fuel\nTank\nCapacity").place(x = 190, y = 150)
    ac_fuel_entry = Entry(ac_details_screen, width = 10, textvariable=ac_fuel)
    ac_fuel_entry.place(x = 240, y = 160)

    Label(ac_details_screen, text="in Liters").place(x = 300, y = 160)

    Label(ac_details_screen, text="Flight Time\nRequirement").place(x = 80, y = 250)
    ac_ft_entry = Entry(ac_details_screen, width = 10, textvariable=ac_ft_req)
    ac_ft_entry.place(x = 170, y = 255)
    Label(ac_details_screen, text="(in Hours)").place(x = 80, y = 280)

    Button(ac_details_screen, text="INSERT", height=2, command=add_ac_verify).place(x = 200, y = 300)

## End of addaircraft() 

def add_ac_verify():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
     
    try:
         sql = "INSERT INTO Aircraft(AC_ID,TYPE,SEAT_CAPACITY,FUEL_TANK,REQUIRED_FT) VALUES(%s,%s,%s,%s,%s)"
         val = (int(aid.get()),actype.get(),int(ac_capacity.get()),int(ac_fuel.get()),int(ac_ft_req.get()))
         print(val)
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful\n1 row Inserted")
    except mysql.connector.Error:
         mydb.rollback()
         # Display messagebox to login   
         messagebox.showinfo("ERROR", "Can't Insert\nDulicate Aircraft ID")
    mydb.close()
    ac_details_screen.destroy()      
## End of add_ac_verify()

def addcrew():
   global c_details_screen 
   c_details_screen = Toplevel(root)   ###  ????
   c_details_screen.title("Add Crew")
   c_details_screen.geometry("400x300")
   c_details_screen.iconbitmap(r'ac.ico')
   
   Label(c_details_screen, text="Please enter Crew details", font=('Times',12,'bold','italic')).place(x = 120, y = 10)
   Label(c_details_screen, text="* indicates value required", font=('Times',12, 'bold','italic')).place(x = 120, y = 30)
 
   global cid
   global cname
   global c_mno 
   global c_ft

   cid = StringVar()
   cname = StringVar()
   c_mno = StringVar()
   c_ft = StringVar()
 
   Label(c_details_screen, text="Employee ID * ").place(x = 20, y = 80)
   c_id_entry = Entry(c_details_screen, width = 10, textvariable=cid)
   c_id_entry.place(x = 100, y = 80)

   Label(c_details_screen, text="Name").place(x = 200, y = 80)
   c_type_entry = Entry(c_details_screen, textvariable=cname)
   c_type_entry.place(x = 240, y = 80)

   Label(c_details_screen, text="Mobile").place(x = 20, y = 160)
   c_mno_entry = Entry(c_details_screen, width = 10, textvariable=c_mno)
   c_mno_entry.place(x = 80, y = 160)

   Label(c_details_screen, text="Comleted\nFlight Time").place(x = 200, y = 150)
   c_ft_entry = Entry(c_details_screen, width = 10, textvariable=c_ft)
   c_ft_entry.place(x = 270, y = 160)
   Label(c_details_screen, text="(in Hours)").place(x = 200, y = 180)
   
   Button(c_details_screen, text=" INSERT ", height=2, command=add_crew_verify).place(x = 120, y = 220)
## End of addcrew()

def add_crew_verify():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
     
    try:
         sql = "INSERT INTO Crew(EMPID,ENAME,MOBILE_NO,FLIGHT_TIME_HRS) VALUES(%s,%s,%s,%s)"
         val = (cid.get(),cname.get(),c_mno.get(),int(c_ft.get()))
         print(val)
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful\n1 row inserted")
    except mysql.connector.Error:
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Insert\nDulicate Employee ID")
    mydb.close()
    c_details_screen.destroy()  
## End of add_crew_verify()
def addvendor():
    
    global v_details_screen 
    v_details_screen = Toplevel(root)   ###  ????
    v_details_screen.title("Add Vendor")
    v_details_screen.geometry("400x300")
    v_details_screen.iconbitmap(r'ac.ico')
    
    Label(v_details_screen, text="Please enter Vendor details", font=('Times',12,'bold','italic')).place(x = 120, y = 10)
    Label(v_details_screen, text="* indicates value required", font=('Times',12, 'bold','italic')).place(x = 120, y = 30)
 
    global vid
    global vname
    global v_mno 
    global v_email

    vid = StringVar()
    vname = StringVar()
    v_mno = StringVar()
    v_email = StringVar()
 
    Label(v_details_screen, text="Vendor ID * ").place(x = 20, y = 80)
    v_id_entry = Entry(v_details_screen, width = 10, textvariable=vid)
    v_id_entry.place(x = 100, y = 80)

    Label(v_details_screen, text="Name").place(x = 200, y = 80)
    v_type_entry = Entry(v_details_screen, textvariable=vname)
    v_type_entry.place(x = 240, y = 80)

    Label(v_details_screen, text="Mobile").place(x = 20, y = 160)
    v_mno_entry = Entry(v_details_screen, width = 10, textvariable=v_mno)
    v_mno_entry.place(x = 80, y = 160)

    Label(v_details_screen, text="Email").place(x = 200, y = 160)
    v_email_entry = Entry(v_details_screen, textvariable=v_email)
    v_email_entry.place(x = 240, y = 160)

    Button(v_details_screen, text=" INSERT ", height=2, command=add_vendor_verify).place(x = 120, y = 220)
## End of addvendor()

def add_vendor_verify():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
     
    try:
         sql = "INSERT INTO Vendor(VID,VNAME,MOBILE_NO,EMAIL) VALUES(%s,%s,%s,%s)"
         val = (vid.get(),vname.get(),v_mno.get(),v_email.get())
         print(val)
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful\n1 row inserted")
    except mysql.connector.Error:
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Insert\nDulicate Vendor ID")
    mydb.close()
    v_details_screen.destroy() 
## End of add_vendor_verify()

def addamc():
    global amc_details_screen 
    amc_details_screen = Toplevel(root)   ###  ????
    amc_details_screen.title("AMC")
    amc_details_screen.geometry("400x300")
    amc_details_screen.iconbitmap(r'ac.ico')
    
    Label(amc_details_screen, text="Please enter AMC details", font=('Times',11,'bold','italic')).place(x = 130, y = 20)
    Label(amc_details_screen, text="(* indicates value required)", font=('Times',11, 'bold','italic')).place(x = 120, y = 40)

    global aac_id
    global av_id
    global csd
    global ced

    aac_id = StringVar()
    av_id = StringVar()
    csd = StringVar() 
    ced = StringVar()

    Label(amc_details_screen, text="Aircraft ID *").place(x = 20, y = 120)
    ac_id_entry = Entry(amc_details_screen, width = 10, textvariable=aac_id)
    ac_id_entry.place(x = 90, y = 120)

    Label(amc_details_screen, text="Vendor ID *").place(x = 200, y = 120)
    emp_id_entry = Entry(amc_details_screen, width = 10, textvariable=av_id)
    emp_id_entry.place(x = 280, y = 120)

    Label(amc_details_screen, text="Contract\nStart Date").place(x = 20, y = 180)
    ac_id_entry = Entry(amc_details_screen, width = 15, textvariable=csd)
    ac_id_entry.place(x = 90, y = 180)

    Label(amc_details_screen, text="(yyyy-mm-dd)").place(x = 15, y = 210)

    Label(amc_details_screen, text="Contract\nEnd Date").place(x = 200, y = 180)
    emp_id_entry = Entry(amc_details_screen, width = 15, textvariable=ced)
    emp_id_entry.place(x = 280, y = 180)

    Button(amc_details_screen, text=" INSERT ", height=3, command=add_amc_data).place(x = 160, y = 220)

## End of addamc()

def add_amc_data():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    ## Initially, Last service date is same as contract start date
    sql = "INSERT INTO Maintenance\
        (AC_ID,VID,CONTRACT_START_DATE,CONTRACT_END_DATE,LAST_SERVE) \
         VALUES(%s, %s, %s, %s, %s)"
    val = (int(aac_id.get()), av_id.get(), csd.get(),ced.get(),csd.get())
    print(val)
    try:
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful!\n1 row inserted")
    except mysql.connector.Error as e:
         print(e)
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Insert !!!\nInvalid ID's")
    mydb.close()
    amc_details_screen.destroy()
## End of add_amc_data()

def updateac():
    
    global ac_update_screen 
    ac_update_screen = Toplevel(root)   ###  ????
    ac_update_screen.title("Update Aircraft")
    ac_update_screen.geometry("400x400")
    ac_update_screen.iconbitmap(r'ac.ico')
    Label(ac_update_screen, text="Please enter Aircraft details\nfor  UPDATION", font=('Times',12,'bold','italic')).place(x = 120, y = 10)
    Label(ac_update_screen, text="* indicates value required", font=('Times',12, 'bold','italic')).place(x = 120, y = 30)
 
    global auid
    global acutype
    global acu_capacity 
    global acu_fuel
    global acu_ft_req    
    
    auid = StringVar()
    acutype = StringVar()
    acu_capacity = StringVar()
    acu_fuel = StringVar()
    acu_ft_req = StringVar()
 
    Label(ac_update_screen, text="ID * ").place(x = 20, y = 80)
    acu_id_entry = Entry(ac_update_screen, width = 10, textvariable=auid)
    acu_id_entry.place(x = 80, y = 80)

    Label(ac_update_screen, text="Type").place(x = 200, y = 80)
    acu_type_entry = Entry(ac_update_screen, textvariable=acutype)
    acu_type_entry.place(x = 240, y = 80)

    Label(ac_update_screen, text="Seating\nCapacity").place(x = 15, y = 150)
    ac_cap_entry = Entry(ac_update_screen, width = 10, textvariable=acu_capacity)
    ac_cap_entry.place(x = 80, y = 160)

    Label(ac_update_screen, text="Fuel\nTank\nCapacity").place(x = 190, y = 150)
    acu_fuel_entry = Entry(ac_update_screen, width = 10, textvariable=acu_fuel)
    acu_fuel_entry.place(x = 240, y = 160)

    Label(ac_update_screen, text="in Liters").place(x = 300, y = 160)

    Label(ac_update_screen, text="Flight Time\nRequirement").place(x = 80, y = 250)
    acu_ft_entry = Entry(ac_update_screen, width = 10, textvariable=acu_ft_req)
    acu_ft_entry.place(x = 170, y = 255)
    Label(ac_update_screen, text="(in Hours)").place(x = 80, y = 280)

    Button(ac_update_screen, text=" UPDATE ", height=2, command=update_ac_verify).place(x = 200, y = 300)
## End of updateac()

def update_ac_verify():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
      )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
     
    sql = "SELECT COUNT(TYPE) FROM Aircraft WHERE AC_ID = %s"
    val = (int(auid.get()),)
    count = 0
    try:
        cursor.execute(sql,val)
        for x in cursor:
            count = x[0];
      
    except mysql.connector.Error:
        print ("Error")
        
    print("Row count: ",count)    
    if (count == 1):
            sql1 = "UPDATE Aircraft SET TYPE = %s, SEAT_CAPACITY = %s,\
             FUEL_TANK = %s, REQUIRED_FT = %s \
                 WHERE AC_ID = %s"
            val1 = (acutype.get(),int(acu_capacity.get()),int(acu_fuel.get()),int(acu_ft_req.get()),int(auid.get()))
         
            try:
                cursor.execute(sql1, val1)
                mydb.commit()
                messagebox.showinfo("Success", "Operation Successful\n1 row Updated")
            except mysql.connector.Error:
                mydb.rollback()
                # Display messagebox to login   
                messagebox.showinfo("ERROR", "Can't Update !!!\n Check values")
    else:
        messagebox.showinfo("ERROR", "Can't Update !!!\n Aircraft ID does not exists")
    
    mydb.close()
    ac_update_screen.destroy() 
## End of update_ac_verify()

def updatecrew():
   global cu_details_screen 
   cu_details_screen = Toplevel(root)   ###  ????
   cu_details_screen.title("Update Crew")
   cu_details_screen.geometry("400x300")
   cu_details_screen.iconbitmap(r'ac.ico')
   
   Label(cu_details_screen, text="Please enter Crew details", font=('Times',12,'bold','italic')).place(x = 120, y = 10)
   Label(cu_details_screen, text="* indicates value required", font=('Times',12, 'bold','italic')).place(x = 120, y = 30)
 
   global cuid
   global cuname
   global cu_mno 
   global cu_ft

   cuid = StringVar()
   cuname = StringVar()
   cu_mno = StringVar()
   cu_ft = StringVar()
 
   Label(cu_details_screen, text="Employee ID * ").place(x = 20, y = 80)
   cu_id_entry = Entry(cu_details_screen, width = 10, textvariable=cuid)
   cu_id_entry.place(x = 100, y = 80)

   Label(cu_details_screen, text="Name").place(x = 200, y = 80)
   cu_type_entry = Entry(cu_details_screen, textvariable=cuname)
   cu_type_entry.place(x = 240, y = 80)

   Label(cu_details_screen, text="Mobile").place(x = 20, y = 160)
   cu_mno_entry = Entry(cu_details_screen, width = 10, textvariable=cu_mno)
   cu_mno_entry.place(x = 80, y = 160)

   Label(cu_details_screen, text="Comleted\nFlight Time").place(x = 200, y = 150)
   cu_ft_entry = Entry(cu_details_screen, width = 10, textvariable=cu_ft)
   cu_ft_entry.place(x = 270, y = 160)
   Label(cu_details_screen, text="(in Hours)").place(x = 200, y = 180)

   Button(cu_details_screen, text=" UPDATE ", height=2, command=update_crew_verify).place(x = 170, y = 220)
## End of updatecrew()

def update_crew_verify():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
      )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    
    sql = "SELECT COUNT(ENAME) FROM Crew WHERE EMPID = %s"
    val = (cuid.get(),)
    count = 0
    
    try:
        cursor.execute(sql,val)
        for x in cursor:
            count = x[0];
    except mysql.connector.Error:
        print ("Error")
    
    print("Count: ", count)
    if (count == 1):
         sql1 = "UPDATE Crew SET ENAME = %s, MOBILE_NO = %s, \
             FLIGHT_TIME_HRS = %s WHERE EMPID = %s"
         val1 = (cuname.get(),cu_mno.get(),int(cu_ft.get()),cuid.get())
         try:
             cursor.execute(sql1, val1)
             mydb.commit()
             messagebox.showinfo("Success", "Operation Successful\n1 row Updated")
         except mysql.connector.Error:
             mydb.rollback()
             messagebox.showinfo("ERROR", "Can't Update !!!\n Check values")
    else:
         # Display messagebox to login   
         messagebox.showinfo("ERROR", "Can't Update !!!\n Employee ID does not exists")
    mydb.close()
    cu_details_screen.destroy() 
## End of update_crew_verify()

def updatevendor():
    global vu_details_screen 
    vu_details_screen = Toplevel(root)   ###  ????
    vu_details_screen.title("Update Vendor")
    vu_details_screen.geometry("400x300")
    vu_details_screen.iconbitmap(r'ac.ico')
    
    Label(vu_details_screen, text="Please enter Vendor details for Updation", font=('Times',12,'bold','italic')).place(x = 120, y = 10)
    Label(vu_details_screen, text="* indicates value required", font=('Times',12, 'bold','italic')).place(x = 120, y = 30)
 
    global vuid
    global vuname
    global vu_mno 
    global vu_email

    vuid = StringVar()
    vuname = StringVar()
    vu_mno = StringVar()
    vu_email = StringVar()
 
    Label(vu_details_screen, text="Vendor ID * ").place(x = 20, y = 80)
    vu_id_entry = Entry(vu_details_screen, width = 10, textvariable=vuid)
    vu_id_entry.place(x = 100, y = 80)

    Label(vu_details_screen, text="Name").place(x = 200, y = 80)
    vu_type_entry = Entry(vu_details_screen, textvariable=vuname)
    vu_type_entry.place(x = 240, y = 80)

    Label(vu_details_screen, text="Mobile").place(x = 20, y = 160)
    vu_mno_entry = Entry(vu_details_screen, width = 10, textvariable=vu_mno)
    vu_mno_entry.place(x = 80, y = 160)

    Label(vu_details_screen, text="Email").place(x = 200, y = 160)
    vu_email_entry = Entry(vu_details_screen, textvariable=vu_email)
    vu_email_entry.place(x = 240, y = 160)

    Button(vu_details_screen, text=" UPDATE ", height=2, command=update_vendor_verify).place(x = 160, y = 220)
## End of updatevendor()

def update_vendor_verify():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
      )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    sql = "SELECT COUNT(VNAME) FROM Vendor WHERE VID = %s"
    val = (vuid.get(),)
    count = 0
    
    try:
        cursor.execute(sql,val)
        for x in cursor:
            count = x[0];
    except mysql.connector.Error:
        print ("Error")
        
    if (count == 1):
        try:
            sql1 = "UPDATE Vendor SET VNAME = %s,MOBILE_NO = %s,EMAIL = %s WHERE VID = %s"
            val1 = (vuname.get(),vu_mno.get(),vu_email.get(),vuid.get())
            cursor.execute(sql1, val1)
            mydb.commit()
            messagebox.showinfo("Success", "Operation Successful\n 1 row Updated")
        except mysql.connector.Error:
            mydb.rollback()
            # Display messagebox to login   
            messagebox.showinfo("ERROR", "Can't Update !!!\n Vendor ID does not exists")
    mydb.close()
    vu_details_screen.destroy() 
## End of update_vendor_verify()

def assigncrew():
    global assign_details_screen 
    
    assign_details_screen = Toplevel(root)   ###  ????
    assign_details_screen.title("Assign")
    assign_details_screen.geometry("400x300")
    assign_details_screen.iconbitmap(r'ac.ico')
    
    Label(assign_details_screen, text="Please enter Aircraft ID\nAnd\nEmployee ID of Crew Vendor details", font=('Times',11,'bold','italic')).place(x = 90, y = 10)
    Label(assign_details_screen, text="(* indicates value required)", font=('Times',11, 'bold','italic')).place(x = 120, y = 70)
 
    global ac_id
    global emp_id

    ac_id = StringVar()
    emp_id = StringVar()
 
    Label(assign_details_screen, text="Aircraft ID *").place(x = 20, y = 140)
    ac_id_entry = Entry(assign_details_screen, width = 10, textvariable=ac_id)
    ac_id_entry.place(x = 90, y = 140)

    Label(assign_details_screen, text="Employee ID *").place(x = 200, y = 140)
    emp_id_entry = Entry(assign_details_screen, width = 10, textvariable=emp_id)
    emp_id_entry.place(x = 280, y = 140)

    Button(assign_details_screen, text=" Help\nAircraft ", height=3, command=display_ac_data).place(x = 90, y = 220)
    Button(assign_details_screen, text="  Help\n  Crew  ", height=3, command=display_crew_data).place(x = 160, y = 220)
    Button(assign_details_screen, text=" Assign ", height=3, command=assign_data).place(x = 230, y = 220)
## End of assigncrew()

def display_ac_data():
    global display_screen
    display_screen = Toplevel(assign_details_screen )
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    sql = "SELECT AC_ID, TYPE, REQUIRED_FT FROM Aircraft"
    lst = []
    val = ('AC ID', 'TYPE', 'REQ FT(hrs)')
    lst.append(val)
    cursor.execute(sql)
    for x in cursor:
        lst.append(x)
 
# find total number of rows and
# columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    for i in range(total_rows):
      for j in range(total_columns):
         e = Entry(display_screen, width=20, fg='blue',font=('Arial',10,'bold'))
         e.grid(row=i, column=j)
         e.insert(END, lst[i][j])
## End of display_ac_data
         
def display_crew_data():
    global display_screen
    display_screen = Toplevel(assign_details_screen )
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    sql = "SELECT EMPID, ENAME, FLIGHT_TIME_HRS FROM Crew"
    lst = []
    val = ('EMPID', 'NAME', 'FLIGHT TIME(HRS)')
    lst.append(val)
    cursor.execute(sql)
    for x in cursor:
        lst.append(x)
 
# find total number of rows and
# columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    for i in range(total_rows):
      for j in range(total_columns):
         e = Entry(display_screen, width=20, fg='blue',font=('Arial',10,'bold'))
         e.grid(row=i, column=j)
         e.insert(END, lst[i][j])
## End of display_crew_data()

def assign_data():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    
    sql = "INSERT INTO Assign(AC_ID,EMPID) VALUES(%s, %s)"
    val = (int(ac_id.get()), emp_id.get())
    print("Assign : ",val)
    try:
        cursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success", "Operation Successful!\n1 row inserted")
    except mysql.connector.Error as e:
         print(e)
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Insert !!!\nInvalid ID's\nPress HELP for assistance")
    mydb.close()
    assign_details_screen.destroy()
## End of assign_data()

def reminder_vendor():
    
    remind_screen = Toplevel(root)
    remind_screen.title("Send Reminders to Vendors")
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    today = datetime.datetime.now()
    yy = today.year
    mm = today.month - 1
    dd = today.day
    print(today, yy, mm, dd)
    sql = "SELECT VID FROM Maintenance WHERE\
        (MONTH(LAST_SERVE) < %s AND \
         DAY(LAST_SERVE) < %s) OR\
         (YEAR(LAST_SERVE)< %s) GROUP BY VID"  
    val=(mm,dd,yy)
    lst = []  
    lstemail = []
    try:
        cursor.execute(sql,val)
        for x in cursor:
            lst.append(x)
        print("Reminder list: ",lst)
    except mysql.connector.Error as e:
        print("Reminder list:",e)
    try:    
        sql1 = "SELECT VNAME,EMAIL FROM Vendor WHERE VID = %s"    
        for i in lst:
            cursor.execute(sql1,i)
            for j in cursor:
                lstemail.append(j)
        # find total number of rows and
        # columns in list
        total_rows = len(lstemail)
        print("Print :",lstemail)
        if(total_rows!=0) :
           total_columns = len(lstemail[0])

           for i in range(total_rows):
              for j in range(total_columns):
                  e = Entry(remind_screen, width=30, fg='blue',font=('Arial',10,'bold'))
                  e.grid(row=i, column=j)
                  e.insert(END, lstemail[i][j])
        else:
            messagebox.showinfo("Success", "No Pending Aircraft Service")
    except mysql.connector.Error as e:
        print(e)
        messagebox.showinfo("ERROR","ERROR!!!")
    
## End of reminder_vendor()

def terminate_amc():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")   
    cursor.execute("SELECT AC_ID, VID FROM Maintenance WHERE CONTRACT_END_DATE < CURDATE()")
    
    lst = []
    for x in cursor:
        lst.append(x)
    size = len(lst)
    print("size: ",size)
    sql = "DELETE FROM Maintenance WHERE AC_ID = %s AND VID = %s"
    try:
        for i in range(size):
           cursor.execute(sql,lst[i])
           mydb.commit();
           print("Terminated AMC (AC_ID, VID):  ",lst[i]) 
        messagebox.showinfo("SUCCESS", "Terminated Overdue AMCs")
    except mysql.connector.Error as e:
        print(e)
        messagebox.showinfo("ERROR", "Check Aircraft & Vendor IDs")
    mydb.close()
## End of terminate_amc()


def updateamc():
    
    global amc_update_screen 
    amc_update_screen = Toplevel(root)   ###  ????
    amc_update_screen.title("Update Amc")
    amc_update_screen.geometry("400x300")
    amc_update_screen.iconbitmap(r'ac.ico')
    
    Label(amc_update_screen, text="Please enter AMC details for Updation", font=('Times',11,'bold','italic')).place(x = 100, y = 20)
    Label(amc_update_screen, text="(* indicates value required)", font=('Times',11, 'bold','italic')).place(x = 120, y = 40)

    global auac_id
    global auv_id
    global last_ser

    auac_id = StringVar()
    auv_id = StringVar()
    last_ser = StringVar()

    Label(amc_update_screen, text="Aircraft ID *").place(x = 20, y = 120)
    auc_id_entry = Entry(amc_update_screen, width = 10, textvariable=auac_id)
    auc_id_entry.place(x = 90, y = 120)

    Label(amc_update_screen, text="Vendor ID *").place(x = 200, y = 120)
    avu_id_entry = Entry(amc_update_screen, width = 10, textvariable=auv_id)
    avu_id_entry.place(x = 280, y = 120)

    Label(amc_update_screen, text="Last Serviced ").place(x = 20, y = 180)
    aals_entry = Entry(amc_update_screen, width = 10, textvariable=last_ser)
    aals_entry.place(x = 100, y = 180)
    
    Label(amc_update_screen, text="(yyyy-mm-dd)").place(x = 15, y = 200)

    Button(amc_update_screen, text=" UPDATE ", height=3, command=update_amc_data).place(x = 160, y = 220)
    
## End of updateamc()

def update_amc_data():
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "DB123"
     )
     
    cursor = mydb.cursor()
    cursor.execute("USE ams2")
    
    sql = "UPDATE Maintenance SET LAST_SERVE = %s WHERE AC_ID = %s AND VID = %s"
    val = (last_ser.get(),int(auac_id.get()), auv_id.get())
    print(val)
    try:
         cursor.execute(sql, val)
         mydb.commit()
         messagebox.showinfo("Success", "Operation Successful!\n1 row Updated")
    except mysql.connector.Error as e:
         print(e)
         mydb.rollback()
         messagebox.showinfo("ERROR", "Can't Update !!!\nInvalid ID's")
    mydb.close()
    amc_update_screen.destroy()
    
## End of update_amc_data()

def main_user_menu_screen():
    global root
    root = Tk()
    menubar = Menu(root)
    root.title("Staff")
    root.geometry('400x300')
    root.iconbitmap(r'ac.ico') #set window's icon
    
    ntabmenu = Menu(menubar, tearoff=0)
    ntabmenu.add_command(label="Aircraft", command=addaircraft)
    ntabmenu.add_command(label="Crew", command=addcrew)
    ntabmenu.add_command(label="Vendor", command=addvendor)
    ntabmenu.add_command(label="AMC", command=addamc)

    ntabmenu.add_separator()

    ntabmenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="New", menu=ntabmenu)

    emenu = Menu(menubar, tearoff=0)
    emenu.add_command(label="Aircraft", command=updateac)
    emenu.add_command(label="Crew", command=updatecrew)
    emenu.add_command(label="Vendor", command=updatevendor)
    emenu.add_command(label="AMC", command=updateamc)
    menubar.add_cascade(label="Edit", menu=emenu)

    othersmenu = Menu(menubar, tearoff=0)
    othersmenu.add_command(label="Assign", command=assigncrew)
    othersmenu.add_command(label="Reminder", command=reminder_vendor)
    othersmenu.add_command(label="Terminate AMC", command=terminate_amc)

    menubar.add_cascade(label="Others", menu=othersmenu)

    root.config(menu=menubar)
    root.mainloop()
### End of main_user_menu_screen()