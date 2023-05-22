class tskmgr:
    
    def start():
        import os
        from Resources.setting import DebugMode
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        os.chdir("..")
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
        FSsize = os.path.getsize("TextFS-Nightly")
 
    def refresh():
        import os
        from Resources.setting import DebugMode
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        os.chdir("..")
        mainsize = os.path.getsize("main.py")
        temp_exists = os.path.exists("Temp")
        temp_exists = 0
        if temp_exists == True:
            tempsize = os.path.getsize("Temp")
        loaded_exists = os.path.exists("Loaded")
        if loaded_exists == True:
            loadedsize = os.path.getsize("Loaded")
        os.chdir("..")
        FSsize = os.path.getsize("TextFS-Nightly")
        if loadedsize > 500000000:
            print("WARNING: LOADED ASSETS ARE OVER 5GB.")

    def display(state="Normal"):
        import os
        from Resources.setting import DebugMode
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        os.chdir("..")
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
        FSsize = os.path.getsize("TextFS-Nightly")
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