import time as t
from tkinter import Tk,Label,Button,Canvas
import winsound as w

time_yo=[1,2]
minuteur=21
indicator="YES"
nb=0
start=4
def clicker(event):
    global nb
    if nb==0:
        update()
    nb+=1
    print(nb)

def update():
    global time_yo,minuteur,indicator,nb,start

    time_yo.append(t.gmtime().tm_sec)
    if time_yo[-1]>time_yo[-2] and indicator=="YES":
        minuteur-=1
        lbl["text"]=minuteur

    if minuteur<=0:
        canvas_click.destroy()
        indicator="NO"
        ratio=nb/20
        lbl["text"]="You do {} in 20 second :\n{} click/second".format(nb,ratio)

    """if minuteur<=0:
        lbl["text"]="ALARM DRING DRING"
        w.PlaySound("bensound-epic.wav", w.SND_FILENAME)"""

    window.after(100,update)

def change_time(x):
    global minuteur,nb
    if nb==0:
        minuteur=x
        lbl["text"]="  TIME \n {}".format(x)


window=Tk()
window.geometry("500x500")
x=window.winfo_reqwidth()
y=window.winfo_reqheight()

lbl=Label(window,text=" TIME : 20 ",font=(("Arial"),20),fg="red")
lbl.pack(expand=True)

canvas_click=Canvas(window,width=300,height=300,bg="red")
canvas_click.pack(expand=True)

btn_20=Button(window,text="20",command=lambda:change_time(20))
btn_20.place(x=10,y=40)
btn_40=Button(window,text="40",command=lambda:change_time(40))
btn_40.place(x=450,y=10)
btn_60=Button(window,text="60",command=lambda:change_time(60))
btn_60.place(x=450,y=40)
btn_10=Button(window,text="10",command=lambda:change_time(10))
btn_10.place(x=10,y=10)

canvas_click.bind("<Button-1>",clicker)
window.mainloop()