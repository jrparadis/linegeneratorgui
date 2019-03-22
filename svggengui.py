#generates sinewave based generative SVG files suitable for pen plotting

from tkinter import *
import turtle
from canvasvg import canvasvg
import math

resx = 1500
resy = 1100

def draw(t, leng, angle, x,y):
        t.pu()
        t.setpos(x,y)
        t.pd()
        t.seth(angle)
        t.forward(leng)
        
def clicked():
        t = turtle.Turtle()
        t.ht()
        t.pu()
        turtle.tracer(2000,20)
        turtle.screensize(resx,resy)        
        coordsy = [y for y in range(int(resy/2),int(-resy/2), int(yskip.get()))]
        coordsx = [x for x in range(int(-resx/2),int(resx/2), int(xskip.get()))]
        for y in coordsy:
                for x in coordsx:
                        if x == 0:
                                pass
                        else:
                                ycur = int(yformula.get())
                                lcur = float(lformula.get())
                                scur = int(sineformula.get())
                                #changing the bitwise operators here gets interesting patterns
                                draw(t,lcur,float(angle.get()),x,math.sin(ycur+(x^x^x&x))*scur)
        outlbl.configure(text="done, ready.")

def output():
        canvasvg.saveall("F:\\py\\plotter\\gui\\bwlines.svg", turtle.getcanvas())
        #optimize svg rendering into related areas - cuts down on times and plotter jumping around
        svg = ''
        with open('F:\\py\\plotter\\gui\\bwlines.svg', 'r') as f:
            svg += f.read()
            
        splitlist = svg.split('<')
        newlist = []
        for each in splitlist:
            newlist.append(''.join(('<',each)))

        body = sorted(newlist[4:-2])

        with open('F:\\py\\plotter\\gui\\bwlines.svg','w') as f:
            f.write(newlist[1])
            f.write(newlist[2])
            f.write(newlist[3])
            for each in body:
                f.write(each)
            f.write(newlist[-1])

        outlbl.configure(text="Output as \nbwlines.svg")
        
window = Tk()
window.title("SVG Line Generator")
window.geometry('160x240')

angletext= DoubleVar()
angletext.set(135)
anglelabel = Label(window, text="angle")
anglelabel.grid(column=0, row=0)
angle = Entry(window,width=10,textvariable=angletext)
angle.grid(column=1,row=0)

xrestext = IntVar()
xrestext.set(resx)
xlabel = Label(window, text="x resolution")
xlabel.grid(column=0, row=1)
xres = Entry(window,width=10,textvariable=xrestext)
xres.grid(column=1,row=1)

yrestext = IntVar()
yrestext.set(resy)
ylabel = Label(window, text="y resolution")
ylabel.grid(column=0, row=2)
yres = Entry(window,width=10,textvariable=yrestext)
yres.grid(column=1,row=2)

xskiptext = IntVar()
xskiptext.set(15)
xskiplabel = Label(window, text="horizontal skip")
xskiplabel.grid(column=0, row=3)
xskip = Entry(window,width=10,textvariable=xskiptext)
xskip.grid(column=1,row=3)

yskiptext = IntVar()
yskiptext.set(-30)
yskiplabel = Label(window, text="verticle skip")
yskiplabel.grid(column=0, row=4)
yskip = Entry(window,width=10,textvariable=yskiptext)
yskip.grid(column=1,row=4)

yformula = DoubleVar()
yformula.set(2)
yformulalabel = Label(window, text="y mod")
yformulalabel.grid(column=0, row=5)
yformula = Entry(window,width=10,textvariable=yformula)
yformula.grid(column=1,row=5)

lformulatext = DoubleVar()
lformulatext.set(3)
lformulalabel = Label(window, text="length")
lformulalabel.grid(column=0, row=6)
lformula = Entry(window,width=10,textvariable=lformulatext)
lformula.grid(column=1,row=6)

sineamptext = DoubleVar()
sineamptext.set(300)
sineamplabel = Label(window, text="sine amplitude")
sineamplabel.grid(column=0, row=7)
sineformula = Entry(window,width=10,textvariable=sineamptext)
sineformula.grid(column=1,row=7)

outlbl = Label(window, text="ready.")
outlbl.grid(column=0, row=10)

btn = Button(window, text="draw", command=clicked).grid(column=0, row=9)
btn2 = Button(window, text="export SVG", command=output).grid(column=1, row=9)

window.mainloop()
