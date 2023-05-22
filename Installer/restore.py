class Restore:
    # Restore Boot.py in Resources
    def Restore_Boot(args):
        import os
        RSFBOOT = open("Boot.py","w")
        RS_CONTENTS_1 = "# Unlike setting.py, this file is intended for\n# preferences that are not meant to be changed\n# in the later future.\n"
        RS_CONTENTS_2 = "\nOpened = " + str(args)
        RSFBOOT.write(RS_CONTENTS_1)
        RSFBOOT.write(RS_CONTENTS_2)