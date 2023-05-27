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
        if loaded_exists == True:
            loadedsize = os.path.getsize("Loaded")
        os.chdir("..")
        FSsize = os.path.getsize("TextFS")
        if loadedsize > 500000000:
            print("WARNING: LOADED ASSETS ARE OVER 5GB.")
        all = mainsize + tempsize + FSsize
        return all

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
    def Dump():
        import os
        import datetime
        from log import Log
        Log("Started diskmgr dump")
        dumpLogs = 0
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        logsExist = os.path.exists("Logs")
        if logsExist == False:
            os.mkdir("Logs")
        dumpLogs =+ logsSize
        os.chdir("Logs")
        dumpStat = open("diskDump.txt","a")
        os.chdir("..")
        mainsize = os.path.getsize("main.py")
        dumpLogs =+ mainsize
        temp_exists = os.path.exists("Temp")
        if temp_exists == True:
            tempsize = os.path.getsize("Temp")
            dumpLogs =+ tempsize
        loaded_exists = os.path.exists("Loaded")
        if loaded_exists == True:
            loadedsize = os.path.getsize("Loaded")
            dumpLogs =+ loadedsize
        os.chdir("..")
        FSsize = os.path.getsize("TextFS")
        os.chdir("TextFS")
        dumpLogs =+ FSsize
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        logsSize = os.path.getsize("Logs")
        dumpLogs =+ logsSize
        os.chdir("Logs")
        dumpStat = open("diskDump.txt","a")
        dumpStat.write("\nTime of dump: "+str(datetime.datetime.now()))
        dumpStat.write("\nTotal disk usage: "+str(dumpLogs))
        dumpStat.write("\nmain.py usage: "+str(mainsize))
        dumpStat.write("\nTemp usage: "+str(tempsize))
        dumpStat.write("\nSize of loaded assets: "+str(loadedsize))
        dumpStat.write("\nEnded dump.")
        Log("Ended diskmgr dump")