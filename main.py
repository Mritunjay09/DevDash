from customtkinter import *
from navbar import Navbar
from dash import Dash
from config import Config
from env import Env

class App(CTkScrollableFrame):
    def __init__(self, root: CTk):
        super().__init__(master=root, border_width=0, corner_radius=0)
        self.root = root

        self.container = CTkFrame(self.root)
        self.container.pack(fill="both", expand=True)

        self.pages = {
            "dash": Dash(self.container),
            "config": Config(self.container),
            "env": Env(self.container)
        }

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.switch_page("dash")

        self.base_app = Navbar(self.root, self.switch_page)
        self.base_app.pack(side='bottom', fill='x')

    def switch_page(self, page_name):
        self.pages[page_name].tkraise()

root = CTk()
set_appearance_mode("Dark")
root.geometry('1400x860')
app = App(root = root)


app.mainloop()