def Log(Contents):
    import os
    import datetime
    CurrentTime = datetime.datetime.now()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("..")
    os.chdir("Logs")