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