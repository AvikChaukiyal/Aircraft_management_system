# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:00:02 2022

@author: Avik Chaukiyal

"""

import tkinter as tk               #To create GUI
from loginadmin import * 
from loginuser import *

def buttonClick1(self):
    print("Admin Clicked")
    welcome_screen.destroy()
    main_account_screen()
    
def buttonClick2(self):
    print("Staff Clicked")
    welcome_screen.destroy()
    main_user_account_screen()
    
#create root Windows
global welcome_screen
welcome_screen = tk.Tk()
welcome_screen.title('AMS')
welcome_screen.iconbitmap(r'ac.ico')

# create frame as child to root window
f = tk.Frame(welcome_screen, height=500, width=600)

#let the frame will not shrink
f.propagate(0)

#attach frame to root window
f.pack()

#Display welcome message
t = tk.Label(f, text='Welcome\nto\nAircraft Management System', justify=tk.CENTER, 
             font=('Times', 30, 'bold', 'italic'), fg='maroon')
t.pack(side=tk.TOP, pady=50)

#create a bush button as child to frame
buttonAdmin = tk.Button(f, text='Admin', width=15, height=2, bg='yellow', fg='blue',
           activebackground='green', activeforeground='red')
buttonUser = tk.Button(f, text='Staff', width=15, height=2, bg='orange', fg='blue',
           activebackground='green', activeforeground='red')

buttonAdmin.pack(side=tk.LEFT, padx=50)
buttonUser.pack(side=tk.RIGHT, padx=50)

#bind left button to bottonClick()
buttonAdmin.bind('<Button-1>', buttonClick1)
buttonUser.bind('<Button-1>', buttonClick2)

# Display Name
t1 = tk.Label(f, text='Avik Chaukiyal\n', width=30,  
             font=('Times', 10, 'bold', 'italic'), fg='maroon')
t1.pack(side=tk.BOTTOM)
#root window handles mouse click event
welcome_screen.mainloop()
