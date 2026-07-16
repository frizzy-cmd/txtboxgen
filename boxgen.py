import tkinter as tk
from tkinter import messagebox, ttk

def show_custom_box():
    funcs = {
        "error": messagebox.showerror,
        "warning": messagebox.showwarning,
        "question": messagebox.askquestion,
        "info": messagebox.showinfo
    }
    
    t = title_entry.get().strip() or "Title"
    m = msg_entry.get().strip() or "Message"
    icon = icon_var.get()
    
    # an fallback
    funcs.get(icon, messagebox.showinfo)(title=t, message=m)

root = tk.Tk()
root.title("Textbox gen")
root.geometry("350x250")
root.resizable(False, False)

blank = tk.PhotoImage(width=1, height=1)
root.iconphoto(False, blank)

tk.Label(root, text="Title:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
title_entry = tk.Entry(root, width=30)
title_entry.insert(0, "Title")
title_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Msg:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
msg_entry = tk.Entry(root, width=30)
msg_entry.insert(0, "Message")
msg_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Icon:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
icon_var = tk.StringVar(value="Error")
icon_menu = ttk.Combobox(root, textvariable=icon_var, values=["Info", "Warning", "Error", "Question"], state="readonly", width=27)
icon_menu.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Trigger", command=show_custom_box, bg="#a10b18", fg="white").grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()