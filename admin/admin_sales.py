from tkinter import *


root = Tk()
root.geometry("1000x700")
root.title("Admin sales")
root.configure(background="white")



page_title = Label(root, text="Sales", bg="white", padx=5, pady=5, font=(16))
page_title.grid(row=0, column=0)

########## back button #########
def back():
    root.destroy()
    import admin_console_2

back_btn = Button(root, text="Back", bg="dodgerblue3", command=back, fg="white")
back_btn.grid(row=1, column=0)


root.mainloop()