import re

def interpret_stdlib(line):
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
                    print(eval(strline))
                else:
                    print("a: An error occured: Unsupported operation")
            elif line.startswith("sub("):
                line = line.lstrip("sum(")
                line = line.rstrip(")")
                line = line.replace(" ", "")
                if '-' in line and '+' and '*' and '/' and '%' not in strline:
                    print(eval(strline))
                else:
                    print("a: An error occured: Unsupported operation")
        elif line.startswith("string."):
            line = line.lstrip("string.")
            if line.startswith("newline()"):
                print('\n')