from tkinter import *
from tkinter import messagebox
import math

root =Tk()
root.geometry("600x600")
root.title("CALCULATOR")
root.configure(bg="snow")

mylabel=Label(root,text="CALCULATOR",font=("arial",20,"bold"))
mylabel.pack()

myframe=LabelFrame(root)
mydisplay=Entry(root,width=22,borderwidth=5,font=("arial",23),bg="snow")
mydisplay.pack()

#button functions
def one():
    n=1
    mydisplay.insert(10,'1')
    return n
def two():
    n=2
    mydisplay.insert(10,'2')
    return n
def three():
    n=3
    mydisplay.insert(10,'3')
    return n
def four():
    n=4
    mydisplay.insert(10,'4')
    return n
def five():
    n=5
    mydisplay.insert(10,'5')
    return n
def six():
    n=6
    mydisplay.insert(10,'6')
    return n
def seven():
    n=7
    mydisplay.insert(10,'7')
    return n
def eight():
    n=8
    mydisplay.insert(10,'8')
    return n
def nine():
    n=9
    mydisplay.insert(10,'9')
    return n
def zero():
    n=0
    mydisplay.insert(10,'0')
    return n
def plus():
    mydisplay.insert(10,"+")
    return "+"
def minus():
    mydisplay.insert(10,"-")
    return "-"
def mult():
    mydisplay.insert(10,"*")
    return "*"
def divide():
    mydisplay.insert(10,"/")
    return "/"
def dot():
    mydisplay.insert(10,".")
def power():
    mydisplay.insert(10,"**")
def floor():
    mydisplay.insert(10,"//")
def mod():
    mydisplay.insert(10,"%")
def inverse():
    mydisplay.insert(10,"1/")
def root1():
    mydisplay.insert(10,"**0.5")
def cube():
    mydisplay.insert(10,"**3")
def sq():
    mydisplay.insert(10,"**2")
def clear():
    mydisplay.delete(0,END)
def cb():
    mydisplay.insert(10,"**(1/3)")
def result():
    try:
        r=eval(mydisplay.get())
        mydisplay.delete(0,END)
        mydisplay.insert(10,r)
    except SyntaxError:
        mydisplay.delete(0,END)
        mydisplay.insert(10,"INVALID")
    
mybutton1=Button(myframe,text="9",width=8,height=4,command=nine,bg="azure",font=("arial",10,"bold"))
mybutton1.grid(row=1,column=1)
mybutton2=Button(myframe,text="8",width=8,height=4,command=eight,bg="azure",font=("arial",10,"bold"))
mybutton2.grid(row=1,column=2)
mybutton3=Button(myframe,text="7",width=8,height=4,command=seven,bg="azure",font=("arial",10,"bold"))
mybutton3.grid(row=1,column=3)
mybutton4=Button(myframe,text="6",width=8,height=4,command=six,bg="azure",font=("arial",10,"bold"))
mybutton4.grid(row=2,column=1)
mybutton5=Button(myframe,text="5",width=8,height=4,command=five,bg="azure",font=("arial",10,"bold"))
mybutton5.grid(row=2,column=2)
mybutton6=Button(myframe,text="4",width=8,height=4,command=four,bg="azure",font=("arial",10,"bold"))
mybutton6.grid(row=2,column=3)
mybutton7=Button(myframe,text="3",width=8,height=4,command=three,bg="azure",font=("arial",10,"bold"))
mybutton7.grid(row=3,column=1)
mybutton8=Button(myframe,text="2",width=8,height=4,command=two,bg="azure",font=("arial",10,"bold"))
mybutton8.grid(row=3,column=2)
mybutton9=Button(myframe,text="1",width=8,height=4,command=one,bg="azure",font=("arial",10,"bold"))
mybutton9.grid(row=3,column=3)
mybutton10=Button(myframe,text="0",width=8,height=4,command=zero,bg="azure",font=("arial",10,"bold"))
mybutton10.grid(row=4,column=1)
mybutton11=Button(myframe,text=".",width=8,height=4,command=dot,bg="azure",font=("arial",10,"bold"))
mybutton11.grid(row=4,column=2)
mybutton12=Button(myframe,text="=",width=8,height=4,command=result,bg="thistle",font=("arial",10,"bold"))
mybutton12.grid(row=4,column=5)

mybutton13=Button(myframe,text="/",width=8,height=4,command=divide,bg="linen",font=("arial",10,"bold"))
mybutton13.grid(row=4,column=4)
mybutton14=Button(myframe,text="+",width=8,height=4,command=plus,bg="linen",font=("arial",10,"bold"))
mybutton14.grid(row=3,column=4)
mybutton15=Button(myframe,text="-",width=8,height=4,command=minus,bg="linen",font=("arial",10,"bold"))
mybutton15.grid(row=2,column=4)
mybutton16=Button(myframe,text="*",width=8,height=4,command=mult,bg="linen",font=("arial",10,"bold"))
mybutton16.grid(row=1,column=4)
mybutton17=Button(myframe,text="**",width=8,height=4,command=power,bg="linen",font=("arial",10,"bold"))
mybutton17.grid(row=1,column=5)
mybutton18=Button(myframe,text="//",width=8,height=4,command=floor,bg="linen",font=("arial",10,"bold"))
mybutton18.grid(row=2,column=5)
mybutton19=Button(myframe,text="%",width=8,height=4,command=mod,bg="linen",font=("arial",10,"bold"))
mybutton19.grid(row=3,column=5)
mybutton20=Button(myframe,text="1/x",width=8,height=4,command=inverse,bg="linen",font=("arial",10,"bold"))
mybutton20.grid(row=4,column=3)
mybutton21=Button(myframe,text="CL",width=8,height=4,command=clear,bg="thistle",font=("arial",10,"bold"))
mybutton21.grid(row=5,column=5)
mybutton22=Button(myframe,text="root",width=8,height=4,command=root1,bg="linen",font=("arial",10,"bold"))
mybutton22.grid(row=5,column=2)
mybutton22=Button(myframe,text="cb.rt",width=8,height=4,command=cb,bg="linen",font=("arial",10,"bold"))
mybutton22.grid(row=5,column=1)
mybutton23=Button(myframe,text="x**3",width=8,height=4,command=cube,bg="linen",font=("arial",10,"bold"))
mybutton23.grid(row=5,column=3)
mybutton23=Button(myframe,text="x**2",width=8,height=4,command=sq,bg="linen",font=("arial",10,"bold"))
mybutton23.grid(row=5,column=4)

myframe.pack()
root.mainloop()
