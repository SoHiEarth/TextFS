# DONT FORGET TO ADD THE COMMAND TO HERE
commandList = ["--diskmgr:DUMP",
               "--about:VERSION","--about:CHANNEL","--about:NAME","--about:CHANGELOG",
               "list:LOGS","list:CMD"]
argsList = ["--diskmgr:DISPLAY","--diskmgr:REFRESH"]
# Functions {
class Program:
    def Version():
        from Resources.about import Program_Info
        print("SysMess | Version: "+Program_Info.version)
    def Channel():
        from Resources.about import Program_Info
        print("SysMess | Channel: "+Program_Info.channel)
    def Name():
        from Resources.about import Program_Info
        print("SysMess | Program Name: "+Program_Info.name)
    def Changelog():
        from Resources.about import Program_Info
        print("SysMess | Current Version: "+Program_Info.pdesc)
        for change in Program_Info.changelog:
            print("        | "+change)
    def listCommands():
        for item in commandList:
            print("        | "+item)
        for item in argsList:
            print("        | "+item)
class Dump:
    def LogsDump():
        import os
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        logs_exist = os.path.exists("Logs")
        if logs_exist == False:
            print("SysMess | Error: No Logs")
            return 404
        os.chdir("Logs")
        txt = open("Log.txt","r")
        content = txt.readlines()
        for line in content:
            line.replace("\n","")
            print("LogsOut | "+line)
        return 0
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
class Clean:
    def ForceClean():
        import os
        import shutil
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        pycacheExists = os.path.exists("__pycache__")
        logsExists = os.path.exists("Logs")
        tempExists = os.path.exists("Temp")
        craftExists = os.path.exists("Aircraft")
        locationsExists = os.path.exists("Locations")
        if pycacheExists == True:
            shutil.rmtree("__pycache__")
        if logsExists == True:
            shutil.rmtree("Logs")
        if tempExists == True:
            shutil.rmtree("Temp")
        if craftExists == True:
            shutil.rmtree("Aircraft")
        if locationsExists == True:
            shutil.rmtree("Locations")
# }
def findArg(consoleInput):
    args = [""]
    while consoleInput != "exit":
        if consoleInput == "/exit":
            return args
        if consoleInput in commandList:
            # Recognize active commands, append to here {
            if consoleInput == "list:CMD":
                Program.listCommands()
            if consoleInput == "list:LOGS":
                Dump.LogsDump()
            if consoleInput == "--about:VERSION":
                Program.Version()
            if consoleInput == "--about:CHANNEL":
                Program.Channel()
            if consoleInput == "--about:NAME":
                Program.Name()
            if consoleInput == "--about:CHANGELOG":
                Program.Changelog()
            if consoleInput == "--diskmgr:DUMP":
                Dump.diskmgrDump()
            # }
        if consoleInput in argsList:
            # Recognize scheduled arguments
            args.append(consoleInput)
        consoleInput = input("Console | ")