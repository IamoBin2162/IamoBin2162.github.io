from pprint import pprint
from sys import stdout, stdin, stderr

def Fprint(write_to, *a):
    for elem in a:
        print(elem, end="", file=write_to)

def Fprintf(write_to, format, *a):
    print(format % a, end="", file=write_to)

def Fprintln(write_to, *a):
    for elem in a:
        print(elem, file=write_to)

def Print(*values):
    for value in values:
        print(value, end="")

def Printf(format, *values):
    print(format % values, end="")

def Println(*values):
    for value in values:
        print(value)

def Sprint(*values):
    result = ""
    for value in values:
        result += value
    return result

def Sprintf(format, *values):
    result = ""
    result += format % values
    return result

def Sprintln(*values):
    result = ""
    for value in values:
        result += value
    return result + "\n"

def Open(file, mode):
    return open(file, mode)

def Fget(file):
    return file.readline()

def Fgets(file):
    return file.readlines()

def Fgetc(file):
    return file.readline()[0]

def Fputs(file, to_write):
    f = Open(file, "w")
    f.write(to_write)

def Close(file):
    return file.close()

def Puts(*values):
    for value in values:
        print(value)

def Putc(*values):
    for value in values:
        print(value[0])

def Lprint(*values):
    for value in values:
        if type(value) == list:
            print(value, end="")
        else:
            raise TypeError("value must be a list")

def Lprintln(*values):
    for value in values:
        if type(value) == list:
            print(value)
        else:
            raise TypeError("value must be a list")

def Pprintln(*values):
    for value in values:
        pprint(value)

def Pprintf(format, *values):
    pprint(format % values)

def Eprint(message):
    print(message, file=stderr, end="")

def Eprintf(format, message):
    print(format % message, file=stderr)

def Eprintln(message):
    print(message, file=stderr)