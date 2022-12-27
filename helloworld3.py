import tkinter as tk
from tkinter import messagebox
import os


root = tk.Tk()

root.title("Hello World GUI")

def build_It():
    ent1=ent1_var.get()
    ent2=ent2_var.get() 
         
    ent1_var.set("")
    ent2_var.set("")
    
    file = open(ent1 + ".py", "w+")
    file.write("print('" + ent2 + "')")
    file.close()

ent1_var=tk.StringVar()
ent2_var=tk.StringVar()

label = tk.Label(root, text="Over Engineered Hello World for python.", font=('Ariel', 18))
label.grid(row=0, column=1)

lb1 = tk.Label(root, text="What to name the file?", font=('Ariel', 16))
lb1.grid(row=1, column=0)

ent1 = tk.Entry(root, textvariable = ent1_var, borderwidth=5, width=30)
ent1.grid(row=1, column=1)

lb2 = tk.Label(root, text="What is in file?", font=('Ariel', 16))
lb2.grid(row=2, column=0)

ent2 = tk.Entry(root, textvariable = ent2_var, borderwidth=5, width=30,)
ent2.grid(row=2, column=1)

button1 = tk.Button(root, text="Build!", font=('Arial', 18), command=build_It)
button1.grid(row=4, column=1, padx=10, pady=10)
button2 = tk.Button(root, text="Exit", font=('Arial', 18), command=root.destroy)
button2.grid(row=4, column=2, padx=10, pady=10)



root.mainloop()
