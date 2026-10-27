import tkinter as tk
from tkinter import messagebox, ttk, filedialog

def show_custom_box():
    funcs = {
        "error": messagebox.showerror,
        "warning": messagebox.showwarning,
        "question": messagebox.askquestion,
        "info": messagebox.showinfo
    }
    
    t = title_entry.get().strip() or "Title"
    m = msg_entry.get().strip() or "Message"
    icon = icon_var.get().lower()
    
    box_func = funcs.get(icon, messagebox.showinfo)
    box_func(title=t, message=m)

# this is for our image picker for the icon
def pick_icon():
    file_path = filedialog.askopenfilename(
        title="Select image",
        filetypes=[("Image files", "*.png *.gif *.ico")]
    )
    
    if file_path:
        try:
            global custom_icon # so python doesnt kill it
            custom_icon = tk.PhotoImage(file=file_path)
            root.iconphoto(False, custom_icon)
            
            # we'll also update the entry why not
            icon_path_entry.delete(0, tk.END)
            icon_path_entry.insert(0, file_path.split("/")[-1])
        except Exception as e:
            messagebox.showerror("Oops", f"Could not load image:\n{e}")

# tkinter start

root = tk.Tk()
root.title("Textbox gen")
root.geometry("350x290")
root.resizable(False, False)

blank = tk.PhotoImage(width=1, height=1)
root.iconphoto(False, blank)

# setup UI
tk.Label(root, text="Title:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
title_entry = tk.Entry(root, width=30)
title_entry.insert(0, "Title")
title_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Msg:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
msg_entry = tk.Entry(root, width=30)
msg_entry.insert(0, "Message")
msg_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Type:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
icon_var = tk.StringVar(value="Error")
icon_menu = ttk.Combobox(root, textvariable=icon_var, values=["Info", "Warning", "Error", "Question"], state="readonly", width=27)
icon_menu.grid(row=2, column=1, padx=10, pady=5)

# icon
tk.Label(root, text="Icon Img:").grid(row=3, column=0, padx=10, pady=5, sticky="w")

frame = tk.Frame(root)
frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")

icon_path_entry = tk.Entry(frame, width=19)
icon_path_entry.insert(0, "No image chosen")
icon_path_entry.pack(side=tk.LEFT, padx=(0, 5))

browse_btn = tk.Button(frame, text="Browse", command=pick_icon, width=6)
browse_btn.pack(side=tk.LEFT)

btn = tk.Button(root, text="Trigger", command=show_custom_box, bg="#a10b18", fg="white", width=28)
btn.grid(row=4, column=0, columnspan=2, pady=15)

#end

root.mainloop()
