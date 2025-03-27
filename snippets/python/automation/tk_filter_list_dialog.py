import sys
import tkinter as tk

apps = sys.stdin.read().strip().split()

root = tk.Tk()
entry = tk.Entry(root, width=50)
entry.pack()
entry.focus_set()
listbox = tk.Listbox(root, width=50)
listbox.pack()

def select(event):
    print(listbox.get(tk.ACTIVE))
    root.destroy()
    root.quit()

def update_listbox(event):
    search_term = entry.get().lower()
    listbox.delete(0, tk.END)
    for app in apps:
        if search_term in app.lower():
            listbox.insert(tk.END, app)

entry.bind("<KeyRelease>", update_listbox)
root.bind("<Return>", select)
root.bind("<Escape>", select)
update_listbox(None)

root.mainloop()
