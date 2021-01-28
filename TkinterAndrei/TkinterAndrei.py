from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
from tkinter.messagebox import*
import sys, fileinput
def phonk():
    a=m1.selection_get()
    if a==0:
        tabs.select(0)
    elif a==1:
        tabs.select(1)
    elif a==2:
        tabs.select(2)
def funktion():
    pass
def open_():
    file=askopenfilename()
    for text in fileinput(file):
        txt_box.insert(0.0,text)
    #f=open(file,"r",encoding="utf-8-sig")
    #text=f.readlines()
def save_():
    file=asksaveasfile(mode="w",defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()
def exit_():
    if askyesno("","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")

root=Tk()
root.geometry("500x400")
root.title("Elemendid Tkinteris")
tabs=ttk.Notebook(root)
N=7
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Seitsmes"]
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)
tab6=Frame(tabs)
tab7=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")
tabs.add(tab5,text="Viies")
tabs.add(tab6,text="Kuues")
tabs.add(tab7,text="Seitsmes")

#tabs_list[[Frame,str]]
#for i in range(N):
#    t="tab"+str
#    tabs_list.append(Frame(tabs))
#    tabs_list=Frame(tabs_list)
#    tabs.add(tab,text=texts[i])
M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=0)
M.add_cascade(label="Menu1",menu=m1)
m1.add_command(label="Com1",command=funktion)
m1.add_command(label="Com2",command=funktion)
m1.add_command(label="Com3",command=funktion)
m1.add_command(label="Com4",command=funktion)

m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_command(label="Violet",command=lambda:root.config(bg="violet"))

btn_open=Button(tab1,text="Open",command=open_)
btn_save=Button(tab2,text="Save",command=save_)
btn_exit=Button(tab3,text="Exit",command=exit_)
txt_box=scrolledtext.ScrolledText(tab1)
txt_box=Text(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

m4=Menu(M,tearoff=0)
M.add_cascade(label="Resolutions",menu=m4)
m4.add_command(label="Big",command=lambda:root.geometry("600x500"))
m4.add_command(label="Medium",command=lambda:root.geometry("500x400"))
m4.add_command(label="Small",command=lambda:root.geometry("400x300"))

tabs.pack(fill="both")
root.mainloop()