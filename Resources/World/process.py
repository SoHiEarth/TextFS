import os

class Process:
    @staticmethod
    def scan(state):
        cwd = os.path.dirname(os.path.abspath(__file__))
        os.chdir(cwd)
        os.chdir("..")
        os.chdir("..")
        crafts_exist = os.path.exists("Aircraft")
        loc_exist = os.path.exists("Locations")
        if crafts_exist:
            Avail_Crafts = os.listdir("Aircraft")
        else:
            Avail_Crafts = [""]
        if loc_exist:
            Avail_Loc = os.listdir("Locations")
        else:
            Avail_Loc = [""]
        if state != "quiet":
            print("Available Aircraft")
        for c in Avail_Crafts:
            ispy = c.endswith(".py")
            iscft = c.endswith(".cft")
            if ispy:
                c = c.replace(".py", "")
            if iscft:
                c = c.replace(".cft", "")
            if state != "quiet":
                print(c)
        if state != "quiet":
            print("Available locations")
        for l in Avail_Loc:
            ispy = l.endswith(".py")
            isloc = l.endswith(".loc")
            if ispy:
                l = l.replace(".py", "")
            if isloc:
                l = l.replace(".loc", "")
            if state != "quiet":
                print(l)
    
    @staticmethod
    def Move(cft, loc):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        os.chdir("..")
        aircraft_content = os.listdir("Aircraft")
        os.chdir("Aircraft")
        for craft in aircraft_content:
            if cft in craft:
                targetc_path = os.path.abspath(craft)
                movec = open(targetc_path, "r")
                moveccon = movec.read()
                movec.close()
                break
        os.chdir("..")
        os.chdir("Loaded")
        placec = open("TargetAircraft.py", "w")
        placec.write(moveccon)
        placec.close()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        os.chdir("..")
        location_content = os.listdir("Locations")
        os.chdir("Locations")
        for location in location_content:
            if loc in location:
                targetl_path = os.path.abspath(location)
                movel = open(targetl_path, "r")
                movelcon = movel.read()
                movel.close()
                break
        os.chdir("..")
        os.chdir("Loaded")
        placec = open("TargetLocation.py", "w")
        placec.write(movelcon)
        placec.close()
