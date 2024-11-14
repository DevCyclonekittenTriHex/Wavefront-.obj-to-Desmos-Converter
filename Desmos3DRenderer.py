import tkinter as tk
import tkinter.messagebox
import math
from DesmosConverterModule import *

currentalias = []
root = tk.Tk()
root.title("Wavefront (.obj) to Desmos 3D Object")
root.minsize(300,500)
root.maxsize(300,500)





#labels
titlelabel = tk.Label(root, text = 'Convert Wavefront .Obj to Desmos Object:', font=('calibre',10, 'bold'))
filelabel = tk.Label(root, text = 'FilePath:', font=('calibre',10, 'bold'))
namelabel = tk.Label(root, text = 'ObjectName:', font=('calibre',10, 'bold'))
roundinglabel =tk.Label(root, text = 'Rounding :', font=('calibre',10, 'bold'))
roundinglabel2 =tk.Label(root, text = 'places', font=('calibre',10))
#Entrywidget
nameobj = tk.Entry(root, font=('calibre',10,'normal'))
filepath = tk.Entry(root, font=('calibre',10,'normal'))
roundinglength = tk.Entry(root, font=('calibre',10,'normal'))
#Button

def ConvertTo2D():
    Load2D(filepath.get(),root,int(roundinglength.get()),nameobj.get())
    return
def ConvertTo3D():
    Load3D(filepath.get(),root,int(roundinglength.get()))
    return
def CreateStandalone2D():
    GenerateCommandsForStandaloneProject2D(False,root)
    return
convertbtn2d = tk.Button(root, text="Convert To 2D Renderer",command=ConvertTo2D)
convertbtn3d = tk.Button(root, text="Convert To 3D Renderer",command=ConvertTo3D)
create2d = tk.Button(root, text="Create 2D Renderer Environment",command=CreateStandalone2D)

titlelabel.grid(row =0,column=1,columnspan=3)
#Labels
namelabel.grid(row=1, column=1)
filelabel.grid(row=2, column=1)
roundinglabel.grid(row=3,column=1)
roundinglabel2.grid(row=3,column=3)
#EntryWidgets
nameobj.grid(row=1,column=2)
filepath.grid(row=2,column=2)
roundinglength.grid(row=3,column=2)



#Buttons
convertbtn2d.grid(row=10,column=2)
convertbtn3d.grid(row=9,column=2)
create2d.grid(row=8,column=2)

nameobj.insert(0, "Cube001") 
filepath.insert(0, "TestObj/cube.obj") 
roundinglength.insert(0,"2")

root.mainloop()



