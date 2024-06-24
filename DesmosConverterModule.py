import tkinter as tk
import tkinter.messagebox
import math
import webbrowser
#Used by functions
currentalias = []
#Startup
f=open("settings.txt","r")
words=f.read().split(",")
f.close()

DisableCopyToClipboard=False


#Converting
def Load2D(path,rt,decimalrounding,name):
    string = path
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
    
    convertedfaces = Convert2D(vertex,face,rt,decimalrounding,name)
def Load3D(path,rt,decimalrounding):
    string = path
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
    
    if MSGStandalone():
        convertedfaces = Convert3D(vertex,face,True,rt,decimalrounding)
    else:
        convertedfaces = Convert3D(vertex,face,False,rt,decimalrounding)  
def GenerateCommandsForStandaloneProject2D(rotate,root):
    cmd = ""

    cmd = cmd + """
    c_{1}=0\n
    c_{2}=0\n
    c_{3}=50\n
    C_{xrot}=0\n
    C_{yrot}=0\n
    C_{zrot}=0\n
    C_{xscale}=1\n
    C_{yscale}=1\n
    C_{zscale}=1\n
    """
    
    cmd = cmd + """
    X\left(a,b,c\\right)=\left(\\frac{c_{3}}{c_{3}+c\cdot C_{zscale}}\left(a\cdot C_{xscale}+c_{1}\\right)\\right)\n
    Y\left(a,b,c\\right)=\left(\\frac{c_{3}}{c_{3}+c\cdot C_{zscale}}\left(b\cdot C_{yscale}+c_{2}\\right)\\right)\n
    X_{x}\left(a,b,c\\right)=\ X_{y}\left(a,b\cos\left(C_{xrot}\\right)-c\sin\left(C_{xrot}\\right),b\sin\left(C_{xrot}\\right)+c\cos\left(C_{xrot}\\right)\\right)\n
    Y_{x}\left(a,b,c\\right)=\ Y_{y}\left(a,b\cos\left(C_{xrot}\\right)-c\sin\left(C_{xrot}\\right),b\sin\left(C_{xrot}\\right)+c\cos\left(C_{xrot}\\right)\\right)\n
    X_{y}\left(a,b,c\\right)=\ X_{z}\left(a\cos\left(C_{yrot}\\right)+c\sin\left(C_{yrot}\\right),b,-a\sin\left(C_{yrot}\\right)+c\cos\left(C_{yrot}\\right)\\right)\n
    Y_{y}\left(a,b,c\\right)=\ Y_{z}\left(a\cos\left(C_{yrot}\\right)+c\sin\left(C_{yrot}\\right),b,-a\sin\left(C_{yrot}\\right)+c\cos\left(C_{yrot}\\right)\\right)\n
    X_{z}\ \left(a,b,c\\right)=\ X\left(a\cos\left(C_{zrot}\\right)-b\sin\left(C_{zrot}\\right),a\sin\left(C_{zrot}\\right)+b\cos\left(C_{zrot}\\right),c\\right)\n
    Y_{z}\ \left(a,b,c\\right)=\ Y\left(a\cos\left(C_{zrot}\\right)-b\sin\left(C_{zrot}\\right),a\sin\left(C_{zrot}\\right)+b\cos\left(C_{zrot}\\right),c\\right)\n
    """
    cmd = cmd + GenerateAlias("3")+"\n"
    cmd = cmd + GenerateAlias("4")+"\n"
    cmd = cmd + GenerateAlias("6")+"\n"
    cmd = cmd + GenerateAlias("12")+"\n"
    cmd = cmd + GenerateAlias("16")+"\n"
    cmd = cmd + GenerateAlias("32")+"\n"
    f = open("Output/command_customrender_environment_2d.txt","w+")
    f.write(cmd)
    f.close()
    ToClipboard(cmd,root)
def Convert2D(vertex,face,rt,decimalrounding,name):
    faces = []
    for i in range(len(face)):
        #print(f"Face {i+1}:")
        key = face[i].split(" ")
        curr = []
        
        for i2 in range(len(key)-1):
            index =key[i2+1].split("/")
            
            selv = vertex[int(index[0])-1]
            curr.append(selv)
        faces.append(ToFace(curr,decimalrounding))
    
    cmd = "["
    for i in range(len(faces)-1):
        cmd = cmd + faces[i]+","
    cmd = cmd + faces[len(faces)-1]
    cmd = cmd + "]"
    #print(cmd) 
    ToClipboard(cmd,rt)
    f=open("Output/command_"+name+".txt","w")
    f.write(cmd)
    f.close()
    MSGClipboard(name)
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
                ToClipboard(cmd,rt)
def Convert3D(vertex,face,standalone,rt,decimalrounding):
    faces = []
    for i in range(len(face)):
        #print(f"Face {i+1}:")
        key = face[i].split(" ")
        curr = []
        
        for i2 in range(len(key)-1):
            index =key[i2+1].split("/")
            
            selv = vertex[int(index[0])-1]
            curr.append(selv)
        faces.append(ToPolygon3D(curr,decimalrounding))
    #print(faces)
    MSGDebug()
    #ToClipboard(faces)
    return
    cmd = "["
    for i in range(len(faces)-1):
        cmd = cmd + faces[i]+","
    cmd = cmd + faces[len(faces)-1]
    cmd = cmd + "]"
    #print(cmd) 
    ToClipboard(cmd,rt)
    f=open("Output/command_"+nameobj.get()+".txt","w")
    f.write(cmd)
    f.close()
    MSGClipboard()    
def GenerateAlias(integer):
    
    cmd = "F_{"+integer+"}"
    cmd = cmd + "(a,b,c,d)=\\operatorname{polygon}("
    for i in range(int(integer)):
        cmd = cmd + "(X_{x}(a["+str(i+1)+"],b["+str(i+1)+"],c["+str(i+1)+"]),Y_{x}(a["+str(i+1)+"],b["+str(i+1)+"],c["+str(i+1)+"])),"
    cmd = cmd + "removethis"
    cmd = cmd.replace(",removethis","")
    cmd = cmd + ")"
    cmd = cmd.replace(")","\\right)")
    cmd = cmd.replace("(","\\left(")
    cmd = cmd.replace("[","\\left[")
    cmd = cmd.replace("]","\\right]")
    #print(cmd)
    return cmd
def ToFace(facevertex,decimalrounding):
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
def ToPolygon3D(vertex,decimalrounding):
    
    
    
    curr = []
    if(len(vertex))==4:
        
        for i in range(4-2):
            cmd = ""
            cmd = cmd + "triangle\\left(\\left("+vertex[0].split()[1]+","+vertex[0].split()[2]+","+vertex[0].split()[3]+"\\\right),"
            cmd = cmd + "\\left("+vertex[i+1].split()[1]+","+vertex[i+1].split()[2]+","+vertex[i+1].split()[3]+"\\\right),"
            cmd = cmd + "\\left("+vertex[i+2].split()[1]+","+vertex[i+2].split()[2]+","+vertex[i+2].split()[3]+"\\\right)\\\right)"
            cmd = cmd + "\n"
            
            curr.append(cmd)
    return curr
def ToClipboard(string,root):
    root.clipboard_clear()
    root.clipboard_append(string)
    root.update()
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
            pass
            #print("I AM PROBABLY STUPID")
            #print(c)
            #print(cam)
#MessageFeedBack
def MSGFileError():
    yn = tk.messagebox.showerror("File not found error","File not found")
    return yn
def MSGClipboard(name):
    if DisableCopyToClipboard==True:
        return
    yn = tk.messagebox.showinfo("Copied!","Copied Command to Clipboard\nCommand availiable in command_"+name+".txt")
    return yn
def MSGStandalone():
    yn = tk.messagebox.askyesno("3D Option","Do you want to generate the object as a standalone object (can be pasted into any project). Clicking No will generate it for designated project")
    return yn
def MSGAliasError(desc):

    yn2 = tk.messagebox.askyesno("Generate Vertex-Face Alias", f"""Your Object has faces with unsupported default vertex count.
                                \n Do you want to generate a Alias to support your object.
                                \n Face-Vertex Count Missing:{desc}""")
    return yn2
def MSGAliasCreated():

    yn = tk.messagebox.askyesno("Alias Created Sucessfully","Do you want to copy to clipboard. \n Alias still retrievable in file command_"+nameobj.get()+"_aliasfix.txt")
    return yn
def MSGDebug():

    yn = tk.messagebox.showerror("Disabled","This Feature is Disabled! Complain to the developer to hurry up and add it! :(")
    return yn
def MSGWebsiteOpener():
    yn = tk.messagebox.askyesno("Redirect","Do you want to open the 2D Renderer Desmos Project")
    if(yn):
        webbrowser.open('https://www.desmos.com/calculator/hqkrjcobkk')  # Go to example.com
#On Startup Settings Applier

if(words[0].split(":")[1]=="1"):
    MSGWebsiteOpener()

if(words[1].split(":")[1]=="1"):
    DisableCopyToClipboard = True
#print(words)