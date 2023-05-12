class Read:
    def Vis():
        import os
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        load_exists = os.path.exists("Loaded")
        if load_exists == False:
            return 0
        from Loaded.TargetAircraft import Data
        if ModuleNotFoundError == True:
            cte = input("The selected aircraft was not found. You'll be flying in nothing here, do you want to continue? [\"Y\",\"N\"]")
            if cte == "Y":
                pass
            else:
                return 0
        from Loaded.TargetLocation import Data
        if ModuleNotFoundError == True:
            pass
        