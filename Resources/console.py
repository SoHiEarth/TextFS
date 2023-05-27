def console():
    args = []
    consoleInput = input("Console | ")
    args.append(consoleInput)
    while consoleInput != "/exit":
        consoleInput = input("Console | ")
        if consoleInput == "/exit":
            print("SysMess | Exiting...")
            return args
        args.append(consoleInput)