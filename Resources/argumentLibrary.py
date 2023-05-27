commandList = ["--tskmgr:DUMP"]
argsList = ["--tskmgr:DISPLAY","--tskmgr:REFRESH"]
class Dump:
    def tskmgrDump():
        import os
        import diskmgr
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("..")
        diskmgr.tskmgr.Dump()
def findArg(consoleInput):
    arguments = [""]
    while consoleInput != "/exit":
        if consoleInput == "/exit":
            return arguments
        if "--tskmgrDUMP" in consoleInput:
            Dump.tskmgrDump()
            print("SysMess | Completed tskmgrDump")
        consoleInput = input("Console | ")