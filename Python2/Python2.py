import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import math

root = tk.Tk()

error_shown = False

def show():
    error_shown=False
    try:
        selected_option = combobox.get().strip() 
        a = float(entry3.get())
        b = float(entry1.get())
        c = float(entry4.get())
        d = float(entry3.get())
        x_values = np.linspace(-10, 10, 100)  # Добавляем инициализацию x_values
        if(selected_option=='Прямая'):
            y_values = pow((a * pow(x_values,c))/b, 1/d)
        elif(selected_option=='sin(x)'):
            y_values=np.sin(pow(a*x_values,c))/b**(1/d)
        elif(selected_option=='cos(x)'):
            y_values=np.cos(pow(a*x_values,c))/b**(1/d)
        plt.xticks(np.arange(-10, 11, 1))  # Деления на оси X с шагом 1
        plt.yticks(np.arange(-10, 11, 1))  # Деления на оси Y с шагом 1
        plt.plot(x_values, y_values, '-r')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
    except ValueError:
        if not error_shown:
            button.config(state="disabled")  
            messagebox.showerror("Ошибка", "Некорректный ввод данных.\nПожалуйста, введите числа.")
            error_shown = True
            button.config(state="normal") 
            
def update_button(event):  # Функция для обновления кнопки при изменении выбора
    selected_option = combobox.get().strip()
    if selected_option == 'Прямая':
        button.config(text="Построить прямую")
        
        label1.config(text="*Y")
        label1.grid(row=0,column=1)

        entry1.config(width=5, font=("Courier New", 12))
        entry1.grid(row=0,column=0)

        label2.config(text="^")
        label2.grid(row=0,column=2)

        entry2.config(width=5, font=("Courier New", 12))
        entry2.grid(row=0,column=3)

        labequal.config(text="=")
        labequal.grid(row=0,column=4)

        label3.config(text="*X")
        label3.grid(row=0,column=6)

        entry3.config(width=5, font=("Courier New", 12))
        entry3.grid(row=0,column=5)

        label4.config(text="^")
        label4.grid(row=0,column=7)

        entry4.config(width=5, font=("Courier New", 12))
        entry4.grid(row=0,column=8)
    elif selected_option == 'sin(x)':
        button.config(text="Построить sin(x)")
    elif selected_option == 'cos(x)':
        button.config(text="Построить cos(x)")
 
        
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 300
window_height = 100
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")



frame = tk.Frame(root)
frame.pack(expand=True)

label1 = tk.Label(frame,text="*Y")
label1.grid(row=0,column=1)

entry1=tk.Entry(frame, width=5, font=("Courier New", 12))
entry1.grid(row=0,column=0)

label2 = tk.Label(frame,text="^")
label2.grid(row=0,column=2)

entry2=tk.Entry(frame, width=5, font=("Courier New", 12))
entry2.grid(row=0,column=3)

labequal = tk.Label(frame,text="=")
labequal.grid(row=0,column=4)

label3 = tk.Label(frame,text="*X")
label3.grid(row=0,column=6)

entry3=tk.Entry(frame, width=5, font=("Courier New", 12))
entry3.grid(row=0,column=5)

label4 = tk.Label(frame,text="^")
label4.grid(row=0,column=7)

entry4=tk.Entry(frame, width=5, font=("Courier New", 12))
entry4.grid(row=0,column=8)

button = tk.Button(root, text="Результат", command=show)
button.pack()

options = ["Прямая", "sin(x)", "cos(x)"]  # Список опций для Combobox

combobox = ttk.Combobox(frame, values=options)
combobox.current(0)
combobox.grid(row=1, column=0, columnspan=9, sticky="ew")
combobox.bind("<<ComboboxSelected>>", update_button)

root.mainloop()

