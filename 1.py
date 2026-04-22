import tkinter as tk
#
window = tk.Tk()
window.title('Список оборудования')
window.geometry('300x400')
window.configure(bg="#7D807F")

frame = tk.Frame(window, bg="#B9C8D8")
frame.pack(padx=40, pady=20, fill='both', expand=True)

def add_item():
    if entry.get().strip():
        lb.insert(tk.END, entry.get())
        entry.delete(0, tk.END)

def delete_item():
    selected = lb.curselection()
    if selected:
        lb.delete(selected[0])

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lb = tk.Listbox(frame, height=10, width=40, bg="#C5DBEE", fg='#000000', bd=3, relief='sunken', selectbackground="#c1d61f", selectforeground="#C0B0B0", selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lb.yview)

entry = tk.Entry(window, font=('Arial', 10), width=25)
entry.pack(pady=5)

button_1 = tk.Button(window, text='Добавить товар', bg="#38E815", fg='#000000', font=('Arial', 11, 'bold'), cursor='wait', command=add_item)
button_1.pack(pady=5)

button_2 = tk.Button(window, text='🗑 Удалить товар', bg="#E81616", fg='#000000', font=('Arial', 11, 'bold'), command=delete_item)
button_2.pack(pady=5)

for i in range(1,11):
    lb.insert(tk.END, i)

window.mainloop()
