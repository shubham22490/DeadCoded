import tkinter as tk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CREATE with your DATE")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (1x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.main_frame = customtkinter.CTkFrame(self, width=1100, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")




        self.label_text = "Craft Your Reel Story"
        label_font = ("Helvetica", 40)
        self.label = customtkinter.CTkLabel(self.main_frame, text=self.label_text, anchor="center", font=label_font)
        self.label.grid(row=0, column=0, padx=(0,0), pady=(20, 0), sticky="nsew", columnspan=5)

        self.label_2 = customtkinter.CTkLabel(self.main_frame, text="Create captivating short videos in seconds! Express your story with just a few words.")
        self.label_2.grid(row=1, column=0, padx=20, pady=(30, 0))

        self.textbox = customtkinter.CTkTextbox(self.main_frame, width=500)
        self.textbox.grid(row=2, column=0, padx=(320, 320), pady=(100, 0), sticky="nsew")
        self.textbox.insert("0.0", "Enter the prompt!")

        self.text_variable = tk.StringVar() #text 

        self.generate_button_hindi = customtkinter.CTkButton(self.main_frame, command=self.generate_button_event)
        self.generate_button_hindi.place(x=400, y=480)
        self.generate_button_hindi.configure(text="in Hindi")

        self.generate_button_eng = customtkinter.CTkButton(self.main_frame, command=self.generate_button_event)
        self.generate_button_eng.place(x=550, y=480)
        self.generate_button_eng.configure(text="in English")

        self.label_2 = customtkinter.CTkLabel(self.main_frame, text="Generate", font=("Helvetica",25))
        self.label_2.grid(row=4, column=0, padx=20, pady=(10, 0))

        self.label_1 = customtkinter.CTkLabel(self.main_frame, text="Your video will be generated shortly.")
        self.label_1.place(x=450, y=520)

        self.main_frame.grid_columnconfigure(0, weight=1)
     
        
        self.mic = customtkinter.CTkButton(self.main_frame, command=self.button_click,  width=10, corner_radius=10)
        self.mic.configure(text="\U0001F3A4", font=("Arial",20))
        self.mic.place(x=735, y=225)  

    def button_click(self):
        print("Button clicked!")
       

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def generate_button_event(self):
        
        #the text entered in the textbox
        self.text_variable.set(self.textbox.get("1.0", "end-1c"))
        
        customtkinter.set_appearance_mode("System")

        popup_width = 300
        popup_height = 200

        self.update_idletasks()  # Ensure window is updated to get correct dimensions
        self_width = self.winfo_width()
        self_height = self.winfo_height()

        x = self.winfo_x() + (self_width - popup_width) // 2
        y = self.winfo_y() + (self_height - popup_height) // 2

        popup = tk.Toplevel(self, background="grey")
        popup.title("Video Generated")
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        label = tk.Label(popup, text="Your video has been generated successfully.", fg="black", bg="grey")
        label.pack(pady=10)

        download = tk.Button(popup, text="Download", fg="black", command=lambda: self.popup_action("Download"))
        download.pack(pady=0)

        youtube = tk.Button(popup, text="Upload on YouTube", fg="black", command=lambda: self.popup_action("Youtube"))
        youtube.pack(side="left", padx=22, pady=10)

        google = tk.Button(popup, text="Sign-in on Google", fg="black", command=lambda: self.popup_action("Google"))
        google.pack(side="left", padx=10, pady=10)



    def popup_action(str):
        print("")
    

if __name__ == "__main__":
    app = App()
    app.mainloop()