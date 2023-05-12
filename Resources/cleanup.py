def Cleanup(type):
    import os
    import shutil
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
        print(os.getcwd())
        temp_exists = os.path.exists("Temp")
        load_exists = os.path.exists("Loaded")
        if temp_exists == True:
            shutil.rmtree("Temp")
        if load_exists == True:
            shutil.rmtree("Loaded")
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