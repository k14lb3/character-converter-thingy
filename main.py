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


def cmd_char(characters):
    char, char_r = None, None

    while True:
        char = input("Input character: ")

        if len(char) == 1:
            break

        print("Invalid input.")

    while True:
        char_r = input("Input replacement: ")

        if len(char_r) == 1:
            break

        print("Invalid input.")

    characters[char] = char_r


def cmd_dchar(characters):
    print("Character\tReplacement")
    for char, char_r in characters.items():
        print(f'{char}\t\t{char_r}')


def main():
    cmd_help()

    characters = {}

    while True:

        cmd = input("\n➡ ")

        if cmd == CMD_CONVERT:
            cmd_convert()
        elif cmd == CMD_CHAR:
            cmd_char(characters)
        elif cmd == CMD_DCHAR:
            cmd_dchar(characters)
        elif cmd == CMD_HELP:
            cmd_help()
        elif cmd == CMD_EXIT:
            return
        else:
            print(f"Command not found: {cmd}")


if __name__ == "__main__":
    main()
