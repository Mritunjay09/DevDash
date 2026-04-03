import customtkinter as ctk
import threading
import json
from env import Env

import psutil
from pynvml import *

nvmlInit()

ctk.set_appearance_mode("dark")

cpu_load, ram_use, gpu_load = 0, 0, 0
old = psutil.net_io_counters()


ctk.set_appearance_mode("dark")

def setactive():
    pass

def add_workspace():
    root = ctk.CTk()
    root.geometry("600x500")
    Env(root).pack(fill="both", expand=True)
    root.mainloop()


class EnvironmentRow(ctk.CTkFrame):
    def __init__(self, parent, name, desc, status="standby"):
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
        top.pack(anchor="w")

        title = ctk.CTkLabel(
            top,
            text=name,
            font=("Consolas", 15, "bold")
        )
        title.pack(side="left")

        badge_color = "#00ff66" if active else "#334155"

        badge = ctk.CTkLabel(
            top,
            text=status.upper(),
            fg_color=badge_color,
            corner_radius=4,
            padx=6,
            text_color="black" if active else "#9aa5b1",
            font=("Consolas", 11)
        )
        badge.pack(side="left", padx=10)

        # Description
        desc_label = ctk.CTkLabel(
            text_frame,
            text=desc,
            text_color="#6f8195",
            font=("Consolas", 12)
        )
        desc_label.pack(anchor="w")

        # Arrow button
        arrow = ctk.CTkButton(
            self,
            text=">",
            width=40,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#1f2933",
            hover_color="#1b2228",
            command=lambda: setactive()
        )
        arrow.pack(side="right", padx=10, pady=10)

class Environment(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#0b0f12")

        title = ctk.CTkLabel(
            self,
            text="ENVIRONMENTS",
            font=("Consolas", 16, "bold"),
            text_color="#7a8fa6"
        )
        title.pack(anchor="w", padx=20, pady=(20,10))

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="x", padx=20)

        try:
            with open("env.json", "r") as f:
                data = json.load(f)
                if "workspace" in data:
                    for i in range(len(data['workspace'])):
                        EnvironmentRow(container,data['workspace'][i]['title'],data['workspace'][i]['apps'])
                else:
                    notfound = ctk.CTkLabel(
                    container,
                    text="CREATE ENV",
                    font=("Consolas", 20, "bold"),
                    text_color="#7a8fa6"
                    )
                    notfound.pack()
        except FileNotFoundError:
            notfound = ctk.CTkLabel(
            container,
            text="CREATE ENV",
            font=("Consolas", 20, "bold"),
            text_color="#7a8fa6"
            )
            notfound.pack()

class update_telemetry():
    def __init__(self, cpu, ram, gpu, net):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.net = net
        self.update()

    def update(self):
        global cpu_load, ram_use, gpu_load, old
        cpu_load = psutil.cpu_percent(interval=1)
        ram_use = psutil.virtual_memory().percent
        handle = nvmlDeviceGetHandleByIndex(0)
        util = nvmlDeviceGetUtilizationRates(handle)
        gpu_load = util.memory

        new = psutil.net_io_counters()

        self.cpu.value.configure(text=f"{cpu_load}%")
        self.cpu.progress.set(cpu_load / 100)

        self.ram.value.configure(text=f"{ram_use}%")
        self.ram.progress.set(ram_use / 100)

        self.gpu.value.configure(text=f"{gpu_load}%")
        self.gpu.progress.set(gpu_load / 100)

        self.net.value.configure(text=f"{(new.bytes_sent + new.bytes_recv - old.bytes_sent - old.bytes_recv) / 1048576:.1f} MB/s")
        old = new
        threading.Timer(0.2, self.update).start()

class TelemetryCard(ctk.CTkFrame):
    def __init__(self, parent, title, value, unit="", color="#00ff66"):
        super().__init__(parent, width=180, height=120, corner_radius=8, fg_color="#11161c")

        self.grid_propagate(False)

        # Title
        self.title = ctk.CTkLabel(
            self,
            text=title,
            text_color="#7a8fa6",
            font=("Consolas", 12)
        )
        self.title.grid(row=0, column=0, sticky="w", padx=12, pady=(10,0))

        # Value
        self.value = ctk.CTkLabel(
            self,
            text=f"{value}{unit}",
            font=("Consolas", 28, "bold")
        )
        self.value.grid(row=1, column=0, columnspan=2, sticky="w", padx=12)

        # Progress bar
        self.progress = ctk.CTkProgressBar(
            self,
            height=6,
            width= 150,
            progress_color=color
        )
        self.progress.set(0.4)
        self.progress.grid(row=2, column=0, columnspan=2, sticky="ew", padx=12, pady=12)


class System_info(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#0b0f12")

        header = ctk.CTkLabel(
            self,
            text="SYSTEM TELEMETRY",
            font=("Consolas", 16, "bold"),
            text_color="#6f8195"
        )
        header.pack(anchor="w", padx=20, pady=(20,10))

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.pack(anchor="w", padx=20, pady=20)

        cards.grid_columnconfigure((0,1,2,3), weight=1)

        cpu = TelemetryCard(cards, "CPU LOAD", "23", "%", "#00ff66")
        cpu.grid(row=0, column=0, padx=10)

        ram = TelemetryCard(cards, "RAM USE", "8.2", " GB", "#aab7c4")
        ram.grid(row=0, column=1, padx=8)

        gpu = TelemetryCard(cards, "GPU UTIL", "15", "%", "#ff4d4d")
        gpu.grid(row=0, column=2, padx=8)

        net = TelemetryCard(cards, "NET TRAFFIC", "420", " Kb", "#00ff66")
        net.grid(row=0, column=3, padx=8)
        update_telemetry(cpu, ram, gpu, net)

class journal(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, height=600, width=400, fg_color="#0b0f12")

        self.title = ctk.CTkLabel(
            self,
            text="SYSTEM JOURNAL",
            text_color="#7a8fa6",
            font=("Consolas", 16, "bold")
        )
        self.title.pack(anchor="w", padx=20, pady=(20,10))

        self.log_box = ctk.CTkTextbox(
            self,
            height=120,
            fg_color="#11161c",
            border_width=1
        )
        self.log_box.pack(fill="both", expand=True, padx=10, pady=10)

        # Tag colors
        self.log_box.tag_config("ok", foreground="#00ff66")
        self.log_box.tag_config("info", foreground="#4da6ff")
        self.log_box.tag_config("warn", foreground="#ffaa00")
        self.log_box.tag_config("time", foreground="#6f8195")

        self.log_box.configure(state="disabled")

    def add_log(self, time, level, message):

        self.log_box.configure(state="normal")

        self.log_box.insert("end", f"{time} ", "time")

        if level == "OK":
            self.log_box.insert("end", "[OK] ", "ok")

        elif level == "INF":
            self.log_box.insert("end", "[INF] ", "info")

        elif level == "WRN":
            self.log_box.insert("end", "[WRN] ", "warn")

        self.log_box.insert("end", message + "\n")

        self.log_box.see("end")
        self.log_box.configure(state="disabled")

class Dash(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, height=1200, width=600, fg_color="#11161c")


        self.system_info = System_info(self)
        self.system_info.pack(fill="both", expand=True)


        self.add_button = ctk.CTkButton(
            self,
            text="+ Add New Workspace",
            width=1400,
            height=50,
            fg_color="transparent",
            border_width=1,
            border_color="#00ff66",
            text_color="#363d42",
            bg_color="#00ff66",
            hover_color="#070808",
            font=("Arial", 20, "bold"),
            command=lambda: add_workspace()
        )

        self.add_button.pack(fill="y", expand=True)

        self.env = Environment(self)
        self.env.pack(fill="both", expand=True)

        self.journal = journal(self)
        self.journal.pack(fill="both", expand=True,)

        self.journal.add_log("14:20:01", "OK", "Started Workspace 'Coding'...")
        self.journal.add_log("14:18:45", "INF", "GPU temp stabilized at 54°C.")
        self.journal.add_log("14:15:22", "WRN", "Container 'redis-prod' > 2GB.")