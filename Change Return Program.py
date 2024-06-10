from tkinter import *
t=Tk()
t.geometry("400x400")
lbl1=Label(t,text="Enter bill amount: ")
lbl1.pack()
inp1=Entry(t)
inp1.pack()

lbl2=Label(t,text="Enter cash amount given by customer: ")
lbl2.pack()

inp2=Entry(t)
inp2.pack()

def fun1():
    txt1.delete("0.0",END)
    a=inp1.get()
    b=inp2.get()
    txt1.insert("0.0",int(b)-int(a))

btn1=Button(t,text="Submit",command=fun1)
btn1.pack()

txt1=Text(t)
txt1.pack()
t.mainloop()
