# Moon programming language

# Variables:

    $name = "mobin"
    # this makes 'name' variable

    grade = 'A'!
    # normal one

    <time = 5>
    # with <>

    number := 5
    # another way to create a variable, it's by :=

    my number = 0
    # creating local variable by 'my'

    local name = "Mobin"
    # creating local variable by 'local'

    native number = 5
    # creating local variable by 'native'

    our grade = 'A'
    # normal variable

    lit $n = 0
    # creating variables with lit

    set n to 8
    # creating variables with set and to

    @name = "Mobin"
    # class variable that is created in __main__ class

    static num = 0
    # global variable

    global n
    n = 5
    # another global

    auto thing = [0, 1]
    # auto type choose
    # no diffrence, cause Python usually doesn't care about types

    never shit = nothing
    # a variable which, it will NOT be used, so: 'puts shit' has Error

# NOTICE
When i was writing this file (REDAME), i did NOT write concepts by the degree of importance! I just wrote them wherever i was at the file (README)

# Comments:
as you see in code, we use '#' for writing comments
    
    # moon is a programming language

# lit
this is a keyword to make a varaible, but this will be saved into VARIABLES dict!
maybe we can call it a version of local variables
but you access these variables only with io.vprint or io.vprintln or io.vprintf

    lit $name = "Mobin"
    io.vprintln('$name')!

# OOP:
moon is an object-oriented programming language
    
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

    'printf "Hello"
    # this is OK
    # but only for the callings that they need at least one argument, not more !
    # 'printf "Hello", "World"
    # not OK
    # note that for this one, it needs to be started with '

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

    loop:
        fmt.Println("Hello")
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
    # returns a random number in [0, max]
    # this is a math range, if your math is good you uderstood it
    # but if no, 
    # [0, max] means, if we call the random number 'x'
    # so: 0 <= x <= max
    # if you didn't understand, just f*ck off BRO

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
    # uses for printing local variables ( my, local, native )
    # note that value must be string
    # this function does not print an '\n' at the end

    lprintln(value) -> Any
    # uses for printing local variables ( my, local, native )
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

    warn(msg="")
    # raises a warning with msg
    
    error(__type, msg)
    # raises the __type error with msg

    putchar(code)
    # returns chr of code

    putchars(*codes)
    # returns chr of codes in one string

    countc(string, what_char)
    # returns the count of what_char in string

    assertEqual(a, b)
    # asserts if a and b are equal

    assertTrue(a)
    # asserts if a is true (not just True, but also all true values)

    assertFalse(a)
    # asserts if a is false (not just False, but also all falsy values)

    scanf()
    # returns the input

    strlen(s)
    # returns the length of s

    strcpy(s)
    # returns a copy of s

    strcat(a, b)
    # returns joined version of a and b

    atoi(s)
    # returns int version of s

    atof(s)
    # returns float version of s

    abort()
    # exits the program with code 1

    alert(value)
    # returns a warning with msg

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
but it is used for local variables ( my, local, native )

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
macros can be defined by define or macro keyword

    define __my_macro(a, b) a if a < b else b
    # func-like macro
    # yeah, kinda hard to read
    # it like:
    # def __my_macro(a, b):
    #   return a if a < b else b
    
    define magic_number 2162
    # var

    macro __my(a, b) a if a < b else b
    # func-like macro
    puts __my(4, 8)

    macro number 0xaa
    # var-like macro
    puts number

# consume
moves a value to a new variable, leaving the original variable empty (nil)

    a := 0
    b := 1
    consume a to b
    puts a
    # nil
    puts b
    # 0

# back-ticks
you can use back-ticks (``) to run commands in your command line. it uses 'system' built-in function

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
here, we are going to introduce two special variables: _ and ERR

when you get any input from any function in 'io' that gets input, it is gonna save the result to _

    puts _
    # None
    $x = io.read(">>> ")
    # giving some inputs...
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
match-case is exactly what switch-case does
    
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

# native
this makes a native (local) variable

    native secret_number = 2162

# type
it is used for creating aliases

    type number = int

# struct
it is a bunch of variables, but, as you know, NOT with values, but with ONLY and ONLY with their TYPES

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
    # creating an instance, maybe we can call it, for our enum, with this syntax:
    # enum A_NAME ENUM_NAME = STRING_NAME_OF_A_VALUE_OF_OUR_ENUM
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

NOTE THAT NOW WE HAVE 'include' AND 'require' AS KEYWORDS NOW 

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

    div(a, b)
a / b

    unreachable(msg="")
gives an assertion with msg

    unimplemented()
raises UnimplementedError

    var_dump(*values)
prints with this syntax: type(len) value

    call(fn, *args)
calls the function with args

    each(arr, fn)
for each element in arr, implements fn, then returns the result in an array

    take(arr, n)
returns first n values of arr

    assert_equal(a, b)
raises an assertion if a and b are not equal

    assert_type(a, b)
raises an assertion if a and b are not at the same type

    retry(fn, *args, count=3)
runs the fn with args count times

    __random__()
returns a 5 length random string (from both ascii letters and digits)

    String(value)
returns the str version of value

    Number(value)
returns the num version of value

    Bool(value)
returns the bool version of value

    π
math.pi

    e
math.e

    𝜏
math.tau

# addr
syntax: addr VALUE as SAVE \
addr keyword gets the ptr of VALUE, and then saves it to SAVE

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
when you start a line with &, you tell moon that you will have a block (a bunch or lines of code); DO NOT FORGET 'end'

    &print(
        "hi",
        "bye"
    ) end

    # ---------------------------


    &values = {
        0,
        1,
        2,
    } end

    # without &, you would get an error

    puts values

    # ---------------------------

    &def person(
        name: str,
        age: int,
        city: str,
    ) -> str:
        return f"{name} is {age} years old that lives in {city}"
    end

    # suppose you are a fan of type annotation (sorry but f*ck type annotations), or you wanna write functions as Python recommends you can to do

    puts person("mobin", 17, "Urmia")

# private functions
you can make private functions not only in classes and even in module-level

    class pub_and_priv:

        def pub(self):
            return "pub"
        
        @visibility.private
        def priv(self):
            return "priv"

        def another_pub(self):
            return "another pub"

    end

    $pp = pub_and_priv()
    puts pp.pub()
    puts pp.another_pub()
    # puts pp.priv()
    # error

#### note that only that function that is given to visibility.private is private, else are public (except for __SOME_NAME that Python itself sees them as private)

    @visibility.private()
    def pr():
        print("Hello")
    end
    
    # pr()!
    # error

# expect
it is a class that has some functions

    expect(5).toBeEqualTo(8)
    # False

    expect(5).toBeGreaterThan(8)
    # False

    expect(5).toBeLessThan(8)
    # True

    expect(5).toBeGreterEqualTo(8)
    # False

    expect(5).toBeLessEqualTo(8)
    # True

    expect(5).toBeNotEqualTo(8)
    # True

    expect(5).toBeIn([2, 5, 3])
    # True

    expect(5).toBeNotIn([2, 3])
    # True

# channels
if you've ever programmed in Go, you know what channels are

    chan.send("Hello, World")!
    chan.send("Hello")!
    chan.send("Bye")!
    print(chan.is_empty())!
    print(chan.size())!
    print(chan.get())!
    print(chan.size())!
    print(chan.get())!
    print(chan.get())!
    print(chan.size())!
    print(chan.is_empty())!
    print(chan.is_full())!
    chan.close()!
    chan.send("hi")!
    # error
    # be aware that when you close a channel, sending and getting values cause Error

    # chan.send sends a value to a channel
    # chan.get gets and removes the last element (if exisits) and returns it
    # chan.is_empty and chan.is_full checks for emptyness and fullness of that channel
    # chan.size returns the size of the channel

# putv
it is for printing the value of lit variables

    lit 5 = 6
    putv 5
    # 6

# ~> 
this is called, soft-calling that is used for calling functions and methods
but why soft?
because it first checks that the given param(s) is(are) (a) valid thing(s) or not !
if it(they) is(are), prints the result of calling it.
if it(they) is(are) not, passes so __softly__, without any errors

    typeof ~> Nil
    # #<Nil>

    typeof ~> NotValid
    # 
    # 👆🏻 nothing in the result

# var
creates a new variable
but var has so many things that you can use them :)

#### soft-calling:
it is as mentioned, but here it returns the result !

#### =>
calling functions with params (but you can do it without params also)
    
    var call = io.sprint => "Hi"
    var res = A_FREAKING_FUNC =>

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
you can use these ops and etc. with var

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
    var n_i = "h" notin "bye"
    var s = sin pi
    var c = cos pi
    var t = tan pi
    var sq = sqrt 4
    var cb = cbrt 8
    var l = log 10
    var nl = ln e
    var c = 4 <=> 5
    var short_hand = 5 < 4 ? True : False
    var d = printf("Hello") ?? "Error"
    # if the left has errors returns right else passes
    var block = do
        name = "Mobin"
        printf("Hello")
        printf(f"Hello {name}")
        printf("Bye")
    end
    var a = await 2 printf("Hello")
    # await in var-level
    # but syntax in not as function-level
    # it gets two things: a number (seconds) to delay, then a work to do
    var r = 0 through 10
    var ar = 'a' through 'e'
    # note: 'through' uses Range class
    var contains = [0, 1] has 2
    var contains2 = [0, 1] lacks 2
    var abs = |-5|
    # absolute value with ||
    # note: || is only available with var
    var fact = 5!
    # factorial
    # this is not as same as ! in the module-level that runs Python code!
    var conv = 5_f
    # to float
    var conv2 = 1.5_i
    # to integer
    var conv3 = 0_b
    # to boolean
    var conv4 = 7895_s
    # to string

say hi to new ops (that we saw examples of them above!): __isnot__, __notin__, __has__, __lacks__\
isnot = is not\
notin = not in\
has = in\
lacks = not in

#### pipeline (|>)
you can use them as you could in the module-level

    var p = Nil |> io.sprint
    puts p

#### ~=, ===
for comparison

~= checks for loose equality
=== checks for strict equality

    num := 5

    var compar = 5.4 ~= 5
    var compar2 = num === 5

#### div by zero

    var divByZero = 1 / 0
    puts divByZero
    # undefined

# inc, decr
inc is ++\
decr is --

    num := 5
    inc num
    puts num
    # 6
    decr num
    puts num
    # 5

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

# undo, redo
undoable is a class that makes an object then you can travel in time and get previous value

    state := undoable({"c": 0})
    state["c"] = 1!
    state["c"] = 2!
    print(state)!
    state.undo()!
    print(state)!
    state.undo()!
    print(state)!
    state.redo()!
    print(state)!

# again
exectes the last line (not block) again

    puts "hi"
    again
    # hi
    # hi

# block
block makes a block then in the future you can run it

    block b:
        printf("Hello")
    end
    does b

# does
as you saw in the last example, does is used to run the blocks

    block b:
        printf("Hello")
    end
    does b
    # Hello

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

    sleep 5
    # 5s

    wait 5
    # 5s

# lable, goto
we can define a lable and just use it in the future by goto

    lable here:
        printf("Hello")
    end

    goto here

# awaitfor
it is a syntax sugar (maybe we can call it that)

    2 awaitfor printf("Hello")
    # translates to: (Python)
    
    # async def __RAND_NAME__():
    #    await asyncio.sleep(2)
    #    printf("Hello")
    # asyncio.run(__RAND_NAME__())

    # that __RAND_NAME__ is a random name that moon makes
    
# fixme
this is used for telling the coder that that line or maybe that block needs some repair

    fixme as "This code needs your fix to be ran"

# some new types

    si := short_int(32767)
    # (-32768, 32767]

    usi := ushort_int(65535)
    # (0, 65535]

    ui := unsigned_int(4294967295)
    # (0, 4294967295]

    li := long_int(2147483647)
    # (-2147483648, 2147483647]

    uli := ulong_int(4294967295)
    # (0, 4294967295]

    lli := long_long_int(2**63)
    # (-(2**63), (2**63)]

    ulli := ulong_long_int(18446744073709551615)
    # (0, 18446744073709551615]


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
    | add      | at var: add op (+)                                                                                            |
    | sub      | at var: sub op (-)                                                                                            |
    | mult     | at var: mult op (*)                                                                                           |
    | div      | at var: div op (/)                                                                                            |
    | pow      | at var: pow op (**)                                                                                           |
    | sqrt     | at var: square root                                                                                           |
    | cbrt     | at var: cube root                                                                                             |
    | sin      | at var: sin of a radian                                                                                       |
    | cos      | at var: cos of a radian                                                                                       |
    | tan      | at var: tan of a radian                                                                                       |
    | log      | at var: log in base 10                                                                                        |
    | ln       | at var: log in base e ( natural log )                                                                         |
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
    | to       | is used with set, mirror, consume,                                                                            |
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
    | isnot    | checks for not being an object                                                                                |
    | notin    | checks for not being in an iterator                                                                           |
    | cast     | cast types                                                                                                    |
    | inc      | ++                                                                                                            |
    | decr     | --       note: decr is not dec                                                                                |
    | macro    | as like as define                                                                                             |
    | lable    | creates a new lable                                                                                           |
    | goto     | is used to go to a lable                                                                                      |
    | through  | is used to make Ranges                                                                                        |
    | namespace| is used for making namespaces                                                                                 |
    | interface| is used for making interfaces                                                                                 |
    | again    | is used for redoing the last line                                                                             |
    | block    | is used for creating blocks                                                                                   |
    | does     | is used for running blocks                                                                                    |
    | awaitfor | is a syntax sugar for async functions                                                                         |
    | ensure   | just like assert                                                                                              |
    | fixme    | is used to tell the coder that the code needs fix at a line or maybe block!                                   |
    | has      | is like in keyword                                                                                            |
    | lacks    | is like notin                                                                                                 |
    | native   | is for making local variables                                                                                 |

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
            # but note that there is nothing called private in python !
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
    # because when you are reading stdin, with readlines, this is going to read the lines till the end, but the end for stdin is ^C (i think this is only in Windows), so your program will not finish until ^C
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
    # printing pointer of 7 ! (&7)
    _ >> (_ * (_ & 7))
    # printing the direfrenced pointer of 7
    # _ >>   ( _ * (        _ & 7 ) )
    # print    direfrence   getting pointer
    $p = _ & 'hello'
    # saving pointer of hello in p
    _ >> p
    # prints p
    _ >> (_ * p)
    # derefrecing p
    _ >> f"{p} -> {_ * p}"
    # prints p and direfrenced version of p

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

    puts hello
    if ERR is not None:
        printf(ERR)
    end
    if not ok:
        printf(ERR)
    end

    require t
    include t
    # run these to see the diffrence

    lit 5 = 6
    # don't worry, no error here
    # lit makes and saves variables in a dict
    # so name can be everything, cause it is a string
    putv 5
    # putv used for printing lit variables