class Process:
    def scan(state):
        import os
        cwd = os.path.dirname(os.path.abspath(__file__))
        os.chdir(cwd)
        os.chdir("..")
        os.chdir("..")
        crafts_exist = os.path.exists("Aircraft")
        loc_exist = os.path.exists("Locations")
        if crafts_exist == True:
            Avail_Crafts = os.listdir("Aircraft")
        else:
            Avail_Crafts = [""]
        if loc_exist == True:
            Avail_Loc = os.listdir("Locations")
        else:
            Avail_Loc = [""]
        if state != "quiet":
            print("Available Aircraft")
        for c in Avail_Crafts:
            ispy = c.endswith(".py")
            iscft = c.endswith(".cft")
            if ispy == True:
                c = c.replace(".py","")
            if iscft == True:
                c = c.replace(".cft","")
            if state != "quiet":
                print(c)
        if state != "quiet":
            print("Available locations")
        for l in Avail_Loc:
            ispy = l.endswith(".py")
            isloc = l.endswith(".loc")
            if ispy == True:
                l = l.replace(".py","")
            if isloc == True:
                l = l.replace(".loc","")
            if state != "quiet":
                print(l)
    def Move(cft,loc):
        import os
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        os.chdir("..")
        aircraft_content = os.listdir("Aircraft")
        location_content = os.listdir("Locations")
        os.chdir("Aircraft")
        for craft in aircraft_content:
            if cft in craft:
                targetc_path = os.path.abspath(craft)
                movec = open(targetc_path,"r")
                movecon = movec.read()
                break
        os.chdir("..")
        os.chdir("Loaded")
        placec = open("TargetAircraft.py","w")
        placec.write(movecon)
        os.chdir("..")
        for location in location_content:
            if location in loc:
                targetl_path = os.path.abspath(loc)
                movel = open(targetl_path,"r")
                global moveconl
                moveconl = movel.read()
                break
        os.chdir("Loaded")
        placel = open("TargetLocation.py","w")
        placel.write(moveconl)
