from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Registration form")
root.geometry("900x700")

#main labels
mylabel1=Label(root,text="STUDENT REGISTRATION FORM",fg="red",font=("arial",20,"bold"))
mylabel1.pack()
mylabel2=Label(root,text="SESSION 2024-2025",fg="blue",font=("arial",20,"bold"))
mylabel2.pack()
myframe=LabelFrame(root)
mylabel3=Label(myframe,text="NAME:")
mylabel3.grid(row=3,column=1)

#frame labels
mylabel4=Label(myframe,text="ROLL. No.:")
mylabel4.grid(row=4,column=1)
mylabel5=Label(myframe,text="ADDRESS:")
mylabel5.grid(row=5,column=1)
mylabel6=Label(myframe,text="COURSE:")
mylabel6.grid(row=6,column=1)
mylabel7=Label(myframe,text="BRANCH:")
mylabel7.grid(row=7,column=1)
mylabel8=Label(myframe,text="GENDER:")
mylabel8.grid(row=8,column=1)

#checkboxes
var1=IntVar()
var2=IntVar()
var3=IntVar()
ckb1=Checkbutton(myframe,text="B TECH",variable=var1)
ckb1.grid(row=6,column=2)
ckb2=Checkbutton(myframe,text="MCA",variable=var2)
ckb2.grid(row=6,column=3)
ckb3=Checkbutton(myframe,text="MBA",variable=var3)
ckb3.grid(row=6,column=4)

#radiobutton
val1=IntVar()
val2=IntVar()
val3=IntVar()
rb1=Radiobutton(myframe,text="MALE",variable=val1)
rb1.grid(row=8,column=2)
rb2=Radiobutton(myframe,text="FEMALE",variable=val2)
rb2.grid(row=8,column=3)
rb3=Radiobutton(myframe,text="OTHER",variable=val3)
rb3.grid(row=8,column=4)

#entry pt
ent1=Entry(myframe,width=30,borderwidth=5)
ent1.grid(row=3,column=2)
ent2=Entry(myframe,width=30,borderwidth=5)
ent2.grid(row=4,column=2)
ent3=Entry(myframe,width=30,borderwidth=5)
ent3.grid(row=5,column=2)
myframe.pack()

#definiton of button
def submit():
    messagebox.showinfo("INFORMATION","SUCCESSFULLY REGISTERED")
def clear():
    messagebox.showinfo("INFORMATION","ENTER THE DATA")

#button
mybutton1=Button(myframe,text="SUBMIT",bg="yellow",command=submit)
mybutton1.grid(row=11,column=5)
mybutton2=Button(myframe,text="CLEAR",fg="white",bg="RED",command=clear)
mybutton2.grid(row=11,column=6)

# list box
lb=Listbox(myframe)
lb.insert(1,"CSE")
lb.insert(2,"AIML")
lb.insert(3,"AI")
lb.insert(4,"DS")
lb.insert(5,"IoT")
lb.insert(6,"CSBS")
lb.insert(7,"CYS")
lb.insert(8,"CSE")
lb.grid(row=7,column=2)
root.mainloop()
