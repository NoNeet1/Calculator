import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()

def show(): #функция для создания графика
    try:
        selected_option = combobox.get().strip() 
        #ввод данных
        a = float(entry3.get().strip())
        b = float(entry1.get().strip())
        c = float(entry4.get().strip())
        d = float(entry2.get().strip())
        Y1 = float(entry5.get().strip())
        Y2 = float(entry6.get().strip())
        delY=float(entry7.get().strip())
        X1=float(entry8.get().strip())
        X2=float(entry9.get().strip())
        delX=float(entry10.get().strip())
        x_values = np.linspace(X1 * np.pi, X2 * np.pi, 1000) #x принимает для тригонометрических графиков
        if(Y1>Y2 and delY<=0 and b!=0 and a!=0):
            raise ValueError  #вызов ошибки, если введены неправильные данные
        if(selected_option=='Прямая'):
            x_values = np.linspace(X1, X2, 100) #x принимает для прямых графиков
            y_values = pow((a * pow(x_values,c))/b, 1/d)
        elif(selected_option=='sin(x)'):
            y_values = b * np.power(np.sin(np.power(d*x_values, a)), c)
        elif(selected_option=='cos(x)'):
            y_values = b * np.power(np.cos(np.power(d*x_values, a)), c)
        #Пока что tg(x) и ctg(x) работают некорректно, если менять значения X внутри tg и ctg
        elif selected_option == 'tg(x)':
            y_values = np.apply_along_axis(lambda x: np.squeeze(b * np.power(np.tan(np.power(d*x_values, a)), c)), 0, x_values)
            y_values[:-1][np.diff(np.sign(y_values)) != 0] = np.nan
        elif selected_option == 'ctg(x)':
            y_values = np.apply_along_axis(lambda x: np.squeeze(b * np.power(1/(np.tan(np.power(d*x_values, a))), c)) , 0, x_values)
            y_values[:-1][np.diff(np.sign(y_values)) != 0] = np.nan
        plt.xlim(X1, X2)
        plt.ylim(Y1, Y2)
        plt.xticks(np.arange(X1, X2+delX, delX))  # Деления на оси X 
        plt.yticks(np.arange(Y1, Y2+delY, delY))  # Деления на оси Y 
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot(x_values, y_values, '-r')
        plt.grid(True)
        plt.show()
    except ValueError: #вызов ошибки, если введены не все данные
            button.config(state="disabled")  
            messagebox.showerror("Ошибка", "Некорректный ввод данных.")
            button.config(state="normal") 
           
def update_button(event):  # Функция для обновления кнопки при изменении выбора
    selected_option = combobox.get().strip()
    if selected_option == 'Прямая':
        button.config(text="Построить прямую")
        #восстановление изначального вида интерфейса
        labequal.config(text="=")
        label1.config(text="*Y")
        label1.grid(row=0,column=1)
        entry1.grid(row=0,column=0)
        label2.config(text="^")
        label2.grid(row=0,column=2)
        entry2.grid(row=0,column=3)
        labequal.config(text="=")
        labequal.grid(row=0,column=4)
        label3.config(text="*X")
        label3.grid(row=0,column=6)
        entry3.grid(row=0,column=5)
        label4.config(text="^")
        label4.grid(row=0,column=7)
        entry4.grid(row=0,column=8)
    else:
        #изменения вида интерфейса при выборе тригонометрической функции
        label1.config(text="Y") 
        label2.config(text="=")
        entry1.grid(row=0,column=3)
        labequal.grid(row=0,column=4)
        entry2.grid(row=0,column=5)
        label3.config(text="*X^")
        entry3.grid(row=0,column=7)
        label4.config(text=")^")
        label4.grid(row=0,column=8)
        entry4.grid(row=0,column=9)
        if selected_option=='sin(x)':
            button.config(text="Построить sin(x)")
            labequal.config(text="(sin(")
        elif selected_option == 'cos(x)':
            button.config(text="Построить cos(x)")
            labequal.config(text="(cos(")
        elif selected_option == 'tg(x)':
            button.config(text="Построить tg(x)")
            labequal.config(text="(tg(")
        elif selected_option == 'ctg(x)':
            button.config(text="Построить ctg(x)")
            labequal.config(text="(ctg(")
    

#данные для вида окна       
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 120
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

#данные по умолчанию введённые в entry
defY2=tk.StringVar(value="10")
defDelY=tk.StringVar(value='1')
defY1=tk.StringVar(value="-10")
defX2=tk.StringVar(value="10")
defDelX=tk.StringVar(value='1')
defX1=tk.StringVar(value="-10")

#Создание интерфейса
#строка функции
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

#данные для оси Y
label6=tk.Label(frame,text="Ось Y=")
label6.grid(row=2,column=0)

label7=tk.Label(frame,text="[")
label7.grid(row=2,column=1)

entry5=tk.Entry(frame, width=5, font=("Courier New", 12), textvariable=defY1)
entry5.grid(row=2,column=2)

label7=tk.Label(frame,text=";")
label7.grid(row=2,column=3)

entry6=tk.Entry(frame, width=5, font=("Courier New", 12), textvariable=defY2)
entry6.grid(row=2,column=4)

label7=tk.Label(frame,text="]", )
label7.grid(row=2,column=5)

label7=tk.Label(frame,text="Шаг Y=")
label7.grid(row=2,column=6)

entry7=tk.Entry(frame, width=5, font=("Courier New", 12), textvariable=defDelY)
entry7.grid(row=2,column=7)

#данные для оси X
label8=tk.Label(frame,text="Ось X=")
label8.grid(row=3,column=0)

label9=tk.Label(frame,text="[")
label9.grid(row=3,column=1)

entry8=tk.Entry(frame, width=5, font=("Courier New", 12), textvariable=defX1)
entry8.grid(row=3,column=2)

label10=tk.Label(frame,text=";")
label10.grid(row=3,column=3)

entry9=tk.Entry(frame, width=5, font=("Courier New", 12), textvariable=defX2)
entry9.grid(row=3,column=4)

label11=tk.Label(frame,text="]", )
label11.grid(row=3,column=5)

label12=tk.Label(frame,text="Шаг X=")
label12.grid(row=3,column=6)

entry10=tk.Entry(frame, width=5, font=("Courier New", 12), textvariable=defDelX)
entry10.grid(row=3,column=7)

button = tk.Button(root, text="", command=show) #кнопка
button.grid(row=3, column=0, columnspan=9, sticky="ew")

options = ["Прямая", "sin(x)", "cos(x)", "tg(x)", "ctg(x)"]  # Список опций для Combobox

combobox = ttk.Combobox(root, values=options, state="readonly")
combobox.current(0)
combobox.grid(row=1, column=0, columnspan=10, sticky="ew")
combobox.bind("<<ComboboxSelected>>", update_button)

root.mainloop()

