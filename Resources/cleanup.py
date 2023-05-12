def Cleanup(type):
    import os
    import shutil
    from Installer.restore import Restore
    from Resources.setting import DebugMode
    if type == "Partial":
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        temp_exists = os.path.exists("Temp")
        load_exists = os.path.exists("Load")
        if temp_exists == True:
            shutil.rmtree("Temp")
        if load_exists == True:
            shutil.rmtree("Loaded")
    else:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        temp_exists = os.path.exists("Temp")
        load_exists = os.path.exists("Loaded")
        if temp_exists == True:
            shutil.rmtree("Temp")
        if load_exists == True:
            shutil.rmtree("Loaded")
        os.chdir("Resources")
        cache_exists = os.path.exists("__pycache__")
        if cache_exists == True:
            shutil.rmtree("__pycache__")
        os.chdir("..")
        os.chdir("Installer")
        cache_exists = os.path.exists("__pycache__")
        if cache_exists == True:
            shutil.rmtree("__pycache__")
        os.chdir("..")
        cache_exists = os.path.exists("__pycache__")
        if cache_exists == True:
            shutil.rmtree("__pycache__")
    print("Cleanup complete.")
    if DebugMode == 1:
        tot = 0
        logs_exist = os.path.exists("Logs")
        if logs_exist == True:
            shutil.rmtree("Logs")
        aircraft_exist = os.path.exists("Aircraft")
        if aircraft_exist == True:
            crafts = os.listdir("Aircraft")
            for c in crafts:
                tot = tot + 1
            print("There are "+str(tot)+" aircraft in your /Aircraft/ folder. Wipe them? [\"Y\",\"N\"]")
            cwipe = input("")
            if cwipe == "Y":
                shutil.rmtree("Aircraft")
        loc_exist = os.path.exists("Locations")
        if loc_exist == True:
            locations = os.listdir("Locations")
            tot = 0
            for l in locations:
                tot = tot+1
            print("There are "+str(tot)+" locations in your /Locations/ folder. Wipe them? [\"Y\",\"N\"]")
            lwipe = input("")
            if lwipe == "Y":
                shutil.rmtree("Locations")
        os.chdir("Resources")
        Restore.Restore_Boot(0)