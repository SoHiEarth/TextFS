class diskmgr:
    def start():
        import os
        from Resources.setting import DebugMode
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        mainsize = os.path.getsize("main.py")
        temp_exists = os.path.exists("Temp")
        temp_exists = 0
        if temp_exists == True:
            tempsize = os.path.getsize("Temp")
        loaded_exists = os.path.exists("Loaded")
        loadedsize = 0
        if loaded_exists == True:
            loadedsize = os.path.getsize("Loaded")
        os.chdir("..")
        FSsize = os.path.getsize("TextFS")
 
    def refresh():
        import os
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        mainSize = os.path.getsize("main.py")
        resourcesSize = os.path.getsize("Resources")
        installerSize = os.path.getsize("Installer")
        tempSize = 0
        temp_exists = os.path.exists("Temp")
        if temp_exists == True:
            tempSize = os.path.getsize("Temp")
        loadedSize = 0
        loaded_exists = os.path.exists("Loaded")
        if loaded_exists == True:
            loadedSize = os.path.getsize("Loaded")
        cacheSize = 0
        cache_exists = os.path.getsize("__pycache__")
        if cache_exists == True:
            cacheSize = os.path.getsize("__pycache__")
        all = mainSize + resourcesSize + installerSize + tempSize + loadedSize
        return all

    def display(state="Normal"):
        import os
        from Resources.setting import DebugMode
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        mainsize = os.path.getsize("main.py")
        temp_exists = os.path.exists("Temp")
        tempsize = 0
        if temp_exists == True:
            tempsize = os.path.getsize("Temp")
        loaded_exists = os.path.exists("Loaded")
        loadedsize = 0
        if loaded_exists == True:
            loadedsize = os.path.getsize("Loaded")
        os.chdir("..")
        FSsize = os.path.getsize("TextFS")
        print("Disk Usage:")
        if state == "init":
            print("Flight Simulator usage (Before load):", str(FSsize))
            print("Main.py usage: " + str(mainsize))
        if state == "Normal":
            print("Flight Simulator usage:",str(FSsize))
            if DebugMode == True:
                print("Temp directory size: "+ str(tempsize))
                print("Loaded assets size: "+ str(loadedsize))
        if state == "ingame":
            print("Flight Simulator usage",str(FSsize))
            print("Main.py usage: " + str(mainsize))
            if DebugMode == True:
                print("Temp directory size: "+ str(tempsize))
                print("Loaded assets size: "+ str(loadedsize))