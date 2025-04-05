# Moon programming language

# Variables:

    $name = "mobin"
    # this makes 'name' variable
    grade = 'A'!
    # normal one
    number := 5
    # another way to create a variable, it's by :=
    my number = 0
    # creating local variable by 'my'
    local name = "Mobin"
    # creating local variable by 'local'
    our grade = 'A'
    # normal variable
    lit $n = 0
    # creating variables with lit
    set n to 8
    # creating variables with set and to

# lit
this is a keyword to make a varaible, but this will be saved into VARIABLES dict!
maybe we can call it another version of local variables
but you access these variables only with io.vprint or io.vprintln or io.vprintf

    lit $name = "Mobin"
    io.vprintln('$name')!

# Comments:
as you see in code, we use '#' for writing comments
    
    # moon is a programming language

# OOP:
moon is a object-oriented programming language
    
    class Car:
	    def __init__(self, name, year):
		    self.name = name
		    self.year = year
    end
    # you should end the block with end
    # but only the first block needs end
    # so you do not need to use end for '__init__'
    
    BMW = Car("BMW", 2024)
    # creating an instance of Car
    io.print(BMW)!
    # for calling function there are some ways

# Calling functions:

    io.print("moon")!
    # end with '!' for calling it

    <io.print("moon")>
    # write it between '<' and '>'

    io.sprint -> "moon"
    # use '->'
    # but '->' prints the result
    # so we use io.sprint for not getting nil
    # because io.print at the end returns nil

    # so:
    $x = io.print("moon")
    io.print(x == nil)!
    # True

    def say_hello():
        io.print("hello")
    end
    say_hello <-
    # if the function gets no parameter, you can call it with <-
    # you can also call this function (that takes no param) like this:
    # say_hello -> 

    io.print => "hello"
    # this will not print the result
    # so we do not take nil (e.g. in printing)

    say_hello <=
    # if the function gets no parameter, you can call it with <=
    # you can also call this function (that takes no param) like this:
    # say_hello => 
    # but as i said, it does not print the result !

# if - elif - else:

    if True:
        io.print("one")
    elif True:
        io.print("two")
    else:
        io.print("three")
    # one

# alpha-numbers:

there are alpha-numbers in moon
like one, two, ...

    io.print(one + two)
    # 3
    # it is from one to ten, not higher

    # but you can make it like
    # eleven = "1" + "1"
    # so:
    $eleven = to_i(to_s(one) + to_s(one))
    # to_s function return the string type of the param
    # to_i function return the int type of the param
    # as same as: int("1" + "1")

# Lambda functions:

    $double  = lambda a: a * 2
    $double2 = (a) -> a * 2

# Loops:

    for x in [1, 2]:
        io.print(x)
        # 1
        # 2
    end

    $x = 0
    while x < 5:
        io.print(x)
        x += 1
        # 1 
        # ...
        # 4
    end

    $x = 0
    until x < 5:
        io.print(x)
        x += 1
        # 1 ... 4
    end

    $x = 0
    unless x == 5:
        io.print(x)
        x += 1
        # 1 .. 4
    end

    $list = Range('d', 'f').new()
    foreach elem as list:
        printf(elem)
    end

# Pipeline:

    nil |> typeof |> io.print
    # this is as same as:
    io.print(typeof(nil))
    # #<nil>

# switch-case:

    $name = "mobin"
    switch name:
        case "mobin":
        # if name == "mobin": ...
            io.print("author")
        case _:
        # else: ...
            io.print("user")
    end
    # "case _" means else !

# do-block

    # FUNCTION_OR_STH do |NAME|:
    #   ...
    # end
    io.open("main.txt", "r") do |file|:
        io.printf("%s", io.freads(file))
    end

# io

io is one of the built-in classes, it has so GOOOOD functions you can use in your program

    print(*values, sep="\t") -> nil
    # prints values with seperator \t (of course you can change it !) and at the end it does not print a new line, and returns nil

    println(*values, sep="\t") -> nil
    # prints values with seperator \t (of course you can change it !) and at the end it prints a new line, and returns nil

    throw(__err, message: str = "") -> NoReturn
    # raises the __err ( MUST be derived from BaseException ) with message message

    open(file, mode) -> IO_WRAPER
    # opens the file with mode mode

    freads(file) -> list
    # reads lines from file

    fread(file) -> str
    # reads a line from file

    freadc(file) -> str
    # reads a char from file

    fprint(file, *values) -> nil
    # puts values in file and a new line, then returns nil

    fprintf(file, base: str, *other) -> nil
    # puts base % other in file and a new line, then returns nil
    # it formats the base
    io.open("...", "r") do |file|:
        io.fprintf(file, "hello %s", "mobin")
    end

    close(file) -> NoReturn
    # closes the file

    status(file) -> str
    # returns the status of the file (is opened or closed)

    read(prompt) -> str
    # gets an input with prompt, and saves the input in _

    fwrite(*values, file) -> nil
    # writes values in file, then returns nil

    gets -> str
    # gets an input string and saves it in _

    getc -> str
    # gets an input char and saves it in _

    putc(*values) -> nil
    # prints a char
    # if any type except char is given, raises error

    printf(base: str, *values) -> nil
    # if base is not string, raises error
    # prints base % values

    sprint(value) -> Any
    # returns value
    $name = io.sprint("mobin")
    # name = "mobin"

    sprintf(base: str, *values) -> nil
    # formatted sprint

    var_dump(*values) -> nil
    # prints some result about values
    # prints: TYPE(LENGTH) VALUE
    io.var_dump("hello")
    # str(5) hello

    Return(value) -> Any
    # returns value

    system(command) -> int
    # this will use os.system to execute command

    print_r(__value: list | dict | set | tuple) -> nil
    # prints the __values but in pretty way
    # if __value is not list or dict or set or tuple, raises error
    # then returns nil

    exit(code: int = 0) -> NoReturn
    # system exit with code code

    id(__obj: object) -> str
    # return hex format of int id of __obj
    # this is guaranteed to be unique for every object

    rand(max: int) -> int
    # returns random.randint(0, max)
    # = 
    # returns a random in [0, max]
    # this is a math range, if your math is good you uderstood it
    # but if no
    # [0, max] means, if we call the random number 'x'
    # so: 0 <= x <= max

    sleep(sec: float) -> NoReturn
    # sleeps for sec

    format
    # just like sprintf

    catch(__to_do: str, __err_type)
    # it tries: exec(__to_do)
    # excepts BaseException as e, if type of e is not the __err_type
    # returns ERR, else prints e, then returns True, and if there is no problem, returns nil
    # so
    # if there is error and __err_type is the error type, it returns True
    # but if there is error and __err_type is not the error type, it returns ERR
    # but if there is no error, 
    # it returns nil
    # look at this example: 
    $x = io.catch("io.printf(hello)", NameError)
    io.printf("%s", x == True)!
    # error, True
    $x = io.catch("io.printf(hello)", KeyError)
    io.printf("%s", x == ERR)!
    # True
    $x = io.catch("io.printf('hello')", NameError)
    io.printf("%s", x == nil)!
    # 'hello', True

    pprint(*values) -> nil
    # pretty print values with \n

    pprintf(base: str, *other) -> nil
    # formated pretty print with \n

    puts(*values) -> nil
    # uses pprint to pretty print values

    lprint(value) -> Any
    # uses for printing local variables ( my, local )
    # note that value must be string
    # this function does not print an '\n' at the end

    lprintln(value) -> Any
    # uses for printing local variables ( my, local )
    # note that value must be string
    # this function does print an '\n' at the end

    cprint(*values, sep="\t", end="\n", file=stdout) -> Any
    # uses for printing values but, customly !

    vprint(*values)
    # prints variables that are created by lit keyword
    # each value must be string

        lit $name = "moon"
        io.vprintln('$name')!

    vprintf(format, *values)
    # formated version

    vprintln(*values)
    # prints variables that are created by lit keyword, with \n at the end

# fmt
a standard library for Moon

    Fprint(write_to, *a)
    # prints "a" to write_to file

    Fprintf(write_to, format, *a)
    # prints formated version of "a" in write_to file

    Fprintln(write_to, *a)
    # as same as Fprint but with a \n in the end

    Print(*values)
    # prints values

    Printf(format, *values)
    # prints formated version of values

    Println(*values)
    # prints values with \n at the end

    Sprint(*values)
    # returns values
    # this is used to save values in variable(s)

    Sprintf(format, *values)
    # returns formated version of values

    Sprintln(*values)
    # returns values with \n at the end

    Puts(*values)
    # prints values

    Putc(*values)
    # prints char
    # if values are not char, this will print the first char of value
    # not for nums

    Lprint(*values)
    # prints values, but they must be list

    Lprintln(*values)
    # prints values, but they must be list with \n at the end

    Pprintln(*values)
    # pretty print of values with \n at the end

    Pprintf(format, *values)
    # pretty print of values with \n at the end

    Open(file, mode)
    # opens the file with mode mode

    Fget(file)
    # returns file.readline()

    Fgets(file)
    # returns file.readlines()

    Fgetc(file)
    # returns first char of file.readline()

    Fputs(file, to_write)
    # writes to_write in file

    Eprint(message)
    # prints message to stderr

    Eprintf(format, message)
    # prints formated message to stderr

    Eprintln(message)
    # prints message to stderr with \n at the end

# discard
uses for deleting a variable from your file
but it is used for local variables ( my, local )

    my num = 0
    io.lprint(num)!
    discard num
    io.lprint(num)!

# defer
Defer is used to ensure that a function call is performed later in a program’s execution, usually for purposes of cleanup.

    defer printf("Bye World")

# END
END block will be executed last

    END {
      
      printf("Bye World")

    }

# defer vs. END
defer is for doing a work
but END is a block, so you can do numbers of works

note: if you have defer and END block at the same time in your file, first, defer will be ran, then END block
so END block is a better end for your program

# loop
creates an infinite loop

    loop:
        fmt.Println("Hello")
    end

# macro
macros can be define by define keyword

    define __my_macro(a, b) a if a < b else b
    # func-like macro
    define magic_number 2162
    # var

# consume
moves a value to a new variable, leaving the original variable empty

    a := 0
    b := 1
    consume a to b
    puts a
    # nil
    puts b
    # 0

# back-ticks

you can use back-ticks (``) to run the command in your command line. it uses system built-in function

    `cd`

# decoraters

as python, moon has decoraters
you can use them with @

    include('typing')
    @typing.final
    class Test:
        ...
    end

# Some special variables

here, we are going to introduce two special variable: _ and ERR

when you get any input from any function in 'io' that gets input, is going to save the result to _

    puts _
    # None
    $x = io.read(">>> ")
    puts x == _
    # True

when there is any error in your program, in many cases, moon continues to reading the file (except some errors)
but if there is, the type and the message will be saved to ERR, but if there is no error, ERR is None

    puts ERR
    # None

    io.throw(TypeError, "Mooooon")!
    puts ERR
    # #<TypeError: Mooooon>

# match - case
match is exactly what switch case does
    
    $name = "Mobin"
    match name:
        case "Mobin":
            printf("Admin")
        case _:
            printf("User")
    end

# !
! is used for executing code in python as like as <>

    name = "Mobin"!
    printf(name)!
    # Mobin

# todo
todo is a keyword that is used to specify that some code is not yet implemented. \
e.g

    todo as "I haven't completed it yet"

# panic
it is used to crash the program when the program has reached a point that should never be reached. \
e.g

    panic as "Oh Noooooo"

# local
this makes a local variable
    
    local name = "Mobin"

# type
it is used for creating alias

    type number = int

# struct
it is a bunch of variables

    struct Student:
        name: str
        age: int
        grade: str
    end

    $Ali = Student()
    $Ali.name = "Ali"
    $Ali.age = 15
    $Ali.grade = 'A'
    puts Ali.name

# enum
it is a bunch of values

    enum week {"Sunday": iota()+1, "Monday": iota()+1, "Tuesday": iota()+1, "Wednesday": iota()+1, "Thursday": iota()+1, "Friday": iota()+1, "Saturday": iota()+1}
    enum today week = 'Sunday'
    puts today

# say
prints the value
note that say is a keyword

    say "Hello"

# eq, neq, gt, lt, ge, le

    8 neq 9
    # not equals
    8 eq 8
    # equals
    8 gt 5
    # greater than
    8 lt 9
    # less than
    8 ge 8
    # greater than equal
    8 le 8
    # less than equal

# standard variables and functions
    stdout, stdin, stderr
The stdin , stdout , and stderr global constant pointers are standard streams for input, output, and error output
    
    argv
argv (ARGument Vector) is an array of character pointers listing all the arguments.

    __FILE__
argv[0]

    __VERSION__
version of moon

    __LOCALS__
locals() ( python )

    __GLOBALS__
globals() ( python )

    __NAME__
__ name __  ( python ), and it is usually __ main __

    FILE
__ file __ ( python ), and it is directory for your file

    ERR
we talked about it

    Any
a simple object \
object() ( python )

    self
__ NAME __

    __etype__(input_data)
returns the exact type of the input you give

e.g

__ etype __("123")! \
#int

    each(_)
iterate for the given iterator \
returns iter(_)

    typeof(thing)
returns the type of the given input

    sizeof(thing)
returns the size of the given input

    lenof(thing)
returns the length of the given input

    require(module_package_or_sth)
import the package or moodule you give
but if there is any error in importing, 
this will raise an error

    include(module_package_or_sth)
import the package or moodule you give
but if there is any error in importing, 
this will print a warning

    isinstanceof(__object, __class_or_tuple)
checks if __object you give is instance of __class_or_tuple

    
    measure()
if you call it, after the whole program, 
it will print the time of doing the work

e.g

measure <= \
#processing time: 0.12876248359680176s

    tostring(value)
    toint(value)
    tofloat(value)
i think it is clear

---------------------

    to_s(value)
string version of given input

    to_i(value)
int version of given input

    to_f(value)
float version of given input

    to_c(value)
complex version of given input

    to_l(value)
list version of given input

    to_t(value)
tuple version of given input

    to_set(value)
set version of given input

    to_bin(value)
binary version of given input

    to_b(value)
bool version of given input

    to_o(value)
octal version of given input

    to_n(value)
for every given input, it returns nil

    to_d(key, value)
dict version of given input \
but this takes two input \
1. key
2. value \
it returns {key: value}

-----------

    to_enum(value)
enumerates version of given input

    to_z(value)
for every given input, it returns zero ( 0 )

    to_r(value)
fraction version of given input


    RED
    GREEN
    PURPLE
    CYAN
    YELLOW
    ORANGE
colors

e.g
printf(f"{CYAN}Hello{BASE}")



    UNDERLINE
    BOLD
i think these are clear

    BASE
it gives you a power to make your string a normal string, if you changed it to a colorful or bold or etc.


    iota(reset=False)
it returns an int from 0 to inf \
if you call it once in the program, 
it will return 0 \
then for second time it will return 1, and so on until
you make reset=True \

e.g

printf("%d", iota())! \
#0 \
printf("%d", iota())! \
#1 \
printf("%d", iota(reset=True))! \
#0 \
printf("%d", iota())! \
#1

    is_zero(__obj)
i think this one is clear too

    __clear_exec__()
it just clears the file that "mexec" function uses to execute the code you write in your terminal

    responds_to(__obj, __name)
returns if __obj has an attribute called __name

    PLATFORM
it is your platform \
e.g "Windows"

    printf(base, *values)
copy version of io.printf \
i made this because it is easier to write and use than io.printf

    AND FOR "IO" ( class ) FUNCTIONS, YOU KNOW WE TALKED ABOUT THEM

--------
    pairs(__obj)
if __obj is int or float, returns range(__obj) \
else, returns each(__obj)

    strcpy(value)
it just returns the value, so you can copy it in another variable

    chop(__str)
it returns __str.strip()[0:-1] version of __str

    chomp(__str)
it returns __str.strip()

    argc
it is the length of argv

    make(__type)
it returns __type(), so e.g if you give int, it will call "int()", so will return 0

    system(command)
executes the commad in terminal, and returns the result

    update(__name, new_value)
if __name is defined, it will change the value of __name to new_value, and if it is not defined, this will raise a NameError

    mexec(code)
this function is used to run code ( that is written in Moon) in terminal  \
so this will make a file called "__ exec __.moon" \
then writes the code you give in that file, then puts a "\n" \
then uses system function to call "moon __ exec __.moon"

but there are some problems with this one \
suppose you made a mistake and wrote printff instead of printf, so moon will raise a NameError \
but the problem is here, that if you made a mistake, the error will be given to you until you close the while program \
( IF YOU RUN THE INTERACTIVE VERSION OF MOON, YOU WILL KNOW WHAT I SAY ) \
so i defined a function called "__ clear_exec __" ( that we talked about it ), that will clear the file ( __ exec __.moon )

    parseStmt(value)
parses the statment you give, and runs it \
it uses mexec function

    next(string)
returns next alphabet or number based on your string \
e.g. : \
next("abc")     # "bcd" \
next("a9b")     # "b0c" \
next("1-z")     # "2-a" \
i'm sure you get (by above example) that if there is a char in your string that is not known is alpha or nums, it will be in your result as it was in your string ( "-" was not known by function )

    fail(message)
raises RuntimeError with message message

# addr
syntax: addr VALUE as SAVE \
addr keyword gets the result of ptr of VALUE, saves it to SAVE

    addr nil as nil_ptr
    puts nil_ptr

# when
it is just like if

    $name = 'Mobin'
    when name == "Mobin":
        printf("Admin")
    else :
        printf("User")
    end

# &
when you start a line with &, you tell moon that you will have a block (a bunch or lines of code)

    &print(
        "hi",
        "bye"
    ) end

# putv
it is for printing the value of lit variables

    lit 5 = 6
    putv 5
    # 6

# ~> 
this is called, soft-calling that is used for calling functions and methods
but why soft?
because it first check that the given param(s) is(are) (a) valid thing(s) or not !
if it is, prints the result of calling it
if it is not, passes so __softly__

    typeof ~> Nil
    # #<Nil>

    typeof ~> NotValid
    # 
    # 👆🏻 nothing in the result

# var
creates a new variable
but var has so many so things to be implemented in :)

#### soft-calling:
it is as mentioned, but here it returns the result !

#### =>
calling functions with params
    
    var call = io.sprint => "Hi"

#### <=
calling functios without params

    var another_call = int <=

#### fn
creates a lambda function

    var func = fn (name)       ->    f"Hello {name}"
                  ______       __    _______________
                  parens       ->    no return keyword
                  are          not   for returning !
                  required     =>

#### add, sub, etc.
you can use these ops with var

    var a = 5 add 5
    var s = 5 sub 5
    var m = 5 mult 5
    var d = 5 div 5
    var p = 5 pow 5
    var m2 = 5 mod 5
    var x = 5 xor 5
    var s2 = 5 shr 5
    var s3 = 5 shl 5
    var e = 5 eq 5
    var n = 6 neq 5
    var g = 6 gt 5
    var g_e = 6 ge 6
    var l = 5 lt 6
    var l_e = 5 le 5
    var i_n = Nil isnot Nil
    var i_i = Nil is Nil

say hi to a new op: __isnot__
opposite of is

#### cast
casting types

    num := 1
    var new_one = cast[bool](num)

# cast
a keyword that is available only with var

    var new_value = cast[int](2.71)
    # 2

# nothing
it represents nothingness

# mystery
represents a mystery value

# @lazy
lazy is a class that delays function evaluation until its value is accessed
    
    class Data:
        @lazy
        def show_my_number():
            return 2162
    end

    obj := Data()
    # here nothing has happened yet !
    printf("%s", obj.show_my_number)!

# freeze
freezable is a class that makes an object then you can freeze it !

    f := freezable("arg")
    f.arg := "Hello"
    printf(f.arg)!
    f.freeze()!
    # f.arg := "Bye"
    # 👆🏻 here we have error ( uncomment it and run it to see )
    # cause f is frozen

# also
evalutes two stmts after each other

    printf("%s", Nil) also print(nil)

# after
evalutes the first stmt after the second stmt

    printf("%s", Nil) after print(nil)

# before
evaluates the first stmt before the first stmt

    printf("%s", Nil) before print(nil)

# perhaps
like maybe

# sleep, wait
sleeps and wait for some certain seconds

# writing python code in moon

    <global boobooli>
    <boobooli = 0>
    <print(boobooli)>
    # 0
    # <> uses 'exec' python function
    io.println(boobooli)!
    # even, it's available in your general program, so you can call it for making varibales
    <name = "Mobin">
    <printf(name)>
    # Mobin

# writing Ruby code in moon
with RB keyword, you can write ruby codes in your moon file

    RB (

        p "Hello, World"

    ) end

note that you MUST put ') end' at the end

# writing Lua code in moon
with LUA keyword, you can write Lua code in your moon file

    LUA (

        print("Hello")

    ) end

note that you MUST put ') end' at the end

# writing Zig code in moon
with ZIG keyword, you can write Zig code in your moon file

    ZIG (
        const std = @import("std");

        pub fn main() void {
            std.debug.print("Hello", .{});
        }

    ) end

#### with these three keywords, you can write other language's code in moon, and then, moon will run it auto :)
#### but we still have some languages, but the problem is here, that moon will NOT run that auto :(

# writing C code in moon
with C keyword, you can write C code in your moon file

    C (
        #include <stdio.h>

        int main() {
            printf("Hello, World");
            
            return 0;
        }

    ) end

# writing Asm code in moon
with ASM keyword, you can write Asm code in your moon file

    ASM (

        section .data
        ; and etc.

    ) end

# writing Gleam code in moon
with GLEAM keyword, you can write Gleam code in your moon file

    GLEAM (

        import gleam/io

        pub fn main() {

            io.print("Hello, World")

            Nil

        }

    ) end

# writing C++ code in moon
with CPP keyword, you can write C++ code in your moon file

    CPP (
        #include <iostream>

        int main() {
            std::cout << "Hello, World";

            return 0;
        }

    ) end

### and note that the indentation between () with these keywords are not necessary

# syntax highlighting for moon in vscode
we have a folder called syntax in the directory, that contains files that give you the syntax highlighting
just copy the moon folder from syntax folder in the .vscode folder (that you have it on your device)

# keywords:
    
    | True     | shows boolean true value                                                                                      |
    | False    | shows boolean false value                                                                                     |
    | nil      | a type alias of None, but you'd better use Nil not nil for showing nothing                                    |
    | Nil      | shows nothingness                                                                                             |
    | module   | creates a module                                                                                              |
    | alias    | creates a type alias                                                                                          |
    | dec      | declares a varaible                                                                                           |
    | def      | defines a new function                                                                                        |
    | if       | creates conditions                                                                                            |
    | else     | it can be used with: for, while, if, try, that does when the other blocks are not executed b/c of being false |
    | elif     |                                                    ...                                                        |
    | until    | do sth until condition is false                                                                               |
    | unless   | do sth if consition if false                                                                                  |
    | class    | creates a new class                                                                                           |
    | switch   | switch-case stmt that check on variables                                                                      |
    | case     | ...                                                                                                           |
    | while    | a loop which goes until condition is false                                                                    |
    | for      | a loop that usually is used for iterating over iterators                                                      |
    | try      | try block that tries the code given and catchs errors                                                         |
    | excpect  |                                                     ...                                                       |
    | finally  | this block will be ran not based on try block caught any error or not                                         |
    | async    | async functions                                                                                               |
    | await    | used with only async functions                                                                                |
    | end      | end the block, used with: if-else-elif, while, for, def, try, RB, LUA, ...                                    |
    | yield    | used in generator functions                                                                                   |
    | pass     | passes in a block                                                                                             |
    | continue | continues in a block to the next one                                                                          |
    | break    | breaks a block                                                                                                |
    | is       | checks for an instance                                                                                        |
    | in       | checks for containing                                                                                         |
    | raise    | raises a new error                                                                                            |
    | return   | returns a value or maybe no value and then exits function                                                     |
    | and      | and operator                                                                                                  |
    | or       | or op                                                                                                         |
    | lambda   | creates a lambda and anonymous function                                                                       |
    | as       | is used with importing modules and packages                                                                   |
    | from     | is used with importing modules and packages                                                                   |
    | assert   | raise a assert error if given condition is false                                                              |
    | del      | deletes a varaibles or function or any object                                                                 |
    | global   | declares a new globals variable                                                                               |
    | not      | not op                                                                                                        |
    | with     | is used to wrap the execution of a block with methods defined by a context manager                            |
    | puts     | prints values in the console                                                                                  |
    | putv     | prints the values of variables that are created with lit                                                      |
    | maybe    | sth between True and False; we can have this definition: maybe is (True or False)                             |
    | never    | makes a variable that is not gonna be used                                                                    |
    | do       | is used with: while, blocks                                                                                   |
    | undef    | undefines an object                                                                                           |
    | import   | imports a pakcage or module                                                                                   |
    | None     | shows nothingness, it is came from Python                                                                     |
    | match    | is used with case keyword for a match-case                                                                    |
    | todo     | is used to raise a todo error that warns coder that this code is not complete                                 |
    | panic    | is used to panic when the code reaches where it shouldn't have been                                           |
    | when     | is just if                                                                                                    |
    | foreach  | for each element in an iterator do sth                                                                        |
    | add      | add op (+)                                                                                                    |
    | sub      | sub op (-)                                                                                                    |
    | mult     | mult op (*)                                                                                                   |
    | div      | div op (/)                                                                                                    |
    | pow      | pow op (**)                                                                                                   |
    | mod      | mod op (%)                                                                                                    |
    | xor      | xor op (^)                                                                                                    |
    | shr      | right shift op (>>)                                                                                           |
    | shl      | left shift op (<<)                                                                                            |
    | addr     | returns a pointer of a object and saves it in the varible you give; add STH as RES                            |
    | type     | as a keyword, creates a new type alias                                                                        |
    | struct   | creates a new struct                                                                                          |
    | enum     | creates a new enum                                                                                            |
    | say      | prints values to console                                                                                      |
    | eq       | equal op (==)                                                                                                 |
    | neq      | not equal op (!=)                                                                                             |
    | gt       | greater than (>)                                                                                              |
    | lt       | less that (<)                                                                                                 |
    | ge       | greater than equal (>=)                                                                                       |
    | le       | less than equal (<=)                                                                                          |
    | my       | creates a local variable                                                                                      |
    | our      | creates a global variable                                                                                     |
    | defer    | is used to ensure that a function call is performed later in a program’s execution                            |
    | END      | is used for doing bunch or maybe one work at the end, even if you write it at first of your file              |
    | discard  | discards a object                                                                                             |
    | mut      | creates a muttable varaible                                                                                   |
    | package  | creates a new package                                                                                         |
    | auto     | creeates a new variable                                                                                       |
    | loop     | infinite loop                                                                                                 |
    | lit      | creates a local variable, but a special one, LOOK AT THE END OF 'other things'                                |
    | local    | creates a loacl variable                                                                                      |
    | set      | creates a new variable; set STH to STH_ELSE                                                                   |
    | to       | is used with set, mirror, consume,                                               |
    | define   | creates a new macro; so it can be function-like-macro or varaible-like-macro                                  |
    | nonlocal | declares a new variable which is a nonlocal; used in nested functions                                         |
    | consume  | swap value of variables; consume A to B                                                                       |
    | static   | creates a global variable                                                                                     |
    | forever  | inf loop                                                                                                      |
    | LUA      | gets a Lua code and runs it                                                                                   |
    | RB       | gets a Ruby code and runs it                                                                                  |
    | ZIG      | gets a Zig code and runs it                                                                                   |
    | C        | gets a C code and does NOT run it                                                                             |
    | CPP      | gets a C++ code and does NOT run it                                                                           |
    | GLEAM    | gets a Gleam code and does NOT run it                                                                         |
    | ASM      | gets a Asm code and does NOT run it                                                                           |
    | var      | creates a new variable, but with so many feathers                                                             |
    | fn       | is used in var, to make lambda functions                                                                      |
    | nothing  | represents nothing :)                                                                                         |
    | mystery  | represents a mystery value                                                                                    |
    | also     | evaluates two stmts after each other                                                                          |
    | after    | evaluates the first stmt after the second one                                                                 |
    | before   | evaluates the second stmt after the fisrt one                                                                 |
    | perhaps  | represents perhaps                                                                                            |
    | mirror   | copys an object to another one                                                                                |
    | sleep    | sleeps and waits for some seconds                                                                             |
    | wait     | sleeps and waits for some seconds                                                                             |



# Other Things:

    $age = 16
    $can_vote = age >= 18 and True or False
    # False

    puts nan == nan
    # False !!!

    mexec("if 1:\n\tio.println('hello')\nelse:\n\tio.println('bye'\nend"))
    # executes moon code

    require('math')
    $a = {"p" : print}
    <a["p"]("Hello, World")>
    print = math.sin
    <a["p"](print(1))>
    $sin = a["p"]
    <sin("Bye, World")>
    # playing with name, but this is dangerous !

    include('Int')
    $even_or_odd = (num) -> "even" if Int.is_even(num) else "odd"
    io.print(even_or_odd(5))!
    # odd

    io.print_r([nil, True, False])!
    # print_r prints only list !
    # print_r("hello")!
    # error !!

    include('Time')
    io.print => Time.now
    
    system => 'echo hello'
    # execute command line code

    io.sprint(true)?
    # this is like a debuger
    # true
    #=> nil

    with "hello" as item:
        io.print(item)
        # h
        # e
        # ...
    end

    io.print(Range("a", "e").new())!
    # ['a', 'b', 'c', 'd', 'e']

    never num = 7
    # io.print(num)
    # error: num is not defined
    # creating variables with never makes the variables to be unusable !

    $x = (7..15)
    # a range from 7 to 15
    $y = ?c
    # a char using '?'
    $z = %s[hello, world]
    # a string
    $a = %(hi)
    # a string

    $num = 0
    undef num
    # delets num

    alias new = nil
    # creating a type alias

    $x = 0
    do:
        io.print("hello")
    while x > 1
    end
    # first does the 'do' block and then if condition is true it is gonna do that in a loop

    try:
        io.print(1 / 0)
    except ZeroDivisionError as e:
        io.print(e)
    else:
        io.print(True)
    finally:
        io.print("bye")
    end
    # division by zero
    # bye

    try:
        io.print(1 / 1)
    except ZeroDivisionError as e:
        io.print(e)
    else:
        io.print(True)
    finally:
        io.print("bye")
    end
    # 1.0
    # True
    # bye

    class Person:
        def __init__(self, name: str, age: int, id: int) -> None:
            self.name = name
            self.age = age
            self.__id = id
            # self.__id is private-like
            # but note that there is nothing called private neither in python nor moon !
    end
    $mobin = Person("mobin", 16, 122333)
    # io.print(mobin.name, mobin.age, mobin.__id)!
    # error: Person has no __id !!
    # pyhton for '__' started things will add a '_ClassName' to the begining of it
    # ClassName is the name of the class
    io.print(mobin.name, mobin.age, mobin._Person__id)!
    # true !

    $x = io.catch("io.printf(hello)", NameError)
    io.printf("%s", x == True)!
    # error, True
    $x = io.catch("io.printf(hello)", KeyError)
    io.printf("%s", x == ERR)!
    # True
    $x = io.catch("io.printf('hello')", NameError)
    io.printf("%s", x == nil)!
    # 'hello', True

    $result1 = stdin.readline()
    puts result1
    # getting input with stdin
    # note that, there is no 's' at the end of readline !

    $result2 = stdin.readlines()
    # note that, there is a 's' at the end of readlines !
    # infinitly getting input
    # because when you are reading stdin, with readlines, this is going to read the lines till the end, but the end for stdin is ^C (i think this is only in Windows), so your program will no finish until ^C
    puts result2
    # error: result2 is not defined !


    $pointers = {}
    class io:

        def cout(*values):
            for value in values:
                print(value)

        def cin(prompt):
            return input(prompt)

        def __rshift__(self, value):
            return io.cout(value)

        def __lshift__(self, prompt):
            return io.cin(prompt)

        def __and__(self, value):
            pointers[hex(id(value))] = value
            return hex(id(value))

        def __mul__(self, pointer):
            try:
                return pointers[pointer]
            except KeyError:
                print(f"ERR: {pointer} is not defined or not a pointer")
    end

    $_ = io()
    _ >> "hello"
    # printing hello
    _ >> (_ << ">>> ")
    # printing the gotten input from user with <<
    _ >> (_ & 7)
    # printing pointer of 7 ! (&7 in C or sth)
    _ >> (_ * (_ & 7))
    # printing the derefrenced pointer of 7
    # _ >>   ( _ * (        _ & 7 ) )
    # print    derefrence   getting pointer
    $p = _ & 'hello'
    # saving pointer of hello in p
    _ >> p
    # prints p
    _ >> (_ * p)
    # derefrecing p
    _ >> f"{p} -> {_ * p}"
    # prints p and defrenced version of p
    # but note that in pointers

    with [2, 6, 1, 2] as num:
        printf(to_s(num))
        # 2
        # 6
        # 1
        # 2
    end

    with open("somefile", "r") as f:
        printf("%s", f)
        # reads the whole file
        # if i don't wanna lie, i don't know why is this reading the file !
    end

    lit 5 = 6
    # don't worry, no error here
    # lit makes and saves variables in a dict
    # so name can be everything, cause it is a string
    putv 5
    # putv used for printing lit variables