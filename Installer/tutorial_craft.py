def b738():
    import os
    os.chdir("Installer")
    os.chdir("Tanks")
    b738_content_open = open("B738.txt","r")
    b738_content = b738_content_open.read()
    os.chdir("..")
    os.chdir("..")
    write = open("Aircraft/B738.py","w")
    write.write(b738_content)
def b773er():
    import os
    os.chdir("Installer")
    os.chdir("Tanks")
    b77w_content_open = open("B77w.txt","r")
    b77w_content = b77w_content_open.read()
    os.chdir("..")
    os.chdir("..")
    write = open("Aircraft/B77W.py","w")
    write.write(b77w_content)