from Console.functions import Program
from Console.functions import Dump
from Console.functions import Clean
from Console.functions import FPS
from Console.Customizeable.commandLists import commandList
from Console.Customizeable.argsLists import argsList
def findArg(consoleInput):
    args = [""]
    while consoleInput != "exit":
        if consoleInput == "exit": 
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
        else:
            print("Message | Command \""+consoleInput+"\" not found.")
        consoleInput = input("Console | ")