# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def exit_app():
    root.quit()
    root.destroy()


def new_file():
    text_area.delete("1.0", tk.END)


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", "ფაილი შენახულია UTF-8 ფორმატში")


def cut_text(event=None):
    text_area.event_generate("<<Cut>>")


def copy_text(event=None):
    text_area.event_generate("<<Copy>>")


def paste_text(event=None):
    text_area.event_generate("<<Paste>>")


def undo_text(event=None):
    text_area.event_generate("<<Undo>>")


def redo_text(event=None):
    text_area.event_generate("<<Redo>>")


def select_all(event=None):
    text_area.tag_add("sel", "1.0", "end")
    return "break"


# ===== MAIN WINDOW =====

root = tk.Tk()
root.title("Mini UTF-8 Text Editor")
root.geometry("700x450")

# ===== MENU =====

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=undo_text)
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=redo_text)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=cut_text)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=copy_text)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)

# ===== TEXT AREA =====

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_area = tk.Text(
    frame,
    wrap=tk.WORD,
    undo=True,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set
)

text_area.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text_area.yview)

# ===== SHORTCUTS =====

root.bind("<Control-x>", cut_text)
root.bind("<Control-c>", copy_text)
root.bind("<Control-v>", paste_text)
root.bind("<Control-z>", undo_text)
root.bind("<Control-y>", redo_text)
root.bind("<Control-a>", select_all)

# ===== START =====

root.mainloop()
