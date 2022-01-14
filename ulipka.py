from tkinter import *
def brov():
        global var_head
        global c
        if var_head.get()=="1":
           c.create_oval((150,400, 400, 50),fill="brown",outline="black")
        elif var_head.get()=="0":
            c.create_arc((80,100,220,100), style=CHORD, start=0, extent=150,outline="black")
            c.create_arc((200,100,320,100), style=CHORD, start=0, extent=150,outline="black")
def glaz1():
    global var_glaz1
    global c
    if var_glaz1.get()=="0":
        c.create_oval((250,100,300,150),fill="red",outline="black")
    elif var_glaz1.get()=="1":
       c.create_oval((250,100,300,150),outline="orange",fill="orange")
def glaz2():
    global var_glaz2
    global c
    if var_glaz2.get()=="0":
        c.create_oval((125,100,175,150),fill="red",outline="black")    
    elif var_glaz2.get()=="1":
        c.create_oval((125,100,175,150),outline="orange",fill="orange")
def nos():
    if var_nos.get()=="1":
        c.create_arc((175,200,350,350),outline="orange",fill="orange")
    elif var_nos.get()=="0":
        c.create_arc((175,200,350,350),fill="green",outline="black")
def rot():
    if var_rot.get()=="1":
        c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="orange")
    elif var_rot.get()=="0":
        c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="black")
root=Tk() 
root.title("SMILe Robot")
#aken.iconbitmap('iconka.ico')
root.geometry('650x600')
f1=Frame(root,width=150,height=500)
f1.pack(side=LEFT)
c=Canvas(root, width=500, height=500, bg="pink") 
#c.create_oval((15,15,450,500),fill="orange")#golova
c.create_oval((125,100,175,150),fill="red",outline="black")#glaz1
c.create_oval((250,100,300,150),fill="red",outline="black")#glaz2
c.create_arc((175,200,350,350),fill="green",outline="black")#nos
c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150)#rot
c.create_arc((80,100,220,100), style=CHORD, start=0, extent=150,outline="black")
c.create_arc((200,100,320,100), style=CHORD, start=0, extent=150,outline="black")
c.pack(side=LEFT)
var_brov=StringVar()
brov=Checkbutton(fm,text="Брови",font="Calibri 26", fg="blue",variable=var_brov,onvalue="0",offvalue="1",command=brov)
var_glaz1=StringVar()
glaz1=Checkbutton(fm,text="Правый глаз",font="Calibri 26", fg="blue",variable=var_glaz1,onvalue="0",offvalue="1",command=glaz1)
var_glaz2=StringVar()
glaz2=Checkbutton(fm,text="Левый глаз",font="Calibri 26", fg="blue",variable=var_glaz2,onvalue="0",offvalue="1",command=glaz2)
var_rot=StringVar()
rot=Checkbutton(fm,text="Рот",font="Calibri 26", fg="blue",variable=var_rot,onvalue="0",offvalue="1",command=rot)
var_nos=StringVar()
nos=Checkbutton(fm,text="Нос",font="Calibri 26", fg="blue",variable=var_nos,onvalue="0",offvalue="1",command=nos)
brov.pack(side=RIGHT)
rot.pack(side=RIGHT)
nos.pack(side=RIGHT)
glaz1.pack(side=RIGHT)
glaz2.pack(side=RIGHT)
tk.mainloop()
