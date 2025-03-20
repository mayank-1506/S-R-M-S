import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Result Management System")
        self.root.geometry("1200x480+80+170")  
        self.root.config(bg="white")  
        self.root.focus_force()

        # Title Label
        self.title_label = Label(self.root, text="𝓥𝓲𝓮𝔀 𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓡𝓮𝓼𝓾𝓵𝓽𝓼", font=("Arial", 20, "bold"), bg="blue", fg="white")
        self.title_label.pack(pady=10)

        # Search Section
        self.var_search = StringVar()

        Label(self.root, text="Search by Roll No.", font=("goudy old style", 20, "bold"), bg="white").place(x=280, y=100)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg="lightyellow").place(x=520, y=100, width=150)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=680, y=100, width=90, height=34)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=780, y=100, width=90, height=34)

        # Labels for Displaying Results
        labels = ["Roll No.", "Name", "Course", "Marks Obt", "Full Marks", "Percentage"]
        x_positions = [150, 300, 450, 600, 750, 900]

        for i, text in enumerate(labels):
            Label(self.root, text=text, font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=x_positions[i], y=230, width=150, height=50)

        # Result Fields
        self.roll = Label(self.root, font=("goudy old style", 20), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)

        self.name = Label(self.root, font=("goudy old style", 20), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(self.root, font=("goudy old style", 20), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks = Label(self.root, font=("goudy old style", 20), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)

        self.full = Label(self.root, font=("goudy old style", 20), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=750, y=280, width=150, height=50)

        self.per = Label(self.root, font=("goudy old style", 20), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)

        # Delete Button
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=550, y=350, width=100, height=35)

    def search(self):
        """Fetch student details from the database based on roll number."""
        roll_no = self.var_search.get().strip()

        if roll_no == "":
            messagebox.showerror("Error", "Please enter a Roll Number!", parent=self.root)
            return

        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM result WHERE roll=?", (roll_no,))  # Fix: tuple issue
            row = cur.fetchone()

            if row:
                self.roll.config(text=row[0])  
                self.name.config(text=row[1])
                self.course.config(text=row[2])
                self.marks.config(text=row[3])
                self.full.config(text=row[4])
                self.per.config(text=row[5])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
                self.clear()

        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

        finally:
            con.close()

    def clear(self):
        """Clear all fields and reset search box."""
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")

    def delete(self):
        """Delete a student record based on roll number."""
        roll_no = self.var_search.get().strip()

        if roll_no == "":
            messagebox.showerror("Error", "Please enter a Roll Number!", parent=self.root)
            return

        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM result WHERE roll=?", (roll_no,))
            row = cur.fetchone()

            if row:
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete Roll No: {roll_no}?", parent=self.root)
                if confirm:
                    cur.execute("DELETE FROM result WHERE roll=?", (roll_no,))
                    con.commit()
                    messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                    self.clear()
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
