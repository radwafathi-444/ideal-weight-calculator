#رضوي فتحي عبد اللطيف مندور 
from tkinter import *

import tkinter as tk

# نافذة البرنامج

myframe = tk.Tk()
myframe.title("حاسبة الوزن المثالي")
myframe.geometry("450x450")  
myframe.configure(bg="white") 
 

# العنوان
mylabel = Label(myframe, text="برنامج حساب الوزن المثالي", 
font=("Helvetica 18 bold"), bg="white", fg="black")
mylabel.pack(pady=20)


label = Label(myframe, text=":ادخل طولك بالسنتيمتر", 
 font=("Helvetica 16 bold"), bg="white", fg="black")
label.pack(pady=10)

# إدخال الطول
myheight = Entry(myframe, font=("Helvetica 16"), width=20)
myheight.pack(pady=10)

#  النتيجة
myresult = tk.Frame(myframe, bg="white")
myresult.pack(pady=20)

# دالة حساب الوزن
def calculate():
    height = float(myheight.get())
    ideal = height - 100
    myresultlabel = Label(myresult, text=f"وزنك المثالي هو: {ideal:.1f} كجم", 
    font=("Helvetica 16 bold"), fg="black", bg="white")
    myresultlabel.pack(pady=5)

# زر الحساب
mybutton = Button(myframe, text="احسب الآن", fg="white", bg="orange", font=("Helvetica 16 bold"), 
padx=10, pady=10, width=20, command=calculate)
mybutton.pack(pady=20)

myframe.mainloop()
