def aircraftMove():
    import os
    tc=input("Choose your aircraft: ")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    aircraft_content = os.listdir("Aircraft")
    os.chdir("Aircraft")
    for craft in aircraft_content:
        if tc in craft:
                targetc_path = os.path.abspath(craft)
                movec = open(targetc_path, "r")
                moveccon = movec.read()
                movec.close()
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                os.chdir("Loaded")
                placec = open("TargetAircraft.py", "w")
                placec.write(moveccon)
                placec.close()
                break
def locationMove():
    import os
    tl=input("Choose your location: ")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    location_content = os.listdir("Locations")
    os.chdir("Locations")
    movelcon = ""
    for location in location_content:
        if tl in location:
            targetl_path = os.path.abspath(location)
            movel = open(targetl_path, "r")
            movelcon = movel.read()
            movel.close()
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            os.chdir("Loaded")
            placec = open("TargetLocation.py", "w")
            placec.write(movelcon)
            placec.close()
            break