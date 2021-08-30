from tkinter import *
from PIL import ImageTk,Image
import mysql.connector



root = Tk()

root.geometry("900x600")
root.title("Admin login")
root.configure(background="white")


#database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="N@nser1234",
    database="dpos"
)
#print(db)

admin_cursor = db.cursor()
#cursor.execute("CREATE DATABASE dpos")

admin_cursor.execute("CREATE TABLE IF NOT EXISTS admin (admin_id INT AUTO_INCREMENT PRIMARY KEY, \
    username VARCHAR(50), \
    password VARCHAR(50),  \
    admin VARCHAR(15))")

admin_query = "SELECT * FROM admin"

#function defs
#logging in
def login():
    username = name_txt.get()
    pwd = pwd_txt.get()
    admin_cursor.execute(admin_query)
    admin_info = admin_cursor.fetchall()
    for admin in admin_info:
        if username == admin[1] and pwd == admin[2]:
            # notify.config(text="It is what it is")
            root.destroy()
            import admin_console_2
        else:
            notify.config(text="wrong cred")






page_title = Label(root, text="Admin Login", font=("Times", 20), bg="white")
page_title.pack(ipadx=10, ipady=10)

logo_img = Image.open("images/pos_logo.png")
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

login_btn = Button(login_frame, text="login", width=15, command=login, fg="white",
                    bg="dodgerblue2")
login_btn.pack(padx=10, pady=10)

notify = Label(root, text="", font="Times", fg="red", bg="white")
notify.pack(padx=10, pady=10)







root.mainloop()