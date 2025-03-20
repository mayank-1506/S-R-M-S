import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Result Management System")
        self.root.geometry("1200x480+80+170")  # Set window size and position
        self.root.config(bg="white")  # Background color
        self.root.focus_force()

        # Add a title label
        self.title_label = Label(self.root, text="𝓜𝓪𝓷𝓪𝓰𝓮 𝓬𝓸𝓾𝓻𝓼𝓮 𝓓𝓮𝓽𝓪𝓲𝓵𝓼", font=("Arial", 20, "bold"), bg="white", fg="black")
        self.title_label.pack(pady=10)

        # Course Name Label and Entry
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white")
        lbl_courseName.place(x=10, y=60)
        self.entry_courseName = Entry(self.root, font=("goudy old style", 15), bg="lightgray")
        self.entry_courseName.place(x=150, y=60, width=300)

        # Duration Label and Entry
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white")
        lbl_duration.place(x=10, y=100)
        self.entry_duration = Entry(self.root, font=("goudy old style", 15), bg="lightgray")
        self.entry_duration.place(x=150, y=100, width=300)

        # Charges Label and Entry
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white")
        lbl_charges.place(x=10, y=140)
        self.entry_charges = Entry(self.root, font=("goudy old style", 15), bg="lightgray")
        self.entry_charges.place(x=150, y=140, width=300)

        # Description Label and Textbox
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white")
        lbl_description.place(x=10, y=180)
        self.txt_description = Text(self.root, font=("goudy old style", 15), bg="lightgray", height=4, width=40)
        self.txt_description.place(x=150, y=180)

        # Buttons: Update, Save, Delete, Clear
        btn_update = Button(self.root, text="Update", font=("goudy old style", 12, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.update_course)
        btn_update.place(x=150, y=350, width=130, height=35)

        btn_save = Button(self.root, text="Save", font=("goudy old style", 12, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.save_course)
        btn_save.place(x=290, y=350, width=130, height=35)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 12, "bold"), bg="#e43b06", fg="white", cursor="hand2", command=self.delete_course)
        btn_delete.place(x=430, y=350, width=130, height=35)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 12, "bold"), bg="#038074", fg="white", cursor="hand2", command=self.clear_fields)
        btn_clear.place(x=570, y=350, width=130, height=35)

        # Search Course Section (Right top corner)
        lbl_search_courseName = Label(self.root, text="Search Course", font=("goudy old style", 15, "bold"), bg="white")
        lbl_search_courseName.place(x=720, y=60)

        self.entry_search_course = Entry(self.root, font=("goudy old style", 15), bg="lightgray")
        self.entry_search_course.place(x=880, y=60, width=250)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 12, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.search_course)
        btn_search.place(x=1140, y=60, width=100, height=30)

        # Frame for Course Data (C_Frame) - increased width to 800
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=800, height=340)

        # Create Scrollbars
        self.yscrollbar = Scrollbar(self.C_Frame, orient=VERTICAL)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.xscrollbar = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        # Treeview for Course Data (using ttk.Treeview)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), show="headings", yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)

        # Define columns and headings
        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Course Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        # Set column widths (optional)
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=200)
        self.CourseTable.column("duration", width=150)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=250)

        self.CourseTable.pack(fill=BOTH, expand=1)

        # Configure the scrollbars to work with the Treeview
        self.yscrollbar.config(command=self.CourseTable.yview)
        self.xscrollbar.config(command=self.CourseTable.xview)

        # Show the courses initially
        self.show()

    def search_course(self):
        course_name = self.entry_search_course.get()
        con = sqlite3.connect("srms.db")
        cur = con.cursor() 
        try:
            cur.execute("SELECT * FROM courses WHERE course_name LIKE ?", ('%' + course_name + '%',))
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def update_course(self):
        course_name = self.entry_courseName.get()  # Get the course name from the entry field
        if not course_name:
            messagebox.showerror("Error", "Course name should be required", parent=self.root)
            return

        con = sqlite3.connect("srms.db")  # Connect to the database
        cur = con.cursor()
        try:
            # Check if the course exists
            cur.execute("SELECT * FROM courses WHERE course_name=?", (course_name,))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Course not found", parent=self.root)  # Show error if course is not found
                return

            # Ask for confirmation before updating the course
            op = messagebox.askyesno("Confirm", "Do you really want to update this course?", parent=self.root)
            if op:
                # Get the new course details from the entry fields
                new_duration = self.entry_duration.get()
                new_charges = self.entry_charges.get()
                new_description = self.txt_description.get("1.0", "end-1c")  # Get the text from the description box

                # Update the course information in the database
                cur.execute("""
                    UPDATE courses
                    SET duration = ?, charges = ?, description = ?
                    WHERE course_name = ?
                """, (new_duration, new_charges, new_description, course_name))
                con.commit()  # Commit the changes

                messagebox.showinfo("Update", "Course updated successfully", parent=self.root)  # Show success message

                self.clear_fields()  # Clear the fields
                self.show()  # Refresh the course list
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")  # Handle any exceptions
        finally:
            con.close()  # Close the database connection

    def save_course(self):
        course_name = self.entry_courseName.get()
        duration = self.entry_duration.get()
        charges = self.entry_charges.get()
        description = self.txt_description.get("1.0", "end-1c")

        self.add(course_name, duration, charges, description)

        self.clear_fields()



    

    def clear_fields(self):
        self.entry_courseName.delete(0, END)
        self.entry_duration.delete(0, END)
        self.entry_charges.delete(0, END)
        self.txt_description.delete("1.0", "end")
        self.entry_search_course.delete(0, END)

    def delete_course(self):
        course_name = self.entry_courseName.get()
        if not course_name:
            messagebox.showerror("Error", "Course name should be required", parent=self.root)
            return

        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM courses WHERE course_name=?", (course_name,))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Course not found", parent=self.root)
                return

            op = messagebox.askyesno("Confirm", "Do you really want to delete this course?", parent=self.root)
            if op:
                cur.execute("DELETE FROM courses WHERE course_name=?", (course_name,))
                con.commit()
                messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
                self.clear_fields()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def add(self, course_name, duration, charges, description):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            if course_name == "":
                messagebox.showerror("Error", "Course name is required", parent=self.root)
            else:
                cur.execute("""
                    INSERT INTO courses (course_name, duration, charges, description)
                    VALUES (?, ?, ?, ?)
                """, (course_name, duration, charges, description))
                con.commit()
                messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM courses")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()



def search(self):
    course_name = self.entry_search_course.get()
    con = sqlite3.connect("srms.db")
    cur = con.cursor()
    try:
        # Use parameterized query to prevent SQL injection and properly format the LIKE clause
        cur.execute("SELECT * FROM courses WHERE course_name LIKE ?", ('%' + course_name + '%',))
        rows = cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert('', END, values=row)
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")
    finally:
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
