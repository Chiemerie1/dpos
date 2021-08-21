from tkinter import *
import mysql.connector
from mysql.connector.errors import custom_error_exception



root = Tk()

# root.geometry("900x600")
root.title("POS Admin")
root.configure(background="gray29")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="N@nser1234",
    database="dpos"
)
#print(db)

cursor = db.cursor()
#cursor.execute("CREATE DATABASE dpos")

# cursor.execute("CREATE TABLE customers (user_id INT AUTO_INCREMENT PRIMARY KEY, \
#     first_name VARCHAR(50), \
#     last_name VARCHAR(50),  \
#     username VARCHAR(15), \
#     designation VARCHAR(15))")

# cursor.execute("CREATE TABLE products (product_id INT AUTO_INCREMENT PRIMARY KEY, \
#     name VARCHAR(100), \
#     category VARCHAR(100), \
#     price INT(10))")

# cursor.execute("ALTER TABLE customers RENAME to users")

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

# cursor.execute("SELECT * FROM users")
# for x in cursor.description:
#     print (x)

# cursor.execute("SELECT * FROM products")
# for x in cursor.description:
#     print (x)

#functions
#clear fields
def clear_uentry():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    un_entry.delete(0, END)
    tt_entry.delete(0, END)

def clear_pentry():
    pn_entry.delete(0, END)
    pnum_entry.delete(0, END)
    pcat_entry.delete(0, END)
    price_entry.delete(0, END)

#submit to database
def u_submit():
    sql_code = "INSERT INTO users (first_name, last_name, username, designation) VALUES (%s, %s, %s, %s )"
    values = (fn_entry.get(),
                ln_entry.get(),
                un_entry.get(),
                tt_entry.get()
            )
    cursor.execute(sql_code, values)
    db.commit()
    clear_uentry()

def p_submit():
    sql_code = "INSERT INTO products (name, category, price) VALUES (%s, %s, %s)"
    values = (pn_entry.get(),
                #pnum_entry.get(),
                pcat_entry.get(),
                price_entry.get()
            )
    cursor.execute(sql_code, values)
    db.commit()
    clear_pentry()



title_label = Label(root, text="Admin Console", fg="white", bg="gray29")
title_label.grid(row=0, pady=10)
#frames
frame1 = LabelFrame(root, bg="grey", text="Users")
frame2 = LabelFrame(root, bg="grey", text="Products")

frame1.grid(row=1, column=0, padx=10, pady=5)
frame2.grid(row=1, column=1, padx=10, pady=5)

fn_label = Label(frame1, text="First name", padx=10, pady=5, bg="grey")
ln_label = Label(frame1, text="Last name", padx=10, pady=5, bg="grey")
un_label = Label(frame1, text="Username", padx=10, pady=5, bg="grey")
tt_label = Label(frame1, text="Title", padx=10, pady=5, bg="grey")

fn_label.grid(row=0, column=1, padx=10, pady=5)
ln_label.grid(row=1, column=1, padx=10, pady=5)
un_label.grid(row=2, column=1, padx=10, pady=5)
tt_label.grid(row=3, column=1, padx=10, pady=5, sticky=W)

fn_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
ln_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
un_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
tt_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")

fn_entry.grid(row=0, column=2, padx= 10)
ln_entry.grid(row=1, column=2, padx= 10)
un_entry.grid(row=2, column=2, padx= 10)
tt_entry.grid(row=3, column=2, padx= 10)

user_submit = Button(frame1, text="Submit", command=u_submit, border=2, width=10, fg="white", bg="medium sea green")
user_submit.grid(row=4, column=1, padx=10, pady=5)

uclear_btn = Button(frame1, text="clear", border=2, command=clear_uentry, width=10,  bg="navajowhite4", fg="white")
uclear_btn.grid(row=4, column=2, padx=10, pady=5)

pn_label = Label(frame2, text="Name", padx=10, pady=5, bg="grey")
pnum_label = Label(frame2, text="Number", padx=10, pady=5, bg="grey")
pcat_label = Label(frame2, text="Category", padx=10, pady=5, bg="grey")
price_label = Label(frame2, text="Price", padx=10, pady=5, bg="grey")

pn_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)
pnum_label.grid(row=1, column=1, padx=10, pady=5, sticky=W)
pcat_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)
price_label.grid(row=3, column=1, padx=10, pady=5, sticky=W)

pn_entry = Entry(frame2, borderwidth=2, bg="gray30", fg="white")
pnum_entry = Entry(frame2, borderwidth=2, bg="gray30", fg="white")
pcat_entry = Entry(frame2, borderwidth=2, bg="gray30", fg="white")
price_entry = Entry(frame2, borderwidth=2, bg="gray30", fg="white")

pn_entry.grid(row=0, column=2, padx= 10)
pnum_entry.grid(row=1, column=2, padx= 10)
pcat_entry.grid(row=2, column=2, padx= 10)
price_entry.grid(row=3, column=2, padx= 10)

product_submit = Button(frame2, text="Submit", border=2, width=10, command=p_submit, fg="white", bg="medium sea green")
product_submit.grid(row=4, column=1, padx=10, pady=5)
pclear_btn = Button(frame2, text="clear", border=2, width=10, command=clear_pentry, bg="navajowhite4", fg="white")
pclear_btn.grid(row=4, column=2, padx=10, pady=5)


#Checking database
# cursor.execute("SELECT * FROM users")
# response = cursor.fetchall()
# for x in response:
#     print(x[2])

# cursor.execute("SELECT * FROM products")
# response = cursor.fetchall()
# for x in response:
#     print(x)














root.mainloop()