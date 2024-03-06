import statistics
import paren
import interpret_stdlib

def interpret(line):
    # find tokens and execute them
    if line.startswith("#"):
        pass
    elif line.startswith("echo"):
        line = line.lstrip('echo ')
        if ';' not in line:
            print("a: An error occured: missing a ';'")
        else:
            try:
                line = line.rstrip(';')
                print(eval(line))
            except Exception as e:
                line = line.rstrip(';')
                print(line)
    else:
        interpret_stdlib.interpret_stdlib(line)

    

interpret("echo 'hi';")
interpret("string.newline()")
interpret("math.printnf.sum(1 + 1 )")
interpret("# this is a comment")