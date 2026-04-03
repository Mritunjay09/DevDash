import customtkinter as ctk

ctk.set_appearance_mode("dark")

def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

class Config(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame = parent

        title = ctk.CTkLabel(
            self,
            text="Switch Theme",
            font=("Consolas", 16, "bold"),
            text_color="#7a8fa6"
        )
        title.pack(anchor="w", padx=20, pady=(20,10))

        self.mode = ctk.CTkFrame(master=self, height=80, bg_color= "#0b0f12")
        self.mode.pack(fill='x')

        self.mode.grid_columnconfigure((0,1), weight=1)

        self.Light = ctk.CTkButton(self.mode, text="Light", text_color="#8a96a3", font=("Arial", 16, "bold"),
                         fg_color="transparent", hover_color="#002b1a", height=40, command=toggle_theme)
        self.Light.grid(row=0, column=0, padx=20,sticky="nsew",)

        # Right section
        self.Dark = ctk.CTkButton(self.mode, text="Dark", text_color="#8a96a3", font=("Arial", 16, "bold"),
                           fg_color="transparent", hover_color="#002b1a", height=40, command=toggle_theme)
        self.Dark.grid(row=0, column=1, padx=20, sticky="nsew")

        label = ctk.CTkLabel(
            self,
            text="Startup Application",
            font=("Consolas", 16, "bold"),
            text_color="#7a8fa6"
        )
        label.pack(anchor="w", padx=20, pady=(20,10))



