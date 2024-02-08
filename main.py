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

        # background_image = tkinter.PhotoImage(file=")
        # background_label = tk.Label(self.main_frame, image=background_image)
        # background_label.place(relwidth=1, relheight=1)

        self.main_frame = customtkinter.CTkFrame(self, width=1100, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(self.main_frame, width=500)
        self.textbox.grid(row=2, column=0, padx=(320, 320), pady=(100, 0), sticky="nsew")
        # Insert a speaker symbol (Unicode character) at the top right of the textbox
        speaker_symbol = "\U0001F3A4"  # Unicode character for speaker symbol
        self.textbox.insert("1.end", speaker_symbol)  # "1.end" refers to the end of line 1
        

        self.label_1 = customtkinter.CTkLabel(self.main_frame, text="Your video will be generated shortly.")
        self.label_1.grid(row=3, column=0, padx=20, pady=(10, 0))

        self.label_2 = customtkinter.CTkLabel(self.main_frame, text="Create captivating short videos in seconds! Express your story with just a few words.")
        self.label_2.grid(row=1, column=0, padx=20, pady=(30, 0))

        self.label_text = "Craft Your Reel Story"
        label_font = ("Helvetica", 40)
        self.label = customtkinter.CTkLabel(self.main_frame, text=self.label_text, anchor="center", font=label_font)
        self.label.grid(row=0, column=0, padx=(0,0), pady=(20, 0), sticky="nsew", columnspan=5)
      
        self.main_frame.grid_columnconfigure(0, weight=1)

     
       

        # create radiobutton frame
     
        

      

       


       
        self.textbox.insert("0.0", "Enter the prompt!                                                                                                              ")
       

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()