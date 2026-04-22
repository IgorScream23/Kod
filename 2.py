import tkinter as tk

window = tk.Tk()
window.title('Список оборудования')
window.geometry('300x370')
window.configure(bg="#A39999")

frame = tk.Frame(bg="#D7ECDB")
frame.pack(padx=40, pady=20, fill='both', expand=True)

def add_item():
    if entry.get().strip():
        lb.insert(tk.END, entry.get())
        entry.delete(0, tk.END)

def delete_item():
    selected = lb.curselection()
    if selected:
        for i in reversed(selected):
            lb.delete(i)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.X)

lb = tk.Listbox(frame, width=30, height=10, bg = "#EBC2C2", fg='#000000', font=('Arial', 11), bd=3, relief="sunken", selectmode=tk.MULTIPLE,xscrollcommand=scrollbar.set)
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lb.xview)

entry = tk.Entry(window, font=('Arial', 10), width=25)
entry.pack(pady=5)

button_1 = tk.Button(window, text='Добавить товар', font=('Arial', 10, 'bold'), bg="#10BE3C", fg='#000000', cursor='hand2', command=add_item)
button_1.pack(pady=5)

button_2 = tk.Button(window, text='Удалить товар', font=('Arial', 10, 'bold'), bg="#D72727", fg='#000000', cursor='hand2', command=delete_item)
button_2.pack(pady=5)

for i in range(1,10):
    lb.insert(tk.END, i)

window.mainloop()
