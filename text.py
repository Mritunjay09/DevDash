import customtkinter

# Callback function
def optionmenu_callback(choice):
    print("Option menu selected:", choice)

app = customtkinter.CTk()
app.geometry("400x200")

# Create option menu with values and a callback
optionmenu = customtkinter.CTkOptionMenu(
    master=app,
    values=["Option 1", "Option 2", "Option 3"],
    command=optionmenu_callback
)
optionmenu.pack(pady=20)
optionmenu.set("Option 2") # Set default

app.mainloop()
