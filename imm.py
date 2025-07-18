"""
interpreter of main moon

running a script:

    in command line:

        moon FILE_NAME
"""

import sys
import types
import os
import time
import typing
import random
import platform
import math
from ast import literal_eval
from pprint import pprint as __pp__
from fractions import Fraction
from collections import namedtuple
# from warnings import deprecated
import re
from collections import Counter
import dis
from difflib import SequenceMatcher
from typing import Final
import functools
import warnings
import asyncio
import queue
import threading
from dataclasses import dataclass
import string
from icecream import ic
import traceback
import threading
import datetime
from dotenv import load_dotenv
from typing import TypeVar, Generic, Self
import inspect
import builtins

def bytecode(src):
    return dis.dis(compile(src, '<string>', 'exec'))

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
__VERSION__ = 5
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
ok = not ERR
Any = object()
# self = __NAME__

# T: TypeVar = TypeVar('T')
# E: TypeVar = TypeVar('E')

# class Result(Generic[T, E]): ...

# class Ok(Result[T, E]):
#     def __init__(self, value):
#         self.value = value

#     def __repr__(self):
#         return f"Ok({self.value!r})"

# class Error(Result[T, E]):
#     def __init__(self, error):
#         self.error = error

#     def __repr__(self):
#         return f"Error({self.error!r})"

class IO:

    def __rshift__(self, value):
        print(value)
    
    def __lshift__(self, prompt):
        return input(prompt)

    def __and__(self, v):
        return ptr(v)

    def __gt__(self, v):
        return v

IO = IO()

class STDOUT:
    def __rshift__(self, value):
        print(value, file=stdout)

class STDIN:
    def __lshift__(self, prompt):
        return input(prompt)

STDOUT = STDOUT()
STDIN = STDIN()

class Stack:

    stack = []

    def push(value):
        Stack.stack.append(value)

    def pop():
        return Stack.stack.pop()

    def top():
        return Stack.stack[-1]

    def print():
        print(Stack.stack.pop())

    def get():
        print(Stack.top())

    def all():
        print(Stack.stack)
    
    def add():
        Stack.stack.append(Stack.stack.pop() + Stack.stack.pop())

    def sub():
        Stack.stack.append(Stack.stack.pop() - Stack.stack.pop())

    def mult():
        Stack.stack.append(Stack.stack.pop() * Stack.stack.pop())

    def div():
        Stack.stack.append(Stack.stack.pop() / Stack.stack.pop())

    def pow():
        Stack.stack.append(Stack.stack.pop() ** Stack.stack.pop())

    def putchar(unicode_code):
        Stack.stack.append(chr(unicode_code))

keywords = [
    'true', 'false', 'nil', 'module', 'alias', 'dec', 'def', 'if', 'elif', 'else', 'until', 'unless', 'class', 'switch', 'case', 'while', 'for',
    'try', 'except', 'finally', 'async', 'await', 'end', 'yield', 'pass', 'continue', 'break', 'is', 'in', 'raise', 'return', 'and', 'or',
    'lambda', 'as', 'from', 'assert', 'del', 'global', 'not', 'with', 'puts', 'maybe', 'never', 'do', 'undef', 'True', 'False', 'import', 'None', 
    'match', 'todo', 'panic', 'when', 'foreach',  'add', 'sub', 'mult', 'div', 'pow', 'mod', 'xor', 'shr', 'shl', 'addr', 'type', 'struct', 'enum', 
    'say', 'eq', 'neq', 'gt', 'ge', 'lt', 'le', 'my', 'our', 'defer', 'END', 'discard', 'mut', 'package', 'auto', 'loop', 'lit', 'local', 'set', 
    'to', 'define', 'nonlocal', 'consume', 'static', 'forever', 'LUA', 'RB', 'ZIG', 'C', 'CPP', 'GLEAM', 'ASM', 'putv', 'var', 'fn', 'isnot', 
    'cast', 'inc', 'decr', 'macro', 'notin', 'also', 'before', 'after', 'perhaps', 'mirror', 'sleep', 'wait', 'mystery', 'nothing', 'undefined', 
    'unknown', 'Nil', 'HUGE_VAL', 'through', 'namespace', 'interface', 'again', 'block', 'does', 'awaitfor', 'ensure', 'fixme', 'has', 'lacks',
    'sqrt', 'cbrt', 'sin', 'cos', 'tan', 'log', 'ln', 'native', 'proc', 'let', 'fun', 'object', 'of', 'co', 'use', 'whilst', 'affirm', 
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
    return a, b

def load(expr):
    return lambda: exec(expr)

# def dofile(file=stdout):
#     if file != stdout:
#         with open(file, "r") as _f:
#             __clear_exec__()
#             for _line in _f.readlines():
#                 mexec(_line)
    
#     else:
#         _p = io.scanf()
#         __clear_exec__()
#         mexec(_p)
#     __clear_exec__()

class Symbol:

    def __init__(self, arg):
        self.arg = arg
        if not self.arg.strip().startswith(":"):
            raise NameError(f"symbol without ':' ?, try :{self.arg}")
    
    def __repr__(self) -> str:
        return self.arg

    def to_s(self):
        return str(self.arg[self.arg.index(":")+1:])

    def next(self):
        # gets next unicode char
        c = str(self.arg[self.arg.index(":")+1:])
        code = ord(c)
        return chr(code + 1)

    def startswith(self, with_what):
        if str(self.arg[self.arg.index(":")+1:]).startswith(with_what):
            return True
        return False

    def endswith(self, with_what):
        if str(self.arg[self.arg.index(":")+1:]).endswith(with_what):
            return True
        return False

    def __len__(self):
        return len(str(self.arg[self.arg.index(":")+1:]))

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
    
    # if value in [true, True, false, False]:
    #     return "#<bool>"
    
    # if value == maybe:
    #     return "#<maybe>"
    
    # if value in keywords:
    #     return "#<keyword>"
    
    # if value in __GLOBALS__ or value in __LOCALS__:
    #     return "#<built-in function or method or variable>"

    # if value == None:
    #     return "#<None>"

    # if value == inf:
    #     return "#<infinity>"
    
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

    
    # if value in [stdin, stdout, stderr]:
    #     return "#<stdio>"
    
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

def bytecode(code):
    code_obj = compile(code, '<string>', 'exec')
    return dis.dis(code_obj)

iota_counter = 0
def iota(reset = False):
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

def is_falsy(__obj):
    if __obj == '' or __obj == 0 or  __obj == false or __obj == False:
        return True
    else:
        return False

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

def to_n(value):
    return Nil

def to_d(key, value) -> dict:
    return { key : value }

def to_enum(value) -> enumerate:
    return enumerate(value)

def to_z(value) -> int:
    return 0

def to_r(value) -> Fraction:
    return Fraction(value)

def to_sym(value) -> Symbol:
    return Symbol(f":{value}")

def responds_to(__obj: object, __name: str) -> bool:
    return hasattr(__obj, __name)

__locals__ = {}
class Error(BaseException): ...
class TodoError(BaseException): ...
class PanicError(BaseException): ...
todo_found = False
panic_found = False
fixme_found = False

__locals__["\0"] = ''

def Ok(expression):
    try:
        eval(expression)
    except BaseException as e:
        return False, e
    return True

class Range:

    global alpha
    alpha = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
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

def __moon__(expr):
    # returns the expr which is with python syntax to moon syntax
    # don't have energy to complete this one, but i think it's a good idea :(
    ...

def __py__(expr):
    # returns the expr which is with moon syntax to py syntax
    # don't have energy to complete this one, but i think it's a good idea :(
    ...

pi = math.pi
e = math.e
tau = math.tau

def append(object, to_add):
    if type(object) == list:
        object.append(to_add)
    else:
        object += to_add
    
    return object

def split(string, with_what):
    return string.split(with_what)

def leq(a, b):
    # loose equal
    if type(a) in [int, float] and type(b) in [int, float]:
        return round(a) == round(b)    
    else:
        return a == b

def seq(a, b):
    # strict equal
    if type(a) == type(b) and a == b and ptr(a) == ptr(b) and id(a) == id(b):
        return True
    return False

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
        raise TypeError("cannot modify Nil")
    
    def __getattr__(self, name):
        print(f"[TRACE] accessed Nil attribute: {name}")
        return self
    
    def __len__(self):
        return 0
    
    def __iter__(self):
        return iter([])
    
    def __getitem__(self, idx):
        raise IndexError("Nil does not support item access")
    
    def __contains__(self, value):
        return False
    
    def __setitem__(self, idx, value):
        raise SyntaxError("Nil does not support item setting")
    
Nil = nil_t()
NilPtr = ptr(Nil)
NonePtr = ptr(None)

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

    def warn(msg=""):
        raise Warning(msg)
    
    def error(__type, msg):
        raise __type(msg)
        
    def putchar(code):
        return chr(code)
        
    def putchars(*codes):
        res = ""
        for code in codes:
            res += chr(code)
        
        return res

    def countc(string, what_char):
        count = 0
        for char in string:
            if char == what_char:
                count += 1

        return count

    def assertEqual(a, b):
        assert a == b, f"{a} and {b} are not equal"

    def assertTrue(a):
        assert a, f"{a} is not true"

    def assertFalse(a):
        assert not a, f"{a} is not false"

    def scanf(): 
        global _
        _ = input()
        return _

    def strlen(s: str):
        return len(s)

    def strcpy(s: str):
        return s

    def strcat(a: str, b: str):
        return a + b

    def atoi(s: str):
        return int(s)

    def atof(s: str):
        return float(s)

    def abort():
        io.exit(1)

    def alert(value):
        return Warning(YELLOW + value + BASE)

    def getenv(name):
        load_dotenv()
        return os.getenv(name)

    def echo(key):
        print(STACK[key])

    class mem:
        
        global POINTERS, STORE
        POINTERS = {}
        STORE = {}
        
        def __and__(self, value):
            POINTERS[ptr(value)] = value
            return ptr(value)

        def __mul__(self, pointer):
            return POINTERS[pointer]

        def recall(self, key):
            return STORE.get(key, Nil)

        def imprint(self, key, value):
            STORE[key] = value

        def forget(self, key):
            return STORE.pop(key)

        def clear(self):
            STORE.clear()
            return Nil

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

class NoMethodFoundError(BaseException): ...

class _KERNEL_META(type):
    def __getattr__(cls, name):
        frame = inspect.currentframe().f_back

        if name in frame.f_locals:
            return frame.f_locals[name]

        elif name in frame.f_globals:
            return frame.f_globals[name]

        elif hasattr(builtins, name):
            return getattr(builtins, name)
        
        else:
            raise NoMethodFoundError(f"Kernel has no attr {name}")
        
class Kernel(metaclass=_KERNEL_META): ...

class SizeError(Exception): ...
# def make(__type, message = "", size = None):
#     if size == None:
#         size = 0
#         return __type(message)
    
#     if size is not None and sizeof(__type(message)) > size:
#         raise SizeError(f"bigger size than expected, expect {size} but got {sizeof(__type(message))}")

#     return __type(message)

def make(T):
    if T == int:
        return 0

    elif T == float:
        return 0.0

    elif T == complex:
        return 0 + 1j

    elif T == str:
        return ""

    elif T == list:
        return []

    elif T == tuple:
        return tuple()

    elif T == range:
        return range(0, 1)

    elif T == dict:
        return dict()

    elif T == set:
        return set()

    elif T == frozenset:
        return frozenset()

    elif T == bool:
        return True

    elif T == bytes:
        return bytes()

    elif T == bytearray:
        return bytearray()

    elif T == memoryview:
        return memoryview

    elif T == None:
        return None

    elif T == Nil:
        return Nil

    elif T == Range:
        return Range(0, 1).new()

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

def parseInt(value):
    return int(value)

def parseFloat(value):
    return float(value)

def TEST():
    print(f"HI FROM {LINE}")

def debug(expr):
    try:
        expr
    except BaseException as e:
        return Error(), Nil, e
    else:
        return "OK", Nil

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

def unreachable(msg = ""):
    assert False, msg

class UnimplementedError(BaseException): ...

global unimplemented_found
def unimplemented():
    unimplemented_found = True
    raise UnimplementedError("this code is incomplete; complete it then run it again")

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
    def __init__(self, arg):
        self._frozen = False
        self.arg = arg
        setattr(self, to_s(arg), Nil)

    def __repr__(self):
        return to_s(self.arg)
    
    def freeze(self):
        self._frozen = True

    def __setattr__(self, name, value):
        if getattr(self, '_frozen', False) and name != '_frozen':
            raise AttributeError(f"object is frozen")
        super().__setattr__(name, value)

def DidYouMean2(a, b):
    return SequenceMatcher(None, a, b).ratio()

lable_names = []
__code__ = Nil
ALIASES = {}
INFO = {}

def var_dump(*values):
    for val in values:
        if val in [None, Nil, nil]:
            print(val)
            continue
        
        if type(val) in [int, float]:
            print(f"{val.__class__.__name__}({val})")
            continue
            
        print(f"{val.__class__.__name__}({len(val)}) {val}")

    return Nil

# class CONST:

#     global __vars
#     __vars = {}
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
#         if self.name in __vars.keys():
#             raise SyntaxError(f"already initialized constant {self.name}; Cannot recreate it")
        
#         __vars[self.name] = self.value

#     def __repr__(self):
#         return to_s(self.value)
    
#     def __set__(self):
#         raise SyntaxError(f"already initialized constant {self.name}; Cannot recreate it")


# def __def(name, value):
#     if (name + ptr(name)) not in globals():
#         globals()[name + ptr(name)] = value
    
#     else:
#         raise SyntaxError(f"already initialized constant {name}; Cannot recreate it")
    
# def __const(name):
#     return globals()[name + ptr(name)]

class visibility:
    _private_mode = False

    @classmethod
    def enable_private(cls):
        cls._private_mode = True

    @classmethod
    def disable_private(cls):
        cls._private_mode = False

    @staticmethod
    def private(func):
        visibility.enable_private()
        def wrapper(*args, **kwargs):
            if visibility._private_mode:
                raise PermissionError(f"trying to access the private '{func.__name__}'")
            return func(*args, **kwargs)
        return wrapper

def deprecated(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # warnings.warn(
            #     f"Function {func.__name__} is deprecated: {message}",
            #     category=DeprecationWarning,
            #     stacklevel=2
            # )
            print(Warning(YELLOW + f"Function {RED + func.__name__ + BASE + YELLOW} is deprecated: {CYAN + message}" + BASE))
            return func(*args, **kwargs)
        return wrapper
    return decorator

class iter:

    def __init__(self, n=0):
        self.n = n

    def times(self, func):
        for idx in range(self.n):
            func(idx)

    def each(self, func):
        for idx in range(len(self.n)):
            func(self.n[idx])

class expect:

    def __init__(self, value):
        self.value = value

    def toBeEqualTo(self, to):
        return self.value == to
    
    def toBeGreaterThan(self, than):
        return self.value > than
    
    def toBeLessThan(self, than):
        return self.value < than

    def toBeGreterEqualTo(self, to):
        return self.value >= to
    
    def toBeLessEqualTo(self, to):
        return self.value <= to

    def toBeNotEqualTo(self, to):
        return self.value != to

    def toBeIn(self, what):
        return self.value in what

    def toBeNotIn(self, what):
        return self.value not in what

ch = queue.Queue()
class chan:

    def send(value):
        ch.put(value)

    def get():
        return ch.get()

    def is_empty():
        return ch.empty()
    
    def is_full():
        return ch.full()

    def close():
        ch.shutdown()

    def size():
        return ch.qsize()

class RangeError(BaseException): ...

class short_int(int):
    def __init__(self, value):
        if not value in range(-32768, 32767+1):
            raise RangeError(f"{value} is not accessible in [-32768, 32767] ")
        super().__init__()

class ushort_int(int): 
    def __init__(self, value):
        if not value in range(0, 65535+1):
            raise RangeError(f"{value} is not accessible in [0, 65535] ")
        super().__init__()
        
class unsigned_int(int): 
    def __init__(self, value):
        if not value in range(0, 4294967295+1):
            raise RangeError(f"{value} is not accessible in [0, 4294967295] ")
        super().__init__()
        
class long_int(int): 
    def __init__(self, value):
        if not value in range(-2147483648, 2147483647+1):
            raise RangeError(f"{value} is not accessible in [-2147483648, 2147483647] ")
        super().__init__()
        
class ulong_int(int): 
    def __init__(self, value):
        if not value in range(0, 4294967295+1):
            raise RangeError(f"{value} is not accessible in [0, 4294967295] ")
        super().__init__()
        
class long_long_int(int): 
    def __init__(self, value):
        if not value in range(-(2**63), (2**63)+1):
            raise RangeError(f"{value} is not accessible in [-(2**63), (2**63)] ")
        super().__init__()
        
class ulong_long_int(int): 
    def __init__(self, value):
        if not value in range(0, 18446744073709551615+1):
            raise RangeError(f"{value} is not accessible in [0, 18446744073709551615] ")
        super().__init__()

class undoable:

    def __init__(self, init_state):
        self._history = [init_state.copy()]
        self._pointer = 0

    def set(self, key, value):
        current = self._history[self._pointer].copy()
        current[key] = value
        self._history = self._history[:self._pointer + 1]
        self._history.append(current)
        self._pointer += 1

    def get(self, key):
        return self._history[self._pointer][key]
    
    def undo(self):
        if self._pointer > 0:
            self._pointer -= 1

    def redo(self):
        if self._pointer < len(self._history) - 1:
            self._pointer += 1

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.set(key, value)

    def __repr__(self):
        return f"{self._history[self._pointer]}"

def call(fn, *args):
    return fn(*args)

def each(arr, fn):
    for elem in arr:
        yield fn(elem)

def take(arr, n):
    res = []
    for idx in range(len(arr)):
        if idx == n:
            break
        res.append(arr[idx])
    return res

def assert_equal(a, b):
    assert a == b, f"{a} and {b} are not equal"

def assert_type(a, b):
    assert typeof(a) == typeof(b), f"{a} and {b} are not with same type"

def retry(fn, *args, count=3):
    done = 0
    while done < count:
        io.sprint(fn(*args))
        done += 1
    return Nil

def __random__():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

class FixMeError(BaseException): ...

# class String(str): ...
# class Integer(int): ...
# class Float(float): ...
# class Complex(complex): ...
# class Array(list): ...
# class Dict(dict): ...
# class Set(set): ...
# class Tuple(tuple): ...

def String(value):
    return str(value)

def Number(value):
    if __etype__(value) == int:
        return int(value)
    
    elif __etype__(value) == float:
        return float(value)
    
    else:
        return nan
    
def Bool(value):
    return bool(value)

π = math.pi
e = math.e
𝜏 = math.tau

def define_singleton_method(name, value):
    globals()[name] = value
    return Nil

STACK = {}

class void_t:
    def __len__(self):
        return 0
    
    def __repr__(self):
        return "void"
    
    def __bool__(self):
        return False
    
    def __add__(self, v):
        return v
    
void = void_t()
_G = __GLOBALS__
_V = __VERSION__

class _list(list):
    
    def __init__(self, iterable):
        self.it = iterable

    def __lshift__(self, value):
        self.it.append(value)
        return self.it

    def __repr__(self):
        return to_s(self.it)
    
    @property
    def first(self):
        return self.it[0]
    
    @property
    def last(self):
        return self.it[-1]

class _str(str):
    
    def __init__(self, value):
        self.v = value

    def __lshift__(self, value):
        self.v += value
        return self.v

class channel:

    def __init__(self, __type):
        self.t = __type
        self.ch = queue.Queue()

    def __rshift__(self, value):
        if type(value) == self.t:
            self.ch.put(value)

        else:
            raise TypeError(f"expected {self.t} but got {type(value)}")

    def __lshift__(self, value):
        if value in [void, Nil, nil, None]:
            return self.ch.get()

        else:
            raise NameError(f"{value} is not acceptible, use void or Nil or nil or None")

    def __gt__(self, value):
        if type(value) == self.t:
            self.ch.put_nowait(value)

        else:
            raise TypeError(f"expected {self.t} but got {type(value)}")

    def __lt__(self, value):
        if value in [void, Nil, nil, None]:
            return self.ch.get_nowait()

        else:
            raise NameError(f"{value} is not acceptible, use void or Nil or nil or None")

    # def isEmpty(self):
    #     return self.ch.empty()

    # def isFull(self):
    #     return self.ch.full()

    # def size(self):
    #     return self.ch.qsize() 

def callMain():
    try:
        exec("main()")
    except NameError:
        pass

with open(argv[1], "r") as file:
    lines = file.readlines()

    for i in range(len(lines)):
        LINE = i + 1
        file = sys.argv[1]
        file = file.strip()

        msg = lines[i]
        __line__ = msg

        try:
            if "#" in msg or msg.strip() == "":
                continue

            elif ":=" in msg:
                exec(f"{msg[:msg.index(":=")].strip()} = {msg[msg.index(":=")+2:].strip()}")
            
            elif msg.strip().endswith("!"):
                exec(f"{msg[:msg.strip().index("!")]}")

            elif msg.strip().endswith("?"):
                try:
                    eval(msg[:msg.strip().index('?')].strip())
                except BaseException as e:
                    print(f"{RED}{e.__class__.__name__}: {CYAN}{e}{BASE}")
                else:
                    pass

#            elif len(msg.strip().split(" ")) == 2 and msg.strip().startswith("'"):
#                exec(f"{msg.split()[0][msg.index("'")+1:].strip()}({msg.split()[1].strip()})")
            
            elif msg.startswith("&"):
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(f"{msg[msg.index("&")+1:]}{BLOCK[:BLOCK.index("end")]}")
            
            # elif "COMMENT" in msg and "(" in msg:
            #     BLOCK = ""
            #     items = [lines[x] for x in range(i+1, len(lines))]
            #     for k in range(len(items)):
            #         for n in items[k]:
            #             BLOCK += n
            #     continue

            elif "CPP" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.cpp", "w") as f:
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
            
            elif "require" in msg or "include" in msg:
                try:
                    exec(f"import {msg.split()[1].strip()}")
                except ModuleNotFoundError as e:
                    if "require" in msg:
                        raise e

                    elif "include" in msg:
                        raise Warning(e)
                
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

                    elif "through" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1].strip()}Range({msg[msg.index("=")+1:msg.index("through")]}, {msg[msg.index("through")+7:].strip()}).new()")

                    elif "(" in msg and ")" in msg and ";" in msg:
                        messages = msg[msg.index("(")+1:msg.index(")")].split(";")
                        for idx in range(len(messages)):
                            if messages[idx] == messages[-1]:
                                exec(f"{msg[msg.index("var")+3:msg.index("=")+1].strip()} {messages[idx].strip()}")
                            else:
                                exec(messages[idx].strip())

                    elif "<=>" in msg:
                        first_one = msg[msg.index("=")+1:msg.index("<=>")].strip()
                        second_one = msg[msg.index("<=>")+3:].strip()
                        if eval(first_one) > eval(second_one):
                            exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}1")
                        elif eval(second_one) > eval(first_one):
                            exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}-1")
                        elif eval(first_one) == eval(second_one):
                            exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}0")
                            
                    elif "=>" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("=>")].strip()}({msg[msg.index("=>")+2:].strip()})")

                    elif "<=" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("<=")].strip()}()")

                    elif "add" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("add")]}+{msg[msg.index("add")+3:]}")

                    elif "sub" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("sub")]}-{msg[msg.index("sub")+3:]}")

                    elif "div" in msg and not "/" in msg:
                        try:
                            exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("div")]}/{msg[msg.index("div")+3:]}")
                        except ZeroDivisionError as e:
                            exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {undefined}")

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

                    elif "notin" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:msg.index("notin")].strip()} not in {msg[msg.index("notin")+5:].strip()}")

                    elif "sqrt" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.sqrt({msg[msg.index("sqrt")+4:].strip()})")
                    
                    elif "cbrt" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.cbrt({msg[msg.index("cbrt")+4:].strip()})")

                    elif "log" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.log10({msg[msg.index("log")+3:].strip()})")
                    
                    elif "ln" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.log({msg[msg.index("ln")+2:].strip()})")

                    elif "sin" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.sin({msg[msg.index("sin")+3:].strip()})")

                    elif "cos" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.cos({msg[msg.index("cos")+3:].strip()})")

                    elif "tan" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = math.tan({msg[msg.index("tan")+3:].strip()})")

                    elif "cot" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = 1/math.tan({msg[msg.index("cot")+3:].strip()})")

                    elif "|>" in msg:
                        items = msg[msg.index("=")+1:].split("|>")
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
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1].strip()}{result + ")" * (count - 1)}")

                    elif "~=" in msg:
                        first_one = msg[msg.index("=")+1:msg.index("~=")].strip()
                        second_one = msg[msg.index("~=")+2:].strip()
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}leq({first_one}, {second_one})")

                    elif "===" in msg:
                        first_one = msg[msg.index("=")+1:msg.index("===")].strip()
                        second_one = msg[msg.index("===")+3:].strip()
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}seq({first_one}, {second_one})")

                    elif "?" in msg and ":" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}{msg[msg.index("?")+1:msg.index(":")]} if {msg[msg.index("=")+1:msg.index("?")]} else {msg[msg.index(":")+1:]}")

                    elif "??" in msg:
                        try:
                            exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}{msg[msg.index("=")+1:msg.index("??")]}")
                        except:
                            exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}{msg[msg.index("??")+2:].strip()}")

                    elif "if" in msg:
                        BLOCK = ""
                        items = [lines[x] for x in range(i+1, len(lines))]
                        for k in range(len(items)):
                            for n in items[k]:
                                BLOCK += n
                                
                        exec(
f"""{msg[msg.index("=")+1:].strip()} 
    {msg[msg.index("var")+3:msg.index("=")+1].strip()} {BLOCK[:BLOCK.index("else")].strip()}
{BLOCK[BLOCK.index("else"):BLOCK.index(":")+1].strip()}
    {msg[msg.index("var")+3:msg.index("=")+1].strip()} {BLOCK[BLOCK.index(":")+1:BLOCK.index("end")].strip()}

""")

                    elif "do" in msg:
                        BLOCK = ""
                        items = [lines[x] for x in range(i+1, len(lines))]
                        for k in range(len(items)):
                            for n in items[k]:
                                BLOCK += n

                        exec(f"""

def __{msg[msg.index("var")+3:msg.index("=")].strip()}(): 
{BLOCK[:BLOCK.index("end")]}

{msg[msg.index("var")+3:msg.index("=")].strip()} = __{msg[msg.index("var")+3:msg.index("=")].strip()}()
if {msg[msg.index("var")+3:msg.index("=")].strip()} == "main":
    {msg[msg.index("var")+3:msg.index("=")].strip()}


""")   
                    
                    elif "await" in msg:
                        body = msg[msg.index("=")+1:].split()
                        exec(
                            f"""
async def __{msg[msg.index("var")+3:msg.index("=")].strip()}():
    await asyncio.sleep({body[1]})
    {body[2]}

{msg[msg.index("var")+3:msg.index("=")].strip()} = asyncio.run(__{msg[msg.index("var")+3:msg.index("=")].strip()}())
"""

                        )

                    elif "has" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}{msg[msg.index("has")+3:].strip()} in {msg[msg.index("=")+1:msg.index("has")].strip()}")
                    
                    elif "lacks" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()}{msg[msg.index("lacks")+5:].strip()} not in {msg[msg.index("=")+1:msg.index("lacks")].strip()}")

                    elif msg.count("|") == 2:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} abs({msg.strip()[msg.index("|")+1:-1].strip()})")

                    elif msg.strip().endswith("!"):
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} math.factorial({msg[msg.index("=")+1:msg.index("!")].strip()})")

                    elif "_f" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} float({msg[msg.index("=")+1:msg.index("_f")].strip()})")

                    elif "_i" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} int({msg[msg.index("=")+1:msg.index("_i")].strip()})")

                    elif "_s" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} str({msg[msg.index("=")+1:msg.index("_s")].strip()})")

                    elif "_b" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} bool({msg[msg.index("=")+1:msg.index("_b")].strip()})")
                    
                    elif ":" in msg:
                        exec(f"{msg[msg.index("var")+3:msg.index("=")+1:].strip()} {eval(msg[msg.index("=")+1:msg.index(":")].strip()).__class__.__name__}({msg[msg.index("=")+1:msg.index(":")].strip()}).{msg[msg.index(":")+1:]}")

                    else:
                        try:
                            exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}")
                        except ZeroDivisionError as e:
                            exec(f"{msg[msg.index("var")+3:msg.index("=")].strip()} = {undefined}")

            # elif ">>" in msg or "<<" in msg:
            #     exec(msg)
                
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

            elif "<" in msg and ">" in msg: 
                exec(msg[msg.index("<")+1:msg.index(">")])
            
            elif msg.count('`') == 2:
                system(msg.strip()[msg.index("`")+1:-1].strip())

            elif "puts" in msg:
                if type(eval(msg[msg.index("puts")+4:].strip())) in [list, dict, set, tuple, frozenset]:
                    __pp__(eval(msg[msg.index("puts")+4:].strip()))
                else:
                    print(eval(msg[msg.index("puts")+4:].strip())) 
            
            # elif "test" in msg:
            #     BLOCK = ""
            #     items = [lines[x] for x in range(i+1, len(lines))]
            #     for k in range(len(items)):
            #         for n in items[k]:
            #             BLOCK += n


            elif "use" in msg:
                exec(f"from {msg[msg.index("use")+3:msg.index(".")].strip()} import {msg[msg.index(".")+1:].strip()}")
            
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
                    
            elif "let" in msg and not "if" in msg:
                STACK[f"{msg[msg.index("let")+3:msg.index("=")].strip()}"] = eval(msg[msg.index("=")+1:])

            elif "fun" in msg:
                # if "," in msg[msg.index("(")+1:msg.index(")")]:
                global args
                args = msg[msg.index("(")+1:msg.index(")")].split(",")
                args = {arg.strip(): None for arg in args}
                
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n

                __todo = BLOCK[:BLOCK.index("end")]
                args["todo"] = __todo.strip()
                STACK[f"{msg[msg.index("fun")+3:msg.index("(")].strip()}"] = args

                # else:
                #     ...

            elif msg.strip().startswith("%"):
                works = STACK[msg[msg.index("%")+1:msg.index("(")]]
                # if "," in msg[msg.index("(")+1:msg.index(")")]:
                values = msg[msg.index("(")+1:msg.index(")")].split(",")
                todo = works.popitem()
                if len(works) != len(values):
                    raise KeyError("not enough or more")
                else:
                    pass

                for j in range(len(values)):
                    if __etype__(values[j].strip()) == int or __etype__(values[j].strip()) == float:
                        values[j] = eval(values[j].strip())
                    else:
                        values[j] = (values[j].strip())

                works = dict(zip(works.keys(), values))
                for k in works.keys():
                    try:
                        nk = k
                        if nk == "":
                            nk = __random__()
                        exec(f"{nk} = {works[k]}")
                    except BaseException as e:
                        raise e.__class__(e)
                
                todos = todo[1].split("\n")
                for a_todo in todos:
                    exec(a_todo.strip())

            elif "co" in msg:
                exec(f"threading.Thread(target={msg[msg.index("co")+2:msg.index("(")].strip()}).start()")

            elif "object" in msg and "of" in msg and "=" in msg:
                exec(f"{msg[:msg.index('object')]} {msg[msg.index('of')+2:msg.index("{")].strip()}({msg[msg.index('{')+1:msg.index('}')]})")

            elif "object" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                items = BLOCK[:BLOCK.index("end")].strip().split(",")
                res = ""
                for j in range(len(items)):
                    res += f"self.{items[j].strip()} = {items[j].strip()}\n        "

                try:
                    exec(f"""
class {msg[msg.index("object")+6:msg.index(":")].strip()}:
    def __init__(self, {BLOCK[:BLOCK.index("end")].strip()}):
        {res.strip()}  
"""
                )
                except BaseException as e:
                    raise e.__class__(e)

            elif "awaitfor" in msg:
                rand_name_for_async_func = f"__{__random__()}__"
                exec(
                    f"""
async def {rand_name_for_async_func}():
    await asyncio.sleep({msg[:msg.index("awaitfor")].strip()})
    {msg[msg.index("awaitfor")+8:].strip()}
asyncio.run({rand_name_for_async_func}())

"""
                )

            elif ":" in msg and not "def" in msg and not "class" in msg and not "if" in msg and not "elif" in msg and not "else" in msg and not "for" in msg and not "while" in msg\
                and not "module" in msg and not "def" in msg and not "until" in msg and not "unless" in msg and not "switch" in msg and not "case" in msg and not "try" in msg \
                and not "except" in msg and not "finally" in msg and not "struct" in msg and not "foreach" in msg and not "when" in msg and not "match" in msg and not "loop" in msg\
                and not "forever" in msg and not "block" in msg and not "namespace" in msg and not "interface" in msg and not "fun" in msg and not "object":
                exec(f"print({eval(msg[:msg.index(":")]).__class__.__name__}({msg[:msg.index(":")]}).{msg[msg.index(":")+1:]})")

            # elif ":" in msg:
            #     exec(f"print({eval(msg[:msg.index(":")]).__class__.__name__}({msg[:msg.index(":")]}).{msg[msg.index(":")+1:]})")

            elif "ensure" in msg:
                exec(f"assert {msg[msg.index("ensure")+6:]}")

            elif "affirm" in msg:
                exec(f"assert {msg[msg.index("affirm")+6:]}")

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

            elif "sleep" in msg and not "io" in msg and not "time" in msg and not "asyncio" in msg:
                time.sleep(float(msg[msg.index("sleep")+5:].strip()))

            elif "wait" in msg:
                time.sleep(float(msg[msg.index("wait")+4:].strip()))          

            elif "inc" in msg:
                exec(f"{msg[msg.index("inc")+3:].strip()} += 1")

            elif "decr" in msg:
                exec(f"{msg[msg.index("decr")+4:].strip()} -= 1")

            elif "lable" in msg and ":" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                lable_names.append(msg[msg.index("lable")+5:msg.index(":")].strip())
                exec(
                    f"""
def {msg[msg.index("lable")+5:msg.index(":")].strip()}():
    {BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "goto" in msg:
                name = msg[msg.index("goto")+4:].strip()
                if name in lable_names:
                    exec(f"{name}()")
                
                else:
                    raise NameError(f"{name} is not defined")

            elif "proc" in msg:
                exec(
                    f"""
def {msg[msg.index("proc")+4:msg.index("=")]}:
    {msg[msg.index("=")+1:]}

"""
                )

            elif "block" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n

                exec(
                    f"""
def {msg[msg.index("block")+5:msg.index(":")]}():
    {BLOCK[:BLOCK.index("end")]}
"""
                )

            elif "does" in msg:
                exec(f"{msg[msg.index("does")+4:].strip()}()")

            elif "again" in msg:
                previous_line = lines[i-1]
                __clear_exec__()
                mexec(previous_line)

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

            elif "macro" in msg:
                if "(" in msg and ")" in msg:
                    exec(
                        f"""
def {msg[msg.index("macro")+5:msg.index(")")+1]}: return {msg[msg.index(")")+1:].strip()}
"""
                    )

                elif not "(" in msg and not ")" in msg:
                    items = msg.split()
                    exec(f"{items[1]} = {items[2]}")


            elif "@" in msg and "=" in msg:
                exec(
                    f"""
class {__name__}:
    {msg[msg.index("@")+1:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}
"""                    
)

            # elif "@" in msg and not "=" in msg:
            #     BLOCK = ""
            #     items = [lines[x] for x in range(i+1, len(lines))]
            #     for k in range(len(items)):
            #         for n in items[k]:
            #             BLOCK += n

            #     exec(
            #         f"{msg}{BLOCK[:BLOCK.index("end")]}"
            #     )
                
            elif "set" in msg and "to" in msg:
                exec(f"{msg[msg.index("set")+3:msg.index("to")].strip()} = {msg[msg.index("to")+2:].strip()}")

            elif "consume" in msg and "to" in msg:
                exec(f"{msg[msg.index("to")+2:].strip()} = {msg[msg.index("consume")+7:msg.index("to")].strip()}; {msg[msg.index("consume")+7:msg.index("to")].strip()} = Nil")

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
{BLOCK[:BLOCK.index("end")]}
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

            elif "namespace" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
                    f"""
class {msg[msg.index("namespace")+9:msg.index(":")]}:
{BLOCK[:BLOCK.index("end")]}

"""
                )

            elif "interface" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n

                exec(
                    f"""
class {msg[msg.index("interface")+9:msg.index(":")]}:
{BLOCK[:BLOCK.index("end")]}

"""
                )

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

            elif "native" in msg and "=" in msg:
                name = msg[msg.index("native")+6:msg.index("=")].strip()
                value = eval(msg[msg.index("=")+1:].strip())
                __locals__[name] = value
                name = __locals__[name]

            elif "our" in msg and "=" in msg:
                exec(f"{msg[msg.index("our")+3:].strip()}")

            elif "todo" in msg and "as" in msg:
                # global m
                # m = msg[msg.index("as")+2:].strip()
                # todo_found = True
                # line_todo = i + 1
                raise TodoError(f"todo found; {msg[msg.index("as")+2:]}")

            elif "fixme" in msg and "as" in msg:
                # m = msg[msg.index("as")+2:].strip()
                # fixme_found = True
                # line_fixme = i + 1
                raise FixMeError(f"fixme found; this code needs fixing; {msg[msg.index("as")+2:]}")
            
            elif "panic" in msg and "as" in msg:
                # m = msg[msg.index("as")+2:].strip()
                # panic_found = True
                # line_panic = i + 1
                raise PanicError(f"panic; {msg[msg.index("as")+2:]}")

            elif "alias" in msg:
                exec(f"type {msg[msg.index("alias")+5:msg.index("=")].strip()} = {msg[msg.index("=")+1:].strip()}")

            elif "with" in msg and "as" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                exec(
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
            
            elif "if" in msg and "let" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n

                exec(
                    f"""
if {msg[msg.index("let")+3:msg.index("as")].strip()} is not None:
    {msg[msg.index("as")+2:msg.index(":")].strip()} = {msg[msg.index("let")+3:msg.index("as")].strip()}
    {BLOCK[:BLOCK.index("end")].strip()}

"""
                )
            
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

            elif "whilst" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                msg = msg.replace("whilst", "while")
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

            elif "import" in msg or "assert" in msg:
                exec(msg)

            elif "C" in msg and "(" in msg:
                BLOCK = ""
                items = [lines[x] for x in range(i+1, len(lines))]
                for k in range(len(items)):
                    for n in items[k]:
                        BLOCK += n
                with open("__main__.c", "w") as f:
                    f.write(BLOCK[:BLOCK.index(") end")])

            # elif "add" in msg:
            #     nums = msg.split("add")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         result += eval(nums[i].strip())
            #     print(result)

            # elif "sub" in msg:
            #     nums = msg.split("sub")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result += -(eval(nums[i].strip()))
            #     print(result)

            # elif "mult" in msg:
            #     nums = msg.split("mult")
            #     result = 1
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         result *= eval(nums[i].strip())
            #     print(result)

            # elif "div" in msg:
            #     nums = msg.split("div")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result /= eval(nums[i].strip())
            #     print(result)

            # elif "pow" in msg:
            #     nums = msg.split("pow")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result **= eval(nums[i].strip())
            #     print(result)

            # elif "mod" in msg:
            #     nums = msg.split("mod")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result %= eval(nums[i].strip())
            #     print(result)

            # elif "xor" in msg:
            #     nums = msg.split("xor")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result ^= eval(nums[i].strip())
            #     print(result)

            # elif "shr" in msg:
            #     nums = msg.split("shr")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result >>= eval(nums[i].strip())
            #     print(result)

            # elif "shl" in msg:
            #     nums = msg.split("shl")
            #     result = 0
            #     for i in range(len(nums)):
            #         nums[i] = nums[i].strip()
            #         if i == 0:
            #             result += eval(nums[i].strip())
            #         if i != 0:
            #             result <<= eval(nums[i].strip())
            #     print(result)
                
            # elif "neq" in msg:
            #     first = eval(msg[:msg.index("neq")].strip())
            #     second = eval(msg[msg.index("neq")+3:].strip())
            #     print(first != second)
            
            # elif "eq" in msg:
            #     first = eval(msg[:msg.index("eq")].strip())
            #     second = eval(msg[msg.index("eq")+2:].strip())
            #     print(first == second)

            # elif "gt" in msg:
            #     first = eval(msg[:msg.index("gt")].strip())
            #     second = eval(msg[msg.index("gt")+2:].strip())
            #     print(first > second)

            # elif "ge" in msg:
            #     first = eval(msg[:msg.index("ge")].strip())
            #     second = eval(msg[msg.index("ge")+2:].strip())
            #     print(first >= second)

            # elif "lt" in msg:
            #     first = eval(msg[:msg.index("lt")].strip())
            #     second = eval(msg[msg.index("lt")+2:].strip())
            #     print(first < second)

            # elif "le" in msg:
            #     first = eval(msg[:msg.index("le")].strip())
            #     second = eval(msg[msg.index("le")+2:].strip())
            #     print(first <= second)

            else:
                with open("undefined.log", "w") as f:
                    f.write(msg)

                # for idx in range(len(keywords)):
                #     if DidYouMean2(msg, keywords[idx]) >= 0.7:
                #         raise NameError(f"Did You Mean '{keywords[idx]}'?")

            # try:
            #     if __name__ == "__main__":
            #         main()
            # except NameError as e:
            #     if "name main is not defined" in str(e):
            #         pass
            #     else:
            #         raise NameError(e)
            INFO[i + 1] = True

        except KeyboardInterrupt:
            print(UNDERLINE + 'Interrupt' + BASE)

        except TodoError as e:
#             print(f"""
# {e.__class__.__name__}: {e}

#     ┌─ {__FILE__}: {i+1}
#     │
#     │  {msg.strip()}
#     │  {'^' * len(msg.strip())}  here
    

#             """)
            tb = traceback.extract_tb(sys.exc_info()[2])
            res = ""  
            for f in tb:
                res += f"[py]: {f.lineno}: in {f.name}\n\t"
            res += f"[moon]: {i+1}: in {__FILE__}"

            print(f"""{__FILE__}: {i+1}: {e}
stack traceback:
        {res}
""")
            break

        except PanicError as e:
#             print(f"""
# {e.__class__.__name__}: {e}

#     ┌─ {__FILE__}: {i+1}
#     │
#     │  {msg.strip()}
#     │  {'^' * len(msg.strip())}  here
    

#             """)
            tb = traceback.extract_tb(sys.exc_info()[2])
            res = ""  
            for f in tb:
                res += f"[py]: {f.lineno}: in {f.name}\n\t"
            res += f"[moon]: {i+1}: in {__FILE__}"

            print(f"""{__FILE__}: {i+1}: {e}
stack traceback:
        {res}
""")
            break

#         except FixMeError as e:
#             print(f"""
# {e.__class__.__name__}: {e}

#     ┌─ {__FILE__}: {i+1}
#     │
#     │  {msg.strip()}
#     │  {'^' * len(msg.strip())}  here
    

#             """)

        # except DeprecationWarning as e:
            # print("got it")

        except BaseException as e:
            # raise e.__class__(e)

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


            tb = traceback.extract_tb(sys.exc_info()[2])
            res = ""  
            for f in tb:
                res += f"[py]: {f.lineno}: in {f.name}\n\t"
            res += f"[moon]: {i+1}: in {__FILE__}"

            new_type3 = f"""{__FILE__}: {i+1}: {e} ({UNDERLINE}{BOLD}{e.__class__.__name__}{BASE})
stack traceback:
        {res}
"""

            ERR = f"#<{e.__class__.__name__}: {e}>"
            VARIABLES['$!'] = f"{e.__class__.__name__}: {e}"

            if e.__class__ == IndentationError:
                # print(YELLOW + "IndentationWarning: unexpected indent" + f", line {BASE}{PURPLE}{i+1}" + BASE)
                continue
                
            if e.__class__ == SyntaxError and "expected 'except' or 'finally' block" in str(e):
                print(YELLOW + str(SyntaxError(f"SyntaxError: expected 'except' or 'finally' block, line {PURPLE}{i+1}{BASE}")))
                continue

            if e.__class__ == Warning:
                print(YELLOW + str(Warning("Warning: " + str(e) + BASE)))
                continue


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

            # print(type3)
            # print(new_type)
            # print(new_type2)
            print(new_type3)
            INFO[i + 1] = False
            break

if show:
    print(f"processing time: {time.time() - start}s")

# if todo_found:
#     raise TodoError(f"todo found; be sure to finish it before running your program; at line {line_todo}")

# if panic_found:
#     raise PanicError(f"panic found; at line {line_panic}")

# if fixme_found:
#     raise FixMeError(f"this code needs fixing; at line {line_fixme}")

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

callMain()

