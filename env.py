import customtkinter as ctk

ctk.set_appearance_mode("dark")

def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def setactive():
    pass

class EnvironmentRow(ctk.CTkFrame):
    def __init__(self, parent, name,status="standby"):
        super().__init__(parent, height=70, corner_radius=6, fg_color="#11161c")

        self.pack(fill="x", pady=6, padx=10)
        self.grid_columnconfigure(0, weight=1)

        active = status.lower() == "active"

        # Left status indicator
        if active:
            bar = ctk.CTkFrame(self, width=4, height=10, fg_color="#00ff66")
            bar.pack(side="left", fill="both", padx=(0,10))

        # Text container
        text_frame = ctk.CTkFrame(self, fg_color="transparent")
        text_frame.pack(side="left", fill="both", expand=True)

        # Top row (name + badge)
        top = ctk.CTkFrame(text_frame, fg_color="transparent")
        top.pack(pady=12, padx=10, anchor="w")

        title = ctk.CTkLabel(
            top,
            text=name,
            font=("Consolas", 15, "bold")
        )
        title.pack(side="left")

        badge_color = "#00ff66" if active else "#334155"

        badge = ctk.CTkLabel(
            self,
            text=status.upper(),
            fg_color=badge_color,
            corner_radius=4,
            padx=6,
            text_color="black" if active else "#9aa5b1",
            font=("Arial", 14, "bold")
        )
        badge.pack(side="left", padx=20)

        # Arrow button
        arrow = ctk.CTkButton(
            self,
            text="+",
            width=40,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#1f2933",
            hover_color="#1b2228",
            command=lambda: setactive()
        )
        arrow.pack(side="right", padx=10, pady=10)



class Env(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        title_label = ctk.CTkLabel(
            self,
            text="CREATE WORKSPACE",
            font=("Consolas", 16, "bold"),
            text_color="#7a8fa6"
        )
        title_label.pack(anchor="w", padx=20, pady=(20, 10))

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(fill="x", padx=20)

        # ONE row container
        top = ctk.CTkFrame(frame, fg_color="transparent")
        top.pack(fill="x")

        # Entry
        title = ctk.CTkEntry(
            top,
            placeholder_text="Title",
            font=("Consolas", 16, "bold"),
            width= 150,
            height= 40
        )
        title.pack(side="left", padx=(0, 10))

        app_label = ctk.CTkLabel(
            frame,
            text="SELECT AN APPLICATION",
            font=("Consolas", 16, "bold"),
            text_color="#7a8fa6"
        )
        app_label.pack(anchor="w", pady=(20, 10))

        Apps = ctk.CTkScrollableFrame(
            frame,
            height=300,
            fg_color="#0b0f12",
        )

        values=['Vs Code', 'Terminal', 'Postman', 'Docker', 'Obs', 'Discord', 'Neovim']
        for i in values:
            EnvironmentRow(Apps, i, "Testing")
        Apps.pack(fill="both", expand=True, pady=10)
