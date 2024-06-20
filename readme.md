HOW TO USE SOFTWARE:
  This code is currently in Beta stage, the raw code is not compiled and requires python plus a few modules listed below:
  -Math Module
  -Tkinter Module
  -Python 3+
  Running Desmos3DConverter.py will have a gui which has a few boxes:
  Name of Object (This will appear inside Desmos)
  Filename of .obj file (This is not path dependant, enter "TestObj/cube.obj" or enter "C:\...../cube.obj")
  Rounding To (This reduces the amount of decimal places in floating point numbers. This can reduce lag or character count)

  Convert to 2D Button:
    Will convert the object into a string that is copied to clipboard,
    command is retreivable in command_"Name of Object".txt
    
    If you obj has an unsupported face vertex count a dialogue will appear.
    Clicking yes will fix this error. You have two choices afterwards:
    -Yes, this will copy the fix command to clipboard, erasing the shape command.
    -No, this will not copy it and keep the shape command.
    
    Clicking No will still keep the fix command in comand_"name"_aliasfix.txt
    Paste the shape command into link: (https://www.desmos.com/calculator/hqkrjcobkk)
    Paste the fix command (if needed) into a folder for easier use.
  
  Convert to 3D Button:
    Currently Disabled!
  
