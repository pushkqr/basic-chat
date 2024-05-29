import firebase_admin
from firebase_admin import credentials, auth, db
from tkinter import *
import threading
from SendingApp import SendingApp
from ReceivingApp import ReceivingApp

BG = "#91C8E4"
CURR_USER = ""

cred = credentials.Certificate("serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://basic-chat-c0602-default-rtdb.asia-southeast1.firebasedatabase.app'
})

def signup():
    email = signup_mail_entry.get()
    password = signup_password_entry.get()
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        db.reference(f"messages/{email.replace('.', ',')}").set({"initialized": True})
        title.config(text="Sign-Up Successful! Please Log In.")
    except Exception as e:
        print("Signup failed:", e)
        title.config(text="Sign-Up Failed! Try Again.")
        status_label.config(text="Sign-Up Failed! Please check the details and try again.", fg="red")

def login():
    global CURR_USER
    email = login_mail_entry.get()
    password = login_password_entry.get()
    try:
        user = auth.get_user_by_email(email)
        CURR_USER = email.replace('.', ',')
        title.config(text="Successfully Logged In!")
        status_label.config(text="")
        hide_login_signup_widgets()
        open_chat_windows()
    except Exception as e:
        print("Login failed:", e)
        title.config(text="Login Failed! Try Again.")
        status_label.config(text="Login Failed! Invalid credentials.", fg="red")

def hide_login_signup_widgets():
    login_mail_label.grid_remove()
    login_mail_entry.grid_remove()
    login_password_label.grid_remove()
    login_password_entry.grid_remove()
    login_btn.grid_remove()
    signup_mail_label.grid_remove()
    signup_mail_entry.grid_remove()
    signup_password_label.grid_remove()
    signup_password_entry.grid_remove()
    signup_btn.grid_remove()
    window.withdraw()

def open_chat_windows():
    sending_thread = threading.Thread(target=sending_app, daemon=True)
    receiving_thread = threading.Thread(target=receiving_app, daemon=True)

    sending_thread.start()
    receiving_thread.start()

def sending_app():
    app = SendingApp(CURR_USER, db)
    app.root.mainloop()

def receiving_app():
    app = ReceivingApp(CURR_USER, db)
    app.root.mainloop()

window = Tk()
window.config(padx=55, pady=20, bg=BG)
window.minsize(450, 300)
window.title("Chat")
title = Label(text="Log-In / Sign-Up", font=("Amiri", 35, "bold italic"), bg=BG, fg="#213555")
title.grid(row=0, column=1, padx=30)

# Login widgets
login_mail_label = Label(text="Login Email:", bg=BG, fg="black")
login_mail_label.grid(row=1, column=0, pady=5)
login_mail_entry = Entry(width=30)
login_mail_entry.grid(row=1, column=1, pady=5)

login_password_label = Label(text="Login Password:", bg=BG, fg="black")
login_password_label.grid(row=2, column=0, pady=5)
login_password_entry = Entry(width=30, show="*")
login_password_entry.grid(row=2, column=1, pady=5)

login_btn = Button(text="Login", bg="lightblue", command=login, fg="black")
login_btn.grid(row=3, column=1, pady=5)

# Sign-up widgets
signup_mail_label = Label(text="Sign-Up Email:", bg=BG, fg="black")
signup_mail_label.grid(row=4, column=0, pady=5)
signup_mail_entry = Entry(width=30)
signup_mail_entry.grid(row=4, column=1, pady=5)

signup_password_label = Label(text="Sign-Up Password:", bg=BG, fg="black")
signup_password_label.grid(row=5, column=0, pady=5)
signup_password_entry = Entry(width=30, show="*")
signup_password_entry.grid(row=5,column=1, pady=5)

signup_btn = Button(text="Sign-Up", bg="lightgreen", command=signup, fg="black")
signup_btn.grid(row=6, column=1, pady=5)

status_label = Label(text="", bg=BG, fg="red")
status_label.grid(row=7, column=1, pady=5)

window.mainloop()
