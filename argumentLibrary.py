commandList = ["--diskmgr:DUMP"]
argsList = ["--diskmgr:DISPLAY","--diskmgr:REFRESH"]
class Dump:
    def diskmgrDump():
        import os
        import datetime
        from Resources.log import Log
        Log("Started diskmgr dump")
        dumpLogs = 0
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
        dumpLogs = mainSize + resourcesSize + installerSize + tempSize + loadedSize
        os.chdir("Logs")
        dumpStat = open("diskDump.txt","a")
        dumpStat.write("Time of dump: "+str(datetime.datetime.now()))
        dumpStat.write("\nTotal disk usage: "+str(dumpLogs))
        Log("Total disk usage: "+str(dumpLogs))
        dumpStat.write("\nmain.py usage: "+str(mainSize))
        Log("main.py usage: "+str(mainSize))
        dumpStat.write("\nSize of resources: "+str(resourcesSize))
        Log("Size of resources: "+str(resourcesSize))
        dumpStat.write("\nSize of installer: "+str(installerSize))
        Log("Size of installer: "+str(installerSize))
        dumpStat.write("\nTemp usage: "+str(tempSize))
        Log("Temp usage: "+str(tempSize))
        dumpStat.write("\nSize of loaded assets: "+str(loadedSize))
        Log("Size of loaded assets: "+str(loadedSize))
        dumpStat.write("\nSize of __pycache__: "+str(cacheSize))
        Log("Size of __pycache__:"+str(cacheSize))
        Log("Ended diskmgr dump")
def findArg(consoleInput):
    args = [""]
    while consoleInput != "exit":
        if consoleInput == "/exit":
            return args
        if consoleInput in commandList:
            # Recognize active commands
            if consoleInput == "--diskmgr:DUMP":
                Dump.diskmgrDump()
        if consoleInput in argsList:
            # Recognize scheduled arguments
            args.append(consoleInput)
        consoleInput = input("Console | ")