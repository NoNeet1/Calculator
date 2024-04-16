
import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()

def x():
    input_text=entry.get()

def y():
    input_text=entry.get()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 500
window_height = 300
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack(expand=True)


label1 = tk.Label(frame,text="X=")
label1.grid(row=0,column=0)

entry1=tk.Entry(frame)
entry1.grid(row=0,column=1)

label2 = tk.Label(frame,text="Y=")
label2.grid(row=1,column=0)

entry2=tk.Entry(frame)
entry2.grid(row=1,column=1)

label3 = tk.Label(frame,text="Степень X=")
label3.grid(row=0,column=2)

entry3=tk.Entry(frame)
entry3.grid(row=0,column=3)

label4 = tk.Label(frame,text="Степень Y=")
label4.grid(row=1,column=2)

entry4=tk.Entry(frame)
entry4.grid(row=1,column=3)

button = tk.Button(root, text="Результат")

root.mainloop()
plt.plot([1,2,3,4])
plt.show()