import sys
import open_file
import shell


def main():
    print("The A interpreter.\nlicense() for license or exit() to exit()\nType .test to use the interactive interperter.")
    while True:
        userinput = input(">")
        if userinput.startswith("license()"):
            print("The A programming language is licensed under the Apache 2.0 license.\nThe license can be found here: https://www.apache.org/licenses/LICENSE-2.0.")
        elif userinput.startswith("exit()"):
            sys.exit()
        elif userinput.startswith(".test"):
            shell.shell()
        elif len(userinput) < 1:
            pass
        else:
            try:
                open_file.open_file(userinput)
            except FileNotFoundError as e:
                print(f"a: An error occured: {e}")
main()
