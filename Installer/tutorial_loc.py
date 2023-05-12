def KORD():
    import os
    os.chdir("Installer")
    os.chdir("Tanks")
    CORD_content_open = open("KORD.txt","r")
    CORD_content = CORD_content_open.read()
    os.chdir("..")
    os.chdir("..")
    write = open("Locations/KORD.py","w")
    write.write(CORD_content)
def KLAX():
    import os
    os.chdir("Installer")
    os.chdir("Tanks")
    CORD_content_open = open("KLAX.txt","r")
    CORD_content = CORD_content_open.read()
    os.chdir("..")
    os.chdir("..")
    write = open("Locations/KLAX.py","w")
    write.write(CORD_content)
def blank():
    import os
    os.chdir("Installer")
    os.chdir("Tanks")
    blank_content_open = open("blank.txt","r")
    blank_content = blank_content_open.read()
    os.chdir("..")
    os.chdir("..")
    write = open("Locations/WHITESPACE.py","w")
    write.write(blank_content)