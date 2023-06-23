import time
import os
import shutil

folder = input("Path: ")
days = 30
timeInSeconds = 0
isexist = bool(False)

currentTime = time.time()

timeInSeconds = days * 24 * 60 * 60

print(os.path.exists(folder))

#Changing cwd to the folder specified
os.chdir(os.path.join(os.getcwd(),folder))
listOfFiles = os.listdir() 

listOfFiles1 = os.walk(folder)
for path, subdirs, files in os.walk(folder):
    for name in files:
        fileLocation = os.path.join(path,name)
       
        # take modified time for each file and compare with current time
        fileTime = int(os.stat(fileLocation).st_mtime)
        #File modified before days and then delete it
       
        diff = int(currentTime - timeInSeconds)
        if (fileTime < currentTime - timeInSeconds):
           
            print("delete: ", name)
            if os.path.isfile(fileLocation):
                os.remove(fileLocation) 
            # if it is a folder then delete it using shutil.rmtree(fileLocation)
            elif os.pathisdir(fileLocation):
                shutil.rmtree(fileLocation)
            
