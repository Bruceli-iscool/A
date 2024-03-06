import statistics
import paren
import interpret_stdlib

var = {}
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
    elif "=" in line:
        line = line.replace(" ", "")
        varname, value = line.split("=")
        if ";" not in line:
            print("a: An error occured: Expected ';'")
        else:
            value = value.replace(";", "")
            var[varname] = value
    else:
        interpret_stdlib.interpret_stdlib(line, var)
    

    

interpret("echo 'hi';")
interpret("string.newline()")
interpret("math.printnf.sum(1 + 1 );")
interpret("x= 5;")
print(var)
interpret("# this is a comment")