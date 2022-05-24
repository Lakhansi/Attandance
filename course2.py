from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
class login:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")

        # ====image in background=======
        self.b_img = Image.open("cimag.jpg")
        # self.b_img = self.b_img.resize((1080, 720), Image.ANTIALIAS)
        self.b_img = ImageTk.PhotoImage(self.b_img)

        self.lbl_bg = Label(self.root, image=self.b_img).place(x=0, y=50, width=1920, height=1050)

        #========title=========

        title=Label(self.root, text="Student Management", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        #=========Menu========
        M_Frame=LabelFrame(self.root, text="Menu", font=("times new roman", 15), bg="#505050")
        M_Frame.place(x=5, y=70,width=1900, height=80)

        # Adding transparent background property
        # trans=root.wm_attributes('-transparentcolor', '#ab23ff')

        btn_cse=Button(M_Frame, text="Diploma CS", font=("goudy old style", 20, "bold"), bg="#505050", fg="white", cursor="hand2", command=self.add_course).place(x=20,y=5, width=200,height=40)
        btn_civil=Button(M_Frame, text="Diploma Civil", font=("goudy old style", 20, "bold"), bg="#505050", fg="white", cursor="hand2").place(x=350,y=5, width=200,height=40)
        btn_mechnical=Button(M_Frame, text="Diploma Mechnical", font=("goudy old style", 20, "bold"), bg="#505050", fg="white", cursor="hand2").place(x=680,y=5, width=240,height=40)
        btn_ee=Button(M_Frame, text="Diploma E.E", font=("goudy old style", 20, "bold"), bg="#505050", fg="white", cursor="hand2").place(x=1030,y=5, width=240,height=40)
        btn_btech=Button(M_Frame, text="B-Tech", font=("goudy old style", 20, "bold"), bg="#505050", fg="white", cursor="hand2").place(x=1390,y=5, width=200,height=40)
        btn_exit=Button(M_Frame, text="Exit", font=("goudy old style", 20, "bold"), bg="#505050", fg="white", cursor="hand2",command=self.root.destroy ).place(x=1700,y=5, width=180,height=40)

        #==============image in title=====
        self.bg_img=Image.open("imgg.png")
        self.bg_img=self.bg_img.resize((60,45), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(title, image=self.bg_img, bg="#033054").place(x=750, y=0)

        #=======update_detail=========
        # self.lbl_course=Label(self.root, text="Total Course\n[0]", font=("goudy old style", 20)).place(x=400, y=530)

        #==========footer=======
        footer=Label(self.root, text="SRMS-Student Management\nContact us for any Technical Issue:  987xxxx01",font=("goudy old style", 12), bg="#262626",fg="white").pack(side=BOTTOM, fill=X, pady=10)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
if __name__=="__main__":
    root= Tk()
    obj=login(root)
    root.mainloop()