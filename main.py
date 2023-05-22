
# Import Modules.

from virt import virt
from Resources.about import Program_Info
from Installer.restore import Restore
from Resources.Boot import Opened
if ImportError == True:
    Restore.Restore_Boot(0)
    from Resources.Boot import Opened
from Resources.ec import ec
from Resources.cleanup import Cleanup
from Resources.setting import SafeMode
from Resources.setting import DebugMode

# Partial cleanup to remove unwanted files.

Cleanup("Partial")

modulename = "time"
import time
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

modulename = "sys"
import sys
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

modulename = "os"
import os
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

modulename = "shutil"
import shutil
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

modulename = "platform"
import platform
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

modulename = "datetime"
import datetime
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

modulename = "time"
import time
if ImportError == True:
    print("Failed to import module:",modulename)
    print("Bye!")

# Present version Info

print(Program_Info.name)
if Program_Info.channel == "Beta" or "Nightly":
    print("This is a installation of "+Program_Info.channel+"!")
    print("Debug mode will be on by default.")
    DebugMode = 1
print("Version "+Program_Info.version)
print("What's new:\n"+Program_Info.pdesc)
print("Changelog:\n")
rpt = 0
for c in Program_Info.changelog:
    if c == "Done":
       print("Done.")
    else:
        print(c+"\n")
    rpt = rpt+1
    if rpt == 5:
        print("...")
        break
rpt = 0

# Check if program is runnning. (Only in Safe Mode.)

if SafeMode == 1:
    STEP = "init"
    INIT_PROOF = 1
    if INIT_PROOF != 1:
        print("Error at step init. Code:",ec.init.initc,"Desc:",ec.init.inite)
        print("This is a critical error. Maybe you have broken installations?")
        waitloop = 0
        while waitloop != 5:
            if waitloop == 5:
                sys.exit(2)
            remaining = 5 - waitloop
            print("Exiting in "+ str(remaining) +"...")
            waitloop = waitloop + 1
            time.sleep(1)

# Check if the Aircraft dir and Locations dir exist.
# If not, make it.

os.chdir(os.path.dirname(os.path.abspath(__file__)))
craft_exists = os.path.exists("Aircraft")
loc_exists = os.path.exists("Locations")
if craft_exists == False:
    os.mkdir("Aircraft")
if loc_exists == False:
    os.mkdir("Locations")

# See if this program was opened before.

if Opened == 0:
    Restore.Restore_Boot(1)
elif Opened == 1:
    pass
else:
    Restore.Restore_Boot(1)

# Ask for tutorial setup, only if the program is on first startup.

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if Opened == 0:
    mktutorial = input("Do you want to install tutorials? [\"Y\",\"N\"]")
    if mktutorial == "Y":
        print("You can install from b738, b773er, and a A320. Choose wisely; you can only pick one!")
        select_aircraft = input()
        if select_aircraft == "b738":
            from Installer.tutorial_craft import b738
            b738()
        if select_aircraft == "b773er":
            from Installer.tutorial_craft import b773er
            b773er()
        else:
            pass
        print("You can get also get KLAX, KORD, and WHITESPACE.")
        select_location = input()
        if select_location == "KLAX":
            from Installer.tutorial_loc import KLAX
            KLAX()
            if FileNotFoundError == True:
                print("Failed to install "+select_location)
                Restore.Restore_Boot(0)
        if select_location == "KORD":
            from Installer.tutorial_loc import KORD
            KORD()
            if FileNotFoundError == True:
                print("Failed to install "+select_location)
                Restore.Restore_Boot(0)
        if select_location == "WHITESPACE":
            from Installer.tutorial_loc import blank
            blank()
            if FileNotFoundError == True:
                print("Failed to install "+select_location)
                Restore.Restore_Boot(0)
            else:
                pass

# Start main bootlevel

print("Initializing...")
startboot = time.time()
print("Starting main bootlevel")

# Start task manager

from Resources.tskmgr import tskmgr
tskmgr.start()
tskmgr.display("init")

# Scan aircraft and locations

from Resources.World.process import Process
Process.scan("quiet")

# Start second bootlevel

print("Starting second bootlevel")

# Create temp & loaded files

os.chdir(os.path.dirname(os.path.abspath(__file__)))
Temp_Exists = os.path.exists("Temp")
Loaded_Exists = os.path.exists("Loaded")
if Temp_Exists == False:
    os.mkdir("Temp")
if Loaded_Exists == False:
    os.mkdir("Loaded")
os.path.dirname(os.path.abspath(__file__))

# Accept debugmode

dbg = False
if DebugMode == 1:
    "Debug Mode is locked and loaded."
    dbg = True

# If debugmode is on, log.

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if DebugMode == True:
    log_exists = os.path.exists("Logs")
    if log_exists == False:
        os.mkdir("Logs")
    os.chdir("Logs")
    logboot = open("boot.log","a")
    crt_time = datetime.datetime.now()
    logboot.write(str(crt_time)+": Booted successfully.\n")
    print("Logged boot record to "+os.path.dirname(os.getcwd())+"/Logs")
    os.chdir("..")
        

# End boot

endboot = time.time()
elapsed = endboot - startboot
print("Took "+ str(elapsed) +" seconds to boot.")
print("Ended boot.")

# Define main loop


# List aircraft and locations
Process.scan("")

# Choose aircraft and location
# Move data to Loaded
from loadProcess import aircraftMove,locationMove
aircraftMove()

locationMove()

# Ask for world configuration
world_config = input("World configuration; (Blank or \"Auto\" is automatically set)")
if world_config == "" or " " or "Auto" or "auto":
    GravityStrength = 9.807
else:
    GravityStrength = input("Gravity Strength (m/s):")
    GravityStrength = int(GravityStrength)
    DragCoefficient = input("Drag coeffecient:")

# Start virtual world.
virt.Read()
virt.start()
virt.main(GravityStrength)

# Start cleaning up and begin shutdown.

Cleanup("")


# Shutdown

print("Bye!")