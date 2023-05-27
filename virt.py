class virt:
    # File output func. Just for the convenience.
    def fileOut(posX,posY,posZ,rotX,rotY,rotZ,aspd,gspd,enginePower,vertSpd,last=False):
        import os
        # Declare write data as a single variable
        outputData = "PositionX = "+posX+"\nPositionY = "+posY+"\nPositionZ = "+posZ+"\nRotationX = "+rotX+"\nRotationY = "+rotY+"\nRotationZ = "+rotZ+"\nAirspeed = "+aspd+"\nGroundspeed = "+gspd+"\nThrottle = "+enginePower+"\nVerticalSpeed = "+enginePower
        # Change cwd
        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        os.chdir("..")
        direCheck = os.path.exists("Output")
        if direCheck == False:
            os.mkdir("Output")
        os.chdir("Output")
        # Write to file
        outFile = open("Output.py","w")
        outFile.write(outputData)
        if last == True:
            outFile.close()

# Start function

    def start():
        import os
        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        os.chdir("..")
        print("Loading assets")
        loaded_exists = os.path.exists("Loaded")
        if loaded_exists == True:
            pass
        else:
            print("Loaded assets are missing. Try again.")

# Main game loop

    def main(args,fps = 60,Repeat = True):
        import time
        from PhysicsLibrary import FPSCounter
        from PhysicsLibrary import World
        from Resources.tskmgr import tskmgr
        while Repeat == True:
            try:
                startframe = time.time()
                print(World.Position(0,0,0,100,0,0,0))
                # Add code from here...
                if "--tskmgr:DISPLAY" in args:
                    tskmgr.display()
                if "--tskmgr:REFRESH" in args:
                    tskmgr.refresh()
                # To here as main game exec. code
                
                endframe = time.time()
                FPSCounter.FPSCount(startframe,endframe,fps)
            except KeyboardInterrupt:
                print()
                print("Stopping...")
                break
        if Repeat == False:
            try:
                startframe = time.time()
                print(World.Position(0,0,0,100,0,0,0))
                endframe = time.time()
                FPSCounter.FPSCount(startframe,endframe)
            except KeyboardInterrupt:
                print()
                print("Stopping...")

    class Read:
        def sread():
            import os
            os.chdir(os.path.abspath(os.path.dirname(__file__)))
            os.chdir("..")
            load_exists = os.path.exists("Loaded")
            if load_exists == False:
                return 0
            if load_exists == True:
                from Loaded.TargetAircraft import Data
                if ModuleNotFoundError == True:
                    cte = input("The selected aircraft was not found. You'll be flying in nothing here, do you want to continue? [\"Y\",\"N\"]")
                    if cte == "Y":
                        pass
                    else:
                        return 0
                from Loaded.TargetLocation import Data
                if ModuleNotFoundError == True:
                    cte = input("Critical Error. No location was loaded. Try again, or report this problem to \n\"Github.com/SoHiEarth/TextFS\"")
                    SystemExit