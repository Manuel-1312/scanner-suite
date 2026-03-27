import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

PROFILE_DIR = Path(__file__).resolve().parents[1] / "profiles"

class ScannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scanner Suite - Zenmap+")
        self.geometry("640x360")
        self.profile_var = tk.StringVar(value="quick.json")
        self.engines_var = tk.StringVar(value="nmap,masscan")
        self._build()

    def _build(self):
        frm = ttk.Frame(self, padding=20)
        frm.pack(expand=True, fill="both")
        ttk.Label(frm, text="Perfil").grid(column=0, row=0, sticky="w")
        ttk.Combobox(frm, textvariable=self.profile_var, values=[p.name for p in PROFILE_DIR.glob("*.json")]).grid(column=1, row=0)
        ttk.Label(frm, text="Motores").grid(column=0, row=1, sticky="w")
        ttk.Entry(frm, textvariable=self.engines_var).grid(column=1, row=1)
        ttk.Button(frm, text="Escanear", command=self._on_scan).grid(column=0, row=2, columnspan=2, pady=10)

    def _on_scan(self):
        profile = PROFILE_DIR / self.profile_var.get()
        if not profile.exists():
            messagebox.showerror("Perfil","Perfil no encontrado")
            return
        data = json.loads(profile.read_text())
        messagebox.showinfo("Perfil","Listo para ejecutar: %s" % data.get("target"))

if __name__ == "__main__":
    ScannerApp().mainloop()
