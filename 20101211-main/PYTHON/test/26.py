#메모장
import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename()
    if path:
        text.delete(1.0, tk.END)
        text.insert(1.0, open(path, 'r', encoding='utf-8').read())

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        open(path, 'w', encoding='utf-8').write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("메모장")
root.geometry("500x400")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
menu.add_cascade(label="파일", menu=file_menu)

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()