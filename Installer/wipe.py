import time
print("So you've come here...")
time.sleep(2)
print("This will wipe some stuff...")
time.sleep(2)
print("The accuracy of wipe is not insured.")
time.sleep(2)
print("You might crash the program.")
time.sleep(2)
print("You might break your program.")
time.sleep(2)
print("Your program might not start again.")
time.sleep(2)
print("It'll never see the light of day.")
time.sleep(2)
print("Wiping is still very early. Some files that shouldn't be deleted may be deleted\ndue to a bug in the wipe.py program.")
time.sleep(5)
wipecon = input("Are you sure you want to wipe?")
if wipecon == "Yes":
    import os
    import shutil
    print("Deleting everything not required from",os.getcwd())
    shutil.rmtree("Aircraft")
    shutil.rmtree("Locations")
    os.chdir("/Resources")
    os.remove("Boot.py")