CMD_CONVERT = "convert"
CMD_CHAR = "char"
CMD_DCHAR = "dchar"
CMD_HELP = "help"
CMD_EXIT = "exit"


COMMANDS = {
    CMD_CONVERT: "Convert characters in a given input string.",
    CMD_CHAR: "Add a character that will be converted.",
    CMD_DCHAR: "Display all the characters that will be converted.",
    CMD_HELP: "Display commands.",
    CMD_EXIT: "Exits the program.",
}


def cmd_help():
    print("Commands:")
    for cmd, func in COMMANDS.items():
        print(f"{cmd}\t\t-\t{func}")

def cmd_convert():
    pass

def cmd_char():
    pass

def cmd_lchar():
    pass

def main():
    cmd_help()

    while True:

        cmd = input("\n➡ ")

        if cmd == CMD_CONVERT:
            cmd_convert()
        elif cmd == CMD_CHAR:
            cmd_char()
        elif cmd == CMD_DCHAR:
            cmd_char()
        elif cmd == CMD_HELP:
            cmd_help()
        elif cmd == CMD_EXIT:
            return
        else:
            print(f"Command not found: {cmd}")


if __name__ == "__main__":
    main()
