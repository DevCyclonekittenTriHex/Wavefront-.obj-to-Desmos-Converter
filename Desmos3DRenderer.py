import tkinter as tk
import tkinter.messagebox
import math
root = tk.Tk()
root.title("Wavefront (.obj) to Desmos 3D Object")
decimalrounding = 2
root.minsize(300,500)
root.maxsize(300,500)
def Load():
    string = filepath.get()
    if(string == ""):
        string = "TestObjects/monkey.obj"
    #print(string)
    try:
        f=open(string, "r")
        words = f.read().split("\n")
        
    except FileNotFoundError:
        return
    
    vertex = []
    face = []
    
    #print(words)
    for i in range(len(words)):
        if words[i]!="":
            if words[i][0] == "v":
                
                if words[i][1] == " " :
                    
                    
                    vertex.append(words[i])
                
            if words[i][0] =="f":
                
                face.append(words[i])
    #print(vertex)
    #print(face)
    convertedfaces = Convert(vertex,face)
def GetVectorFromFaces(vertecies):
    # an arbitrarily set of 3D verticies, if the face is planar, getting a vector from 2 points. 
    #will return a right angle from the outside/inside face normal.
    #if a face has non planar points, the face has to be divided into faces which are planar.
    #(increases char count, allows shaded and materials, material properties carry over. lag increased for shaded degrees)
    #finding face normal of planar face, is getting 3 verts (A,B,C), find vector of Pair A,B, and B,C and get the cross product,
    vert = vertecies.split("\")
    v1=vert[0].split(",")
    v2=vert[1].split(",")
    v3=vert[2].split(",")
    ax=v2[0]-v1[0]
    ay=v2[1]-v1[1]
    az=v2[2]-v1[2]
    bx=v3[0]-v2[0]
    by=v3[1]-v2[1]
    bz=v3[2]-v2[2]
    cx = ay*bz − az*by
    cy = az*bx − ax*bz
    cz = ax*by − ay*bx
    
    print(f"Vector: <{cx},{cy},{cz}>")

    #from vector, find angle between vector and cam vector.
    cam = [0,0,-1] #+180 degrees, so vector facing towards camera is facing the same direction as camvector.
    c=[cx,cy,cz]
    angle = (cam[0]*c[0])+(cam[1]*c[1])+(cam[2]*c[2])
    angle = math.acos(angle)
    print(angle)
    
    
def Convert(vertex,face):
    faces = []
    for i in range(len(face)):
        #print(f"Face {i+1}:")
        key = face[i].split(" ")
        curr = []
        
        for i2 in range(len(key)-1):
            index =key[i2+1].split("/")
            
            selv = vertex[int(index[0])-1]
            curr.append(selv)
        faces.append(ToFace(curr))
    print("Command:")
    cmd = "["
    for i in range(len(faces)-1):
        cmd = cmd + faces[i]+","
    cmd = cmd + faces[len(faces)-1]
    cmd = cmd + "]"
    #print(cmd) 
    ToClipboard(cmd) 
def ToFace(facevertex):
    x=[]
    y=[]
    z=[]
    for i in range(len(facevertex)):
        

        vert = facevertex[i].split(" ")
        
        x.append(str(round(float(vert[1]),decimalrounding)))
        y.append(str(round(float(vert[2]),decimalrounding)))
        z.append(str(round(float(vert[3]),decimalrounding)))
        
    #print(f"X: {x}")
    #print(f"Y: {y}")
    #print(f"Z: {z}")
    
    xs= ""
    ys=""
    zs=""
    for i in range(len(x)):
        xs=xs + x[i]+","
    
    for i in range(len(y)):
        ys=ys + y[i]+","
    
    for i in range(len(z)):
        zs=zs + z[i]+","
    xs = xs +"0"
    
    ys = ys +"0"
    
    zs = zs +"0"
    
    lis=["100","1","2","3","4","5","6"]
    #rint(str(len(x)))
    command = f"F_"+"{"+str(len(x))+"}"+f"([{xs}],[{ys}],[{zs}],{len(x)})"
    #print(command)
    return command
        
def ToClipboard(string):
    root.clipboard_clear()
    root.clipboard_append(string)
    root.update()
def checkvalidityofalias():

    yn = tk.messagebox.askyesno("Generate Vertex-Face Alias", "Your Object has faces with unsupported default vertex count.\n Do you want to generate a Alias to support your object. ", parent=root)  
    print(yn)
#checkvalidityofalias()
titlelabel = tk.Label(root, text = 'Convert Wavefront .Obj to Desmos Object:', font=('calibre',10, 'bold'))
filelabel = tk.Label(root, text = 'FileName:', font=('calibre',10, 'bold'))
roundinglabel =tk.Label(root, text = 'Rounding :', font=('calibre',10, 'bold'))
roundinglabel2 =tk.Label(root, text = 'places', font=('calibre',10))

filepath = tk.Entry(root, font=('calibre',10,'normal'))
roundinglength = tk.Entry(root, font=('calibre',10,'normal'))
convertbtn = tk.Button(root, text="Convert",command=Load)

#filepath.insert(TestObjects\monkey.obj')

titlelabel.grid(row =0,column=1,columnspan=3)
filelabel.grid(row=1, column=1)
filepath.grid(row=1,column=2)
#roundinglabel.grid(row=2,column=1)
#roundinglength.grid(row=2,column=2)
#roundinglabel2.grid(row=2,column=3)


convertbtn.grid(row=10,column=2)

root.mainloop()


