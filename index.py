import customtkinter as ctk
import sqlite3
import tkinter as tk
from PIL import Image
from datetime import datetime

# Top Level Class
    


# System Defaults
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.FontManager.load_font("assets/fonts/Poppins.ttf")
profile_img = Image.open("assets/images/profile.png")
delete_img = Image.open("assets/images/delete.png")
go_back_img = Image.open("assets/images/go_back.png")
success_img = Image.open("assets/images/success.png")
bg_img = Image.open("assets/images/bg.jpg")
root = ctk.CTk()
window_width = 1000
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))-50

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root_bg_img= ctk.CTkImage(bg_img, size=(window_width, window_height))
root_bg_lbl = ctk.CTkLabel(root, image= root_bg_img, text= "")
root_bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
root.title("Complaint Management System")
connection = sqlite3.connect("cms.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS complaint_form (
               complaint_no INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(250),
               user_id VARCHAR(250),
               gender VARCHAR(250),
               Subject VARCHAR(250),
               Complaint TEXT,
               Date VARCHAR(250),
               status VARCHAR(250),
               Remarks TEXT,
               user_type VARCHAR(250),
               user_view VARCHAR(250)
               )
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
               account_id INTEGER PRIMARY KEY AUTOINCREMENT,
               username VARCHAR(250),
               password VARCHAR(250),
               user_type VARCHAR(250)
               ) ''')
class ComplaintForm:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection
        

    def submit(self):
        frame_width = 400
        frame_height = 200
        x = (self.root.winfo_width()/2) - (frame_width/2)
        y = (self.root.winfo_height()/2) - (frame_height/2)
        self.success_msg_frm = ctk.CTkFrame(self.root, width= frame_width, height= frame_height, fg_color= "transparent", border_color="green", border_width= 5)
        self.success_icon = ctk.CTkImage(success_img, size=(100,100))
        self.success_msg_lbl = ctk.CTkLabel(self.success_msg_frm, text= "Complaint has been submitted!", font=("Poppins", 18))
        self.success_icon_holder = ctk.CTkLabel(self.success_msg_frm, image=self.success_icon, text="")

        self.success_msg_lbl.pack(fill="x", expand= True, pady = 10, padx= 50)
        self.success_icon_holder.pack(fill= "x", expand= True, pady=(0,10), padx= 50)
        self.success_msg_frm.place(x= x, y = y)
        self.success_msg_frm.after(800, self.success_msg_frm.place_forget)
        self.user_comp_int_frm.after(800, self.user_comp_int_frm.forget)
        
    def show(self, username, user_type):
        self.user_comp_int_frm = ctk.CTkFrame(self.root, fg_color="transparent", border_color= "#00009e", border_width= 5)
        self.username_com_form = tk.StringVar()
        self.userid_com_form = tk.StringVar()
        self.usergender_com_form = tk.StringVar()
        self.subject_com_form = tk.StringVar()
         # Frame for the entire form
        self.header_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.logout_btn = ctk.CTkButton(self.header_frm, text= "Go Back", command = lambda: log_in("complaingoback", "complaingoback"))
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
        self.hide()
        self.username = username
        self.user_type = user_type
        # Packing Widgets
        self.user_name_lbl.pack(padx=(50, 3), pady=(10, 0), side="left")
        self.user_name_ent.pack(padx=(10, 20), pady=(10, 0), side="left")
        self.user_name_ent.insert(0, self.username)
        self.user_name_ent.configure(state= "readonly")
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
        
        self.header_frm.pack(pady = 15, fill= "x", expand = "True", padx= 8)
        self.user_comp_form_frm.pack(padx=20, pady=10)


       
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
                "INSERT INTO complaint_form (name, user_id, gender, Subject, Complaint, Date, status, user_type, Remarks, user_view) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (self.name, self.user_id, self.gender, self.subject, self.complain, datetime.now().strftime("%B %d, %Y"), "Unchecked",self.user_type,"", "1")
            )
            self.connection.commit()
            self.cursor.execute("SELECT * FROM complaint_form")
            self.cursor_records = self.cursor.fetchall()
            self.submit()
            self.show(self.username, self.user_type)
            
    
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

    def show(self):
        self.admin_main_int = ctk.CTkFrame(self.root, fg_color= "transparent", border_color="#00009e", border_width=5, width= 900)
        self.admin_form_frm = ctk.CTkScrollableFrame(self.admin_main_int, border_color="#00009e", border_width=2, width=800, height=500)
        self.header_frm = ctk.CTkFrame(self.admin_main_int, fg_color= "transparent")
        self.logout_btn = ctk.CTkButton(self.header_frm, text= "Logout", command = lambda: log_in("logoutadmin", "logoutadmin"))
        self.admin_title_lbl = ctk.CTkLabel(self.header_frm, text="Complaint Cabinet", font=("Poppins", 35))
        self.delete_all_btn = ctk.CTkButton(self.header_frm, text= "Delete All", font=("Poppins", 12), command= self.delete_all, fg_color="red", hover_color= "pink")

        self.search_frm = ctk.CTkFrame(self.admin_main_int, fg_color="transparent")
        self.search_lbl = ctk.CTkLabel(self.search_frm, text= "Search: ", font = ("Poppins", 18))
        self.search_bar = ctk.CTkEntry(self.search_frm, width= 300)


        self.cursor.execute("SELECT complaint_no, status, user_type, name, Subject FROM complaint_form")
        self.records = self.cursor.fetchall()

        self.header_frm.pack(pady = 15, padx= 20, fill= "x", expand = "True")
        self.search_lbl.pack(side= "left")
        self.search_bar.pack(side = "left", padx= 20)
        self.search_frm.pack(expand = True)
        self.search_bar.bind("<KeyRelease>",self.filter_records)
        self.show_all_records()
        self.logout_btn.pack(padx = (20, 125), side= "left")
        self.admin_title_lbl.pack(side = "left")
        self.delete_all_btn.pack(side= "left", padx = (125, 20))
        
        
        self.admin_main_int.pack(fill= "x", expand= True, padx= 10)
    def filter_records(self, event= None):
        self.keyword = self.search_bar.get()
        self.admin_form_frm.forget()
        self.show_all_records(self.keyword)
    def show_all_records(self, searched_key = ""):
        self.searched_key = searched_key.strip()
        self.cursor.execute(f"SELECT complaint_no, status, user_type, name, Subject FROM complaint_form WHERE complaint_no LIKE '%{self.searched_key}%' OR status LIKE '%{self.searched_key}%' OR user_type LIKE '%{self.searched_key}%' OR name LIKE '%{self.searched_key}%' OR Subject LIKE '%{self.searched_key}%'")
        self.records = self.cursor.fetchall() 
        if len(self.records) == 0:
            self.show_none()
        else:
            self.show_records()
        self.admin_form_frm.pack(fill = "x", expand = True, padx= 20, pady= 10)
    def show_records(self):
        # Clear previous data
        for widget in self.admin_form_frm.winfo_children():
            widget.destroy()

        # Column headers
        columns = ["Complaint\nNo.", "Status", "User\nType", "Name", "Subject"]
        self.header_frame = ctk.CTkFrame(self.admin_form_frm, fg_color="lightgray", corner_radius=8)
        self.header_frame.pack(fill="x", padx=5, pady=2)

        for col_index, col_name in enumerate(columns):
            header_label = ctk.CTkLabel(self.header_frame, text=col_name, font=("Poppins", 15), padx=5, pady=5)
            header_label.grid(row=0, column=col_index, sticky="nsew", padx=2, pady=2)

        # Make the columns expand equally in the header frame
        for col_index in range(len(columns)):
            self.header_frame.grid_columnconfigure(col_index, weight=1, minsize= 120)

        # Display each record as a separate frame
        for num in range(len(self.records)):
            # Create a frame for each row to ensure it acts as a block element
            record_frame = ctk.CTkFrame(self.admin_form_frm, fg_color="#00C0F0", corner_radius= 8)
            record_frame.pack(fill="x", padx=5, pady=2)

            # Bind the entire frame to the click event
            record_frame.bind("<Button-1>", lambda event, complaint_no = self.records[num][0]: self.show_individual_record(complaint_no))
            record_frame.bind("<Enter>", lambda event, f=record_frame: self.on_enter(f))
            record_frame.bind("<Leave>", lambda event, f=record_frame: self.on_leave(f))

            # Display each field inside the record frame in a grid format
            for col_index, field in enumerate(self.records[num]):
                field_label = ctk.CTkLabel(record_frame, text=str(field) if len(str(field)) <= 13 else f"{field[:10]}...", font=("Poppins", 15), padx=5, pady=5, justify = "center")
                field_label.grid(row=0, column=col_index, sticky="nsew", padx=2, pady=2)
                
                field_label.bind("<Button-1>", lambda event, complaint_no = self.records[num][0]: self.show_individual_record(complaint_no))
                field_label.bind("<Enter>", lambda event, f=record_frame: self.on_enter(f))
                field_label.bind("<Leave>", lambda event, f=record_frame: self.on_leave(f))


            # Make the columns expand equally in each record frame
            for col_index in range(len(columns)):
                record_frame.grid_columnconfigure(col_index, weight=1, minsize = 120)
    def hide(self):
        self.admin_main_int.forget()
    def on_enter(self, frame):
        frame.configure(fg_color = '#0083A3')

    def on_leave(self, frame):
        frame.configure(fg_color = '#00C0F0')

    def show_individual_record(self, complaint_no):
        
        self.cursor.execute(f'SELECT * FROM complaint_form WHERE complaint_no = {complaint_no}')
        self.selected_record = self.cursor.fetchall()
        
        self.hide()
        self.complaint_no = self.selected_record[0][0]
        self.user_name = self.selected_record[0][1]
        self.user_id = self.selected_record[0][2]
        self.user_gender = self.selected_record[0][3]
        self.user_subject = self.selected_record[0][4]
        self.user_complaint = self.selected_record[0][5]
        self.user_date = self.selected_record[0][6]
        self.user_status = self.selected_record[0][7]
        self.remarks = self.selected_record[0][8]
        self.user_type = self.selected_record[0][9]

        self.user_comp_int_frm = ctk.CTkFrame(self.root, fg_color="transparent", border_color="#00009e", border_width=5)

        # Frame for the entire form
        self.header_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.user_comp_title_lbl = ctk.CTkLabel(self.header_frm, text=f"Complaint No. {self.complaint_no}", font=("Poppins", 35))
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

        self.immutable_info_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.status_date_frm = ctk.CTkFrame(self.immutable_info_frm, fg_color= "transparent")
        self.status_lbl = ctk.CTkLabel(self.status_date_frm, text= f"Status: {self.user_status}" , font=("Poppins", 15))
        self.date_lbl = ctk.CTkLabel(self.status_date_frm, text= f"Date Submitted: {self.user_date}", font=("Poppins", 15) )
        self.usertype_lbl = ctk.CTkLabel(self.immutable_info_frm, text= f"User Type: {self.user_type}", font=("Poppins", 15), anchor= "w")

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

        self.remark_form_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.remark_form_lbl = ctk.CTkLabel(self.remark_form_frm, text="Remarks:", font=("Poppins", 15))
        self.remark_form_ent = ctk.CTkTextbox(self.user_comp_form_frm, font=("Poppins", 15), width=700, height=150)
        self.remark_form_ent.insert("0.0", self.remarks)
        
        self.remark_form_error_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.remark_form_error_lbl = ctk.CTkLabel(self.remark_form_error_frm, text= "", font=("Poppins", 12), text_color= "red")

        self.solve_com_form_btn = ctk.CTkButton(self.user_comp_form_frm, text="Solve", font=("Poppins", 15), command= self.update)
        

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
        
        self.remark_form_lbl.pack(padx=(50, 3), pady=5, side="left")
        self.remark_form_frm.pack(pady=3, padx=15, fill="x", expand=True)
        self.remark_form_error_lbl.pack(side = "left", padx= 50)
        self.remark_form_error_frm.pack(fill = "x", expand= True, padx= 15)
        self.remark_form_ent.pack(padx=(65, 20), pady=5)

        self.solve_com_form_btn.pack(pady=5)
        self.go_back_icon_holder.pack(side = "left", padx = 5, pady= 10)
        self.go_back_lbl.pack(side= "left", padx = 5, pady= 10)
        
        
        self.delete_icon_holder.pack(side= "left", padx = 5, pady= 10)
        self.delete_complaint_lbl.pack(side= "left", padx = 5, pady= 10)

        self.go_back_frm.pack(side = "left", padx = (20,0))
        self.user_comp_title_lbl.pack(side = "left", padx = (170,75))
        self.delete_frm.pack(side = "left", padx = (0,20))
        self.header_frm.pack(pady = 15, expand = "True")
        
        self.status_lbl.pack(side = "left")
        self.date_lbl.pack(side= "left", padx= (450, 20))
        self.status_date_frm.pack(fill= "x")
        self.usertype_lbl.pack(fill="x")
        self.immutable_info_frm.pack(fill= "x", padx= 75)
        
        
        self.user_comp_form_frm.pack(padx=20, pady=10)


    
        # Pack the main frame
        self.user_comp_int_frm.pack()
    

    def delete_individual_record(self, complaint_no):
        self.cursor.execute(f"SELECT complaint_no FROM complaint_form")
        self.complaint_num_arr = self.cursor.fetchall()
        for num in range(len(self.complaint_num_arr)):
            if self.complaint_num_arr[num][0] == complaint_no:
                self.complaint_num_idx = num
        self.cursor.execute(f"DELETE FROM complaint_form WHERE complaint_no = {complaint_no}")
        self.connection.commit()
        self.next_complaint = self.complaint_num_arr[(self.complaint_num_idx + 1) % len(self.complaint_num_arr)][0]
        self.hide_individual_record()
        if len(self.complaint_num_arr) == 1:
            self.go_back()
        else:
            self.show_individual_record(self.next_complaint)
    
    def hide_individual_record(self):
        self.user_comp_int_frm.forget()

    def go_back(self):
        self.hide_individual_record()
        self.show_all_records()
        self.admin_main_int.pack()

    def show_none(self):
        for widget in self.admin_form_frm.winfo_children():
            widget.destroy()

        self.none_lbl = ctk.CTkLabel(self.admin_form_frm, text="There are no complaints yet currently.", font=("Poppins", 36), height= 500, text_color= "#a6a6a6")
        self.none_lbl.pack(fill= "both", expand= True)

    def delete_all(self):
        self.cursor.execute("DELETE FROM complaint_form")
        self.connection.commit()
        self.hide()
        self.show()
    
    def update(self):
        if self.remark_form_ent.get("0.0", "end-1c") != "":
            self.remark_form_error_lbl.configure(text= "")
            self.cursor.execute(f"UPDATE complaint_form SET Remarks = '{self.remark_form_ent.get("0.0", "end-1c")}', status = 'Solved' WHERE complaint_no = {self.complaint_no}")
            self.connection.commit()
            self.submit()
            self.status_lbl.configure(text= "Status: Solved")
        else:
            self.remark_form_error_lbl.configure(text= "Remark is Required*")
    
    def submit(self):
        frame_width = 400
        frame_height = 200
        x = (self.root.winfo_width()/2) - (frame_width/2)
        y = (self.root.winfo_height()/2) - (frame_height/2)
        self.success_msg_frm = ctk.CTkFrame(self.root, width= frame_width, height= frame_height, fg_color= "transparent", border_color="green", border_width= 5)
        self.success_icon = ctk.CTkImage(success_img, size=(100,100))
        self.success_msg_lbl = ctk.CTkLabel(self.success_msg_frm, text= "Remarks have been successfully sent!", font=("Poppins", 18))
        self.success_icon_holder = ctk.CTkLabel(self.success_msg_frm, image=self.success_icon, text="")

        self.success_msg_lbl.pack(fill="x", expand= True, pady = 10, padx= 50)
        self.success_icon_holder.pack(fill= "x", expand= True, pady=(0,10), padx= 50)
        self.success_msg_frm.place(x= x, y = y)
        self.success_msg_frm.after(800, self.success_msg_frm.place_forget)
class RegisterForm:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection
    
    def show(self):
        self.register_main_int = ctk.CTkFrame(self.root, fg_color= "transparent", width= 500, height=500, border_color= "#00009e", border_width= 5)

        self.header_frm = ctk.CTkFrame(self.register_main_int, fg_color= "transparent")
        self.back_to_login_btn = ctk.CTkButton(self.header_frm, text= "Back to Login", hover_color="gray", text_color= "#00009e", width= 75, fg_color= "transparent", command= lambda: log_in("gobackfromregister", "gobackfromregister"))
        self.header_title = ctk.CTkLabel(self.header_frm, text= "Register Form", font= ("Poppins", 30))

        self.user_username_lbl = ctk.CTkLabel(self.register_main_int, text= "Username:" , font= ("Poppins", 18), text_color= "#00009e", anchor= "w", width= 250)
        self.user_username_ent = ctk.CTkEntry(self.register_main_int, placeholder_text="Enter your username:", corner_radius= 50, width= 400, font= ("Poppins", 14))
        self.user_username_err = ctk.CTkLabel(self.register_main_int, text= "", text_color="red", font= ("Poppins", 10), anchor= "w")
        self.user_password_lbl = ctk.CTkLabel(self.register_main_int, text= "Password:", font= ("Poppins", 18), text_color= "#00009e", anchor= "w", width= 250)
        self.user_password_ent = ctk.CTkEntry(self.register_main_int, placeholder_text="Enter your password:", show= "•", corner_radius= 50, width= 400, font= ("Poppins", 14))
        self.usertype_lbl = ctk.CTkLabel(self.register_main_int, text= "User Type: ", font= ("Poppins", 18), text_color= "#00009e", anchor= "w", width= 400)
        self.usertype_frm = ctk.CTkFrame(self.register_main_int, fg_color="transparent", border_color="gray", border_width= 5, bg_color="transparent")
        self.usertype_dropdown = ctk.CTkOptionMenu(self.usertype_frm, width=250, values=["Student", "Faculty", "Facility", "Others"], font=("Poppins", 15), fg_color= "white", text_color="black")
        self.register_btn = ctk.CTkButton(self.register_main_int, text= "Register", corner_radius= 20, font= ("Poppins", 18), width= 400, command=lambda: self.verify(self.user_username_ent.get(), self.user_password_ent.get(), self.usertype_dropdown.get()))

        self.header_frm.pack(fill= "x", pady= 20, padx= 20)
        self.back_to_login_btn.pack(side= "left")
        self.header_title.pack(side= "left", padx= (50, 100))
        self.user_username_lbl.pack(fill="x", padx= 20)
        self.user_username_ent.pack()
        self.user_username_err.pack(pady= (0, 20))
        self.user_password_lbl.pack(fill="x", padx= 20)
        self.user_password_ent.pack(pady= (0, 40))
        self.usertype_lbl.pack(fill= "x", padx= 20)
        self.usertype_dropdown.pack(padx= 3, pady= 3)
        self.usertype_frm.pack()
        self.register_btn.pack(pady= (30, 10))
        self.register_main_int.pack_propagate(False)
        self.register_main_int.pack(expand= True)
    
    def verify(self, user_name, password, user_type):
        self.user_name = user_name
        self.password = password
        self.user_type = user_type
        if user_name != "" and password != "":
            self.cursor.execute(f"SELECT username FROM accounts WHERE username LIKE '{self.user_name}'")
            self.results = self.cursor.fetchall()
            if len(self.results) == 0:
                self.cursor.execute(f"INSERT INTO accounts (username, password, user_type) VALUES (?,?,?)", (self.user_name, self.password, self.user_type))
                self.connection.commit()
                self.submit()
                self.user_password_ent.delete(0, "end")
                self.user_username_ent.delete(0, "end")
            else:
                self.user_username_err.configure(text= f"{self.user_name} is already taken.")
    
    def hide(self):
        self.register_main_int.forget()\
    
    def submit(self):
        frame_width = 400
        frame_height = 200
        x = (self.root.winfo_width()/2) - (frame_width/2)
        y = (self.root.winfo_height()/2) - (frame_height/2)
        self.success_msg_frm = ctk.CTkFrame(self.root, width= frame_width, height= frame_height, fg_color= "transparent", border_color="green", border_width= 5)
        self.success_icon = ctk.CTkImage(success_img, size=(100,100))
        self.success_msg_lbl = ctk.CTkLabel(self.success_msg_frm, text= "Account has been registered!", font=("Poppins", 18))
        self.success_icon_holder = ctk.CTkLabel(self.success_msg_frm, image=self.success_icon, text="")

        self.success_msg_lbl.pack(fill="x", expand= True, pady = 10, padx= 50)
        self.success_icon_holder.pack(fill= "x", expand= True, pady=(0,10), padx= 50)
        self.success_msg_frm.place(x= x, y = y)
        self.success_msg_frm.after(800, self.success_msg_frm.place_forget)
    
class UserMainInterface:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection

    def show(self, username):
        self.username = username
        self.user_main_int = ctk.CTkFrame(self.root, fg_color= "transparent", width= 600, height= 500, border_color="#00009e", border_width= 5)
        self.logout_btn = ctk.CTkButton(self.user_main_int, text="Logout", font= ("Poppins", 30), width= 450, command=lambda: log_in("logoutuser", "logoutuser"))
        self.create_btn = ctk.CTkButton(self.user_main_int, text="Create New Complaint", font= ("Poppins", 30), width= 450, command= self.create)
        self.view_btn = ctk.CTkButton(self.user_main_int, text="View Submitted Complaints", font= ("Poppins", 30), width= 450, command= self.view)


        
        self.create_btn.pack(pady= 50, padx= 20)
        self.view_btn.pack(pady= 50, padx= 20)
        self.logout_btn.pack(pady= 50, padx= 20)
        self.user_main_int.pack_propagate(False)
        self.user_main_int.pack(expand= True)
    
    def hide(self):
        self.user_main_int.forget()
    
    def create(self):
        self.hide()
        self.cursor.execute(f"SELECT user_type FROM accounts WHERE username LIKE '{self.username}'")
        self.user_type = self.cursor.fetchall()[0][0]
        complaintforminterface.show(self.username, self.user_type)
    
    def view(self):
        self.hide()
        submittedcomplaintinterface.show(self.username)

class SubmittedComplaintInterface:
    def __init__(self, root, cursor, connection):
        self.root = root
        self.cursor = cursor
        self.connection = connection
    
    def show(self, username):
        self.username = username
        self.submitted_frm = ctk.CTkFrame(self.root, fg_color="transparent", border_color="#00009e", border_width=5)
        self.header_frm = ctk.CTkFrame(self.submitted_frm, fg_color= "transparent")
        self.go_back_btn = ctk.CTkButton(self.header_frm, text= "Go Back", font= ("Poppins", 15), command= lambda: log_in("viewgoback", "viewgoback"))
        self.header_lbl = ctk.CTkLabel(self.header_frm, text= "Submitted Complaints", font= ("Poppins", 30))

        self.search_frm = ctk.CTkFrame(self.submitted_frm, fg_color="transparent")
        self.search_lbl = ctk.CTkLabel(self.search_frm, text= "Search: ", font = ("Poppins", 18))
        self.search_bar = ctk.CTkEntry(self.search_frm, width= 300)
        self.submitted_com_frm = ctk.CTkScrollableFrame(self.submitted_frm, fg_color="transparent", border_color="#00009e", border_width=3, width=800, height=500)

        
        self.go_back_btn.pack(side= "left", padx= 50)
        self.header_lbl.pack(side= "left", padx= 70)
        self.header_frm.pack(fill= "x", pady= 10, padx= 10)
        self.search_lbl.pack(side= "left")
        self.search_bar.pack(side = "left", padx= 20)
        self.search_frm.pack(expand = True)
        self.search_bar.bind("<KeyRelease>",self.filter_records)
        self.show_all_records()
        self.submitted_frm.pack(expand= True)

    def filter_records(self, event= None):
        self.keyword = self.search_bar.get()
        self.submitted_com_frm.forget()
        self.show_all_records(self.keyword)
    
    def show_all_records(self, searched_key = ""):
        self.searched_key = searched_key.strip()
        self.cursor.execute(f"SELECT status, complaint_no, Date, Subject FROM complaint_form WHERE name = '{self.username}' AND user_view = '1' AND (complaint_no LIKE '%{self.searched_key}%' OR status LIKE '%{self.searched_key}%' OR Subject LIKE '%{self.searched_key}%')")
        self.records = self.cursor.fetchall() 

        if len(self.records) == 0 :
            self.show_none()
        else:
            self.show_records()
        self.submitted_com_frm.pack(padx= 50, pady= 10)
        
    def show_none(self):
        for widget in self.submitted_com_frm.winfo_children():
            widget.destroy()

        self.none_lbl = ctk.CTkLabel(self.submitted_com_frm, text="There are no complaints yet currently.", font=("Poppins", 36), height= 500, text_color= "#a6a6a6")
        self.none_lbl.pack(expand= True)
    
    def show_records(self):
        for widget in self.submitted_com_frm.winfo_children():
            widget.destroy()
        
        columns = ["Status", "Complaint\nNo.", "Date", "Subject"]
        self.header_frame = ctk.CTkFrame(self.submitted_com_frm, fg_color= "lightgray", corner_radius= 8)
        self.header_frame.pack(fill= "x", padx= 5, pady= 2)

        for col_index, col_name in enumerate(columns):
            header_label = ctk.CTkLabel(self.header_frame, text= col_name, font=("Poppins", 15), padx= 5, pady= 5)
            header_label.grid(row=0, column= col_index, sticky= "nsew", padx= 2, pady=2)
        
        for col_index in range(len(columns)):
            self.header_frame.grid_columnconfigure(col_index, weight= 1, minsize= 200)
        
        for num in range(len(self.records)):
            record_frame = ctk.CTkFrame(self.submitted_com_frm, fg_color = "#00C0F0", corner_radius= 8)
            record_frame.pack(fill= "x", padx= 5, pady= 2)

            record_frame.bind("<Button-1>", lambda event, complaint_no = self.records[num][1] : self.show_individual_record(complaint_no))
            record_frame.bind("<Enter>", lambda event, frame= record_frame: self.on_enter(frame))
            record_frame.bind("<Leave>", lambda event, frame= record_frame: self.on_leave(frame))
            for col_index, field in enumerate(self.records[num]):
                field_label = ctk.CTkLabel(record_frame, text= str(field) if len(str(field)) <= 21 else f"{field[:18]}...", font= ("Poppins", 15), padx= 5, pady= 5, justify = "center")
                field_label.grid(row=0, column= col_index, sticky = "nsew", padx= 2, pady= 2)

                field_label.bind("<Button-1>", lambda event, complaint_no = self.records[num][1]: self.show_individual_record(complaint_no))
                field_label.bind("<Enter>", lambda event, frame= record_frame: self.on_enter(frame))
                field_label.bind("<Leave>", lambda event, frame= record_frame: self.on_leave(frame))
            for col_index in range(len(columns)):
                record_frame.grid_columnconfigure(col_index, weight= 1, minsize=200)


    def hide(self):
        self.submitted_frm.forget()

    def on_enter(self, frame):
        frame.configure(fg_color = '#0083A3')

    def on_leave(self, frame):
        frame.configure(fg_color = '#00C0F0')
    
    def show_individual_record(self, complaint_no):
        self.cursor.execute(f"SELECT * FROM complaint_form WHERE complaint_no = {complaint_no}")
        self.selected_record = self.cursor.fetchall()

        self.submitted_frm.forget()

        self.complaint_no = self.selected_record[0][0]
        self.user_name = self.selected_record[0][1]
        self.user_id = self.selected_record[0][2]
        self.user_gender = self.selected_record[0][3]
        self.user_subject = self.selected_record[0][4]
        self.user_complaint = self.selected_record[0][5]
        self.user_date = self.selected_record[0][6]
        self.user_status = self.selected_record[0][7]
        self.remarks = self.selected_record[0][8]
        self.user_type = self.selected_record[0][9]

        self.user_comp_int_frm = ctk.CTkFrame(self.root, fg_color = "transparent", border_color="#00009e", border_width= 5)

        self.header_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.user_comp_title_lbl = ctk.CTkLabel(self.header_frm, text= f"Complaint No. {self.complaint_no}", font= ("Poppins", 35))
        self.go_back_frm = ctk.CTkFrame(self.header_frm, fg_color= "yellow", border_width= 2, corner_radius= 20)
        self.go_back_icon = ctk.CTkImage(go_back_img, size=(30,30))
        self.go_back_icon_holder = ctk.CTkLabel(self.go_back_frm, image= self.go_back_icon, text="", bg_color="yellow")
        self.go_back_lbl = ctk.CTkLabel(self.go_back_frm, text= "Go Back", font=("Poppins", 15), bg_color="yellow")
        self.go_back_frm.bind("<Button-1>", lambda event: self.goback_individual_record())
        self.go_back_icon_holder.bind("<Button-1>", lambda event: self.goback_individual_record())
        self.go_back_lbl.bind("<Button-1>", lambda event: self.goback_individual_record())

        


        self.delete_frm = ctk.CTkFrame(self.header_frm, fg_color='red', border_width=2, corner_radius= 20)
        self.delete_icon = ctk.CTkImage(delete_img, size=(30,30))
        self.delete_icon_holder = ctk.CTkLabel(self.delete_frm, image= self.delete_icon, text= "", bg_color="transparent")
        self.delete_complaint_lbl = ctk.CTkLabel(self.delete_frm, text="Delete Complaint", font=("Poppins", 15), bg_color="transparent")
        self.delete_frm.bind("<Button-1>", lambda event, complaint_no = complaint_no: self.delete_from_user(complaint_no))
        self.delete_icon_holder.bind("<Button-1>", lambda event, complaint_no = complaint_no: self.delete_from_user(complaint_no))
        self.delete_complaint_lbl.bind("<Button-1>", lambda event, complaint_no = complaint_no: self.delete_from_user(complaint_no))

        self.immutable_info_frm = ctk.CTkFrame(self.user_comp_int_frm, fg_color= "transparent")
        self.status_date_frm = ctk.CTkFrame(self.immutable_info_frm, fg_color= "transparent")
        self.status_lbl = ctk.CTkLabel(self.status_date_frm, text= f"Status: {self.user_status}" , font=("Poppins", 15))
        self.date_lbl = ctk.CTkLabel(self.status_date_frm, text= f"Date Submitted: {self.user_date}", font=("Poppins", 15) )
        self.usertype_lbl = ctk.CTkLabel(self.immutable_info_frm, text= f"User Type: {self.user_type}", font=("Poppins", 15), anchor= "w")

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

        # Remark Frame
        self.remark_form_frm = ctk.CTkFrame(self.user_comp_form_frm, fg_color="transparent")
        self.remark_form_lbl = ctk.CTkLabel(self.remark_form_frm, text="Remarks:", font=("Poppins", 15))
        self.remark_form_ent = ctk.CTkTextbox(self.user_comp_form_frm, font=("Poppins", 15), width=700, height=150)
        self.remark_form_ent.insert("0.0", self.remarks)
        self.remark_form_ent.configure(state= "disabled")

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

        self.remark_form_lbl.pack(padx=(50, 3), pady=5, side="left")
        self.remark_form_frm.pack(pady=3, padx=15, fill="x", expand=True)
        self.remark_form_ent.pack(padx=(65, 20), pady=5)
        
        self.go_back_icon_holder.pack(side = "left", padx = 5, pady= 10)
        self.go_back_lbl.pack(side= "left", padx = 5, pady= 10)
        
        
        self.delete_icon_holder.pack(side= "left", padx = 5, pady= 10)
        self.delete_complaint_lbl.pack(side= "left", padx = 5, pady= 10)

        self.go_back_frm.pack(side = "left", padx = (20,0))
        self.user_comp_title_lbl.pack(side = "left", padx = (170,75))
        self.delete_frm.pack(side = "left", padx = (0,20))
        self.header_frm.pack(pady = 15, expand = "True")
        
        self.status_lbl.pack(side = "left")
        self.date_lbl.pack(side= "left", padx= (450, 20))
        self.status_date_frm.pack(fill= "x")
        self.usertype_lbl.pack(fill="x")
        self.immutable_info_frm.pack(fill= "x", padx= 75)
        
        
        self.user_comp_form_frm.pack(padx=20, pady=10)


    
        # Pack the main frame
        self.user_comp_int_frm.pack()
    def goback_individual_record(self):
        self.user_comp_int_frm.forget()
        self.show_all_records()
        self.submitted_frm.pack()
    def delete_from_user(self, complaint_no):
        self.cursor.execute(f"SELECT complaint_no FROM complaint_form")
        self.complaint_num_arr = self.cursor.fetchall()
        for num in range(len(self.complaint_num_arr)):
            if self.complaint_num_arr[num][0] == complaint_no:
                self.complaint_num_idx = num
        self.complaint_no = complaint_no
        self.cursor.execute(f"UPDATE complaint_form SET user_view = '0' WHERE complaint_no = {self.complaint_no}")
        self.connection.commit()
        self.next_complaint = self.complaint_num_arr[(self.complaint_num_idx + 1) % len(self.complaint_num_arr)][0]
        self.hide_individual_record()
        if len(self.complaint_num_arr) == 1:
            self.goback_individual_record()
        else:
            self.show_individual_record(self.next_complaint)
    def hide_individual_record(self):
        self.user_comp_int_frm.forget()



    
complaintforminterface = ComplaintForm(root, cursor, connection)
adminmaininterface = AdminMainInterface(root, cursor, connection)
registerinterface = RegisterForm(root, cursor, connection)
usermaininterface = UserMainInterface(root, cursor, connection)
submittedcomplaintinterface = SubmittedComplaintInterface(root, cursor, connection)
username_login = None
# Functions
def log_in(username, userpassword):
    global username_login, account_notfound_lbl
    if username == userpassword == "complaingoback":
        complaintforminterface.hide()
        usermaininterface.show(username_login)
        return
    elif username == userpassword == "viewgoback":
        submittedcomplaintinterface.hide()
        usermaininterface.show(username_login)
        return
    elif username == userpassword == "logoutadmin":
        login_frm.pack(pady = (25,15))
        adminmaininterface.hide()
        return
    elif username == userpassword == "logoutuser":
        login_frm.pack(pady = (25,15))
        usermaininterface.hide()
        return
    elif username == userpassword == "register":
        login_frm.forget()
        registerinterface.show()
        return
    elif username == userpassword == "gobackfromregister":
        registerinterface.hide()
        login_frm.pack(pady = (25,15))
        return
    elif username == userpassword == "admin":
        login_frm.forget()
        adminmaininterface.show()
        user_username_ent.delete(0, "end")
        user_password_ent.delete(0, "end")
        return
    cursor.execute(f"SELECT * FROM accounts WHERE username LIKE '{username}'")
    matched_username = cursor.fetchall()
    if len(matched_username) == 0 or (username != matched_username[0][1]) or (userpassword != matched_username[0][2]):
        account_notfound_lbl.configure(text= "Account not found!")
    elif (username == matched_username[0][1]) and (userpassword == matched_username[0][2]):
        login_frm.forget()
        username_login = username
        usermaininterface.show(username_login)
        user_username_ent.delete(0, "end")
        user_password_ent.delete(0, "end")
        account_notfound_lbl.configure(text= "")
    
    
        



# Log in Interface
login_frm = ctk.CTkFrame(root, fg_color= "transparent", border_color="#00009e", border_width= 5, bg_color="transparent")
login_title_frm = ctk.CTkFrame(login_frm, fg_color= "#00009e", corner_radius= 60, bg_color="transparent")
login_title_lbl = ctk.CTkLabel(login_title_frm, text= "Complaint Management System", font= ("Poppins", 30), bg_color= "#00009e", text_color= "#e7e8e8")
login_title_frm.pack(pady= 10, padx= 20)
login_title_lbl.pack(padx = 20, pady = 40)



# Start of User Form #
## End of Variable Holder ##
user_form_frm = ctk.CTkFrame(login_frm, border_color= "#00009e", corner_radius= 20, border_width= 3)
icon_frm = ctk.CTkFrame(user_form_frm)
user_form_icon = ctk.CTkImage(profile_img, size=(80,80))
user_form_icon_holder = ctk.CTkLabel(user_form_frm, image= user_form_icon, text= "", width= 250)
user_form_lbl = ctk.CTkLabel(user_form_frm, text= "Member Login" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
# Error Message
account_notfound_lbl = ctk.CTkLabel(user_form_frm, fg_color="transparent", text= "", font= ("Poppins", 11), text_color= "red")

user_username_lbl = ctk.CTkLabel(user_form_frm, text= "Username:" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_username_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your username:", corner_radius= 50, width= 250, font= ("Poppins", 12), textvariable= username_login)
user_password_lbl = ctk.CTkLabel(user_form_frm, text= "Password:", font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_password_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your password:", show= "•", corner_radius= 50, width= 250, font= ("Poppins", 12))
register_frm = ctk.CTkFrame(user_form_frm, fg_color="transparent")
register_lbl = ctk.CTkLabel(register_frm, text= "Don't have an account?", font= ("Poppins", 10), text_color= "#00009e")
register_btn = ctk.CTkButton(register_frm, text= "Register", fg_color= "transparent", bg_color= "transparent", text_color= "#00009e", hover_color= "gray", font= ("Poppins", 12), width= 50, command= lambda: log_in("register", "register"))
user_form_submit_btn = ctk.CTkButton(user_form_frm, text= "Log in", font= ("Poppins", 15), width= 250, corner_radius= 50, command= lambda: log_in(user_username_ent.get(), user_password_ent.get()))

user_form_icon_holder.pack(pady= (5,0), padx= 20)
user_form_lbl.configure(anchor="center", justify="center")
user_form_lbl.pack(padx= 20, fill= "x")
account_notfound_lbl.pack(expand= True)
user_username_lbl.pack(pady = (5, 0), padx = 20)
user_username_ent.pack(pady = (10, 0), padx = 20)
user_password_lbl.pack(pady = (20, 0), padx = 20)
user_password_ent.pack(pady = (10, 0), padx = 20)
register_frm.pack(pady= (10,0), padx= 20, fill= "x")
register_lbl.pack(side= "left", padx= (30, 5))
register_btn.pack(side= "left")
user_form_submit_btn.pack(pady = (10, 10), padx = 20)
user_form_frm.pack(pady= (15, 10), padx= 20)
login_frm.pack(pady = (25,15))
# End of User Form #


root.mainloop()
