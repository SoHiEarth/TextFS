def Log(Content,end = False):
    import datetime
    import os
    CurrentTime = datetime.datetime.now()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("..")
    os.chdir("Logs")
    Write = open("Log.txt","a")
    Write.write(str(CurrentTime)+" "+str(Content)+"\n")
    if end == True:
        Write.close()
def Display():
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("..")
    os.chdir("Logs")
    Read = open("Log.txt")
    print(Read.read())
    Read.close()