from customtkinter import *


class Navbar(CTkFrame):
    def __init__(self, app: CTkScrollableFrame, switch_page):
        super().__init__(app, fg_color = 'white')

        self.app = app
        self.switch_page = switch_page
        self.navbar = CTkFrame(master=self, height=80, bg_color="#0b0f12")

        self.navbar.grid_columnconfigure((0,1,2), weight=1)

        self.dash = CTkButton(self.navbar, text="DASH", text_color="#8a96a3", font=("Arial", 16, "bold"),
                         fg_color="transparent", height=40, command=lambda: self.switch_page('dash'))
        self.dash.grid(row=0, column=0, padx=20,sticky="nsew",)

        add_button = CTkButton(
            self.navbar,
            text="+",
            width=40,
            height=40,
            fg_color="transparent",
            border_width=2,
            border_color="#00ff66",
            text_color="#00ff66",
            hover_color="#002b1a",
            font=("Arial", 20, "bold"),
            command=lambda: self.switch_page('env')
        )
        add_button.grid(row=0, column=1)

        # Right section
        self.config = CTkButton(self.navbar, text="CONFIG", text_color="#8a96a3", font=("Arial", 16, "bold"),
                           fg_color="transparent", height=40, command=lambda: self.switch_page('config'))
        self.config.grid(row=0, column=2, padx=20, sticky="nsew")

        self.navbar.pack(side="bottom", fill="x")