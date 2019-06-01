import os.path

#Checks to see if the path build is available 

def folderCreate():
    if os.path.exists("./build"):
        print("Build Folder Available")
    else:
        print("N/A")
        print("Creating builder folder...")
        os.mkdir("./build")
        print("finished")
def download():
    os.chdir("./build")
    if os.path.dirname("./build"):
        print("True")
        os.mkdir("./test")
    else:
        print("False")

download()
