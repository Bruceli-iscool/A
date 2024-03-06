import re

def interpret_stdlib(line, varnames):
    """Interpret stdlib functions"""
    if line.startswith("math."):
        # math libary
        line = line.lstrip("math.")
        if line.startswith("printnf."):
            line = line.lstrip("printnf.")
            if line.startswith("sum("):
                line = line.lstrip("sum(")
                line = line.replace(")", "")
                strline = line.replace(" ", "")
                for key, value in varnames.items():
                    strline = strline.replace(str(key), str(value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    strline = strline.replace(';', "")
                    if '+' in strline and '-' and '*' and '/' and '%' not in strline:
                        print(eval(strline))
                    else:
                        print("a: An error occured: Unsupported operation")
            elif line.startswith("sub("):
                line = line.lstrip("sum(")
                line = line.replace(")", "")
                line = line.replace(" ", "")
                for key, value in varnames.items():
                    line = line.replace(str(key), str(value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    line = line.replace(';', "")
                    if '-' in line and '+' and '*' and '/' and '%' not in line:
                        print(eval(line))
                    else:
                        print("a: An error occured: Unsupported operation")
        elif line.startswith("string."):
            line = line.lstrip("string.")
            if line.startswith("newline()"):
                print('\n')