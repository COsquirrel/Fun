import tkinter
import customtkinter
from tkinter import messagebox
import os


root = customtkinter.CTk()
root._set_appearance_mode("dark")
#root.set_default_color_theme("green")
root.title("Hello World GUI")

def build_It():
    ent1=ent1_var.get()
    ent2=ent2_var.get() 
         
    ent1_var.set("")
    ent2_var.set("")
    
    file = open(ent1 + ".py", "w+")
    file.write("print('" + ent2 + "')")
    file.close()

ent1_var=customtkinter.StringVar()
ent2_var=customtkinter.StringVar()

label1 = customtkinter.CTkLabel(root, text="Over Engineered Hello World for python.", font=('Ariel', 18))
label1.grid(row=0, column=1)

lb1 = customtkinter.CTkLabel(root, text="What to name the file?", font=('Ariel', 16))
lb1.grid(row=1, column=0)

ent1 = customtkinter.CTkEntry(root, textvariable = ent1_var)
ent1.grid(row=1, column=1)

lb2 = customtkinter.CTkLabel(root, text="What is in file?", font=('Ariel', 16))
lb2.grid(row=2, column=0)

ent2 = customtkinter.CTkEntry(root, textvariable = ent2_var)
ent2.grid(row=2, column=1)

button1 = customtkinter.CTkButton(root, text="Build!", font=('Arial', 18), command=build_It)
button1.grid(row=4, column=1, padx=10, pady=10)
button2 = customtkinter.CTkButton(root, text="Exit", font=('Arial', 18), command=root.destroy)
button2.grid(row=4, column=2, padx=10, pady=10)



root.mainloop()
