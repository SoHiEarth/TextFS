class tskmgr:
    mainsize = 0
    FSsize = 0
    
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
        FSsize = os.path.getsize("TextFS")
 
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
        loadedsize = 0
        if loaded_exists == True:
            loadedsize = os.path.getsize("Loaded")
        os.chdir("..")
        FSsize = os.path.getsize("TextFS")
 
    def display(state):
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
        FSsize = os.path.getsize("TextFS")
        print("Disk Usage:")
        print("Main.py usage: " + str(mainsize))
        if state == "init":
            print("Flight Simulator usage (Before load):", str(FSsize))
        else:
            print("Flight Simulator usage:",str(FSsize))
        print("Temp directory size: "+ str(tempsize))
        print("Loaded assets size: "+ str(loadedsize))