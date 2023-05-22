def Cleanup(type):
    import os
    import shutil
    from Installer.restore import Restore
    from Resources.setting import DebugMode
    if type == "Partial":
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        temp_exists = os.path.exists("Temp")
        load_exists = os.path.exists("Load")
        if temp_exists == True:
            shutil.rmtree("Temp")
        if load_exists == True:
            shutil.rmtree("Loaded")
    else:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        temp_exists = os.path.exists("Temp")
        load_exists = os.path.exists("Loaded")
        Output_exists = os.path.exists("Output")
        if temp_exists == True:
            shutil.rmtree("Temp")
        if load_exists == True:
            shutil.rmtree("Loaded")
        if Output_exists == True:
            shutil.rmtree("Output")
        os.chdir("Resources")
        cache_exists = os.path.exists("__pycache__")
        if cache_exists == True:
            shutil.rmtree("__pycache__")
        os.chdir("..")
        os.chdir("Installer")
        cache_exists = os.path.exists("__pycache__")
        if cache_exists == True:
            shutil.rmtree("__pycache__")
        os.chdir("..")
        cache_exists = os.path.exists("__pycache__")
        if cache_exists == True:
            shutil.rmtree("__pycache__")
        
    print("Cleanup complete.")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    Restore.Restore_Boot(0)