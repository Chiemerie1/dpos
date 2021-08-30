from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

root = Tk()

root.geometry("900x600")
root.title("user login")
root.configure(background="white")

style = ttk.Style()
style.theme_use("clam")


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="N@nser1234",
    database="dpos"
)
#print(db)

user_cursor = db.cursor()

user_query = "SELECT * FROM users"


#############fn################
#login


def login():
    username = name_txt.get()
    password = pwd_txt.get()
    user_cursor.execute(user_query)
    users_info = user_cursor.fetchall()
    for users in users_info:
        if username == users[3] and password == users[5]:
            notify.config(text="successful")
        else:
            notify.config(text="Wrong credential. Contact Admin")


page_title = Label(root, text="User Login", font=("Times", 16), bg="white")
page_title.pack(ipadx=10, ipady=10)

logo_img = Image.open("images/user_logo.png")
resized = logo_img.resize((200, 200), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resized)
logo_label = Label(root, image=logo, bg="white")
logo_label.pack(padx=10, pady=10)

login_frame = LabelFrame(root, text="Login", padx=10, pady=10, font="Times",
                            bg="white")
login_frame.pack()

name_txt = Entry(login_frame, bg="gray17", fg="white", font="Times")
name_txt.pack(padx=10, pady=10)
name_txt.insert(0, "name")

pwd_txt = Entry(login_frame, bg="gray17", fg="white", font="Times")
pwd_txt.pack(padx=10, pady=10)
pwd_txt.insert(0, "password")

login_btn = Button(login_frame, text="login", command=login, width=15, fg="white",
                    bg="dodgerblue2")
login_btn.pack(padx=10, pady=10)

notify = Label(root, text="", font="Times", fg="red", bg="white")
notify.pack(padx=10, pady=10)

















root.mainloop()