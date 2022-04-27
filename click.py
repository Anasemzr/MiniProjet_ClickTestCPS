import time as t
from tkinter import Tk, Label, Button, Canvas
import winsound as w


class tk(Tk):
    nb = 0

    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x500")
        self.lbl = Label(self, text=" TIME : 20 ", font=("Arial", 20), fg="red")
        self.lbl.pack(expand=True)
        quitter=Button(self,text="QUITTER",command=self.destroy)
        quitter.place(x=220,y=470)

        btn_20 = Button(self, text="20", command=lambda: self.change_time(20))
        btn_20.place(x=10, y=40)
        btn_40 = Button(self, text="40", command=lambda: self.change_time(40))
        btn_40.place(x=470, y=10)
        btn_60 = Button(self, text="60", command=lambda: self.change_time(60))
        btn_60.place(x=470, y=40)
        btn_10 = Button(self, text="10", command=lambda: self.change_time(10))
        btn_10.place(x=10, y=10)

        self.zoneJ = canvas(300, 300)
        self.zoneJ.pack(expand=True)

        self.zoneJ.bind("<Button-1>", self.clicker)

        self.nb = 0
        self.time_yo = [1, 2]
        self.minuteur = 21
        self.indicator = "YES"
        self.tiempo = 20
        self.start()

    def clicker(self, event):
        self.nb += 1

    def change_time(self, x):
        self.tiempo = x
        if self.nb == 0:
            self.minuteur = x
            self.lbl["text"] = "  TIME \n {}".format(x)

    def start(self):
        if self.nb >= 1:
            self.temps()
        self.after(100, self.start)

    def temps(self):
        self.time_yo.append(t.gmtime().tm_sec)
        if self.time_yo[-1] > self.time_yo[-2] and self.indicator == "YES":
            self.minuteur -= 1
            self.lbl["text"] = self.minuteur

        if self.minuteur <= 0 and self.indicator == "YES":
            self.zoneJ.destroy()
            self.indicator = "NO"
            ratio = self.nb / self.tiempo
            self.lbl["text"] = "You do {} in {} second :\n{} click/second".format(self.nb, self.tiempo, ratio)
            self.nb = 0
            btn_restart = Button(self, text="Restart", command=self.restart)
            btn_restart.pack()

        if self.minuteur >= 1:
            self.after(50, self.temps)

    def restart(self):
        self.destroy()
        self.__init__()



class canvas(Canvas):
    def __init__(self, w, h):
        Canvas.__init__(self, width=w, height=h, background="red")


app = tk()
app.mainloop()
