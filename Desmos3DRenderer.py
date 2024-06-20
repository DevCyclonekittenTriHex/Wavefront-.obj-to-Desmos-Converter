import tkinter as tk
import tkinter.messagebox
import math

currentalias = []
root = tk.Tk()
root.title("Wavefront (.obj) to Desmos 3D Object")
decimalrounding = 2
root.minsize(300,500)
root.maxsize(300,500)
def Load(dimensions):
    string = filepath.get()
    currentalias = []
    if(string == ""):
        string = "TestObjects/monkey.obj"
    #print(string)
    try:
        f=open(string, "r")
        words = f.read().split("\n")
        
    except FileNotFoundError:
        MSGFileError()
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
    if(dimensions==3):
        convertedfaces = Convert2D(vertex,face)
    else if dimensions==3:
        convertedfaces = Convert3D(vertex,face)
def Convert2D(vertex,face):
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
    
    cmd = "["
    for i in range(len(faces)-1):
        cmd = cmd + faces[i]+","
    cmd = cmd + faces[len(faces)-1]
    cmd = cmd + "]"
    #print(cmd) 
    ToClipboard(cmd)
    f=open("Output/command_"+nameobj.get()+".txt","w")
    f.write(cmd)
    f.close()
    MSGClipboard()
    #print("New Alaises:")
    if len(currentalias)!=0:
        descriptor = ""
        for i in range(len(currentalias)):
            
            descriptor = descriptor + str(currentalias[i]) +","
        #print(descriptor)
        if MSGAliasError(descriptor)==True:
            
            cmd = ""
            for i in range(len(currentalias)):
                
                cmd = cmd + GenerateAlias(str(currentalias[i]))+"\n"
            f=open("Output/command_"+nameobj.get()+"_aliasfix.txt","a")
            f.write(cmd)
            f.close()
            if MSGAliasCreated()==True:
                ToClipboard(cmd)
        
    
    
def GenerateAlias(integer):
    
    cmd = "F_{"+integer+"}"
    cmd = cmd + "(a,b,c,d)=\operatorname{polygon}("
    for i in range(int(integer)):
        cmd = cmd + "(X_{x}(a["+str(i+1)+"],b["+str(i+1)+"],c["+str(i+1)+"]),Y_{x}(a["+str(i+1)+"],b["+str(i+1)+"],c["+str(i+1)+"]))"
    cmd = cmd + ")"
   # print(cmd)
    return cmd
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
    xyz=""
    for i in range(len(x)):
        xyz +=x[i]+","+y[i]+","+z[i]+"/"
    xyz + "0"
    GetVectorFromFaces(xyz)
    for i in range(len(x)):
        xs=xs + x[i]+","
    
    for i in range(len(y)):
        ys=ys + y[i]+","
    
    for i in range(len(z)):
        zs=zs + z[i]+","
    xs = xs +"0"
    
    ys = ys +"0"
    
    zs = zs +"0"
    found = False
    ind = 0
    if len(x) >= 7:
        for i in range(len(currentalias)):
            if currentalias[i] == len(x):
                found = True
                ind = i
        if found!=True:
            currentalias.append(len(x))
    command = f"F_"+"{"+str(len(x))+"}"+f"([{xs}],[{ys}],[{zs}],{len(x)})"
    #print(command)
    return command
        
def ToClipboard(string):
    root.clipboard_clear()
    root.clipboard_append(string)
    root.update()
def MSGAliasError(desc):

    yn2 = tk.messagebox.askyesno("Generate Vertex-Face Alias", f"""Your Object has faces with unsupported default vertex count.
                                \n Do you want to generate a Alias to support your object.
                                \n Face-Vertex Count Missing:{desc}""", parent=root)
    return yn2
def MSGAliasCreated():
    yn = tk.messagebox.askyesno("Alias Created Sucessfully","Do you want to copy to clipboard. \n Alias still retrievable in file command_"+nameobj.get()+"_aliasfix.txt",parent=root)
    return yn
def GetVectorFromFaces(vertecies):
    # an arbitrarily set of 3D verticies, if the face is planar, getting a vector from 2 points. 
    #will return a right angle from the outside/inside face normal.
    #if a face has non planar points, the face has to be divided into faces which are planar.
    #(increases char count, allows shaded and materials, material properties carry over. lag increased for shaded degrees)
    #finding face normal of planar face, is getting 3 verts (A,B,C), find vector of Pair A,B, and B,C and get the cross product,
    vert = vertecies.split("/")
    v1=vert[0].split(",")
    v2=vert[1].split(",")
    v3=vert[2].split(",")
    ax=float(v2[0])-float(v1[0])
    ay=float(v2[1])-float(v1[1])
    az=float(v2[2])-float(v1[2])
    bx=float(v3[0])-float(v2[0])
    by=float(v3[1])-float(v2[1])
    bz=float(v3[2])-float(v2[2])
    cx = (ay*bz) - (az*by)
    cy =(az*bx) - (ax*bz)
    cz = (ax*by) - (ay*bx)
    
    #print(f"Vector: <{cx},{cy},{cz}>")

    #from vector, find angle between vector and cam vector.
    cam = [0,0,-1] #+180 degrees, so vector facing towards camera is facing the same direction as camvector.
    c=[cx,cy,cz]
    
    
    dotpr = (cam[0]*c[0])+(cam[1]*c[1])+(cam[2]*c[2])
    #print("NEWFACE:")
    
    mag = (math.sqrt(c[0]**2+c[1]**2+c[2]**2)*math.sqrt(cam[0]**2+cam[1]**2+cam[2]**2))
    angle = dotpr/ mag
    #print(cam)
    #print(c)
    #print(dotpr)
    #print(mag)
    #print(angle)
    
    
    
    try:
        angle = math.acos(abs(angle))
        angle = angle *180/math.pi
        #print(f"Angle: {angle}")
        #print(vertecies)
        return angle
    except ValueError:
        if c[0]==0 and c[1] ==0:
            #cadinally allined
            #print("Angle: 0.0")
            return 0
        else:
            print("I AM PROBABLY STUPID")
            #print(c)
            #print(cam)
def MSGFileError():
    yn = tk.messagebox.showerror("File not found error","File not found",parent=root)
    return yn
def MSGClipboard():
    yn = tk.messagebox.showinfo("Copied!","Copied Command to Clipboard\nCommand availiable in command_"+nameobj.get()+".txt",parent=root)
    return yn
#checkvalidityofalias()
GenerateAlias("7")
titlelabel = tk.Label(root, text = 'Convert Wavefront .Obj to Desmos Object:', font=('calibre',10, 'bold'))
filelabel = tk.Label(root, text = 'FilePath:', font=('calibre',10, 'bold'))
roundinglabel =tk.Label(root, text = 'Rounding :', font=('calibre',10, 'bold'))
roundinglabel2 =tk.Label(root, text = 'places', font=('calibre',10))

namelabel = tk.Label(root, text = 'ObjectName:', font=('calibre',10, 'bold'))
nameobj = tk.Entry(root, font=('calibre',10,'normal'))
filepath = tk.Entry(root, font=('calibre',10,'normal'))
roundinglength = tk.Entry(root, font=('calibre',10,'normal'))
convertbtn2d = tk.Button(root, text="Convert To 2D Renderer",command=Load)
convertbtn3d = tk.Button(root, text="Convert To 3D Renderer",command=Load)

#filepath.insert(TestObjects\monkey.obj')

titlelabel.grid(row =0,column=1,columnspan=3)



namelabel.grid(row=1, column=1)
filelabel.grid(row=2, column=1)

nameobj.grid(row=1,column=2)
filepath.grid(row=2,column=2)

roundinglabel.grid(row=3,column=1)
roundinglength.grid(row=3,column=2)
roundinglabel2.grid(row=3,column=3)


convertbtn2d.grid(row=10,column=2)
convertbtn3d.grid(row=9,column=2)

root.mainloop()


