from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.geometry("500x400")
root.config(bg='snow')
choice=IntVar()
Font=('arial',13,'bold')
frame=Frame(root,bg='snow')
frame.pack()
passwordLabel=Label(frame,text='Password Generator Project',font=('times new roman',20,'bold'),fg="red",bg='snow')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(frame,text='Strong',value=1,variable=choice,font=Font,bg="coral",)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(frame,text='Medium',value=2,variable=choice,font=Font,bg="gold")
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(frame,text='Weak',value=3,variable=choice,font=Font,bg="medium aquamarine")
strongradioButton.grid(pady=5)

lengthLabel=Label(frame,text='Password Length',font=Font,fg='red')
lengthLabel.grid(pady=5)

length_Box=Spinbox(frame,from_=5,to_=18,width=5,font=Font,bg="powder blue")
length_Box.grid(pady=5)

generateButton=Button(frame,text='Generate',font=Font,command=generator,bg="light goldenrod")
generateButton.grid(pady=5)

passwordField=Entry(frame,width=25,bd=2,font=Font,bg="skyblue")
passwordField.grid()

copyButton=Button(frame,text='Copy',font=Font,command=copy,bg="SkyBlue3")
copyButton.grid(pady=5)

root.mainloop()
