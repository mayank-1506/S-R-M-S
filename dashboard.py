from tkinter import *
import sqlite3
import requests

from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import time  # Import the time module for the clock
from tkcalendar import Calendar  # Import Calendar from tkcalendar

class SRMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System")
        self.root.geometry("1600x500")
        
        # Load the image for the label
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        
        # Create a label with the image and text
        self.label = Label(root, 
                           text="𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓡𝓮𝓼𝓾𝓵𝓽 𝓜𝓪𝓷𝓪𝓰𝓮𝓶𝓮𝓷𝓽 𝓢𝔂𝓼𝓽𝓮𝓶", 
                           padx=10,
                           compound=LEFT,  # Corrected typo here
                           image=self.logo_dash,
                           font=("Arial", 14))
        
        # Pack the label into the winow
        self.label.pack(pady=20)

         # === News Panel ===
        self.news_frame = LabelFrame(root, text="📢 𝓛𝓪𝓽𝓮𝓼𝓽 𝓔𝓭𝓾𝓬𝓪𝓽𝓲𝓸𝓷 𝓝𝓮𝔀𝓼", font=("times new roman", 15, "bold"), bg="white")
        self.news_frame.place(x=990, y=70, width=535, height=670)

        self.news_text = Text(self.news_frame, font=("Comic Sans MS", 12), wrap=WORD, bg="#E6E6FA", fg="black")
        self.news_text.pack(fill=BOTH, expand=True, padx=5, pady=5)

       

        self.get_news()  # Lo

        # === Menu Frame ===
        M_Frame = LabelFrame(root, text="𝓜𝓮𝓷𝓾𝓼", font=("times new roman", 15), bg="#c4cbcc")
        M_Frame.place(x=10, y=70, width=250, height=330)

       
        

        # Buttons for various actions
        btn_course = Button(M_Frame, text="𝓬𝓸𝓾𝓻𝓼𝓮", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)
        
        btn_student = Button(M_Frame, text="𝓢𝓽𝓾𝓭𝓮𝓷𝓽", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=20, y=80, width=200, height=40)

        btn_result = Button(M_Frame, text="𝓡𝓮𝓼𝓾𝓵𝓽", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=20, y=160, width=200, height=40)

        btn_view = Button(M_Frame, text="𝓥𝓲𝓮𝔀 𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓡𝓮𝓼𝓾𝓵𝓽𝓼", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report)
        btn_view.place(x=20, y=230, width=200, height=40)

        # === Footer Label ===
        footer = Label(root, 
                       text="SRMS-Student Result Management System\nContact Us for any technical issue: 8756953325", 
                       font=("Arial", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        # === Background Image ===
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        # Label to display the background image
        self.lbl_bg = Label(root, image=self.bg_img)
        self.lbl_bg.place(x=280, y=70, width=700, height=330)

        # === Clock Label ===
        self.clock_label = Label(root, font=("Arial", 10, "bold"), bg="white", fg="black")
        self.clock_label.place(x=140, y=405, width=150, height=28)  # Position the clock to the right of the image

        # Call the function to update the clock
        self.update_clock()

        # === Add Calendar ===
        self.calendar_label = Label(root, text="𝓬𝓪𝓵𝓮𝓷𝓭𝓪𝓻", font=("Arial", 15, "bold"), fg="black" ,bg="white")
        self.calendar_label.place(x=10, y=400, width=100, height=28)  # Position the label above the calendar

        # Create the calendar widget
        self.calendar = Calendar(root, selectmode="day", year=2025, month=3, day=20,bg="black")
        self.calendar.place(x=10, y=430,width=250,height=315) # Position the calendar widget to the right of the image

        feedback_frame = LabelFrame(root, text="𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓕𝓮𝓮𝓭𝓫𝓪𝓬𝓴 & 𝓡𝓮𝓶𝓪𝓻𝓴𝓼", font=("times new roman", 15,"bold"), bg="#c4cbcc", fg="black")
        feedback_frame.place(x=280, y=417, width=700, height=327)  # Positioned below the Notes panel

        self.txt_feedback = Text(feedback_frame, font=("Arial", 12), bg="lightyellow", fg="black")
        self.txt_feedback.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Load feedback when app starts
        self.load_feedback()
        
        # Save Button for Feedback
        btn_save_feedback = Button(feedback_frame, text="𝙎𝙖𝙫𝙚 𝙁𝙚𝙚𝙙𝙗𝙖𝙘𝙠", font=("goudy old style", 12, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.save_feedback)
        btn_save_feedback.place(x=537, y=265, width=150, height=30) 

    def save_feedback(self):
        feedback_text = self.txt_feedback.get("1.0", END).strip()
        conn = sqlite3.connect("student_records.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, remarks TEXT)")
        cursor.execute("DELETE FROM feedback")  # Clear previous feedback
        cursor.execute("INSERT INTO feedback (remarks) VALUES (?)", (feedback_text,))
        conn.commit()
        conn.close()

    # === Function to Load Feedback from Database on App Start ===
    def load_feedback(self):
        conn = sqlite3.connect("student_records.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, remarks TEXT)")
        cursor.execute("SELECT remarks FROM feedback")
        row = cursor.fetchone()
        if row:
            self.txt_feedback.insert("1.0", row[0])  # Load saved remarks
        conn.close()

    def update_clock(self):
        # Get the current time in 24-hour format
        current_time = time.strftime("%H:%M:%S %p")
        
        # Update the clock label with the new time
        self.clock_label.config(text=current_time)
        
        # Call this function again after 1000 ms (1 second) to update the clock
        self.clock_label.after(1000, self.update_clock)

    # Add Course function to open a new window
    def add_course(self):
        self.new_win = Toplevel(self.root)  # Create a new top-level window
        self.new_obj = CourseClass(self.new_win)  # Initialize the CourseClass for the new window

    def add_student(self):  # Indentation fixed (aligned with add_course)
        self.new_win = Toplevel(self.root)  # Create a new top-level window
        self.new_obj = studentClass(self.new_win)  # Initialize StudentClass
    
    def add_result(self):  # Indentation fixed (aligned with add_course)
        self.new_win = Toplevel(self.root)  # Create a new top-level window
        self.new_obj = resultClass(self.new_win)
        
    def add_report(self):  # Indentation fixed (aligned with add_course)
        self.new_win = Toplevel(self.root)  # Create a new top-level window
        self.new_obj = reportClass(self.new_win)

 

    def get_news(self):
      api_key = "dae3aaf6d5ab4ff7b7bade633539a659"  # Your API key
      url = f"https://newsapi.org/v2/everything?q=education&language=en&sortBy=publishedAt&apiKey={api_key}"

      try:
         response = requests.get(url)
         data = response.json()
         articles = data.get("articles", [])

         self.news_text.delete("1.0", END)  # Clear previous news

         if not articles:
            self.news_text.insert(END, "No recent education news found.\n")
            return  # ✅ This return is properly inside the function

         for article in articles[:10]:  # Show top 10 articles
            title = article.get("title", "No Title")
            source = article.get("source", {}).get("name", "Unknown Source")
            url = article.get("url", "#")

            self.news_text.insert(END, f"🔹 {title}\n📍 Source: {source}\n🔗 Read More: {url}\n\n")

         self.news_text.insert(END, "🔄 Auto-refreshes every 5 minutes...")
         self.news_text.after(300000, self.get_news)  # Refresh every 5 minutes

      except Exception as e:
         self.news_text.config(state=NORMAL)  # Temporarily enable editing for errors
         self.news_text.insert(END, f"❌ Error loading news: {str(e)}\n")
         self.news_text.config(state=DISABLED)  # Disable again




           



    

if __name__ == "__main__":
    root = Tk()
    obj = SRMS(root)
    root.mainloop()
