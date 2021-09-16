from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector


root = Tk()
root.configure(background="white")
root.title("user console")
root.geometry("1000x700")





db = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="N@nser1234",
    database="dpos"
)
#print(db)

user_cursor = db.cursor()



page_title = Label(root, text="User Console", padx=10, pady=10, bg="white")
page_title.grid(row=0, column=0, columnspan=4)

category_frame = LabelFrame(root, text="category", padx=10, pady=10, height=300)
frame2 = LabelFrame(root, text="frame2", padx=10, pady=10, height=200)
frame3 = LabelFrame(root, text="frame3", padx=10, pady=10, height=200)
frame4 = LabelFrame(root, text="frame4", padx=10,pady=10, height=200)

category_frame.grid(row=1, column=0, padx=20)
frame2.grid(row=1, column=1)
frame3.grid(row=1, column=2)
frame4.grid(row=1, column=3)

category_list = Listbox(category_frame, width=30)
category_list.grid(row=0, column=0, padx=5, pady=5)

query = "SELECT category FROM products"
user_cursor.execute(query)
category = user_cursor.fetchall()
_list = []
for x in category:
    _list.append(x)
_list = set(_list)
print(_list)
for x in _list:
    category_list.insert(END, x)










root.mainloop()