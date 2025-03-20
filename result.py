import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Import required for images

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Result Management System")
        self.root.geometry("1200x480+80+170")  # Set window size and position
        self.root.config(bg="white")  # Background color
        self.root.focus_force()

        # Add a title label
        self.title_label = Label(self.root, text="𝓐𝓭𝓭 𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓡𝓮𝓼𝓾𝓵𝓽𝓼", font=("Arial", 20, "bold"), bg="blue", fg="white")
        self.title_label.pack(pady=10)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmarks = StringVar()
        self.roll_list = []  # Empty initially

        # Labels
        lbl_select = Label(self.root, text="Select student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)

        # Entry Widgets
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, font=("goudy old style", 15), state="readonly", justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=500, y=100, width=90, height=28)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow", state="readonly")
        self.txt_name.place(x=280, y=160, width=310)

        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="lightyellow", state="readonly")
        self.txt_course.place(x=280, y=220, width=310)

        self.txt_marks_ob = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 15), bg="lightyellow")
        self.txt_marks_ob.place(x=280, y=280, width=310)

        self.txt_full_marks = Entry(self.root, textvariable=self.var_fullmarks, font=("goudy old style", 15), bg="lightyellow")
        self.txt_full_marks.place(x=280, y=340, width=310)

        # Buttons - Submit and Clear
        btn_submit = Button(self.root, text="Submit", font=("goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.add)
        btn_submit.place(x=280, y=400, width=150, height=40)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.clear_fields)
        btn_clear.place(x=450, y=400, width=150, height=40)

        # Fetch student roll numbers after initializing widgets
        self.fetch_roll()

        # Load background image
        try:
            self.bg_img = Image.open("images/result.jpg")  # Replace with your image path
            self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)  # Adjust the size as needed
            self.bg_img = ImageTk.PhotoImage(self.bg_img)

            self.bg_label = Label(self.root, image=self.bg_img, bd=2, relief=RAISED)
            self.bg_label.place(x=650, y=100, width=500, height=300)  # Adjust position
        except Exception as e:
            print(f"Error loading image: {e}")

    def fetch_roll(self):
        """Fetch student roll numbers from the database."""
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if rows:
                self.roll_list = [row[0] for row in rows]
                self.txt_student["values"] = self.roll_list  # Update combobox values
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            con.close()

    def search(self):
        """Fetch student details from the database based on roll number."""
        roll_no = self.var_roll.get()
        if roll_no == "Select" or roll_no == "":
            messagebox.showerror("Error", "Please select a student roll number", parent=self.root)
        else:
            con = sqlite3.connect("srms.db")
            cur = con.cursor()
            try:
                cur.execute("SELECT name, course FROM student WHERE roll=?", (roll_no,))
                row = cur.fetchone()
                if row:
                    self.var_name.set(row[0])
                    self.var_course.set(row[1])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
            finally:
                con.close()

    def add(self):
        """Insert student result into the database."""
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=? AND course=?", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already exists", parent=self.root)
                else:
                    percentage = (float(self.var_marks.get()) / float(self.var_fullmarks.get())) * 100
                    cur.execute("INSERT INTO result (roll, name, course, marks_obtained, per, full_marks) VALUES (?, ?, ?, ?, ?, ?)", 
                                (self.var_roll.get(), self.var_name.get(), self.var_course.get(), self.var_marks.get(), f"{percentage:.2f}", self.var_fullmarks.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
        finally:
            con.close()

    def clear_fields(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_fullmarks.set("")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
