from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


root = Tk()
root.geometry("900x600")
root.title("Admin")
root.configure(background="white")



##############styling#################
style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background="white",
                foreground="black")
style.configure('TNotebook.Tab', background="dodgerblue2")
style.map("TNotebook", background= [("selected", "dodgerblue2")])



#database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="N@nser1234",
    database="dpos"
)
#print(db)

cursor = db.cursor()
#cursor.execute("CREATE DATABASE dpos")

cursor.execute("CREATE TABLE  IF NOT EXISTS customers (user_id INT AUTO_INCREMENT PRIMARY KEY, \
    first_name VARCHAR(50), \
    last_name VARCHAR(50),  \
    username VARCHAR(15), \
    designation VARCHAR(15))")

cursor.execute("CREATE TABLE  IF NOT EXISTS products (product_id INT AUTO_INCREMENT PRIMARY KEY, \
    name VARCHAR(100), \
    category VARCHAR(100), \
    price INT(10))")


#messages
def msg_info():
    messagebox.showinfo("success", "submitted successfully")
def msg_error():
    messagebox.showerror("error", "Name not entered")

################ users ##################
#functions
#clear fields

def clear_uentry():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    un_entry.delete(0, END)
    tt_entry.delete(0, END)
    pwd_entry.delete(0, END)

#submit to database
def u_submit():
    sql_code = "INSERT INTO users (first_name, last_name, username, designation, password) VALUES (%s, %s, %s, %s, %s )"
    values = (fn_entry.get(),
                ln_entry.get(),
                un_entry.get(),
                tt_entry.get(),
                pwd_entry.get()
            )
    if len(fn_entry.get()) != 0:
        cursor.execute(sql_code, values)
        db.commit()
        clear_uentry()
        msg_info()
    else:
        msg_error()


admin_title = Label(root, text="Admin Console", padx=10, pady=10,
            font=("Sans", 14), bg="white")

admin_title.grid(row=0, column=0, columnspan=4)

admin_tab = ttk.Notebook(root, width=800, height=400, padding=(20,0,0,0))
admin_tab.grid(row=1, column=0, columnspan=4)

users_tab = Frame(admin_tab, width=900, height=600, bg="white")
#users_tab["padding"] = 10
users_tab.pack(fill=BOTH, expand=True)

products_tab = Frame(admin_tab, width=900, height=600, bg="white")
#products_tab["padding"] = 10
products_tab.pack(fill=BOTH, expand=True)

admin_tab.add(users_tab, text="Users")
admin_tab.add(products_tab, text="Products")

frame1 = LabelFrame(users_tab, text="Users", bg="white")
frame1.grid(row=1, column=0, padx=10, pady=5, ipadx=50)

#users
fn_label = Label(frame1, text="First name", padx=10, pady=5, bg="white")
ln_label = Label(frame1, text="Last name", padx=10, pady=5, bg="white")
un_label = Label(frame1, text="Username", padx=10, pady=5, bg="white")
tt_label = Label(frame1, text="Title", padx=10, pady=5, bg="white")
pwd_label = Label(frame1, text="Password", padx=10, pady=5, bg="white")

fn_label.grid(row=0, column=1, padx=10, pady=5)
ln_label.grid(row=1, column=1, padx=10, pady=5)
un_label.grid(row=2, column=1, padx=10, pady=5)
tt_label.grid(row=3, column=1, padx=10, pady=5, sticky=W)
pwd_label.grid(row=4, column=1, padx=10, pady=5, sticky=W)

fn_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
ln_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
un_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
tt_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")
pwd_entry = Entry(frame1, borderwidth=2, bg="gray30", fg="white")

fn_entry.grid(row=0, column=2, padx= 10)
ln_entry.grid(row=1, column=2, padx= 10)
un_entry.grid(row=2, column=2, padx= 10)
tt_entry.grid(row=3, column=2, padx= 10)
pwd_entry.grid(row=4, column=2, padx= 10)

user_submit = Button(frame1, text="Submit", command=u_submit, border=2, width=10,
                        fg="white", bg="dodgerblue2")
user_submit.grid(row=5, column=1, padx=10, pady=5)

uclear_btn = Button(frame1, text="clear", border=2, command=clear_uentry, width=10,
                    bg="gray19", fg="white")
uclear_btn.grid(row=5, column=2, padx=10, pady=5)

user_info_frame = LabelFrame(users_tab, text="personel information",
                        bg="white", padx=10)
user_info_frame.grid(row=1, column=1, padx=5, pady=5, ipadx=50)
user_list = Listbox(user_info_frame, bg="gray9", font="Times", fg="White", width=30,
                    highlightcolor="gray30")
user_list.pack(pady=5, padx=10)

########### delete user ############
del_user_entry = Entry(users_tab, borderwidth=2, bg="gray30", fg="white")
del_user_entry.grid(row=2, column=0, pady=10)
text='enter name to delete'
del_user_entry.insert(0, text)

del_user_notification = Label(users_tab, borderwidth=2, text="", bg="white", fg="gray30")
del_user_notification.grid(row=3, column=0, pady=10)

def del_user():
    del_query = "DELETE FROM users WHERE first_name = %s"
    first_name = (del_user_entry.get(),)
    cursor.execute(del_query, first_name)
    db.commit()
    del_user_entry.delete(0, END)
    del_user_entry.insert(0, text)
    del_user_notification.config(text="User Deleted")

########### delete product ############
del_prod_entry = Entry(products_tab, borderwidth=2, bg="gray30", fg="white")
del_prod_entry.grid(row=2, column=0, pady=10)
del_prod_entry.insert(0, "enter product to delete")

del_prod_notification = Label(products_tab, borderwidth=2, text="", bg="white", fg="gray30")
del_prod_notification.grid(row=3, column=0, pady=10)

def del_product():
    del_query = "DELETE FROM products WHERE name = %s"
    name = (del_prod_entry.get(),)
    cursor.execute(del_query, name)
    db.commit()
    del_prod_entry.delete(0, END)
    del_prod_entry.insert(0, "enter product to delete")
    del_prod_notification.config(text="Product Deleted")


################ product ##################

def clear_pentry():
    pn_entry.delete(0, END)
    pnum_entry.delete(0, END)
    pcat_entry.delete(0, END)
    price_entry.delete(0, END)

def p_submit():
    sql_code = "INSERT INTO products (name, category, price) VALUES (%s, %s, %s)"
    values = (pn_entry.get(),
                #pnum_entry.get(),
                pcat_entry.get(),
                price_entry.get()
                )
    if len(pn_entry.get()) != 0:
        cursor.execute(sql_code, values)
        db.commit()
        clear_pentry()
        msg_info()
    else:
        msg_error()



frame2 = LabelFrame(products_tab, text="Products", bg="white")
frame2.grid(row=1, column=0, padx=10, pady=5, ipadx=50)

pn_label = Label(frame2, text="Name", padx=10, pady=5, bg="white")
pnum_label = Label(frame2, text="Number", padx=10, pady=5, bg="white")
pcat_label = Label(frame2, text="Category", padx=10, pady=5, bg="white")
price_label = Label(frame2, text="Price", padx=10, pady=5, bg="white")

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

product_submit = Button(frame2, text="Submit", border=2, width=10, command=p_submit, fg="white", bg="dodgerblue2")
product_submit.grid(row=4, column=1, padx=10, pady=5)

pclear_btn = Button(frame2, text="clear", border=2, width=10, command=clear_pentry, bg="gray19", fg="white")
pclear_btn.grid(row=4, column=2, padx=10, pady=5)

product_info_frame = LabelFrame(products_tab, text="product information", padx=10, bg="white")
product_info_frame.grid(row=1, column=1, padx=10, pady=5, ipadx=50)
# show_product_info = Label(product_info_frame, text="here", bg="sea green", fg="white", font="Times")
# show_product_info.pack(padx=10, pady=10)

prod_list = Listbox(product_info_frame, bg="gray9", font="Times", fg="White", width=30,
                    highlightcolor="gray30")
prod_list.pack(pady=5, padx=10)



#displaying data
def user_info_btn():
    cursor.execute("SELECT * FROM users")
    users_info = cursor.fetchall()
    for user in users_info:
        user_list.insert(END, f"Name:  {user[1]}. Role:  {user[4]}")

# product query
product_query = "SELECT * FROM products"

def product_info_button():
    cursor.execute(product_query)
    product_info = cursor.fetchall()
    for product in product_info:
        prod_list.insert(END, f"{product[1]}   NGN {product[3]}")
        #show_product_info.config(text=product)

#display buttons
display_user_btn = Button(root, text="show users", command=user_info_btn,
                            bg="dodgerblue2", fg="white")
display_user_btn.grid(row=2, column=0, pady=5)

product_user_btn = Button(root, text="show product", command=product_info_button,
                            bg="dodgerblue2", fg="white")
product_user_btn.grid(row=2, column=1, pady=5)
remove_user_btn = Button(root, text="Remove User", bg="dodgerblue2", command=del_user, fg="white")
remove_user_btn.grid(row=2, column=2)
remove_user_btn = Button(root, text="Remove product", command=del_product, bg="dodgerblue2", fg="white")
remove_user_btn.grid(row=2, column=3)














root.mainloop()