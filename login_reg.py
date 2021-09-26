# import

from tkinter import *
import os
from tkinter import messagebox
from management_sys import login_page



def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("310x230")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="orange",font=("Times", "15", "bold italic")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username  ",font=("Times", "12", "bold"))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username,font=("Times", "12", "bold"))
    username_entry.pack()
    password_lable = Label(register_screen, text="Password  ",font=("Times", "12", "bold"))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password,font=("Times", "12", "bold"))
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1 ,font=("Times", "12", "bold"), command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("310x230")
    Label(login_screen, text="Enter the details  to login",font=("Times", "15", "bold italic")).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username  ",font=("Times", "12", "bold")).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify,font=("Times", "12", "bold"))
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password  ",font=("Times", "12", "bold")).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify,font=("Times", "12", "bold"))
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, font=("Times", "12", "bold"),command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Success","Registration Success")

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

#popup for login sucess

def login_sucess():
    global login_success_screen
    messagebox.showinfo("Login","Login Success")
    login_page()

#popup for password not recognised

def password_not_recognised():
    global password_not_recognised_screen
    messagebox.showinfo("Incorrect", "Password Not Recognised")

# popup for user not found

def user_not_found():
    global user_not_found_screen
    messagebox.showinfo("Not found","User not found")

# clearing popup

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recognised_screen.destroy()


def delete_user_not_found():
    user_not_found_screen.destroy()

# designing main window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("310x230")
    main_screen.title("Login Or Registration")
    Label(text="Login Or Registration",height ="2", bg="orange", width="310",font=("Times", "15", "bold italic")).pack()
    Label(text="").pack()
    Button(text="Login", height="1", width="28",font=("Times", "12", "bold"), command=login).pack()
    Label(text="").pack()
    Button(text="Register",height="1", width="28",font=("Times", "12", "bold"), command=register).pack()

    main_screen.mainloop()


main_account_screen()