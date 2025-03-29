import customtkinter as ctk
import sqlite3
import tkinter as tk
from PIL import Image

# System Defaults
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.FontManager.load_font("assets/fonts/Poppins.ttf")
profile_img = Image.open("assets/images/profile.png")
root = ctk.CTk()
root.geometry("1000x600")
root.title("Complaint Management System")
connection = sqlite3.connect("cms.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS complaint_form (
               complaint_no INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(250),
               user_id VARCHAR(250),
               gender VARCHAR(250),
               Subject VARCHAR(250),
               Complaint TEXT
               )''')
class ComplaintForm:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection
        self.user_comp_int_frm = ctk.CTkFrame(self.root, fg_color="transparent")
        self.username_com_form = tk.StringVar()
        self.userid_com_form = tk.StringVar()
        self.usergender_com_form = tk.StringVar()
        self.subject_com_form = tk.StringVar()
         # Frame for the entire form
        self.header_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.logout_btn = ctk.CTkButton(self.header_frm, text= "Logout", command = lambda: log_in("logout", "logout"))
        self.user_comp_title_lbl = ctk.CTkLabel(self.header_frm, text="Complaint Form", font=("Poppins", 35))
        self.user_comp_form_frm = ctk.CTkScrollableFrame(self.user_comp_int_frm, border_color="#00009e", border_width=2, width=800, height=500)

        # Name and ID Frame
        self.name_id_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.user_name_frm = ctk.CTkFrame(self.name_id_frm, fg_color="transparent")
        self.user_name_lbl = ctk.CTkLabel(self.user_name_frm, text="Name:", font=("Poppins", 15))
        self.user_name_ent = ctk.CTkEntry(self.user_name_frm, font=("Poppins", 15), placeholder_text="Enter your name", width=250, textvariable=self.username_com_form)
        
        self.user_id_frm = ctk.CTkFrame(self.name_id_frm, fg_color="transparent")
        self.user_id_lbl = ctk.CTkLabel(self.user_id_frm, text="ID Number:", font=("Poppins", 15))
        self.user_id_ent = ctk.CTkEntry(self.user_id_frm, font=("Poppins", 15), placeholder_text="Enter your ID", width=250, textvariable=self.userid_com_form)

        # Gender Frame
        self.gender_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.gender_values = ["Male", "Female", "I prefer not to say..."]
        self.gender_lbl = ctk.CTkLabel(self.gender_frm, text="Gender:", font=("Poppins", 15))
        self.gender_dropdown = ctk.CTkComboBox(self.gender_frm, width=250, values=self.gender_values, font=("Poppins", 15), variable=self.usergender_com_form)

        # Subject Frame
        self.subject_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.subject_lbl = ctk.CTkLabel(self.subject_frm, text="Subject:", font=("Poppins", 15))
        self.subject_ent = ctk.CTkEntry(self.subject_frm, font=("Poppins", 15), placeholder_text="Subject of Complaint", width=500, textvariable=self.subject_com_form)

        # Complaint Frame
        self.com_form_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.com_form_lbl = ctk.CTkLabel(self.com_form_frm, text="Complaint:", font=("Poppins", 15))
        self.com_form_ent = ctk.CTkTextbox(self.user_comp_form_frm, font=("Poppins", 15), width=700, height=150)

        # Submit Button
    def show(self):
        self.hide()
        self.submit_com_form_btn = ctk.CTkButton(self.user_comp_form_frm, text="Submit Now", font=("Poppins", 15), command=self.insert)

        # Packing Widgets
        self.user_name_lbl.pack(padx=(50, 3), pady=(10, 0), side="left")
        self.user_name_ent.pack(padx=(10, 20), pady=(10, 0), side="left")
        self.user_id_lbl.pack(padx=(50, 3), pady=(10, 0), side="left")
        self.user_id_ent.pack(padx=(10, 20), pady=(10, 0), side="left")

        self.gender_lbl.pack(padx=(50, 3), pady=(10, 10), side="left")
        self.gender_dropdown.pack(pady=(0, 3), side="left")

        self.subject_lbl.pack(padx=(50, 3), pady=(15, 10), side="left")
        self.subject_ent.pack(padx=(10, 20), pady=(15, 10), side="left")

        self.com_form_lbl.pack(padx=(50, 3), pady=5, side="left")

        self.user_name_frm.pack(padx=10, pady=1, side="left")
        self.user_id_frm.pack(padx=10, pady=1, side="left")

        self.name_id_frm.pack(pady=20, padx=5)
        self.gender_frm.pack(pady=10, padx=15, fill="x", expand=True)
        self.subject_frm.pack(pady=10, padx=15, fill="x", expand=True)
        self.com_form_frm.pack(pady=3, padx=15, fill="x", expand=True)
        self.com_form_ent.pack(padx=(65, 20), pady=5)
        self.submit_com_form_btn.pack(pady=5)
        self.logout_btn.pack(padx = (20, 125), side= "left")
        self.user_comp_title_lbl.pack(side = "left")
        
        self.header_frm.pack(pady = 15, fill= "x", expand = "True")
        self.user_comp_form_frm.pack(padx=20, pady=5)


       
        # Pack the main frame
        self.user_comp_int_frm.pack()

    def insert(self):
        """Inserts the form data into the database."""
        name = self.username_com_form.get()
        user_id = self.userid_com_form.get()
        gender = self.usergender_com_form.get()
        subject = self.subject_com_form.get()
        complain = self.com_form_ent.get("0.0", "end-1c")

        print(complain)
        self.cursor.execute(
            "INSERT INTO complaint_form (name, user_id, gender, Subject, Complaint) VALUES (?, ?, ?, ?, ?)",
            (name, user_id, gender, subject, complain)
        )
        self.connection.commit()
        self.cursor.execute("SELECT * FROM complaint_form")
        records = self.cursor.fetchall()
        print(records)
        self.show()
    
    def hide(self):
        if hasattr(self, 'gender_dropdown'):
            self.gender_dropdown.set("")
        if hasattr(self, 'subject_ent'):
            self.subject_ent.delete(0, "end")
        if hasattr(self, 'com_form_ent'):
            self.com_form_ent.delete("0.0", "end")
        if hasattr(self, 'user_name_ent'):
            self.user_name_ent.delete(0, "end")
        if hasattr(self, 'user_id_ent'):
            self.user_id_ent.delete(0, "end")
        self.user_comp_int_frm.forget()

complaintforminterface = ComplaintForm(root, cursor, connection)
# Functions
def log_in(username, userpassword):
    global cursor, complaintforminterface
    cursor.execute("SELECT * FROM complaint_form")
    records = cursor.fetchall()
    print(records)
    if username == userpassword == "logout":
        login_frm.pack()
        complaintforminterface.hide()
    elif username.get() == userpassword.get() == "user":
        login_frm.forget()
        complaintforminterface.show()
    elif username.get() == userpassword.get() == "admin":
        login_frm.forget()
        admin_main_int.pack()



# Log in Interface
login_frm = ctk.CTkFrame(root, fg_color= "transparent")
login_title_frm = ctk.CTkFrame(login_frm, fg_color= "#00009e", corner_radius= 60)
login_title_lbl = ctk.CTkLabel(login_title_frm, text= "Complaint Management System", font= ("Poppins", 30), bg_color= "#00009e", text_color= "#e7e8e8")
login_title_frm.pack(pady = (50, 0))
login_title_lbl.pack(padx = 20, pady = 40)

# Start of User Form #
## Variable Holders ##
username_login = tk.StringVar()
userpassword_login = tk.StringVar()
## End of Variable Holder ##
user_form_frm = ctk.CTkFrame(login_frm, border_color= "#00009e", corner_radius= 20, border_width= 3)
icon_frm = ctk.CTkFrame(user_form_frm)
user_form_icon = ctk.CTkImage(profile_img, size=(80,80))
user_form_icon_holder = ctk.CTkLabel(user_form_frm, image= user_form_icon, text= "", width= 250)
user_form_lbl = ctk.CTkLabel(user_form_frm, text= "Member Login" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_username_lbl = ctk.CTkLabel(user_form_frm, text= "Username:" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_username_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your username:", corner_radius= 50, width= 250, font= ("Poppins", 12), textvariable= username_login)
user_password_lbl = ctk.CTkLabel(user_form_frm, text= "Password:", font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_password_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your password:", show= "•", corner_radius= 50, width= 250, font= ("Poppins", 12), textvariable= userpassword_login)
user_form_submit_btn = ctk.CTkButton(user_form_frm, text= "Log in", font= ("Poppins", 15), width= 250, corner_radius= 50, command= lambda: log_in(username_login, userpassword_login))

user_form_icon_holder.pack(pady= (5,0), padx= 20)
user_form_lbl.configure(anchor="center", justify="center")
user_form_lbl.pack(pady= (5, 0), padx= 20, fill= "x")
user_username_lbl.pack(pady = (20, 0), padx = 20)
user_username_ent.pack(pady = (10, 0), padx = 20)
user_password_lbl.pack(pady = (20, 0), padx = 20)
user_password_ent.pack(pady = (10, 10), padx = 20)
user_form_submit_btn.pack(pady = (10, 10), padx = 20)
user_form_frm.pack(pady= (50, 0))
login_frm.pack()
# End of User Form #

# Start of User Complaint Interface #


# Start of Admin Interface #
admin_main_int = ctk.CTkFrame(root, fg_color= "transparent")
user_comp_title_lbl = ctk.CTkLabel(admin_main_int, text= "Complaint Overview", font= ("Poppins", 35))
complaints_frm = ctk.CTkScrollableFrame(admin_main_int, border_color="#00009e", width= 800)

user_comp_title_lbl.pack(pady= 15)
complaints_frm.pack(fill = "x", expand = True)
# End of Admin Interface #
root.mainloop()
