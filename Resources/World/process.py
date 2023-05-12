class Process:
    def scan():
        import os
        cwd = os.path.dirname(os.path.abspath(__file__))
        os.chdir(cwd)
        os.chdir("..")
        os.chdir("..")
        Avail_Crafts = os.listdir("Aircraft")
        Avail_Loc = os.listdir("Locations")
        print("Available Aircraft")
        for c in Avail_Crafts:
            ispy = c.endswith(".py")
            iscft = c.endswith(".cft")
            if ispy == True:
                c = c.replace(".py","")
            if iscft == True:
                c = c.replace(".cft","")
            print(c)
        print("Available locations")
        for l in Avail_Loc:
            ispy = l.endswith(".py")
            isloc = l.endswith(".loc")
            if ispy == True:
                l = l.replace(".py","")
            if isloc == True:
                l = l.replace(".loc","")
            print(l)