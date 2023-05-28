# DONT FORGET TO ADD THE COMMAND TO HERE
commandList = ["--diskmgr:DUMP",
               "--about:VERSION","--about:CHANNEL","--about:NAME","--about:CHANGELOG","--about:SYSTEM",
               "list:LOGS","list:CMD",
               "--clean:AIRCRAFT","--clean:LOCATIONS","--clean:TEMP","--clean:LOADED",
               "--shutdown:SOFT","--shutdown:FORCE","/exit"]
argsList = ["--diskmgr:DISPLAY","--diskmgr:REFRESH","--fps:HIDE","--fps:SHOW","--fps:THROTTLE","--onetime:TRUE","--onetime:FALSE"]
# Functions {
class Program:
    def SystemInfo():
        import platform
        print("SysMess | Platform: "+platform.system())
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
            print("SysMess | "+change)
    def listCommands():
        for item in commandList:
            print("SysMess | "+item)
        for item in argsList:
            print("SysMess | "+item)
    def forceAbort():
        print("SysMess | Force-stopping program...")
        from Resources.log import Log
        Log("Force-Stopped Program using console command --shutdown:FORCE")
        import sys
        sys.exit(7)
    def softAbort():
        import os
        import sys
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        from Resources.cleanup import Cleanup
        Cleanup("ConsoleCMD")
        sys.exit(5)
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
    def aircraftWipe():
        import os
        import shutil
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        craftExists = os.path.exists("Aircraft")
        if craftExists == True:
            shutil.rmtree("Aircraft")
        if craftExists == False:
            print("        | /Aircraft folder doesn't exist")
    def loadedWipe():
        import os
        import shutil
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        loadedExists = os.path.exists("Loaded")
        if loadedExists == True:
            shutil.rmtree("Loaded")
        if loadedExists == False:
            print("        | /Loaded doesn't exist")
    def locationWipe():
        import os
        import shutil
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        locExists = os.path.exists("Locations")
        if locExists == True:
            shutil.rmtree("Locations")
        if locExists == False:
            print("        | /Locations folder doesn't exist")
    def tempWipe():
        import os
        import shutil
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        craftExists = os.path.exists("Temp")
        if craftExists == True:
            shutil.rmtree("Temp")
        if craftExists == False:
            print("        | /Temp folder doesn't exist")
    def forceClean():
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
class FPS:
    def Throttle():
        import os
        throttleValue = input("FPSWait | Input target throttle value:\n        | ")
        throttleValue = int(throttleValue)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("Temp")
        if FileNotFoundError == True:
            print("SysMess | /Temp not found.")
            os.mkdir("Temp")
            os.chdir("Temp")
        writeTemp = open("throttleCtrl.temp","w")
        writeTemp.write(str(throttleValue))
        writeTemp.close()
        return throttleValue
# }
def findArg(consoleInput):
    args = [""]
    while consoleInput != "exit":
        if consoleInput == "/exit":
            # Add or save before closing {
            import os
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            os.chdir("Temp")
            if FileNotFoundError == True:
                print("SysMess | Temp not found.")
                os.mkdir("Temp")
                os.chdir("Temp")
            throttleCtrl_exists = os.path.exists("throttleCtrl.temp")
            if throttleCtrl_exists == False:
                writeTemp = open("throttleCtrl.temp","w")
                writeTemp.write("60")
                writeTemp.close()
            # }
            return args
        if consoleInput in commandList:
            # Recognize active commands, append to here {
                # Base level program commands {
            if consoleInput == "list:CMD":
                Program.listCommands()
            if consoleInput == "list:LOGS":
                Dump.LogsDump()
            if consoleInput == "--about:SYSTEM":
                Program.SystemInfo()
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
            if consoleInput == "--clean:FORCE":
                Clean.forceClean()
            if consoleInput == "--clean:AIRCRAFT":
                Clean.aircraftWipe()
            if consoleInput == "--clean:LOCATIONS":
                Clean.locationWipe()
            if consoleInput == "--clean:LOADED":
                Clean.loadedWipe()
            if consoleInput == "--clean:TEMP":
                Clean.tempWipe()
            if consoleInput == "--shutdown:FORCE":
                Program.forceAbort()
            if consoleInput == "--shutdown:":
                Program.softAbort()
                # }
            # }
        if consoleInput in argsList:
            # Recognize scheduled arguments {
                # Base level program commands {
            if consoleInput == "--fps:THROTTLE":
                args.append("--fps:THROTTLE:"+str(FPS.Throttle()))
            if consoleInput == "--fps:SHOW":
                if "--fps:HIDE" in args:
                    args = list(map(lambda obj: obj.replace("--fps:HIDE",""), args))
            if consoleInput == "--fps:HIDE":
                if "--fps:SHOW" in args:
                    args = list(map(lambda obj: obj.replace("--fps:SHOW", ""), args))
            if consoleInput == "--onetime:TRUE":
                if "--onetime:FALSE":
                    args = list(map(lambda obj: obj.replace("--onetime:FALSE", ""), args))
            if consoleInput == "--onetime:FALSE":
                if "--onetime:TRUE":
                    args = list(map(lambda obj: obj.replace("--onetime:TRUE", ""), args))
            args.append(consoleInput)
                # }
            # }
        consoleInput = input("Console | ")