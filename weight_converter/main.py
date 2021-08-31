from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from PIL import Image, ImageTk
#------------------------------------------------------------basic syntax-----------------------------------------------
root=Tk()
root.minsize(1000,500)
root.maxsize(1000,500)
root['bg']='#0E165F'
#------------------------------------------------------------all functions ---------------------------------------------
i=1
def move():
    global i
    if i==3:
        i=1
    if i==1:
        l4.config(image=img1)
    elif i==2:
        l4.config(image=img2)
    i+=1
    root.after(2000,move)


def calculate():
    weight=weight_variable.get()
    unit=type_weight.get()
    unit2=output_variable.get()
    try:
        if unit=='kg' and unit2=='lbs':
            result_var.set(float(weight)*2.205)
        elif unit=='lbs' and unit2=='kg':
            result_var.set(float(weight)*0.454)
        else:
            result_var.set(weight)
    except ValueError as e:
        msg.showerror('Error',"Wrong input")

def clear():
    result_var.set("")
    weight_variable.set("")
    type_weight.set("")
    output_variable.set("")

#------------------------------------------------------------entry variable---------------------------------------------
weight_variable=StringVar()
type_weight=StringVar()
result_var=StringVar()
output_variable=StringVar()
#------------------------------------------------------------frames-----------------------------------------------------
f1=Frame(root).place(x=150,y=130,height=300,width=300)

#------------------------------------------------------------labels-----------------------------------------------------
l1=Label(root,text="Weight Converter",fg='White',bg='#0E165F',font="comicasansms 20 bold").pack()
l2=Label(root,text="Weight",fg='White',bg='#0E165F',font="comicasansms 15 bold").place(x=550,y=150)
l3=Label(root,text="Input Unit",fg='White',bg='#0E165F',font="comicasansms 15 bold").place(x=550,y=205)
l5=Label(root,text="Output Unit",fg='White',bg='#0E165F',font="comicasansms 15 bold").place(x=550,y=275)
l4=Label(f1)
l4.place(x=150,y=130)


#_-----------------------------------------------------------entry feilds-----------------------------------------------
weight_entry=Entry(root,textvariable=weight_variable,font="comicasansms 15 bold")
weight_entry.place(x=690,y=150)
result_entry=Entry(root,textvariable=result_var,font="comicasansms 15 bold",state="readonly")
result_entry.place(x=690,y=420)

#---------------------------------------------------------list of weights-----------------------------------------------
weight_list=['kg','lbs']
#-----------------------------------------------------------Buttons-----------------------------------------------------
submit_button=Button(root,text="submit",font="comicsansms 15 bold",command=calculate).place(x=550,y=350)
clear_button=Button(root,text="clear",font="comicsansms 15 bold",command=clear).place(x=650,y=350)
#-------------------------------------------------------------comboboc--------------------------------------------------
scroll_box=ttk.Combobox(root,values=weight_list,font="comicasansms 15 bold",state='readonly',textvariable=type_weight)
scroll_box.place(x=690,y=210)
scroll_box.current(0)
scroll_box1=ttk.Combobox(root,values=weight_list,font="comicasansms 15 bold",state='readonly',textvariable=output_variable)
scroll_box1.place(x=690,y=270)
scroll_box1.current(1)
#-------------------------------------------------------------images----------------------------------------------------
img1=ImageTk.PhotoImage(Image.open("weight-converter2.png"))
img2=ImageTk.PhotoImage(Image.open("weight-converter3.png"))
move()



if __name__ == '__main__':
    root.mainloop()