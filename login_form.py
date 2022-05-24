from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
from course2 import login
class login_form:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management")
        self.root.geometry("400x600")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        self.bg_img = Image.open("login.png")
        self.bg_img = self.bg_img.resize((100, 100))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_imgg = Image.open("login2.png")
        self.bg_imgg = self.bg_imgg.resize((250, 80))
        self.bg_imgg = ImageTk.PhotoImage(self.bg_imgg)

        lbtitle = Label( font="arial 30 bold", bg="black")
        lbtitle.pack(pady=20, fill=X)
        lbtitle2=Label(lbtitle, image=self.bg_imgg, bg="black")
        lbtitle2.pack(fill=X, side="left")
        # bordercolor = Frame(self.root, bg="black", width=350, height=450)
        # bordercolor.pack()
        main = Label(self.root, bg="black", bd=0)
        main.place(x=0, y=90,width=600, height=900)
        mainframe= Label(self.root, image=self.bg_img, bd=0, bg="black")
        mainframe.place(x=140, y=90)

        Button(self.root, text="Login", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=self.login).place(
            x=100,
            y=460)

        Button(self.root, text="Reset", height="2", width=20, bg="#1089ff", fg="white", bd=0, command=self.reset).place(
            x=10,
            y=550)
        Button(self.root, text="Exit", height="2", width=20, bg="#00bd56", fg="white", bd=0,
               command=self.root.destroy).place(
            x=240, y=550)



    #
        self.username = Label(self.root, text="Username", font=("arial", 20, "bold"), fg="white", bg="black")
        self.password = Label(self.root, text="Password", font=("arial", 20, "bold"), fg="white", bg="black")
        self.username.place(x=120, y=190)
        self.password.place(x=120, y=310)

        self.username = StringVar()
        self.password = StringVar()

        self.entry_username = Entry(self.root, textvariable=self.username, width=12, bd=2, font=("arial", 25))
        self.entry_password = Entry(self.root, textvariable=self.password, width=12, bd=2, font=("arial", 25), show="*")

        self.entry_username.place(x=80, y=240)
        self.entry_password.place(x=80, y=360)

    def reset(self):
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
    def login(self):
        self.user = self.username.get()
        self.code = self.password.get()

        if self.user == "Lakhan" and self.code == "admin123":
            tmsg.showinfo("Valid", "Login successful")
            self.new_win = Toplevel(self.root)
            self.new_obj = login(self.new_win)

        # End of code
        elif self.user == "" and self.code == "":
            tmsg.showerror("Invalid", "Please enter the username and password")
        elif self.user == "":
            tmsg.showerror("Invalid", "Username is required")
        elif self.code == "":
            tmsg.showerror("Invalid", "Password field is required")
        elif self.user != "Lakhan" and self.code != "admin123":
            tmsg.showerror("Invalid", "Incorrect username and password")
        elif self.user != "Lakhan":
            tmsg.showerror("Invalid", "Please enter a valid username")
        elif self.code != "admin123":
            tmsg.showerror("Invalid", "Please enter a valid password")


if __name__=="__main__":
    root= Tk()
    obj=login_form(root)
    root.mainloop()