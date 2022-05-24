from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql


class CourseClass:

    def __init__(self,root):
        self.root = root
        self.root.title("Student attendance")
        self.root.geometry("1920x1080+0+0")
        self.bd=ImageTk.PhotoImage(file="cimag.jpg")
        self.bd_image=Label(self.root, image=self.bd).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Student Attendance", relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="blue", fg="white")
        title.pack(side=TOP, fill=X)


        # =====All variables=============
        self.student_var=StringVar()
        self.Roll_No_var=StringVar()
        self.branch_var=StringVar()
        self.email_var=StringVar()
        self.attendance_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



        # # ================Manage Frame====================
        #
        First_Frame = Frame(self.root, bd=4, relief=SUNKEN, bg="grey")
        First_Frame.place(x=250, y=90, width=750, height=700)

        # ============Labels====================

        m_title = Label(First_Frame, text="Student:", bg="grey", fg="black", font=("Helvetica", 25, "bold"))
        m_title.grid(row=0, columnspan=2, pady=30, padx=10)

        # #============setting up first Entry================

        entryfram = Entry(First_Frame,textvariable=self.student_var, font=("times new roman", 20, "bold"), bd=5,
                          relief=GROOVE)
        entryfram.grid(row=0, column=2, sticky="w", padx=20)
        #
        # #===========setting up second frame===========
        #
        b_title = Label(First_Frame, text="Roll No:", bg="grey", fg="black", font=("Helvetica", 25, "bold"))
        b_title.grid(row=1, column=1, pady=5, padx=50)
        #
        # #TODO: second code
        rollentry = Entry(First_Frame,textvariable=self.Roll_No_var, font=("times new roman", 20, "bold"), bd=5,
                          relief=GROOVE)
        rollentry.grid(row=1, column=2, pady=15)
        #
        #
        # #===========Setting up Third Frame=============
        c_title = Label(First_Frame, text="Branch:", bg="grey", fg="black", font=("Helvetica", 25, "bold"))
        c_title.grid(row=2, column=1, pady=35)
        #
        # # TODO: Third code
        branchentry = Entry(First_Frame,textvariable=self.branch_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        branchentry.grid(row=2, column=2)

        # #============setting up fourth frame==========
        d_title = Label(First_Frame, text="E-mail:", bg="grey", fg="black", font=("Helvetica", 25, "bold"))
        d_title.grid(row=3, column=1, pady=5)
        #
        # # TODO: Fourth code
        emailentry = Entry(First_Frame,textvariable=self.email_var, font=("times new roman", 20, "bold"), bd=5,
                           relief=GROOVE)
        emailentry.grid(row=3, column=2, pady=15)

        # #=============setting up Fivth Frame============
        e_title = Label(First_Frame, text="Attendance:", bg="grey", fg="black", font=("Helvetica", 25, "bold"))
        e_title.grid(row=4, column=1, pady=35)

        # TODO: Fivth code
        combo_attendance = ttk.Combobox(First_Frame,textvariable=self.attendance_var,
                                        font=("times new roman", 20, "bold"))
        combo_attendance['values'] = ("Present", "Absent")
        combo_attendance.grid(row=4, column=2)

        # ==========Button Frame=======
        btn_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#505050", pady=10)
        btn_frame.place(x=1000, y=550, width=640, height=80)



        addbtn = Button(btn_frame, text="Add", width=12,height=3, command=self.add_students).grid(row=0, column=0,
                                                                                                  pady=2, padx=30)
        updatebtn = Button(btn_frame, text="Update", width=12, height=3, command=self.update_data).grid(row=0, column=1, pady=2, padx=30)
        deletebtn = Button(btn_frame, text="Delete", width=12, height=3, command=self.delete_data).grid(row=0, column=2, pady=2, padx=30)
        Clearbtn = Button(btn_frame, text="Clear", width=12, height=3, command=self.clear).grid(row=0, column=3, pady=2, padx=30)

        Detail_Frame = Frame(self.root, bd=4, relief=SUNKEN, bg="grey")
        Detail_Frame.place(x=18, y=630, width=1625, height=400)

        lbl_search = Label(Detail_Frame, text="Search By", bg="grey", fg="black", font=("times new roman", 25, "bold"))
        lbl_search.grid(row=0, columns=2, padx=10, pady=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search["values"] = ("Students", "Roll_No", "Branch", "E-mail")
        combo_search.grid(row=0, column=5, padx=20, pady=10)

        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=6, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=7, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=8, padx=10, pady=10)

        # ===========Table Frame==============
        Table_Frame = Frame(Detail_Frame, bd=4, relief=SUNKEN, bg="grey")
        Table_Frame.place(x=10, y=70, width=1580, height=300)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,
                                     columns=("student", "roll_no", "branch", "email","attendance"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("student", text="students")
        self.Student_table.heading("roll_no", text="Roll_No")
        self.Student_table.heading("branch", text="Branch")
        self.Student_table.heading("email", text="E-mail")
        self.Student_table.heading("attendance", text="Attendance")
        self.Student_table["show"] = "headings"
        self.Student_table.column("student", width=100)
        self.Student_table.column("roll_no", width=100)
        self.Student_table.column("branch", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("attendance", width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_students(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="data")
        cur = con.cursor()
        cur.execute("insert into students value(%s, %s, %s, %s, %s)", (self.student_var.get(),
                                                                       self.Roll_No_var.get(),
                                                                       self.branch_var.get(),
                                                                       self.email_var.get(),
                                                                       self.attendance_var.get()
                                                                       ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="data")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.student_var.set("")
        self.Roll_No_var.set("")
        self.branch_var.set("")
        self.email_var.set("")
        self.attendance_var.set("")
    def get_cursor(self, ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row= contents['values']
        self.student_var.set(row[0])
        self.Roll_No_var.set(row[1])
        self.branch_var.set(row[2])
        self.email_var.set(row[3])
        self.attendance_var.set(row[4])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="data")
        cur = con.cursor()
        cur.execute("update students set roll_no=%s,branch=%s,email=%s,attendance=%s where students=%s",(
                                                                                     self.Roll_No_var.get(),
                                                                                     self.branch_var.get(),
                                                                                     self.email_var.get(),
                                                                                     self.attendance_var.get(),
                                                                                     self.student_var.get()
                                                                                     ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="data")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="data")
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

if __name__=="__main__":
    root= Tk()
    obj=CourseClass(root)
    root.mainloop()
