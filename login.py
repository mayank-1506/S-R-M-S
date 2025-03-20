from tkinter import *
from tkinter import messagebox
import sqlite3  # Optional: If storing credentials in a database

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - SRMS")
        self.root.geometry("400x350")
        self.root.config(bg="white")

        # ==== Username & Password Labels ====
        Label(self.root, text="Login", font=("Arial", 20, "bold"), bg="white").pack(pady=20)
        Label(self.root, text="Username:", font=("Arial", 12), bg="white").place(x=600, y=100)
        Label(self.root, text="Password:", font=("Arial", 12), bg="white").place(x=600, y=150)

        # ==== Entry Fields ====
        self.username = Entry(self.root, font=("Arial", 12))
        self.username.place(x=700, y=100, width=200)
        self.password = Entry(self.root, font=("Arial", 12), show="*")  # Mask password
        self.password.place(x=700, y=150, width=200)

        # ==== Login Button ====
        Button(self.root, text="𝓛𝓸𝓰𝓲𝓷", font=("Arial", 12, "bold"), bg="#0b5377", fg="white", command=self.login).place(x=650, y=200, width=100)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username == "mc0416" and password == "Krishu@1506":  # Example credentials
            messagebox.showinfo("Login Success", "Welcome to SRMS")
            self.root.destroy()  # Close login window
            self.open_srms()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def open_srms(self):
        from dashboard import SRMS  # Import your main SRMS class
        root = Tk()
        obj = SRMS(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = LoginSystem(root)
    root.mainloop()
