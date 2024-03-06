import statistics
import paren


def interpret(line):
    # find tokens and execute them
    if line.startswith("#"):
        pass
    if line.startswith("echo"):
        line = line.lstrip('echo ')
        if ';' not in line:
            print("a: An error occured: missing a ';'")
        else:
            try:
                line = line.rstrip(';')
                print(eval(line), end="")
            except Exception as e:
                line = line.rstrip(';')
                print(line, end="")
    if line.startswith("math."):
        # math libary
        line = line.lstrip("math.")
        if line.startswith("printnf."):
            line = line.lstrip("printnf.")
            if line.startswith("sum("):
                line = line.lstrip("sum(")
                line = line.rstrip(")")
                strline = line.replace(" ", "")
                if '+' in strline and '-' and '*' and '/' and '%' not in strline:
                    print(eval(strline), end="")
                else:
                    print("a: An error occured: Unsupported operation")
            elif line.startswith("sub("):
                line = line.lstrip("sum(")
                line = line.rstrip(")")
                line = line.replace(" ", "")
                if '-' in line and '+' and '*' and '/' and '%' not in strline:
                    print(eval(strline), end="")
                else:
                    print("a: An error occured: Unsupported operation")
    

interpret("echo 'hi'")
interpret("math.printnf.sum(1 + 1 )")