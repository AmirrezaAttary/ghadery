import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess, os, json

CONFIG_FILE = "config.json"

def load_config():
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            project_entry.insert(0, data.get("project", ""))
            venv_entry.insert(0, data.get("venv", ""))

def save_config():
    data = {"project": project_entry.get(), "venv": venv_entry.get()}
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)
    messagebox.showinfo("ذخیره شد", "مسیرها ذخیره شدند ✅")

def browse_project():
    folder = filedialog.askdirectory()
    if folder:
        project_entry.delete(0, tk.END)
        project_entry.insert(0, folder)

def browse_venv():
    folder = filedialog.askdirectory()
    if folder:
        venv_entry.delete(0, tk.END)
        venv_entry.insert(0, folder)

def run_django():
    project_path = project_entry.get()
    venv_path = venv_entry.get()
    python_path = os.path.join(venv_path, "Scripts", "python.exe")
    manage_py = os.path.join(project_path, "manage.py")

    if not os.path.isfile(python_path) or not os.path.isfile(manage_py):
        messagebox.showerror("خطا", "مسیر python یا manage.py اشتباهه ❌")
        return

    cmd = f'start cmd /k "{python_path} {manage_py} runserver"'
    subprocess.Popen(cmd, shell=True)
    messagebox.showinfo("✅ موفق", "Django runserver اجرا شد")

root = tk.Tk()
root.title("Django Auto Run")

tk.Label(root, text="📁 مسیر پروژه Django:").pack()
project_entry = tk.Entry(root, width=50)
project_entry.pack()
tk.Button(root, text="انتخاب", command=browse_project).pack()

tk.Label(root, text="🧪 مسیر venv:").pack()
venv_entry = tk.Entry(root, width=50)
venv_entry.pack()
tk.Button(root, text="انتخاب", command=browse_venv).pack()

tk.Button(root, text="🚀 Run Django Server", bg="green", fg="white", command=run_django).pack(pady=10)
tk.Button(root, text="💾 ذخیره مسیرها", command=save_config).pack(pady=5)

load_config()
root.mainloop()
