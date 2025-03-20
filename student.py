from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

# Function to ensure the student table exists
def create_table():
    con = sqlite3.connect("srms.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        roll TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        admission_date TEXT,
        course TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
    """)
    con.commit()
    con.close()

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("𝓜𝓪𝓷𝓪𝓰𝓮 𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓓𝓮𝓽𝓪𝓲𝓵𝓼")
        self.root.geometry("1100x550+100+50")
        self.root.config(bg="white")

        # Ensure table exists
        create_table()

        # === Variables ===
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_course = StringVar()
        self.var_admission_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # === Title ===
        title = Label(self.root, text="𝓜𝓪𝓷𝓪𝓰𝓮 𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓓𝓮𝓽𝓪𝓲𝓵𝓼 ", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=10, width=1080, height=40)

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white")
        lbl_address.place(x=20, y=260)
        self.txt_address = Text(self.root,font=("goudy old style", 15), bg="lightyellow", height=2, width=72)
        self.txt_address.place(x=150, y=260)


        # === Labels & Entry Fields ===
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15), bg="white")
        lbl_roll.place(x=20, y=60)
        txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="lightyellow")
        txt_roll.place(x=150, y=60, width=200)

        lbl_dob = Label(self.root, text="D.O.B (dd-mm-yyyy)", font=("goudy old style", 15), bg="white")
        lbl_dob.place(x=400, y=60)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow")
        txt_dob.place(x=600, y=60, width=200)

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=20, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=150, y=100, width=200)

        lbl_contact = Label(self.root, text="Contact No.", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=400, y=100)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=600, y=100, width=200)

        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="white")
        lbl_email.place(x=20, y=140)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow")
        txt_email.place(x=150, y=140, width=200)

        lbl_course = Label(self.root, text="Select Course", font=("goudy old style", 15), bg="white")
        lbl_course.place(x=400, y=140)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="lightyellow")
        txt_course.place(x=600, y=140, width=200)

        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15), bg="white")
        lbl_gender.place(x=20, y=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Male", "Female", "Other"), font=("goudy old style", 15), state="readonly", justify=CENTER)
        cmb_gender.place(x=150, y=180, width=200)
        cmb_gender.current(0)
        
        lbl_admission_date = Label(self.root, text="Admission Date", font=("goudy old style", 15), bg="white")
        lbl_admission_date.place(x=400, y=180)
        txt_admission_date = Entry(self.root, textvariable=self.var_admission_date, font=("goudy old style", 15), bg="lightyellow")
        txt_admission_date.place(x=600, y=180, width=200)

        lbl_state = Label(self.root, text="State", font=("goudy old style", 15), bg="white")
        lbl_state.place(x=20, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="lightyellow")
        txt_state.place(x=150, y=220, width=200)
 
        lbl_city = Label(self.root, text="City", font=("goudy old style", 15), bg="white")
        lbl_city.place(x=400, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15), bg="lightyellow")
        txt_city.place(x=600, y=220, width=100)

        lbl_pin = Label(self.root, text="Pin Code", font=("goudy old style", 15), bg="white")
        lbl_pin.place(x=800, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg="lightyellow")
        txt_pin.place(x=900, y=220, width=100)


        # === Buttons ===
        btn_save = Button(self.root, text="Save", font=("goudy old style", 15), bg="blue", fg="white", command=self.add)
        btn_save.place(x=150, y=320, width=100)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15), bg="blue", fg="white",command=self.delete)
        btn_delete.place(x=260, y=320, width=100)
        

        # === Student Table ===
        frame = Frame(self.root, bd=2, relief=RIDGE)
        frame.place(x=20, y=370, width=1070, height=170)

        scrolly = Scrollbar(frame, orient=VERTICAL)
        scrollx = Scrollbar(frame, orient=HORIZONTAL)

        self.student_table = ttk.Treeview(frame, columns=("roll", "name", "email", "gender", "dob", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        for col in ("roll", "name", "email", "gender", "dob", "state", "city", "pin", "address"):
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.show()  # Load student records when UI opens

    def add(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll number is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Roll number already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                (self.var_roll.get(), self.var_name.get(), self.var_email.get(),
                                 self.var_gender.get(), self.var_dob.get(), self.var_contact.get(),
                                 self.var_admission_date.get(), self.var_course.get(), self.var_state.get(),
                                 self.var_city.get(), self.var_pin.get(), self.txt_address.get("1.0", END).strip()))
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
           self.var_roll.set("")
           self.var_name.set("")
           self.var_email.set("")
           self.var_gender.set("Male")  # Default selection
           self.var_dob.set("")
           self.var_contact.set("")
           self.var_admission_date.set("")
           self.var_course.set("")
           self.var_state.set("")
           self.var_city.set("")
           self.var_pin.set("")
           self.txt_address.delete("1.0", END)  # Clear address text field


    


    def show(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll, name, email, gender, dob, state, city, pin, address FROM student")
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())  # Clear old data
            for row in rows:
                self.student_table.insert("", END, values=row)  # Insert new data
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

      
    def delete(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                 messagebox.showerror("error","roll number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student deleted successfully",parent=self.root)
                        self.clear()
                        self.show()

        except Exception as ex:
                   messagebox.showerror("error",f"error due to{str(ex)}",parent=self.root)
        finally:
            con.close()

                    
                

    


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
