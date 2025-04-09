import customtkinter as ctk
import sqlite3
import tkinter as tk
from PIL import Image

# System Defaults
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.FontManager.load_font("assets/fonts/Poppins.ttf")
profile_img = Image.open("assets/images/profile.png")
delete_img = Image.open("assets/images/delete.png")
go_back_img = Image.open("assets/images/go_back.png")
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
        self.user_comp_form_frm = ctk.CTkFrame(self.user_comp_int_frm, border_color="#00009e", border_width=2, width=800, height=500)

        # Name and ID Frame
        self.name_id_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.user_name_frm = ctk.CTkFrame(self.name_id_frm, fg_color="transparent")
        self.user_name_inf_frm = ctk.CTkFrame(self.user_name_frm, fg_color= "transparent")
        self.user_name_lbl = ctk.CTkLabel(self.user_name_inf_frm, text="Name:", font=("Poppins", 15))
        self.user_name_ent = ctk.CTkEntry(self.user_name_inf_frm, font=("Poppins", 15), placeholder_text="Enter your name", width=250, textvariable=self.username_com_form)
        self.name_error = ctk.CTkLabel(self.user_name_frm, text= "", text_color= "red", font=("Poppins", 12), anchor= "w")


        self.user_id_frm = ctk.CTkFrame(self.name_id_frm, fg_color="transparent")
        self.user_id_inf_frm = ctk.CTkFrame(self.user_id_frm, fg_color = "transparent")
        self.user_id_lbl = ctk.CTkLabel(self.user_id_inf_frm, text="ID Number:", font=("Poppins", 15))
        self.user_id_ent = ctk.CTkEntry(self.user_id_inf_frm, font=("Poppins", 15), placeholder_text="Enter your ID", width=250, textvariable=self.userid_com_form)
        self.id_error = ctk.CTkLabel(self.user_id_frm, text="", text_color="red", font=("Poppins", 12), anchor= "w")
        # Error Message When Left Blank
        # self.name_id_error_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        
        


        # Gender Frame
        self.gender_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.gender_values = ["Male", "Female", "I prefer not to say..."]
        self.gender_lbl = ctk.CTkLabel(self.gender_frm, text="Gender:", font=("Poppins", 15))
        self.gender_dropdown_frm = ctk.CTkFrame(self.gender_frm, border_color= "gray", fg_color= "gray")
        self.gender_dropdown = ctk.CTkOptionMenu(self.gender_dropdown_frm, width=250, values=self.gender_values, font=("Poppins", 15), variable=self.usergender_com_form, fg_color= "white", text_color="black")

        # Error Message When Gender Left Blank
        self.gender_error_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color= "transparent")
        self.gender_error_lbl = ctk.CTkLabel(self.gender_error_frm, text= "", text_color="red", font=("Poppins", 12))
        

        # Subject Frame
        self.subject_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.subject_lbl = ctk.CTkLabel(self.subject_frm, text="Subject:", font=("Poppins", 15))
        self.subject_ent = ctk.CTkEntry(self.subject_frm, font=("Poppins", 15), placeholder_text="Subject of Complaint", width=500, textvariable=self.subject_com_form)

        #Error Message When Subject Left Blank
        self.subject_error_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.subject_error_lbl = ctk.CTkLabel(self.subject_error_frm, text= "", text_color="red", font=("Poppins", 12))

        # Complaint Frame
        self.com_form_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.com_form_lbl = ctk.CTkLabel(self.com_form_frm, text="Complaint:", font=("Poppins", 15))
        self.com_form_ent_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="gray", border_color="gray")
        self.com_form_ent = ctk.CTkTextbox(self.com_form_ent_frm, font=("Poppins", 15), width=700, height=150)

        # Error Message When Complaint is Left blank
        self.com_form_error_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.comp_form_error_lbl = ctk.CTkLabel(self.com_form_error_frm, text= "", font=("Poppins", 12), text_color= "red")

        self.submit_com_form_btn = ctk.CTkButton(self.user_comp_form_frm, text="Submit Now", font=("Poppins", 15), command=self.insert)

        # Submit Button
    def show(self):
        self.hide()

        # Packing Widgets
        self.user_name_lbl.pack(padx=(50, 3), pady=(10, 0), side="left")
        self.user_name_ent.pack(padx=(10, 20), pady=(10, 0), side="left")
        self.user_id_lbl.pack(padx=(50, 3), pady=(10, 0), side="left")
        self.user_id_ent.pack(padx=(10, 20), pady=(10, 0), side="left")

        self.gender_lbl.pack(padx=(50, 11), pady=5, side="left")
        self.gender_dropdown.pack(padx = 2, pady = 2)
        self.gender_dropdown_frm.pack(pady=(0, 3), side="left")

        self.subject_lbl.pack(padx=(50, 3), pady=(5, 5), side="left")
        self.subject_ent.pack(padx=(10, 20), pady=(5, 5), side="left")

        self.com_form_lbl.pack(padx=(50, 3), side="left")
        
        self.user_name_inf_frm.pack()
        self.name_error.pack(padx= (50, 50), fill="x", expand= True)
        self.user_name_frm.pack(padx=10, pady=1, side="left")

        self.user_id_inf_frm.pack()
        self.id_error.pack(padx= (50,50), fill="x", expand= True)
        self.user_id_frm.pack(padx=10, pady=1, side="left")

        self.name_id_frm.pack(pady=(20,0), padx=5)

        
       
        # self.name_id_error_frm.pack(padx=15, fill="x", expand= True)
        self.gender_frm.pack(padx=15, fill="x", expand=True)
        self.gender_error_lbl.pack(side= "left", padx=50)
        self.gender_error_frm.pack(fill= "x", expand= True, padx= 15)
        self.subject_frm.pack(padx=15, fill="x", expand=True)
        self.subject_error_lbl.pack(padx = 50, side = "left")
        self.subject_error_frm.pack(fill = "x", expand= True, padx= 15)
        self.com_form_frm.pack(padx=15, fill="x", expand=True)
        self.comp_form_error_lbl.pack(side = "left", padx= 50)
        self.com_form_error_frm.pack(fill = "x", expand= True, padx= 15)
        self.com_form_ent.pack(padx= 2, pady=2)
        self.com_form_ent_frm.pack(padx=(65, 20))
        self.submit_com_form_btn.pack(pady=5)
        self.logout_btn.pack(padx = (20, 125), side= "left")
        self.user_comp_title_lbl.pack(side = "left")
        
        self.header_frm.pack(pady = 15, fill= "x", expand = "True")
        self.user_comp_form_frm.pack(padx=20, pady=5)


       
        # Pack the main frame
        self.user_comp_int_frm.pack()

    def insert(self):
        self.name = self.username_com_form.get()
        self.user_id = self.userid_com_form.get()
        self.gender = self.usergender_com_form.get()
        self.subject = self.subject_com_form.get()
        self.complain = self.com_form_ent.get("0.0", "end-1c")
        self.has_empty = False
        self.name_error.configure(text= "")
        self.id_error.configure(text= "")
        self.gender_error_lbl.configure(text= "")
        self.subject_error_lbl.configure(text= "")
        self.comp_form_error_lbl.configure(text= "")
        for item in [self.name, self.user_id, self.gender, self.subject, self.complain]:
            if item == self.name == "":
                self.name_error.configure(text= "Name is Required*")
                if not self.has_empty:
                    self.has_empty = True
            if item == self.user_id == "":
                self.id_error.configure(text= "ID Number is Required*")
                if not self.has_empty:
                    self.has_empty = True
            if item == self.gender == "":
                self.gender_error_lbl.configure(text= "Gender is Required*")
                if not self.has_empty:
                    self.has_empty = True
            if item == self.subject == "":
                self.subject_error_lbl.configure(text= "Subject is Required*")
                if not self.has_empty:
                    self.has_empty = True
            if item == self.complain == "":
                self.comp_form_error_lbl.configure(text= "Complaint is Required*")
                if not self.has_empty:
                    self.has_empty = True
            
        if not self.has_empty:
            self.cursor.execute(
                "INSERT INTO complaint_form (name, user_id, gender, Subject, Complaint) VALUES (?, ?, ?, ?, ?)",
                (self.name, self.user_id, self.gender, self.subject, self.complain)
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
class AdminMainInterface:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection
        self.admin_main_int = ctk.CTkFrame(self.root, fg_color= "transparent")
        self.admin_form_frm = ctk.CTkScrollableFrame(self.admin_main_int, border_color="#00009e", border_width=2, width=800, height=500)
    def show(self):
        self.header_frm = ctk.CTkFrame(self.admin_main_int, fg_color= "transparent")
        self.logout_btn = ctk.CTkButton(self.header_frm, text= "Logout", command = lambda: log_in("logoutadmin", "logoutadmin"))
        self.admin_title_lbl = ctk.CTkLabel(self.header_frm, text="Complaint Cabinet", font=("Poppins", 35))
        self.delete_all_btn = ctk.CTkButton(self.header_frm, text= "Delete All", font=("Poppins", 12), command= self.delete_all, fg_color="red", hover_color= "pink")

        self.cursor.execute("SELECT complaint_no, name, Subject FROM complaint_form")
        self.records = self.cursor.fetchall()
        if len(self.records) == 0:
            self.show_none()
        else:
            self.show_records()
        self.logout_btn.pack(padx = (20, 125), side= "left")
        self.admin_title_lbl.pack(side = "left")
        self.delete_all_btn.pack(side= "left", padx = (125, 20))
        self.header_frm.pack(pady = 15, fill= "x", expand = "True")
        self.admin_form_frm.pack(fill = "x", expand = True)
        self.admin_main_int.pack()
    def show_records(self):
        # Clear previous data
        for widget in self.admin_form_frm.winfo_children():
            widget.destroy()

        # Column headers
        columns = ["Complaint\nNo.", "Name", "Subject"]
        header_frame = ctk.CTkFrame(self.admin_form_frm, fg_color="lightgray", corner_radius=8)
        header_frame.pack(fill="x", padx=5, pady=2)

        for col_index, col_name in enumerate(columns):
            header_label = ctk.CTkLabel(header_frame, text=col_name, font=("Poppins", 15), padx=5, pady=5)
            header_label.grid(row=0, column=col_index, sticky="nsew", padx=2, pady=2)

        # Make the columns expand equally in the header frame
        for col_index in range(len(columns)):
            header_frame.grid_columnconfigure(col_index, weight=1, minsize= 200)

        # Display each record as a separate frame
        for num in range(len(self.records)):
            # Create a frame for each row to ensure it acts as a block element
            record_frame = ctk.CTkFrame(self.admin_form_frm, fg_color="#00C0F0", corner_radius=8)
            record_frame.pack(fill="x", padx=5, pady=2)

            # Bind the entire frame to the click event
            record_frame.bind("<Button-1>", lambda event, complaint_no = num+1: self.show_individual_record(complaint_no))
            record_frame.bind("<Enter>", lambda event, f=record_frame: self.on_enter(f))
            record_frame.bind("<Leave>", lambda event, f=record_frame: self.on_leave(f))

            # Display each field inside the record frame in a grid format
            for col_index, field in enumerate(self.records[num]):
                field_label = ctk.CTkLabel(record_frame, text=str(field), font=("Poppins", 15), padx=5, pady=5, justify = "center")
                field_label.grid(row=0, column=col_index, sticky="nsew", padx=2, pady=2)
                
                field_label.bind("<Button-1>", lambda event, complaint_no = self.records[num][0]: self.show_individual_record(complaint_no))
                field_label.bind("<Enter>", lambda event, f=record_frame: self.on_enter(f))
                field_label.bind("<Leave>", lambda event, f=record_frame: self.on_leave(f))


            # Make the columns expand equally in each record frame
            for col_index in range(len(columns)):
                record_frame.grid_columnconfigure(col_index, weight=1, minsize = 200)
    def hide(self):
        self.admin_main_int.forget()

    def on_enter(self, frame):
        frame.configure(fg_color = '#0083A3')

    def on_leave(self, frame):
        frame.configure(fg_color = '#00C0F0')

    def show_individual_record(self, complaint_no):
        self.hide()
        self.cursor.execute(f'SELECT * FROM complaint_form WHERE complaint_no = {complaint_no}')
        self.selected_record = self.cursor.fetchall()
        self.user_name = self.selected_record[0][1]
        self.user_id = self.selected_record[0][2]
        self.user_gender = self.selected_record[0][3]
        self.user_subject = self.selected_record[0][4]
        self.user_complaint = self.selected_record[0][5]

        self.user_comp_int_frm = ctk.CTkFrame(self.root, fg_color="transparent")

         # Frame for the entire form
        self.header_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.user_comp_title_lbl = ctk.CTkLabel(self.header_frm, text="Complaint Form", font=("Poppins", 35))
        self.go_back_frm = ctk.CTkFrame(self.header_frm, fg_color="yellow", border_width=2, corner_radius= 20)
        self.go_back_icon = ctk.CTkImage(go_back_img, size=(30,30))
        self.go_back_icon_holder = ctk.CTkLabel(self.go_back_frm, image= self.go_back_icon, text="", bg_color="yellow")
        self.go_back_lbl = ctk.CTkLabel(self.go_back_frm, text= "Go Back", font=("Poppins", 15), bg_color="yellow")
        self.go_back_frm.bind("<Button-1>", lambda event: self.go_back())
        self.go_back_icon_holder.bind("<Button-1>", lambda event: self.go_back())
        self.go_back_lbl.bind("<Button-1>", lambda event: self.go_back())

        


        self.delete_frm = ctk.CTkFrame(self.header_frm, fg_color='red', border_width=2, corner_radius= 20)
        self.delete_icon = ctk.CTkImage(delete_img, size=(30,30))
        self.delete_icon_holder = ctk.CTkLabel(self.delete_frm, image= self.delete_icon, text= "", bg_color="transparent")
        self.delete_complaint_lbl = ctk.CTkLabel(self.delete_frm, text="Delete Complaint", font=("Poppins", 15), bg_color="transparent")
        self.delete_frm.bind("<Button-1>", lambda event, complaint_no = complaint_no: self.delete_individual_record(complaint_no))
        self.delete_icon_holder.bind("<Button-1>", lambda event, complaint_no = complaint_no: self.delete_individual_record(complaint_no))
        self.delete_complaint_lbl.bind("<Button-1>", lambda event, complaint_no = complaint_no: self.delete_individual_record(complaint_no))
        self.user_comp_form_frm = ctk.CTkScrollableFrame(self.user_comp_int_frm, border_color="#00009e", border_width=2, width=800, height=500)

        
        # Name and ID Frame
        self.name_id_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.user_name_frm = ctk.CTkFrame(self.name_id_frm, fg_color="transparent")
        self.user_name_lbl = ctk.CTkLabel(self.user_name_frm, text="Name:", font=("Poppins", 15))
        self.user_name_ent = ctk.CTkEntry(self.user_name_frm, font=("Poppins", 15), placeholder_text="Enter your name", width=250)
        self.user_name_ent.insert(0, self.user_name)
        self.user_name_ent.configure(state= "readonly")

        self.user_id_frm = ctk.CTkFrame(self.name_id_frm, fg_color="transparent")
        self.user_id_lbl = ctk.CTkLabel(self.user_id_frm, text="ID Number:", font=("Poppins", 15))
        self.user_id_ent = ctk.CTkEntry(self.user_id_frm, font=("Poppins", 15), placeholder_text="Enter your ID", width=250)
        self.user_id_ent.insert(0, self.user_id)
        self.user_id_ent.configure(state = "readonly")
        # Gender Frame
        self.gender_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.gender_lbl = ctk.CTkLabel(self.gender_frm, text="Gender:", font=("Poppins", 15))
        self.gender_dropdown = ctk.CTkEntry(self.gender_frm, width=250, font=("Poppins", 15))
        self.gender_dropdown.insert(0, self.user_gender)
        self.gender_dropdown.configure(state= "readonly")
        # Subject Frame
        self.subject_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.subject_lbl = ctk.CTkLabel(self.subject_frm, text="Subject:", font=("Poppins", 15))
        self.subject_ent = ctk.CTkEntry(self.subject_frm, font=("Poppins", 15), placeholder_text="Subject of Complaint", width=500)
        self.subject_ent.insert(0, self.user_subject)
        self.subject_ent.configure(state= "readonly")
        # Complaint Frame
        self.com_form_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.com_form_lbl = ctk.CTkLabel(self.com_form_frm, text="Complaint:", font=("Poppins", 15))
        self.com_form_ent = ctk.CTkTextbox(self.user_comp_form_frm, font=("Poppins", 15), width=700, height=150)
        self.com_form_ent.insert("0.0", self.user_complaint)
        self.com_form_ent.configure(state= "disabled")

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
        
        self.go_back_icon_holder.pack(side = "left", padx = 5, pady= 10)
        self.go_back_lbl.pack(side= "left", padx = 5, pady= 10)
        
        
        self.delete_icon_holder.pack(side= "left", padx = 5, pady= 10)
        self.delete_complaint_lbl.pack(side= "left", padx = 5, pady= 10)

        self.go_back_frm.pack(side = "left", padx = (20,0))
        self.user_comp_title_lbl.pack(side = "left", padx = (170,75))
        self.delete_frm.pack(side = "left", padx = (0,20))
        self.header_frm.pack(pady = 15, fill= "x", expand = "True")
        
        
        
        self.user_comp_form_frm.pack(padx=20, pady=5)


       
        # Pack the main frame
        self.user_comp_int_frm.pack()
    
    def delete_individual_record(self, complaint_no):
        self.cursor.execute(f"DELETE FROM complaint_form WHERE complaint_no = {complaint_no}")
        self.connection.commit()
        self.cursor.execute(f"SELECT complaint_no FROM complaint_form LIMIT 1")
        self.next_complaint = self.cursor.fetchall()
        self.hide_individual_record()
        if len(self.next_complaint) == 0:
            self.go_back()
        else:
            self.show_individual_record(self.next_complaint[0][0])
    
    def hide_individual_record(self):
        self.user_comp_int_frm.forget()

    def go_back(self):
        self.hide_individual_record()
        self.admin_main_int.pack()
        self.show()

    def show_none(self):
        for widget in self.admin_form_frm.winfo_children():
            widget.destroy()

        self.none_lbl = ctk.CTkLabel(self.admin_form_frm, text="There is are complaints yet currently.", font=("Poppins", 36), height= 500, text_color= "#a6a6a6")
        self.none_lbl.pack(fill= "both", expand= True)

    def delete_all(self):
        self.cursor.execute("DELETE FROM complaint_form")
        self.connection.commit()
        self.hide()
        self.show()
        




    
complaintforminterface = ComplaintForm(root, cursor, connection)
adminmaininterface = AdminMainInterface(root, cursor, connection)
# Functions
def log_in(username, userpassword):
    global cursor, complaintforminterface
    cursor.execute("SELECT * FROM complaint_form")
    records = cursor.fetchall()
    print(records)
    if username == userpassword == "logout":
        login_frm.pack()
        complaintforminterface.hide()
    elif username == userpassword == "logoutadmin":
        login_frm.pack()
        adminmaininterface.hide()
    elif username.get() == userpassword.get() == "user":
        login_frm.forget()
        complaintforminterface.show()
    elif username.get() == userpassword.get() == "admin":
        login_frm.forget()
        adminmaininterface.show()
    
        



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

# End of Admin Interface #
root.mainloop()
