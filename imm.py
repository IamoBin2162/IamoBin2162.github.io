"""
interpreter of main moon

running a script:

    in command line:

        >>> moon FILE_NAME
"""

import sys, types, os, time, typing, random, platform, math
from ast import literal_eval
from pprint import pprint as __pp__
from fractions import Fraction
from collections import namedtuple
# from warnings import deprecated
import re
from collections import Counter

def ptr(n):
    return hex(id(n))

def test(expression):
    try:
        exec(expression)
    except:
        return Error(), False
    else:
        return True

type nil = None
type true = True
type false = False
type maybe = 0 | 1
# type undefined = 'undefined'
type unknown = 'unknown'
type char = 'char'
type HUGE_VAL = 'HUGE_VAL'
type perhaps = maybe

start = time.time()
in_do = False
inf = float('inf')
nan = float('nan')
zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
stdout = sys.stdout
stdin = sys.stdin
stderr = sys.stderr
argv = sys.argv
__FILE__ = argv[1]
__VERSION__ = f"moon v3"
__LOCALS__ = locals()
__GLOBALS__ = globals()
__NAME__ = __name__
FILE = __file__
VARIABLES = {}
VARIABLES['$0'] = __name__
VARIABLES['$!'] = None
VARIABLES['$*'] = argv
VARIABLES['$stdout'] = stdout
VARIABLES['$stdin'] = stdin
VARIABLES['$stderr'] = stderr
VARIABLES['$_'] = None
VARIABLES['$>'] = None
VARIABLES['$<'] = None
VARIABLES['$#'] = len
global ERR
ERR = None
ok = ERR
Any = object()
self = __NAME__

class IO:

    def __rshift__(self, value):
        print(value)
    
    def __lshift__(self, prompt):
        return input(prompt)

IO = IO()

keywords = [
    'true', 'false', 'nil', 'module', 'alias', 'dec', 'def', 'if', 'elif', 'else', 'until', 'unless', 'class', 'switch', 'case', 'while', 'for',
    'try', 'except', 'finally', 'async', 'await', 'end', 'yield', 'pass', 'continue', 'break', 'is', 'in', 'raise', 'return', 'and', 'or',
    'lambda', 'as', 'from', 'assert', 'del', 'global', 'not', 'with', 'puts', 'maybe', 'never', 'do', 'undef', 'True', 'False', 'import', 'None', 
    'match', 'todo', 'panic', 'when', 'foreach',  'add', 'sub', 'mult', 'div', 'pow', 'mod', 'xor', 'shr', 'shl', 'addr', 'type', 'struct', 'enum', 
    'say', 'eq', 'neq', 'gt', 'ge', 'lt', 'le', 'my', 'our', 'defer', 'END', 'discard', 'mut', 'package', 'auto', 'loop', 'lit', 'local', 'set', 
    'to', 'define', 'nonlocal', 'consume', 'static', 'forever', 'LUA', 'RB', 'ZIG', 'C', 'CPP', 'GLEAM', 'ASM', 'putv', 'var', 'fn', 'isnot', 
    'cast', 
]
keywords.sort()

# class Dir:

#     def mkdir(name):
#         os.mkdir(name)

#     def exist(name):
#         ...

#     def is_empty(name):
#         ...

#     def pwd():
#         return os.system("cd")
    
#     def home():
#         ...

#     def chdir(to):
#         return os.system(f"cd {to}")
    
#     def entries():
#         return os.system("dir")
    
#     def glob(pattern):
#         ...

#     def rmdir(name):
#         os.system(f"rmdir {name}")

#     def move(name, to):
#         ...

#     def copy(file, to):
#         ...

# def define(name, value):
#     exec(f"{name} = {value}", __LOCALS__, __GLOBALS__)

def swap(a, b):
    a, b = b, a
    return nil

class Symbol:

    def __init__(self, arg):
        self.arg = arg
    
    def __repr__(self) -> str:
        return f":{self.arg}"

def __etype__(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

_1 = ""
def each(object):
    _1 = ""
    for elem in object:
        _1 += to_s(elem) + "\n"
    return _1

def fail(message):
    raise RuntimeError(message)

def next(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    idx = ""
    result = ""
    if type(string) == str:
        for elem in string:
            if elem in alpha:
                for n in range(len(alpha)):
                    if alpha[n] == elem:
                        idx = alpha[n]
                try:
                    idx = alpha.find(idx)
                    result += alpha[idx + 1]
                except IndexError as e:
                    if "string index out of range" in str(e):
                        result += alpha[0]
            
            elif elem in nums:
                for n in range(len(nums)):
                    if nums[n] == elem:
                        idx = nums[n]
                try:
                    result += nums[int(idx) + 1]
                except IndexError as e:
                    if "string index out of range" in str(e):
                        result += nums[0]

    elif type(string) == int:
        result = Range(0, string+2).new()[-1]

    else:
        raise SyntaxError(f"unknown name for next: {string}")
    
    return result

def before(thing):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    idx = ""
    if type(thing) == str:
        for elem in thing:
            if elem in alpha:
                for n in range(len(alpha)):
                    if alpha[n] == elem:
                        idx = alpha[n]
                        idx = alpha[n - 1]

    elif type(thing) == int:
        idx = Range(0, thing).new()[-1]

    return idx

def __sum__(*n):
    return sum(n)

def __pow__(a, b):
    return a ** b

def typeof(value: typing.Any):

    # if value not in [nil, Nil, None, True, False, true, false, inf, maybe, undefined]:
        # return f"#<{value}>"

    # else:
        # return f"#<{value.__class__.__name__}>"
    
    if value == nil:
        return "#<nil>"
    
    if value == Nil:
        return "#<Nil>"
    
    if value == true:
        return "#<bool>"

    if value == false:
        return "#<bool>"
    
    if value == maybe:
        return "#<maybe>"
    
    if value in keywords:
        return "#<keyword>"
    
    if value in __GLOBALS__ or value in __LOCALS__:
        return "#<built-in function or method or variable>"

    if value == None:
        return "#<None>"

    if value == inf:
        return "#<infinity>"
    
    if value == undefined:
        return "#<undefined>"
    
    # if value == nan:
    #     return "#<nan>"

    # if value in [zero, one, two, three, four, five, six, seven, eight, nine, ten]:
    #     return "#<alpha-number>"

    # can not set 'nan' or our 'alpha-numbers' in here ( like one, two, ... )
    # because nan != nan, so we never get at the if block in which we return #<nan>
    # and for alpha-numbers, we never get at the if block in which we return #<alpha-number>


    # typeof(nan) == #<Number> !
    # typeof(one) == #<Number> !

    
    if value in [stdin, stdout, stderr]:
        return "#<stdio>"
    
    # if value.__class__.__name__ == 'str':
    #     result = 'String'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ in ['int', 'float', 'complex']:
    #     result = 'Number'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'list':
    #     result = 'List'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'dict':
    #     result = 'Dict'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'set':
    #     result = 'Set'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'tuple':
    #     result = 'Tuple'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'object':
    #     result = 'Object'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'bytes':
    #     result = 'Bytes'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'bytearray':
    #     result = 'Bytearray'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'type':
    #     result = 'Type'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'memoryview':
    #     result = 'Memoryview'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'bool':
    #     result = 'Bool'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'slice':
    #     result = 'Slice'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'types.FunctionType':
    #     result = 'Function'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'frozenset':
    #     result = 'Frozenset'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'enumerate':
    #     result = 'Enumerate'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'range':
    #     result = 'Range'
    #     return f"#<{result}>"

    # elif value.__class__.__name__ == 'frozenset':
    #     result = 'Frozenset'
    #     return f"#<{result}>"

    else:
        return f"#<{value.__class__.__name__}>"
    
def require(module_package_or_sth: str):
    try:
        return exec(f"import {module_package_or_sth}", __GLOBALS__, __LOCALS__)
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(e)
    
def include(module_package_or_sth: str):
    try:
        return exec(f"import {module_package_or_sth}", __GLOBALS__, __LOCALS__)
    except ModuleNotFoundError as e:
        print(YELLOW + "warning: " + str(Warning(e)) + BASE)

def isinstanceof(__object: object, __class_or_tuple) -> bool:
    return isinstance(__object, __class_or_tuple)

show = False
def measure():
    global show
    show = True

def sizeof(thing):
    return sys.getsizeof(thing)

def lenof(thing):
    return len(thing)

def tostring(value):
    return str(value)

def toint(value):
    return int(value)

def tofloat(value):
    return float(value)
    
RED = '\033[31m'
GREEN = '\033[32m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
BASE = '\033[0m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
YELLOW = '\033[33m'
ORANGE = '\033[40m'

iota_counter = 0
def iota(reset: bool = False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

def is_zero(__obj: object):
    return True if __obj == 0 else False

def __clear_exec__():
    file = open("__exec__.moon", "w")
    file.write("")

def to_s(value) -> str:
    return str(value)

def to_i(value) -> int:
    return int(value)

def to_f(value) -> float:
    return float(value)

def to_c(value) -> complex:
    return complex(value)

def to_l(value) -> list:
    return list(value)

def to_t(value) -> tuple:
    return tuple(value)

def to_set(value) -> set:
    return set(value)

def to_bin(value) -> bin:
    return bin(value)

def to_b(value) -> bool:
    return bool(value)

def to_o(value) -> oct:
    return oct(value)

def to_n(value) -> nil:
    return nil

def to_d(key, value) -> dict:
    return { key : value }

def to_enum(value) -> enumerate:
    return enumerate(value)

def to_z(value) -> int:
    return 0

def to_r(value) -> Fraction:
    return Fraction(value)

def responds_to(__obj: object, __name: str) -> bool:
    return hasattr(__obj, __name)

__locals__ = {}
class Error(BaseException): ...
class TodoError(BaseException): ...
class PanicError(BaseException): ...
todo_found = False
panic_found = False

def Ok(expression):
    try:
        eval(expression)
    except:
        return False
    return True

class Range:

    global alpha
    alpha = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    def __init__(self, start, end):
        self.start = start
        self.end  = end

    def new(self):
        if type(self.start) == str and type(self.end) == str:
            result = []
            for n in range(len(alpha)):
                if self.start == alpha[n]:
                    result.append(alpha[n])
                
                if not self.start in alpha:
                    raise NameError(f"unknown name: '{self.start}'")
                if not self.end in alpha:
                    raise NameError(f"unknown name: '{self.end}'")
                
                if self.end == alpha[n]:
                    result.append(alpha[n])
                
            n1 = alpha.index(self.start)
            n2 = alpha.index(self.end)
            result = alpha[n1:n2+1]
            return result

        if type(self.start) == int and type(self.end) == int:
            result = list(range(self.start, self.end))
            return result

        else:
            raise NameError("unknwon: try Range(str, str).new() or Range(int, int).new()")
    
_ = None

PLATFORM = platform.system()

def printf(base: str, *values):
        if base.__class__ is not str: raise TypeError(f"str expected for base in printf, but {base.__class__.__name__} is given")
        if values == ():
            print(base)
            return nil
        for value in values:
            print(base % value, sep="\n")
        return nil


class DidYouMean:
    # This is not my code
    # it is from 'https://norvig.com/spell-correct.html'

    def words(text): return re.findall(r'\w+', text.lower())

    WORDS = Counter(words(open('big.txt').read()))

    def P(word, N=sum(WORDS.values())): 
        "Probability of `word`."
        return DidYouMean.WORDS[word] / N

    def correction(word): 
        "Most probable spelling correction for word."
        return max(DidYouMean.candidates(word), key=DidYouMean.P)

    def correction2(word):
        items = word.split(" ")
        result = ""
        for element in items:
            result += max(DidYouMean.candidates(element), key=DidYouMean.P) + " "
        return result

    def candidates(word): 
        "Generate possible spelling corrections for word."
        return (DidYouMean.known([word]) or DidYouMean.known(DidYouMean.edits1(word)) or DidYouMean.known(DidYouMean.edits2(word)) or [word])

    def known(words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in DidYouMean.WORDS)

    def edits1(word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in DidYouMean.edits1(word) for e2 in DidYouMean.edits1(e1))

    
def byte(value):
    if value not in range(0, 255):
        raise Error(f"byte expects uint8, not {value}")
    return int(value)

def rune(value):
    if value not in range(-2147483648, 2147483647):
        raise Error(f"rune expects int32, not {value}")
    return int(value)
    
def any(value):
    t = __etype__(value)
    return t(value)

def error(m):
    return Error(m)

class io:

    def print(*values, sep="\t"):
        for value in values:
            VARIABLES['$>'] = value
            print(value, sep=sep, end="")
        return nil
    
    def println(*values, sep="\t"):
        for value in values:
            VARIABLES['$>'] = value
            print(value, sep=sep)
        return nil

    def throw(__err, message: str = ""):
        raise __err(message)
    
    def open(file, mode):
        return open(file, mode)
    
    def freads(file):
        global _
        _ = file.readlines()
        VARIABLES['$_'] = VARIABLES['$<'] = _
        return _
    
    def fread(file):
        global _
        _ = file.readline()
        VARIABLES['$_'] = VARIABLES['$<'] = _
        return _
    
    def freadc(file):
        global _
        _ = file.readline()[0]
        VARIABLES['$_'] = VARIABLES['$<'] = _
        return _
    
    def fprint(file, *values):
        for value in values:
            print(value, file=file, end="")
        VARIABLES['$>'] = value
        return nil
    
    def fprintln(file, *values):
        for value in values:
            print(value, file=file, end="\n")
        VARIABLES['$>'] = value
        return nil

    def fprintf(file, base: str, *other):
        if base.__class__ is not str: raise TypeError(f"str expected for base in printf, but {base.__class__.__name__} is given")
        if other == ():
            print(base, file=file)
        VARIABLES['$>'] = base % other
        print(base % other, file=file)
        return nil

    def close(file):
        file.close()
        return nil

    def status(file):
        return file.closed
    
    def read(prompt):
        global _
        _ = input(prompt)
        VARIABLES['$_'] = VARIABLES['$<'] = _
        return _
    
    def fwrite(*values, file):
        for value in values:
            file.write(value)
        VARIABLES['$>'] = value
        return nil

    def gets():
        global _
        _ = input()
        VARIABLES['$_'] = VARIABLES['$<'] = _
        return _

    def getc():
        global _
        _ = input()[0]
        VARIABLES['$_'] = VARIABLES['$<'] = _
        return _[0]
    
    def putc(*values) -> nil:
        for value in values:
            try:
                if len(value) != 1:
                    raise SyntaxError(f"'putc' expects char, not {typeof(value)}")
            except TypeError as e:
                if "has no len()" in str(e):
                    if len(str(value)) != 1:
                        raise SyntaxError(f"'putc' expects char, not {typeof(value)}")
                else:
                    raise TypeError(e)
            VARIABLES['$>'] = value
            print(value)
        return nil
    
    def printf(base: str, *values):
        if base.__class__ is not str: raise TypeError(f"str expected for base in printf, but {base.__class__.__name__} is given")
        if values == ():
            print(base)
        for value in values:
            print(base % value, sep="\n")
        VARIABLES['$>'] = value
        return nil

    def sprint(value):
        VARIABLES['$>'] = value
        return value
    
    def sprintf(base: str, *values):
        if base.__class__ is not str: raise TypeError(f"str expected for base in printf, but {base.__class__.__name__} is given")
        if values == ():
            return base
        VARIABLES['$>'] = value
        return base % values
    
    def var_dump(*values):
        for value in values:
            var_type = value.__class__.__name__
            if value == nil:
                var_type = "<type 'nil'>"
            try:
                print(f"{var_type}({len(value)}) {value}")
            except:
                print(f"{var_type}({len(str(value))}) {value}")
        VARIABLES['$>'] = value
        return nil

    def system(command):
        return os.system(command)

    def print_r(__value: list):
        if type(__value) not in [list, dict, set, tuple]:
            raise TypeError(f"'print_r' takes list, dict, set or tuple not {typeof(__value)}")
        VARIABLES['$>'] = __value
        __pp__(__value)
        return nil

    def exit(code: int = 0):
        exit(code=code)

    def id(__obj: object):
        return hex(id(__obj))
    
    def rand(max: int):
        return random.randint(0, max)
    
    def sleep(sec: float):
        time.sleep(sec)

    def format(base: str, *values):
        if values == ():
            return base
        VARIABLES['$>'] = base % values
        return base % values

    def catch(__to_do: str, __err_type):
        try:
            exec(__to_do)
        except BaseException as e:
            if e.__class__ == __err_type:
                print(f"{RED}{e}{BASE}")
                return True
            else:
                return ERR
        else:
            return nil
        # if there is error and __err_type is the error type, it returns True
        # but if there is error and __err_type is not the error type, it returns ERR
        # but if there is no error, it returns nil

    def pprint(*values):
        for value in values:
            VARIABLES['$>'] = value
            __pp__(value)
        return nil

    def pprintf(base: str, *other):
        if base.__class__ is not str: raise TypeError(f"str expected for base in printf, but {base.__class__.__name__} is given")
        VARIABLES['$>'] = base % other
        __pp__(base % other)
        return nil
    
    def puts(*values) -> nil:
        for value in values:
            io.pprint(value)
        VARIABLES['$>'] = value
        return nil

    def lprint(value: str):
        VARIABLES['$>'] = __locals__[f'{value}']
        print(__locals__[f'{value}'], end="")
    
    def lprintln(value: str):
        VARIABLES['$>'] = __locals__[f'{value}']
        print(__locals__[f'{value}'], end="\n")

    def cprint(*values, sep="\t", end="\n", file=stdout, flush=False):
        for value in values:
            VARIABLES['$>'] = value
            print(value, sep=sep, end=end, file=file, flush=flush)

    def vprint(*values: str):
        for value in values:
            VARIABLES['$>'] = value
            print(VARIABLES[value], end="")

    def vprintln(*values: str):
        for value in values:
            VARIABLES['$>'] = value
            print(VARIABLES[value])

    def vprintf(format, *values):
        VARIABLES['$>'] = format % values
        print(VARIABLES[format % values])


class Imaginary(complex):
    ...

def pairs(__obj):
    if __obj.__class__ is int or __obj.__class__ is float:
        return range(__obj)
    return each(__obj)

def strcpy(var, value):
    exec(f"#{var} = #{value}")

def chop(__str: str):
    return __str.strip()[0:-1]

def chomp(__str: str):
    return __str.strip()

argc = lenof(argv)

class SizeError(Exception): ...
def make(__type, message = "", size = None):
    if size == None:
        size = 0
        return __type(message)
    
    if size is not None and sizeof(__type(message)) > size:
        raise SizeError(f"bigger size than expected, expect {size} but got {sizeof(__type(message))}")
    return __type(message)

def system(command):
    return os.system(command)

def update(__name: str, new_value) -> nil:
    if __name not in __GLOBALS__ or __name not in __LOCALS__:
        raise NameError(f"{__name} is not defined")
    exec(f"{__name} = {new_value}", __GLOBALS__, __LOCALS__)
    return nil

def mexec(code):
    # moon exec
    with open("__exec__.moon", "a") as f:
        f.write(code)
        f.write("\n")
    return system("moon __exec__.moon") 

def parseStmt(value):
    return mexec(value)

def TEST(func, print_or_return: str, catch_err: bool, *param):
    try:
        if print_or_return == "print":
            io.print(func(param))

        elif print_or_return == "return":
            return func(param)
        else:
            io.throw(NameError, f"for 'print_or_return' only 'print' or 'return' is acceptible not '{print_or_return}'")
    except BaseException as e:
        if catch_err:
            io.print(e)
        else:
            raise e.__class__(e)

def debug(expr):
    try:
        exec(expr)
    except BaseException as e:
        return Error(), Nil, e
    else:
        return "Ok", Nil

# class Nil:
#     def __repr__(self):
#         return to_s(nil)

# Nil = Nil()

class undefined_t:

    def __repr__(self) -> str:
        return "undefined"
    
    def __bool__(self):
        return False
    
undefined = undefined_t()

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return undefined
    
class nil_t:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

    def __repr__(self) -> str:
        return "Nil"
    
    def __bool__(self):
        return False
    
    def __eq__(self, value):
        return isinstance(value, nil_t)
    
    def __call__(self, *args, **kwds):
        return self
    
    def __setattr__(self, __name, __value):
        raise TypeError("cannot modify nil")
    
    def __getattr__(self, name):
        print(f"[TRACE] accessed nil attribute: {name}")
        return self
    
    def __len__(self):
        return 0
    
    def __iter__(self):
        return iter([])
    
    def __getitem__(self, idx):
        raise IndexError("nil does not support item access")
    
    def __contains__(self, value):
        return False
    
    def __setitem__(self, idx, value):
        raise SyntaxError("nil does not support item setting")
    
Nil = nil_t()
NilPtr = ptr(Nil)
NonePtr = ptr(None)

def unreachable(msg = ""):
    assert False, msg

class nothing_t:

    def __repr__(self):
        return ""

    def __len__(self):
        return 0

nothing = nothing_t()

class mystery_t:

    def __repr__(self):
        return "mystery"
    
mystery = mystery_t()

class lazy:

    def __init__(self, func):
        self.func = func
        self._value = None
        self._evaluated = False

    def __get__(self, instance, owner):
        if not self._evaluated:
            self._value = self.func(instance)
            self._evaluated = True
        return self._value

class freezable:
    def __init__(self, *args):
        self._frozen = False
        for arg in args:
            setattr(self, arg, Nil)

    def freeze(self):
        self._frozen = True

    def __setattr__(self, name, value):
        if getattr(self, '_frozen', False) and name != '_frozen':
            raise AttributeError(f"object is frozen")
        super().__setattr__(name, value)

__code__ = Nil

with open(argv[1], "r") as file:
    lines = file.readlines()

    for i in range(len(lines)):
        LINE = i + 1
        file = sys.argv[1]
        file = file.strip()

        msg = lines[i]
        __line__ = msg

        try:
            if "#" in msg:
                continue

            elif ":=" in msg:
                exec(f"{msg[:msg.index(":=")].strip()} = {msg[msg.index(":=")+2:].strip()}")
            
            elif msg.startswith("&"):
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(f"{msg[msg.index("&")+1:]}{BLOCK[:BLOCK.index("end")]}")

            elif "CPP" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.cpp", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])

            elif "C" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.c", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])

            elif "RB" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.rb", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])
                system("ruby __main__.rb")

            elif "LUA" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.lua", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])
                system("C:\\Users\\Lenovo\\Desktop\\me\\Lua\\lua.exe __main__.lua")

            elif "ASM" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.s", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])

            # elif "GO" in msg and "(" in msg:
            #     BLOCK = ""
            #     items = [lines[x] for x in range(i+1, len(lines))]
            #     for k in range(len(items)):
            #         for n in items[k]:
            #             BLOCK += n
            #     with open("__main__.go", "w") as f:
            #         f.write(BLOCK[:BLOCK.index(") end")])
                
            elif "GLEAM" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.gleam", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])
                
            elif "ZIG" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.zig", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])
                system("zig run __main__.zig")
                    
                
#             elif "BEGIN" in msg and "{" in msg:
#                 BLOCK = ""
#                 items = [lines[x] for x in range(i+1, len(lines))]
#                 for k in range(len(items)):
#                     for n in items[k]:
#                         BLOCK += n
#                 global this_line3
#                 this_line3 = (
#                     f"""
# {BLOCK[:BLOCK.index("}")].strip()}
# """
#                 )
#                 try:
#                     exec(this_line3)
#                 except NameError as e:
#                     if "this_line3" in str(e):
#                         pass
#                     else:
#                         raise NameError(e)

            elif "var" in msg:
                name = msg[msg.index("var")+3:msg.index("=")].strip()
                value = msg[msg.index("=")+1:].strip()

                if ":" in name: raise SyntaxError("type annotation is not allowed in var")

                else:

                    if "~>" in value:
                        try:
                            eval(msg[msg.index("=")+1:msg.index("~>")].strip())
                        except NameError as e:
                            continue
                        else:
                            exec(f"{name} = {msg[msg.index("=")+1:msg.index("~>")].strip()}({msg[msg.index("~>")+2:].strip()})")

                    elif "fn" in value:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = lambda {msg[msg.index("(")+1:msg.index(")")].strip()}: {msg[msg.index("->")+2:].strip()}")

                    elif "=>" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("=>")].strip()}({msg[msg.index("=>")+2:].strip()})")

                    elif "<=" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("<=")].strip()}()")

                    elif "add" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("add")]}+{msg[msg.index("add")+3:]}")

                    elif "sub" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("sub")]}-{msg[msg.index("sub")+3:]}")

                    elif "div" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("div")]}/{msg[msg.index("div")+3:]}")

                    elif "mult" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("mult")]}*{msg[msg.index("mult")+4:]}")

                    elif "pow" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("pow")]}**{msg[msg.index("pow")+3:]}")

                    elif "mod" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("mod")]}%{msg[msg.index("mod")+3:]}")

                    elif "xor" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("xor")]}^{msg[msg.index("xor")+3:]}")

                    elif "shr" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("shr")]}>>{msg[msg.index("shr")+3:]}")

                    elif "shl" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("shl")]}<<{msg[msg.index("shl")+3:]}")
                    
                    elif "neq" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("neq")]} != {msg[msg.index("neq")+3:]}")

                    elif "eq" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("eq")]} == {msg[msg.index("eq")+2:]}")

                    elif "gt" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("gt")]} > {msg[msg.index("gt")+2:]}")

                    elif "ge" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("ge")]} >= {msg[msg.index("ge")+2:]}")

                    elif "lt" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("lt")]} < {msg[msg.index("lt")+2:]}")

                    elif "le" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("le")]} <= {msg[msg.index("le")+2:]}")

                    elif "isnot" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("isnot")]} is not {msg[msg.index("isnot")+5:]}")

                    elif "cast" in msg and "[" in msg and "]" in msg and "(" in msg and ")" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("[")+1:msg.index("]")]}({msg[msg.index("(")+1:msg.index(")")]})")

                    else:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}")

            elif ">>" in msg or "<<" in msg:
                exec(msg)
                
            elif "=>" in msg and not "final" in msg and not "readonly" in msg and not "$" in msg and not "!" in msg:
                exec(f"{msg[:msg.index("=>")].strip()}({msg[msg.index("=>")+2:].strip()})")

            elif "<=" in msg and not "final" in msg and not "readonly" in msg and not "$" in msg and not "!" in msg:
                exec(f"{msg[:msg.index("<=")].strip()}()") if not "(" in msg and not ")" in msg else exec(f"{msg[:msg.index("<=")].strip()}")
            
            elif "->" in msg and not "def" in msg and not ":" in msg and not "fn" in msg and not "$" in msg and not ">>" in msg and not "<<" in msg and not "final" in msg and not "readonly" in msg and not "$" in msg and not "!" in msg:
                exec(f"print({msg[:msg.index("->")].strip()}({msg[msg.index("->")+2:].strip()}))")

            elif "<-" in msg and not "final" in msg and not "readonly" in msg and not "$" in msg and not "!" in msg:
                exec(f"print({msg[:msg.index("<-")].strip()}())") if not "(" in msg and not ")" in msg else exec(f"print({msg[:msg.index("<-")].strip()})")

            elif "~>" in msg:
                try:
                    eval(msg[msg.index("~>")+2:].strip())
                except NameError as e:
                    continue
                else:
                    exec(f"print({msg[:msg.index("~>")].strip()}({msg[msg.index("~>")+2:].strip()}))")

            elif msg.strip().endswith("!"):
                exec(f"{msg[:msg.strip().index("!")]}")

            elif "<" in msg and ">" in msg: 
                exec(msg[msg.index("<")+1:msg.index(">")])
            
            elif msg.count('`') == 2:
                system(msg.strip()[msg.index("`")+1:-1].strip())
            
            elif msg.strip().endswith("?"):
                print(f"{eval(msg[:msg.index('?')])}\n=> {CYAN}{BOLD}Ok, {Nil}{BASE}")

            elif "also" in msg:
                first_one = msg[:msg.index("also")]
                second_one = msg[msg.index("also")+4:]
                exec(f"{first_one.strip()}; {second_one.strip()}")

            elif "after" in msg:
                first_one = msg[:msg.index("after")]
                second_one = msg[msg.index("after")+5:]
                exec(f"{second_one.strip()}; {first_one.strip()}")

            elif "before" in msg:
                first_one = msg[:msg.index("before")]
                second_one = msg[msg.index("before")+6:]
                exec(f"{first_one.strip()}; {second_one.strip()}")

            elif "mirror" in msg:
                from_what = msg[msg.index("mirror")+6:msg.index("to")]
                to_what = msg[msg.index("to")+2:]
                exec(f"{to_what.strip()} = {from_what.strip()}")

            elif "sleep" in msg:
                time.sleep(float(msg[msg.index("sleep")+5:].strip()))

            elif "wait" in msg:
                time.sleep(float(msg[msg.index("wait")+4:].strip()))                

            # elif "again" in msg:
            #     previous_line = lines[i-1]
            #     mexec(previous_line)

#             elif msg.strip().startswith("@") and not "=" in msg:
#                 BLOCK = ""
#                 items = [lines[x] for x in range(i+1, len(lines))]
#                 for k in range(len(items)):
#                     for n in items[k]:
#                         BLOCK += n
#                 exec(
#                     f"""
# {msg}{BLOCK[:BLOCK.index("end")]}
# """
#                 )
                    
#             elif "deprecated" in msg:
#                 BLOCK = ""
#                 items = [lines[x] for x in range(i+1, len(lines))]
#                 for k in range(len(items)):
#                     for n in items[k]:
#                         BLOCK += n
#                 exec(
#                     f"""
# {msg}{BLOCK[:BLOCK.index("end")]}
# """
#                 )

            elif "putv" in msg:
                key = msg[msg.index("putv")+4:].strip()
                print(VARIABLES[key])                

            elif "static" in msg and "=" in msg:
                exec(f"global {msg[msg.index("static")+6:msg.index("=")].strip()}; {msg[msg.index("static")+6:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}")

            elif "define" in msg:
                if "(" in msg and ")" in msg:
                    exec(
                        f"""
def {msg[msg.index("define")+6:msg.index(")")+1]}: return {msg[msg.index(")")+1:].strip()}
"""
                    )

                elif not "(" in msg and not ")" in msg:
                    items = msg.split()
                    exec(f"{items[1]} = {items[2]}")


#             elif "@" in msg and "=" in msg:
#                 exec(
#                     f"""
# class {__name__}:
#     {msg[msg.index("@")+1:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}
# """                    
# )
            elif "set" in msg and "to" in msg:
                exec(f"{msg[msg.index("set")+3:msg.index("to")].strip()} = {msg[msg.index("to")+2:].strip()}")

            elif "consume" in msg and "to" in msg:
                exec(f"{msg[msg.index("to")+2:].strip()} = {msg[msg.index("consume")+7:msg.index("to")].strip()}; {msg[msg.index("consume")+7:msg.index("to")].strip()} = nil")

            elif "lit" in msg and "=" in msg:
                exec(f"VARIABLES['{msg[msg.index("lit")+3:msg.index("=")].strip()}'] = {eval(msg[msg.index("=")+1:].strip())}")

            elif "auto" in msg:
                    exec(f"{msg[msg.index("auto")+4:].strip()}")

            elif "package" in msg:
                now = i
                with open("package.txt", "w") as f:
                    f.write(f"{msg[msg.index("package")+7:].strip()}")
                    with open(f"{msg[msg.index("package")+7:].strip()}.moon", "w") as f2:
                        for line in lines[now+2:]:
                            f2.write(line)
                        
            elif "mut" in msg:
                exec(f"{msg[msg.index("mut")+3:].strip()}")

            elif "defer" in msg:
                global this_line
                this_line = msg
                pass

            elif "END" in msg and "{" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                global this_line2
                this_line2 = (
                    f"""
{BLOCK[:BLOCK.index("}")].strip()}
"""
                )

            elif "puts" in msg:
                if type(eval(msg[msg.index("puts")+4:].strip())) in [list, dict, set, tuple, frozenset]:
                    __pp__(eval(msg[msg.index("puts")+4:].strip()))
                else:
                    print(eval(msg[msg.index("puts")+4:].strip()))  

            elif "never" in msg:
                continue

            elif "type" in msg:
                exec(msg)

            elif "nonlocal" in msg:
                exec(msg)
            
            # elif "final" in msg:
                # k = msg[msg.index("final")+5:msg.index("=")].strip()
                # v = msg[msg.index("=")+1:].strip()
                # consts = namedtuple(k, [k])
                # c = consts(f"{k}={v}")
                # _ = k
                # value = getattr(c, k)
                # exec(f"{value[:value.index("=")].strip()} = {value[value.index("=")+1:].strip()}")

            # elif "readonly" in msg:
            #     k = msg[msg.index("readonly")+8:msg.index("=")].strip()
            #     v = msg[msg.index("=")+1:].strip()
            #     consts = namedtuple(k, [k])
            #     c = consts(f"{k}={v}")
            #     _ = k
            #     value = getattr(c, k)
            #     exec(f"{value[:value.index("=")].strip()} = {value[value.index("=")+1:].strip()}")

            elif "module" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open(f"{msg[msg.index("module")+6:msg.index(":")].strip()}.py", "w") as f:
                    f.write(f"{BLOCK[:BLOCK.index("end")].strip()}")

            elif "foreach" in msg and "as" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
for {msg[msg.index("foreach")+7:msg.index("as")].strip()} in {msg[msg.index("as")+3:msg.index(":")].strip()}:
    {BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "loop" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
while 1:
    {BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "forever" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
while 1:
    {BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "addr" in msg and "as" in msg:
                exec(f"{msg[msg.index("as")+2:].strip()} = ptr({msg[msg.index("addr")+4:msg.index("as")].strip()})")

            elif "say" in msg:
                print(eval(msg[msg.index("say")+3:]))
        
            elif "struct" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                if "def" in BLOCK:
                    raise SyntaxError("can't create functions in struct")
                exec(
                    f"""
class {msg[msg.index("struct")+6:msg.index(":")].strip()}:
    {BLOCK[:BLOCK.index("end")].strip()}
"""
                )

            elif "enum" in msg and "{" in msg and "}" in msg:
                exec(f"""{msg.split(' ')[1].strip()} =  {{{msg[msg.index('{')+1:msg.index("}")]}}}""")
                items = (eval(msg.split(' ')[1].strip())).values()
                items = str(items)[str(items).index("[")+1:str(items).index("]")].split(",")

                for n in range(len(items)):
                    t = __etype__(items[n].strip())
                    if t == int or t == float:
                        pass
                    else:
                        raise TypeError(f"Bad type for enum value. Expected int or float but {__etype__(items[n])} is given")
                    items[n] = t(items[n].strip())

            elif "enum" in msg and "=" in msg and not "{" in msg and not "}" in msg:
                exec(f"""{msg.split(" ")[1].strip()} = {eval(msg.split(" ")[2].strip())[eval(msg[msg.index("=")+1:].strip())]}""")

            elif "discard" in msg:
                __locals__.pop(msg[msg.index("discard")+7:].strip())

            elif "until" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
while {msg[msg.index("until")+5:].strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "local" in msg and "=" in msg:
                name = msg[msg.index("local")+5:msg.index("=")].strip()
                value = eval(msg[msg.index("=")+1:].strip())
                __locals__[name] = value
                name = __locals__[name]

            elif "my" in msg and "=" in msg:
                name = msg[msg.index("my")+2:msg.index("=")].strip()
                value = eval(msg[msg.index("=")+1:].strip())
                __locals__[name] = value
                name = __locals__[name]

            elif "our" in msg and "=" in msg:
                exec(f"{msg[msg.index("our")+3:].strip()}")

            elif "todo" in msg and "as" in msg:
                global m
                m = msg[msg.index("as")+2:].strip()
                todo_found = True
            
            elif "panic" in msg and "as" in msg:
                m = msg[msg.index("as")+2:].strip()
                panic_found = True

            elif "alias" in msg:
                exec(f"type {msg[msg.index("alias")+5:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}")

            elif "with" in msg and "as" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                print(
                    f"""
for {msg[msg.index("as")+2:msg.index(":")].strip()} in {msg[msg.index("with")+4:msg.index("as")].strip()}:
    {BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "async" in msg and "def" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif msg.startswith("$") and "=" in msg:

                # if msg[msg.index("$")+1:msg.index("=")].strip().isupper() or msg[msg.index("$")+1:msg.index("=")].strip()[0].isupper():
                    # if msg[msg.index("$")+1:msg.index("=")].strip() in __GLOBALS__.keys() or msg[msg.index("$")+1:msg.index("=")].strip() in __LOCALS__.keys():
                    #     print(YELLOW + f"Warning: already initialized constant '{msg[msg.index("$")+1:msg.index("=")].strip()}'" + BASE)
                        # raise Warning(YELLOW + f"Warning: already initialized constant '{msg[msg.index("$")+1:msg.index("=")].strip()}'" + BASE)
                    
                if "->" in msg:
                    exec(
                    f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = lambda {msg[msg.index("(")+1:msg.index(")")].strip()}: {msg[msg.index("->")+2:].strip()}
    """
                )

                elif msg[msg.index("=")+1:].strip().startswith("?"):
                    if len(msg[msg.index("?")+1:].strip()) > 1:
                        raise SyntaxError(f"? string should be char (length 1 needed, {len(msg[msg.index('?')+1:].strip())} is given)")
                    
                    if msg[msg.index("?")+1:].strip() == "'":
                        exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = "{msg[msg.index("?")+1:].strip()}"
    """
                    )
                        continue

                    exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = '{msg[msg.index("?")+1:].strip()}'
    """
                    )

                elif "%s" in msg[msg.index("=")+1:].strip() and "[" in msg and "]" in msg:
                    if "'" in msg[msg.index("%s[")+3:msg.index("]")].strip():
                        exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = "{msg[msg.index("%s[")+3:msg.index("]")].strip()}"
    """
                    )
                        continue

                    exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = '{msg[msg.index("%s[")+3:msg.index("]")].strip()}'
    """
                    )

                elif "%(" in msg[msg.index("=")+1:].strip() and ")" in msg[msg.index("=")+1:].strip():
                    if "'" in msg[msg.index("%(")+2:msg.index(")")].strip():
                        exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = "{msg[msg.index("%(")+2:msg.index(")")].strip()}"
    """
                    )
                        continue

                    exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = '{msg[msg.index("%(")+2:msg.index(")")].strip()}'
    """
                    )

                elif msg[msg.index("=")+1:].strip().startswith("!"):
                    exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = not {eval(msg[msg.index("!")+1:].strip())}
    """
                    )

                elif ".." in msg and "(" in msg and ")" in msg:
                    exec(
                        f"""
{msg[msg.index("$")+1:msg.index("=")].strip()} = range{msg[msg.index("=")+1:].strip().split("..")[0].strip()}, {msg[msg.index("=")+1:].strip().split("..")[1].strip()}
    """
                    )

                else:
                    exec(
                    f"""
{msg[msg.index("$")+1:msg.index("=")]} = {msg[msg.index('=')+1:].strip()}
    """
                )

            elif "require" in msg:
                exec(msg)

            elif "include" in msg:
                exec(msg)
                
            elif "next" in msg:
                continue

            elif "raise" in msg:
                exec(msg)

            elif "undef" in msg:
                exec(f"del {msg[msg.index("undef")+5:].strip()}")

            elif "def" in msg:
                if "self" in msg or "__init__" in msg:
                    continue
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "do" in msg and msg.count("|") == 2:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
try:
    with {msg[:msg.index("do")].strip()} as {msg.strip()[msg.index("|")+1:msg.index(":")-1].strip()}:
        {BLOCK[:BLOCK.index("end")].strip()}
except BaseException as e:
    print(e)
"""
                )

            elif "|>" in msg:
                items = msg.split("|>")
                for index in range(len(items)):
                    items[index] = items[index].strip()
                items.reverse()
                result = ""
                count = 0
                for each_elem in items:
                    count += 1
                    if count == len(items):
                        result += each_elem
                    else:
                        result += each_elem + "("
                exec(result + ")" * (count - 1))
            
            elif "elif" in msg: pass

            elif "if" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg.strip()}\n{BLOCK[:BLOCK.strip().index("end")+1]}
"""
                )

            elif "when" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
if {msg[msg.index("when")+4:].strip()}\n{BLOCK[:BLOCK.strip().index("end")+1]}
"""
                )

            elif "unless" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
while not {msg[msg.index("unless")+6:].strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )
            
            elif "dec" in msg:
                if "=" in msg:
                    raise SyntaxError("use of defining at declaring variable!")
                exec(f"{msg[msg.index("dec")+3:].strip()} = nil")

            elif "class" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg.strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "switch" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
match {msg[msg.index("switch")+6:].strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "match" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
match {msg[msg.index("match")+5:].strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "for" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg.strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "do" in msg:
                in_do = True
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{BLOCK[:BLOCK.index("while")].strip()}
{BLOCK[BLOCK.index("while"):BLOCK.index("end")].strip()}:\n{BLOCK[:BLOCK.index("while")]}
"""
                )
                continue

            elif "while" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg.strip()}\n{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "try" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
{msg.strip()}{BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "import" in msg:
                exec(msg)

            elif "add" in msg:
                nums = msg.split("add")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    result += eval(nums[i].strip())
                print(result)

            elif "sub" in msg:
                nums = msg.split("sub")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result += -(eval(nums[i].strip()))
                print(result)

            elif "mult" in msg:
                nums = msg.split("mult")
                result = 1
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    result *= eval(nums[i].strip())
                print(result)

            elif "div" in msg:
                nums = msg.split("div")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result /= eval(nums[i].strip())
                print(result)

            elif "pow" in msg:
                nums = msg.split("pow")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result **= eval(nums[i].strip())
                print(result)

            elif "mod" in msg:
                nums = msg.split("mod")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result %= eval(nums[i].strip())
                print(result)

            elif "xor" in msg:
                nums = msg.split("xor")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result ^= eval(nums[i].strip())
                print(result)

            elif "shr" in msg:
                nums = msg.split("shr")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result >>= eval(nums[i].strip())
                print(result)

            elif "shl" in msg:
                nums = msg.split("shl")
                result = 0
                for i in range(len(nums)):
                    nums[i] = nums[i].strip()
                    if i == 0:
                        result += eval(nums[i].strip())
                    if i != 0:
                        result <<= eval(nums[i].strip())
                print(result)
                
            elif "neq" in msg:
                first = eval(msg[:msg.index("neq")].strip())
                second = eval(msg[msg.index("neq")+3:].strip())
                print(first != second)
            
            elif "eq" in msg:
                first = eval(msg[:msg.index("eq")].strip())
                second = eval(msg[msg.index("eq")+2:].strip())
                print(first == second)

            elif "gt" in msg:
                first = eval(msg[:msg.index("gt")].strip())
                second = eval(msg[msg.index("gt")+2:].strip())
                print(first > second)

            elif "ge" in msg:
                first = eval(msg[:msg.index("ge")].strip())
                second = eval(msg[msg.index("ge")+2:].strip())
                print(first >= second)

            elif "lt" in msg:
                first = eval(msg[:msg.index("lt")].strip())
                second = eval(msg[msg.index("lt")+2:].strip())
                print(first < second)

            elif "le" in msg:
                first = eval(msg[:msg.index("le")].strip())
                second = eval(msg[msg.index("le")+2:].strip())
                print(first <= second)

            else:
                with open("undefined.log", "w") as f:
                    f.write(msg)

            # try:
            #     if __name__ == "__main__":
            #         main()
            # except NameError as e:
            #     if "name main is not defined" in str(e):
            #         pass
            #     else:
            #         raise NameError(e)

        except KeyboardInterrupt:
            print(UNDERLINE + 'Interrupt' + BASE)

        except BaseException as e:
            if msg.endswith("?"):
                print(f"{RED}error in line {i+1} \n=> Error, {e}{BASE}")
                continue
        
            type3 = f'File "{file}", in line {i+1}, in {BOLD}<main>{BASE}\n    {msg}\n    {'^' * len(msg.strip())}\n{e.__class__.__name__}: {e}\n'
            new_type = f'Error: {RED}moon::{e.__class__.__name__}{BASE}\n  {RED}×{BASE} {str(e).capitalize()}\n     ╭[{CYAN}entry #{i+1}{BASE}]\n     │ {BOLD}{UNDERLINE}{msg}{BASE}     .{" " * int(len(msg) / 2 - 1)}{PURPLE}─┬{BASE}\n     .{" " * int(len(msg) / 2)}{PURPLE}│{BASE}\n     .{" " * int(len(msg) / 2)}{PURPLE}╰──{BASE} {BOLD}here: at line {i+1}{BASE}\n     ╰────'

            
            new_type2 = f"""
{e.__class__.__name__}: {e}

    ┌─ {__FILE__}: {i+1}
    │
    │  {msg.strip()}
    │  {'^' * len(msg.strip())}  here
    

            """

            ERR = f"#<{e.__class__.__name__}: {e}>"
            VARIABLES['$!'] = f"{e.__class__.__name__}: {e}"

            if e.__class__ == IndentationError:
                # print(YELLOW + "IndentationWarning: unexpected indent" + f", line {BASE}{PURPLE}{i+1}" + BASE)
                continue
                
            if e.__class__ == SyntaxError and "expected 'except' or 'finally' block" in str(e):
                print(YELLOW + str(SyntaxError(f"immExpectation: expected 'except' or 'finally' block, line {PURPLE}{i+1}{BASE}")))
                continue

            if e.__class__ == Warning:
                # print(YELLOW + str(Warning("Warning: " + str(e) + BASE)))
                print(e)

            if "object of type 'mystery_t' has no len()" in str(e):
                new_type2 = f"""
{e.__class__.__name__}: {e}; {CYAN}mystery is mystery :){BASE}

    ┌─ {__FILE__}: {i+1}
    │
    │  {msg.strip()}
    │  {'^' * len(msg.strip())}  here
    

            """

            if e.__class__ == ZeroDivisionError:
                def x(): return undefined
                x()

            if ERR is not None:
                # __code__ = 0xdeadc0de
                __code__ = hex(3735929054)

            print(new_type2)

if show:
    print(f"processing time: {time.time() - start}s")

if todo_found:
    raise TodoError(f"todo found; This code will crash if it is ran. Be sure to finish it before running your program")

if panic_found:
    raise PanicError(f"panic found;")

try:
    exec(this_line[this_line.index("defer")+5:].strip())
except Exception as e:
    if "this_line" in str(e):
        pass
    else:
        raise BaseException(e)
    
try:
    exec(this_line2)
except NameError as e:
    if "this_line2" in str(e):
        pass
    else:
        raise NameError(e)