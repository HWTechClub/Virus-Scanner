#importing tkinter from library 
from tkinter import *

#defining all the functions
def meta():
    pass
def url():
    pass
def vtFile():
    pass
def vtUrl():
    pass
#make the gui
window=Tk()
window.title("VIRUS SCANNER")
window.geometry("600x600")

#Adding a label 
Label(window, text="Options",font=16).grid(row=0,column=0,sticky=W)

#Add a button
Button(window,text="1.Meta Defender",width=16, command=meta).grid(row=1,column=0,sticky=W)
Button(window,text="2.Url scan",width=16, command=url).grid(row=2,column=0,sticky=W)
Button(window,text="3.virus total file",width=16, command=vtFile).grid(row=3,column=0,sticky=W)
Button(window,text="4.virus total url",width=16, command=vtUrl).grid(row=4,column=0,sticky=W)
window.mainloop()