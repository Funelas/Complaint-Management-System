import customtkinter as ctk
from PIL import Image

# System Defaults
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")
ctk.FontManager.load_font("Poppins.ttf")
profile_img = Image.open("profile.png")
root = ctk.CTk()
root.geometry("1000x600")
root.title("Complaint Management System")

# Log in Interface
login_title_frm = ctk.CTkFrame(root, fg_color= "#00009e", corner_radius= 60)
login_title_lbl = ctk.CTkLabel(login_title_frm, text= "Complaint Management System", font= ("Poppins", 30), bg_color= "#00009e", text_color= "#e7e8e8")
login_title_frm.pack(pady = (50, 0))
login_title_lbl.pack(padx = 20, pady = 40)

# User Form
user_form_frm = ctk.CTkFrame(root, border_color= "#00009e", corner_radius= 20, border_width= 3)
icon_frm = ctk.CTkFrame(user_form_frm)
user_form_icon = ctk.CTkImage(profile_img, size=(80,80))
user_form_icon_holder = ctk.CTkLabel(user_form_frm, image= user_form_icon, text= "", width= 250)
user_form_lbl = ctk.CTkLabel(user_form_frm, text= "Member Login" , font= ("Poppins", 18), text_color= "#00009e", anchor= "w", width= 250)
user_username_lbl = ctk.CTkLabel(user_form_frm, text= "Username:" , font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_username_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your username:", corner_radius= 50, width= 250, font= ("Poppins", 12))
user_password_lbl = ctk.CTkLabel(user_form_frm, text= "Password:", font= ("Poppins", 15), text_color= "#00009e", anchor= "w", width= 250)
user_password_ent = ctk.CTkEntry(user_form_frm, placeholder_text="Enter your password:", show= "•", corner_radius= 50, width= 250, font= ("Poppins", 12))
user_form_submit_btn = ctk.CTkButton(user_form_frm, text= "Log in", font= ("Poppins", 15), width= 250, corner_radius= 50)

user_form_icon_holder.pack(pady= (5,0), padx= 20)
user_form_lbl.configure(anchor="center", justify="center")
user_form_lbl.pack(pady= (5, 0), padx= 20, fill= "x")
user_username_lbl.pack(pady = (20, 0), padx = 20)
user_username_ent.pack(pady = (10, 0), padx = 20)
user_password_lbl.pack(pady = (20, 0), padx = 20)
user_password_ent.pack(pady = (10, 10), padx = 20)
user_form_submit_btn.pack(pady = (10, 10), padx = 20)
user_form_frm.pack(pady= (50, 0))
root.mainloop()
