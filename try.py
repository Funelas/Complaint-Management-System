import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("400x300")

        self.modal = None
        self.offset_x = 0
        self.offset_y = 0

        open_modal_button = ctk.CTkButton(self, text="Open Modal", command=self.open_modal)
        open_modal_button.pack(pady=40)

        # Bind motion of parent window
        self.bind('<Configure>', self.move_modal_with_parent)

    def open_modal(self):
        if self.modal is not None and self.modal.winfo_exists():
            return  # Already open

        self.modal = ctk.CTkToplevel(self)
        self.modal.geometry("250x150")
        self.modal.title("Attached Modal")
        self.modal.overrideredirect(True)  # Optional: remove title bar
        self.modal.grab_set()

        label = ctk.CTkLabel(self.modal, text="I'm attached!")
        label.pack(pady=30)

        self.center_modal_relative()

    def center_modal_relative(self):
        # Position modal centered relative to parent
        self.update_idletasks()

        parent_x = self.winfo_rootx()
        parent_y = self.winfo_rooty()
        parent_w = self.winfo_width()
        parent_h = self.winfo_height()

        modal_w = self.modal.winfo_width()
        modal_h = self.modal.winfo_height()

        x = parent_x + (parent_w - modal_w) // 2
        y = parent_y + (parent_h - modal_h) // 2

        self.modal.geometry(f"+{x}+{y}")

        # Store offset
        self.offset_x = x - parent_x
        self.offset_y = y - parent_y

    def move_modal_with_parent(self, event):
        if self.modal and self.modal.winfo_exists():
            # Move modal relative to parent
            new_x = self.winfo_rootx() + self.offset_x
            new_y = self.winfo_rooty() + self.offset_y
            self.modal.geometry(f"+{new_x}+{new_y}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
