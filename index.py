import customtkinter as ctk
from PIL import Image

# System Defaults
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.FontManager.load_font("assets/fonts/Poppins.ttf")
profile_img = Image.open("assets/images/profile.png")
root = ctk.CTk()
root.geometry("1000x600")
root.title("Complaint Management System")

# Functions
def log_in(account_type):
    print("Function Ran")
    if account_type == 0:
        login_frm.forget()
        user_comp_int_frm.pack()

# Log in Interface
login_frm = ctk.CTkFrame(root, fg_color= "transparent")
login_title_frm = ctk.CTkFrame(login_frm, fg_color= "#00009e", corner_radius= 60)
login_title_lbl = ctk.CTkLabel(login_title_frm, text= "Complaint Management System", font= ("Poppins", 30), bg_color= "#00009e", text_color= "#e7e8e8")
login_title_frm.pack(pady = (50, 0))
login_title_lbl.pack(padx = 20, pady = 40)

# Start of User Form #

user_form_frm = ctk.CTkFrame(login_frm, border_color= "#00009e", corner_radius= 20, border_width= 3)
icon_frm = ctk.CTkFrame(user_form_frm)
user_form_icon = ctk.CTkImage(profile_img, size=(80,80))
user_form_icon_holder = ctk.CTkLabel(user_form_frm, image= user_form_icon, text= "", width= 250)
user_form_lbl = ctk.CTkLabel(user_form_frm, text= "Member Login" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_username_lbl = ctk.CTkLabel(user_form_frm, text= "Username:" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_username_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your username:", corner_radius= 50, width= 250, font= ("Poppins", 12))
user_password_lbl = ctk.CTkLabel(user_form_frm, text= "Password:", font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_password_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your password:", show= "•", corner_radius= 50, width= 250, font= ("Poppins", 12))
user_form_submit_btn = ctk.CTkButton(user_form_frm, text= "Log in", font= ("Poppins", 15), width= 250, corner_radius= 50, command= lambda: log_in(0))

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
user_comp_int_frm = ctk.CTkFrame(root, fg_color= "transparent")
user_comp_title_lbl = ctk.CTkLabel(user_comp_int_frm, text= "Complaint Form", font= ("Poppins", 35))
user_comp_form_frm = ctk.CTkScrollableFrame(user_comp_int_frm, border_color= "#00009e", border_width= 2, width = 800, height = 500)

name_id_frm = ctk.CTkFrame(user_comp_form_frm, fg_color= "transparent")
user_name_frm = ctk.CTkFrame(name_id_frm, fg_color= "transparent")
user_name_lbl = ctk.CTkLabel(user_name_frm, text= "Name: ", font= ("Poppins", 15))
user_name_ent = ctk.CTkEntry(user_name_frm, font= ("Poppins", 15), placeholder_text= "Enter your name", width= 250)
user_id_frm = ctk.CTkFrame(name_id_frm, fg_color= "transparent")
user_id_lbl = ctk.CTkLabel(user_id_frm, text= "ID Number: ", font= ("Poppins", 15))
user_id_ent = ctk.CTkEntry(user_id_frm, font= ("Poppins", 15), placeholder_text= "Enter your ID", width= 250)

gender_frm = ctk.CTkFrame(user_comp_form_frm, fg_color= "transparent")
gender_values = ["Male", "Female", "I prefer not to say..."]
gender_lbl = ctk.CTkLabel(gender_frm, text= "Gender: ", font= ("Poppins", 15))
gender_dropdown = ctk.CTkComboBox(gender_frm, width = 250, values= gender_values, font= ("Poppins", 15))

subject_frm = ctk.CTkFrame(user_comp_form_frm, fg_color= "transparent")
subject_lbl = ctk.CTkLabel(subject_frm, text= "Subject: ", font= ("Poppins", 15))
subject_ent = ctk.CTkEntry(subject_frm, font= ("Poppins", 15), placeholder_text= "Subject of Complaint", width= 500)

com_form_frm = ctk.CTkFrame(user_comp_form_frm, fg_color= "transparent")
com_form_lbl = ctk.CTkLabel(com_form_frm, text= "Complaint: ", font= ("Poppins", 15))
com_form_ent = ctk.CTkTextbox(user_comp_form_frm, font= ("Poppins", 15), width= 700, height = 150)

submit_com_form_btn = ctk.CTkButton(user_comp_form_frm, text= "Submit Now", font= ("Poppins", 15))
user_name_lbl.pack(padx= (50, 3), pady= (10, 0),side= "left")
user_name_ent.pack(padx= (10, 20), pady= (10, 0),side= "left")
user_id_lbl.pack(padx= (50, 3), pady= (10, 0),side= "left")
user_id_ent.pack(padx= (10, 20), pady= (10, 0),side= "left")

gender_lbl.pack(padx= (50, 3), pady= (10, 10), side= "left")
gender_dropdown.pack(pady = (0, 3), side = "left")

subject_lbl.pack(padx= (50, 3), pady= (15, 10), side= "left")
subject_ent.pack(padx= (10, 20), pady= (15, 10), side= "left")

com_form_lbl.pack(padx= (50, 3), pady= 5, side= "left")

user_name_frm.pack(padx = 10, pady = 1, side = "left")
user_id_frm.pack(padx = 10, pady = 1, side = "left")

name_id_frm.pack(pady= 20 , padx = 5)
gender_frm.pack(pady= 10 , padx = 15, fill = "x", expand = True)
subject_frm.pack(pady= 10 , padx = 15, fill = "x", expand = True)
com_form_frm.pack(pady= 3 , padx = 15, fill = "x", expand = True)
com_form_ent.pack(padx= (65, 20), pady= 5)
submit_com_form_btn.pack(pady = 5)
user_comp_title_lbl.pack(pady= 15)
user_comp_form_frm.pack(padx = 20, pady = 5)


# End of User Complaint Interface #
root.mainloop()
