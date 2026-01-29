# Moon Programming Language

Moon is an *_UNREAL_* programming language, which is written with Python, and has great features, maybe.


# Variables

    $name = "Moon Programming Language"

    grade = 'F'!

    <time = 10.5>

    number := 2162

    my password = "Moon2162"

    local i = 0

    native is_male = True

    our email_addres = nil

    lit $message = "Hello"

    let 🌑 = "Moon"

    set j to 1

    @job = None

    static letter = 'Z'

    global name
    name = "Mobin"

    auto arr = [2, 1, 6, 2]

    never type = "INT"

    type Z = int

    mut who = "him"

    var format = ".png"

---------------------------------------------------------

### $

using $ for creating variables, has this syntax

    $VAR_NAME = ...

and VAR_NAME would be available in program

but in $ type-of-varible-making, we have some other featurs also:

    $add1 = (n) -> n + 1
    # functions:
    # --->   (PARAMS) -> WORKS

    $char = ?Z
    # ? is used for saving a char
    # NOTICE that we have no '' or ""

    $string1 = %s[Hi]
    # %s[...] is used for saving a string
    # NOTICE that we have no '' or ""

    $string2 = %(Bye)
    # %(...) is used for saving a string
    # NOTICE that we have no '' or ""

    $range_of_nums1 = (0..2162)
    # (n..m) only if n<=m
    # which makes a range that excludes m itself

    $range_of_nums2 = (0...2162)
    # (n...m) only if n<=m
    # which makes a range that inlucdes m itself

    $not_op = !0
    # ! = not
    # HAVE THIS LINE IN YOUR MIND WITH CODE 1

---------------------------------------------------------


### !

! in the end of the line in **MODULE_LEVEL** runs the line (without the !) in Python, without making anything diffrent in that line


    print("Hello, World")!

NOTICE that this ! is diffrent with ! in CODE 1

NOW YOU CAN GET THAT LINE OUT OF YOUR MIND 

---------------------------------------------------------


### <...>

using <> in **MODULE_LEVEL** runs the inside of it, again, in Python, without making anything diffrent in that line

    <n = 5; print(n)>

---------------------------------------------------------

### :=

:= is an operator which can be used for making varibles, syntax:

    VAR_NAME := ...

and VAR_NAME would be available in your program

---------------------------------------------------------

### my, local, native

make a variable but in Python's '__ locals __' dictionary

---------------------------------------------------------

### our

makes a variable but in Python's '__ globals __' dictionary

---------------------------------------------------------

### lit

makes a _**variable-like**_ in _VARIABLES_ dictionary

**NOTICE**: these type of vars are available with (io.vprint, io.vprintln, io.vprintf) functions, NOT with other printing funcs

    lit his_car = "BMW"
    io.vprintln("his_car")!

NOTICE we gave the _**STRING**_ version of his_car to vprintln func


---------------------------------------------------------

### let

makes a _**variable-like**_ in _STACK_ dictionary

**NOTICE**: these type of vars are available with (io.echo) function, NOT with other printing funcs

    let graphic = "LOW"
    io.echo("graphic")!

NOTICE we gave the _**STRING**_ version of graphic to echo func


---------------------------------------------------------

### set-to

uses this syntax:

    set VAR_NAME to ...

to make a variable

---------------------------------------------------------

### @

makes a varibale in a class that the name of the class is '__ name __' var (Python's)

    @version = 1.0
    print(__main__.version)!

__ main __ is the value of __ name __ var (In this case)

READ MORE ABOUT __ name __ ON INTERNET IF YOU DIDN'T UNDERSTAND THIS

---------------------------------------------------------

### static

makes a global variable

    static how_many_times = 5

and this how_many_times var is available in the program globally

---------------------------------------------------------

### global

exactly like static

    global NAMES
    NAMES = {"BLUH BLUH BLUH ..."}

And as you might understood, the diffrence betwen _static_ and _global_ keyword is how they are written, I MEAN THE NUMBER OF LINES THEY NEED **AT LEAST**, YOU CAN **NOT** WRITE 'global' IN ONE LINE

    # global n = "shit"
    # NAHHHH

---------------------------------------------------------

### auto

doesn't do any special job but at least the face of it shows that it has an auto type, which is **facially** as C++

---------------------------------------------------------

### never

doesn't make the variable, so that it won't be in your program

    never WHO_HAS_LEFT_MATRIX = "?"
    # print(WHO_HAS_LEFT_MATRIX) 
    # IT HAS ERROR

---------------------------------------------------------

### type
is used for creating aliases

    type NAME = str

---------------------------------------------------------

### mut
is used for creating mutable variables
(THIS IS KINDA USED FOR FACES! BECAUSE THERE IS NO CONSTANT OR IMMUTABLE VARIABLE IN PYTHON)

---------------------------------------------------------


### var

creates a new variable with syntax

    var VAR_NAME = ...

but var has so many features in addition to normal vars

#### ~>
this is called, soft-calling that is used for calling functions and methods
but why soft?
because it first checks that the given param(s) is(are) (a) valid thing(s) or not !
if it(they) is(are), it saves the result of calling it(them) in variable.
if it(they) is(are) not, passes so **softly**, without any **errors**

    print ~> SOMETHING_NOT_DEFINED
    #

**_NOTICE soft-calling is also available in module-level, but in there it prints the result of calling the func or method or etc. softly_**

---------------------------------------------------------

#### =>
calling functions with params (but you can do it without params also)
    
    var call = io.sprint => "Hi"
    var res =  io.gets =>

---------------------------------------------------------

#### <=
calling functios without params

    var another_call = int <=

---------------------------------------------------------

#### fn
creates a lambda function

    var func = fn (name)   ->   f"Hello {name}"
                  ______        _______________
                  parens        no return keyword
                  are           is needed
                  required     

---------------------------------------------------------

#### add, sub, ...
let's see some examples:

    var a = 5 add 5
    # +

    var s = 5 sub 5
    # -

    var m = 5 mult 5
    # *

    var d = 5 div 5
    # /

    var p = 5 pow 5
    # **

    var m2 = 5 mod 5
    # %
    
    var x = 5 xor 5

    var s2 = 5 shr 5
    # right shift

    var s3 = 5 shl 5
    # left shift

    var e = 5 eq 5
    # ==

    var n = 6 neq 5
    # !=

    var g = 6 gt 5
    # >

    var g_e = 6 ge 6
    # >=

    var l = 5 lt 6
    # <

    var l_e = 5 le 5
    # <=

    # NOTICE: add, sub, mult, div, pow, mod, eq, neq, gt, ge, lt, le are available in module-level also

    var i_n = Nil isnot Nil
    # is not

    var i_i = Nil is Nil

    var n_i = "h" notin "bye"
    # not in

    var s = sin pi

    var c = cos pi

    var t = tan pi

    var sq = sqrt 4

    var cb = cbrt 8

    var l = log 10
    # log base 10

    var nl = ln e
    # log base e

    var c = 4 <=> 5
    # spaceship-op
    # 1: if left-hand-side is greater -> it returns 1
    # 2: if right-hand-side is greater -> it returns -1
    # 3: if they are equal -> it returns 0

    var short_hand = 5 < 4 ? True : False
    # if 5 < 4:
    #   short_hand = True
    # else:
    #   short_hand = False

    var d = printf("Hello") ?? "Error"
    # if the left-hand-side has any error, it returns right-hand-side, else it just saves right-hand-side

    var block = do
        name = "Mobin"
        printf("Hello")
        printf(f"Hello {name}")
        printf("Bye")
    end
    # a block with do keyword till end

    var a = await 2 printf("Hello")
    # await in var-level
    # NOTICE the synatx in module-level is diffrent
    # await n ...
    # n = seconds to delay
    # ... = works to do

    var r = 0 through 10
    var ar = 'a' through 'e'
    # note: 'through' uses Range class, not range (Python's)

    var contains = [0, 1] has 2
    # in

    var contains2 = [0, 1] lacks 2
    # not in

    var abs = |-5|
    # absolute value with ||
    # NOTICE: || is only available with var

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

so we learnt:

add, sub, mult, div, pow, mod, xor, shr, shl, eq, neq, gt, ge, lt, le, isnot, notin, sin, cos, tan, sqrt, cbrt, log, ln, <=>, ? ... : , ??, do, await, through, has, lacks, |...|, !, _i, _f, _s, _b

NOTICE that any other Python op or (some of) functions may work in var. Like (is, not, in, ...)

#### cast

    var new_value = cast[int](2.71)
    # 2

    # syntax: cast[T](VALUE)

---------------------------------------------------------

#### |>
this is called pipeline, which is like a chain (maybe backward one), that runs a functions

    var p = Nil |> io.sprint
    # p = io.sprint(Nil)
    puts p

    var res = Nil |> io.printf |> typeof
    # res = typeof(io.printf(Nil))
    puts res

---------------------------------------------------------

#### ~=, ===
for comparison

~= checks for **_loose_** equality

=== checks for **_strict_** equality

    num := 5

    var compar = 5.4 ~= 5
    var compar2 = num === 5

---------------------------------------------------------

#### div by zero
in var-level, division by zero is undefined.

in module-level, we get ZeroDivisionError

    var divByZero = 1 / 0
    puts divByZero
    # undefined

---------------------------------------------------------

#### if-else

    var cond = if True:
            Nil
        else:
            nil
        end

    puts cond
    # Nil

NOTICE: there is an 'end'!!

NOTICE: only if and else are ok, do _NOT_ use **_elif_**

---------------------------------------------------------

#### :
this is a short hand for calling a function from a class
    
    string := "Moon & Python"
    var sh = string:split("&")
    # this is as: str .split(string,   "&")
    #             ____       ______    ___
    #             type       name of   the
    #             of"&"      the       value
    #                        given     of the
    #                        var       first
    #                                  attempt


    # NOTICE ':' in module-level is also available
    # but this one is a little diffrent from module-level
    # in module-level IMM will print the result automatically
    # but in var-level IMM will save the result in a variable

---------------------------------------------------------

#### (...;...)
you can use '()' and split your exprssions with ';' and save them in your var

NOTICE: the last expr result will be saved in your var. The other will be ran normally with exec (Python's)

NOTICE: the usage of () in this synatx is required

    var area = (r = 2; __pi = 3.14; __pi * r * r)
    puts area
    # 12.56

---------------------------------------------------------

# Comments
as you might noticed, we used # for writing comments in Moon

    # Hello from this part
    # These lines won't be ran


# if-elif conditions and else

    code := "ADMIN"


    if code == "USER":
        print("Hello, World")

    elif code == "ADMIN":
        print("Do better man, world needs us")

    else:
        print("so who on God's green planet you are?")

    end

>_**NOTICE: In blocks, like (if, def, ...), there is no need to use ! or <>, because the expressions in those get ran directly in Python, but in module-level, we have to use them, because 'IMM' (INERPRETER OF MAIN MOON) translates Moon code to Python's, so it needs a sign or sth!**_

# When-elif-else
just like if-elif-else...


    when 5 > 10:
        print("Hi")
    elif 5 == 10:
        print("OO")
    else:
        print("yup")
    end


# Functions

excatly like Python, we use def for creating normal functions

    def add10(n):
        return n + 10
    end

> In Moon we end every block with 'end' keyword!!

but there is another way also

    define show_magic_number() 2162
    puts show_magic_number()
    # syntax:
    # define NAME(PARAMS) TO_RETURN

    # NOTICE: TO_RETURN can't be a long expression or whatever, it can be just a name or value or ...; because IMM puts a 'return' in back of it and runs it!

for calling funcs, we have some choices:

    io.print("moon")!
    # ...

    <io.printf("%d", 2162)>
    # ...

    io.sprint -> "moon"
    # use '->'
    # which gets tranlated to:
    # print(io.sprint("moon"))
    # but as you saw '->' prints the result
    # so we used io.sprint for not getting nil
    # because io.print at the end returns nil
    
    io.getc <-
    # if the function gets no parameter, you can call it with <- (and ofcourse it prints the result; print(io.getc()))
    # or even
    io.getc ->
    # =======     print(io.getc())

    io.print => "hello"
    # this will be translated to:
    # io.print("hello")
    # and note that there is no printing by default
    # so we do not take nil, e.g. in printing.

    io.exit <=
    # if the function gets no parameter, you can call it with <= (and there is no printing by default!)
    # or even
    io.exit =>

## private functions
you can make private functions

    class pub_and_priv:

        def pub(self):
            return "pub"
        
        @visibility.private
        def priv(self):
            return "priv"

        def another_pub(self):
            return "another pub"

    end

    pp := pub_and_priv()
    puts pp.pub()
    puts pp.another_pub()
    # puts pp.priv()
    # error

*NOTICE*: only that function which is given to visibility.private is private, else are public (except for __SOME_NAME that Python itself sees them as private); unless you use visibility.private again for that func also 

## Behaviors
Behaviors are just functions but with diffrent faces!

e.g.

    be over(a, b),   [onlyif b != 0] => a / b
                 _   _               __
    NOTICE       ,   []              =>

> 'be' shows behavior. 'over' and 'a, b' are the name and params, and 'onlyif' is a keywords that checks the condition that if it is TRUE, function will raise an error or etc., This error or message or whatever can be your personal one or you can let IMM do it. If you wanna do it personally, use 'ifnot' and ':' and the error or message.

    be over2(a, b), [onlyif b != 0; ifnot: raise ZeroDivisionError("Nah")] => a / b


> and after '=>' will be the result that behavior will return


> NOTICE: Do NOT use return keyword after =>, cause IMM itself will return the result

> NOTICE that if you use 'ifnot' you can even print sth, not only raise an error.

    ... ifnot: print("Nah Hell Nah") ...


> NOTICE that the usage of 'ifnot' is optional, so as the first example, you can let IMM handle the error

    # and the usage of them are like functions
    over(10, 5)
    over2(20, 4)

# Loops
as like Python we have (for and while)

    for x in [2, 1, 6, 2]:
        io.print(x)
    end

    n := 0
    while n < 3:
        io.print(n ** 3)
        n += 1
    end

and unlike Python, Moon has (until, unless, foreach, loop, whilst)

    x := 0
    results = []
    until x < 3:
        results.append(x)
        x += 1
    end
    # countinues the loop till x is less than 3

    y := 0
    unless y == 3:
        io.print(io.gets())
        y += 1
    end
    # countinues the loop till x is exactly 3

    list := Range('a', 'f').new()
    # using Range class
    # list now has a list
    foreach elem as list:
    # for elem in list
        io.print(elem)
    end
    
    loop:
    # exactly like 'while True', till the end of the world (except when you press, the magic key, 'CTRL C')
        io.println("Oh")
    end

    idx := 0
    whilst idx < 5:
        printf("%d", idx)
        idx += 1
    end
    # no diffrence with while

    a := 5
    do:
        io.println("TEST IT")
    while a < 0
    end
    # it first does what you tell her to, NO MATTER WHAT CONDITION YOU HAVE, then if the condition is true, it will go on

    num := 0
    forever:
        io.print(num)
        num += 1
    end
    # till the end of the world (NOT WITH THE MAGIC KEY!) 

# Do
creates a block

    io.open("shit.txt", "r") do |file|:
    # file = io.open("shit.txt", "r")
        io.print(io.freads(file))
    end

# Switch-Case
for checking the value of sth (usually), like:

    name := "Moon"

    switch name:
    # means we are only talking about name variable

        case "Python":
        # means if name var is "Python"
            io.print("OOF")

        case "Moon":
        # means if name var is "Moon"
            io.print("YUP")
        
        case _:
        # means if name var is anything else
            io.print("assembly?")
        
        end

# Match-Case
_match-case_ is exactly like _switch-case_

    name := "Mobin"
    match name:
        case "Mobin":
            io.print("Admin")
        case _:
            io.print("User")
    end

# discard
uses for deleting a variable from your (computer's) memory

but it is used for local variables ( my, local, native; which are on __ locals __ dict)

    my num = 0
    io.lprint(num)!
    discard num
    # io.lprint(num)!
    # RUN IT

# defer
Defer is used to ensure that a function call is performed later in a program’s execution, usually for purposes of cleanup.

    __file := io.open("shit.txt", "r")
    defer __file.close()
    io.print(io.freads(__file))

# END
END **_block_** will be executed in the end

    END {
      
      printf("Bye World")

    }

### defer vs. END
1:

- defer is only in one line

- END is a block (maybe bunch of lines)

2:

- if you have 'defer' and 'END' _at the same time_, 'END' will be executed in the end (first defer then END)

> SO: **_END is a real ending_**

# Macro
for defining macros, we have two ways:

- with 'define' keyword

    - 1 
        
            define __my_mac(a, b) a if a < b else b

            # function-like-macro
            # ====== 
            # def __mt_macro(a, b):
            #   return a if a < b else b

            puts __my_macro(4, 5)

    - 2

            define magic_number 2162

            # variable-like-macro
            # ======
            # magic_number = 2162

            puts magic_number

- or with 'macro' keyword

    - 1

            macro __my_mac(a, b) a + b
            # function-like-macro
            # ====== 
            # def __my_mac(a, b):
            #   return a + b

            puts __my_mac(4, 7)

    - 2

           macro version 1
            # variable-like-macro
            # ======  
            # version = 1

            puts version

# Consume
moves the value of first var to the second one, leaving the first one nil

    a, b = 0, 1!
    consume a to b
    puts a, b
    # (nil, 0)

# ``
back-ticks are used for running commands in your terminal which uses 'system' function (Python's)

```bat:
`echo Moon`
```

# &
is used for creating blocks, that IMM will look at them as a block and run them in **Python**. **_DO NOT FORGET 'end'_**

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

    # without &, you would get an error, and that's because IMM read your file line by line, even if it's incomplete! so if IMM sees 'values = {' it will raise an error, but with & you tell IMM that it should keep looking for the rest of expression(s), till the 'end'

    puts values

    # ---------------------------

    # fuck type annotations but anyway, just for an example
    &def person(
        name: str,
        age: int,
        city: str,
    ) -> str:
        return f"{name} is {age} years old that lives in {city}"
    end

# Decorators
just like Python's!

    &@timed
    def showing_grades():
        io.println('A', 'F')
    end
    
    # & is for creating a block
    # @ is for telling IMM (and also indirectly Python) that we have a decorator!

    # NOTICE: @ for decarators is diffrent from @ for making vars!!
    
    # timed is a function(that can be used as a decorator), which accepts a function, and runs the function automatically, and then prints the time of running it

    # ======>
    # A
    # F
    # processing time: ...s

# Todo
_todo_ is a keyword that is used to specify that some code is not yet **implemented**.

    todo as "I haven't completed it yet"
    # if you run this, you'll get TodoError

# Panic
_panic_ is used for crashing the program when the program has reached a point that should never be reached.

    panic as "Oh Noooooo"
    # if you run this, you'll get PanicError

# Fixme
_fixme_ is used for telling the coder that that line or whatever need some repairings

    fixme as "This code needs your fix to be ran"
    # if you run this, you'll get FixmeError

    # todo, panic and fixme are keywords

# Struct
struct makes a block for you to create some variables, but **NOT** with their values, but with ONLY and ONLY with their _*TYPES*_

    struct Student:
        name: str
        age: int
        grade: str
    end

    Ali := Student()
    # making an instance for our struct
    Ali.name = "Ali"!
    Ali.age = 10!
    Ali.grade = 'F'
    # assigning values to empty fields in our struct!

> Q: What do you think about 'Ali.name := "Ali"'?
>
> You might say that it's not possible, because Ali.name ain't a variable. You're 50/50 right and wrong.
>
> Yes, Ali.name is NOT a variable, but because when you use :=, !, <>, ..., IMM will translate Moon code to Python's and run that, so you could even use static, our, local, ...

# Enum
enum is used for saving bunch of values, with key and a value!


    enum week {"Sunday": iota()+1, "Monday": iota()+1, "Tuesday": iota()+1}
    # defining our enum
    # NOTICE: there is no =
    # NOTICE: we wrote our keys in string type
    
    # NOTICE: iota is a functions, which takes a param, which automatically is False, that is used for reseting iota
    # iota is used for returning a number, which starts from 0 till infinity, unless you assign True to its param!
    # NOTICE: because the param is initially False, you don't have to give it every time
    io.print(iota())!
    # 0
    io.print(iota())!
    # 1
    io.print(iota())!
    # 2
    io.print(iota(False))!
    # DOESN'T MATTER
    # 3
    io.print(iota(True))!
    # 0

    # NOTICE: in the defining of our enum week, we used iota()+1 to have 1 till the end!

    enum today week = 'Tuesday'
    # creating an instance
    # syntax:
    # enum VAR_NAME ENUM_S_NAME = ENUM_S_KEY_NAME
    puts today

# Namespace
it creates a block that you can write functions in it

    namespace ns:
        def greet():
            print("Hello")
    end
    b = ns!
    # creating an instance of our namespace
    # NOTICE: NOT
    # b = ns()!
    b.greet()!
    # calling the functions from our instance

> You might ask yourself (or us!) that we said we should end every block in Moon with 'end', so for example, why in the last example (namespace) we only wrote one 'end'?? and we have 2 blocks(namespace, function)!?
>
>
> The answer is because IMM only seeks for only the 'end', not for closing every block!
> so an 'end' would be the end for all blocks which they are within themselves!

# Par
'par' keyword is used for partial syntax

    def sum(a, b):
        return a + b
    end
    par sum10 = sum(10, ?)
    # par keyword is for letting IMM know that ? will be a placeholde
    puts sum10(5)

> We created a function called sum which will get a and b and add them up and return the result. and we created a partial-instance of sum called sum10, which calls sum func with a 10 as first param and a '?' as second param, and '?' is like a placeholder for us to use this partial-instance more in the future, like we called our partial-instance with a 5, so IMM will replace the placeholder ? with 5 and return the result!
>
> NOTICE that we can use more placeholders, like two ?, or three of it and more!

# Say, puts, putv

- say

        say "Hello, world"
        # no diffrence with printing funcs, but it is a keyword


- puts

        puts "Hi"
        # no diffrence with printing funcs, but it is a keyword
        

- putv


        lit two thousands and one hundred and sixty-two = 2162
        # don't worry; no error here!
        # you don't know why? go to 'lit' part in 'Variables' part
        putv two thousands and one hundred and sixty-two
        

# Importing

- use

        use sys.getsizeof
        puts getsizeof("shit")

        use os.*
        # ====== from os import *

        # so you don't need to write 'os.cpu_count()', you just write
        puts cpu_count()
        


- include

        include sys
        # ok

        include shitty_ass_hole_from_nowhere_module
        # Warning: No module name 'shitty_ass_hole_from_nowhere_module'


- require


        require sys
        # ok

        require shitty_ass_hole_from_nowhere_module
        # ModuleNotFoundError!


    > include vs require
    >
    > if you imported an unreal module or sth with include, you will only get a *_warning_*
    >
    > but if you do that with require, you will get a *_error_*!

- import

        # just like Python
        # e.g.

        import sys
        from fractions import Fraction
        from typing import TypeVar, Generic, Self
        from os import *
        import pandas as np
        # ...

        
# Some other keywords

- addr

        # addr keyword gets the ptr of VALUE, and then saves it to SAVE
        # =>     addr VALUE as SAVE

        addr nil as nil_ptr
        puts nil_ptr

- orelse
    
        # orelse keyword is used for debuging, e.g.

        print("Hi") orelse print("some shit happend")

        # if first expr has any error, second one will be ran
        # else, only first expr will be ran

- fun
        
        # a keyword for creating functions
        # IMM saves that function on STACK dict (where let vars are also in)

        fun add(a, b):
            print(a + b)
        end
        %add(7, 8)
        # to call these funcs, use %

        fun hello():
            print("Hello, World")
        end
        %hello(void)

        # NOTICE: if your func (with fun keyword) does NOT accept any arg, in the calling (with %), use void or Nil or nil or None as param

        # %hello(void)
        # %hello(Nil)
        # %hello(nil)
        # %hello(None)

        # NOTICE that so many (not all) other values are gonna work correctly but for an unwritten rule, let's use these!

- co


        # co is a keyword that runs a function concurrently (usually);(but why usually? because of GIL)

        def download():
            io.println(1)
            io.sleep(2)
            io.println(2)
        end
        co download()
        io.println("here")!
        
        # 1
        # here
        # 2

- if let

        # 'if let' is an expr that checks for being None
        
        # you'd learn better with an expamle

        user := "Mobin"
        if let user as name:
            printf(name)
        end
        
        # =======
        # if user is not None:
        #     name = user
        #     printf(name)

        # NOTICE that this let in 'if let' is diffrent from let for creating vars

- inc & decr

        # inc = ++
        # decr = --

        num := 5
        inc num
        puts num
        # 6
        decr num
        puts num
        # 5

- again

        # exectes the last line (not block) again

        puts "hi"
        again
        # hi
        # hi

- block & does

    - block

            # 'block' makes a block that in the future you can run it

            block b:
                printf("Hello")
            end
    
    - does

            # runs the block
            does b


- also & before & after


        printf("%s", Nil) also print(nil)
        printf("%s", Nil) after print(nil)
        printf("%s", Nil) before print(nil)

- sleep & wait

        sleep 5
        # 5s

        wait 5
        # 5s

- lable & goto

        # we can define a lable and just use it in the future by 'goto'

        lable here:
            printf("Hello")
        end

        goto here

- awaitfor

        # it is a syntax sugar (maybe)

            2 awaitfor printf("Hello")
        #   _          _______________
        #  time              job
        #   to
        #   wait

        # =======
        # async def __RAND_NAME__():
        #    await asyncio.sleep(2)
        #    printf("Hello")
        # asyncio.run(__RAND_NAME__())

        # NOTICE that __RAND_NAME__ is a random name that IMM makes

- object & of


        # with object keyword, you can create your object, then with 'of' you can create an instance of it

        object person:
            name, age
        end
        me = object of person {"Mobin",  16}
        #                      _______   __
        #                      for name  age

        puts me.name, me.age

    
- module

        # syntax:
        # module NAME:
        #   ...
        # end

        # IMM makes a Python file with that NAME and puts the ... in that file, and you can import it and use it later!

        module File:
            NA = 6.02 * (10 ** 23)
        end
        require File
        puts File.NA

- dec

        # is used for declaring variables; assigns them to Nil

        dec inp
        # inp = Nil
        inp := io.getc()

- with

        # iterates in the given iterator and does what you tell her to

        with [2, 6, 1, 2] as num:
            # every element of [2, 6, 1, 2] (2, 6, 1, 2) would be num in every iteration

            printf(to_s(num))
            # 2
            # 6
            # 1
            # 2
        end

- undef

        # just like del (Python's)

        name := "Python Programming Language"
        undef name

- discard

        # deletes the given variable from __locals__

- package

        # syntax: package NAME
        # IMM will make a moon file with that NAME, and puts the rest of the source code in NAME.moon

- mirror

        # copies the value of the given var to the new var
        # syntax:
        # mirror OLD to NEW

        d := {1, 2, 3}
        mirror d to new_d

- ensure

        # just like assert (Python's)

        ensure False, "WO, NAH"

- affirm

        # just like assert (Python's)

        affirm False, "WO, NAH"

# Some classes

'*_expect_*' is a class that has some functions:

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

'*_chan_*' is another one

it's just like Go's

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
    # chan.get gets and removes the last element (if exists) and returns it
    # chan.is_empty and chan.is_full checks for emptyness and fullness of that channel
    # chan.size returns the size of the channel

    # NOTICE: in chan class, when you close a chan, you can't make another one


*_channel_* is another one, like Go's again!

    # channel uses a strict typing

    c = channel(str)!
    # a channel of type string (strict)
    c >> "Hello, World"!
    # putting value in c channel
    print(c << void)!
    # getting the value
    # for the value of << use: (void, Nil, nil or None)
    # NOTICE: other values cause error

    c2 = channel(int)!
    c2 > 2162!
    # notice we used > not >>
    print(c2 < Nil)!
    print(c2 < Nil)!

    # > puts an item on channel without blocking
    # >> puts and item on channel
    # < gets an item on channel and delets it without blocking
    # << gets and item on channel and delets it

    # NOTICE: in channel class, you can have more than one channel, in opposite of chan

    # There were some funcs like size or is_empty or etc. that we had at chan, but we know that they are not reliable (as 'queue' module (py) says), so we didn't implemente them

    # We recomend you, to use channel, not chan


# Some new *Type*s

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

# Errors in Moon

in Moon's errors you can see some words like `<module>`, `<string>`, and name of functions and classes

`<module>` shows that error happend in imm.py in module level

`<string>` shows that an error happend while using exec or eval

`[py]` shows that an error happend at imm.py, either in module level or function or method or etc.

`[moon]` shows that an error happend at your moon file

e.g:

    io.throw(Error, "Some shit happend")!                                  *****


    ERROR MESSAGE AT OUTPUT:

    .\main.moon: 1488: Some shit happend (Error)                            no. 1
    stack traceback:                                                        no. 2
        [py]: 1601: in <module>                                             no. 3
        [py]: 1: in <module>                                                no. 4
        [py]: 762: in throw                                                 no. 5
        [moon]: 1488: in .\main.moon                                        no. 6

in no.1: 1488 shows line of error in your moon file

in no.1: "Some shit happend" is the message of error that we created it by io.throw by ourselves (in *****)

in no.1: (Error) shows which type of error happend (as you see we raised (or maybe we can say threw) an "Error") (in *****)

in no.3: 1601 shows line of error in imm.py (if you look at it, it is refered to "!" expr, that we used at ***** to run it)

in no.5: 762  shows line of error in imm.py (if you look at it, it is refered to throw function at io, that we used it here, at this error shows us)

in no.6: 1488 shows line of error in your moon file (as same as in no.1)


#### NOTICE: these line may be changed, because of being updated or sth else


# Other Languages!

## Python

    # <>, !
    # we already talked about them

## Ruby

    # *
    # with 'RB' keyword

    RB (

        put "Hello, World"

    ) end

## Lua

    # *
    # with 'LUA' keyword

    LUA (

        print("Hello")

    ) end

## Zig

    # *
    # with 'ZIG' keyword

    ZIG (
        const std = @import("std");

        pub fn main() void {
            std.debug.print("Hello", .{});
        }

    ) end

## C

    # **
    # with 'C' keyword

    C (
        #include <stdio.h>

        int main() {
            printf("Hello, World");
            
            return 0;
        }

    ) end

## C++

    # **
    # with 'CPP' keyword

    CPP (
        #include <iostream>

        int main() {
            std::cout << "Hello, World";

            return 0;
        }

    ) end

## Asm

    # **
    # with 'ASM' keyword

    ASM (

        section .data
        ; and etc.

    ) end

## Gleam

    # **
    # with 'GLEAM' keyword

    GLEAM (

        import gleam/io

        pub fn main() {

            io.print("Hello, World")

            Nil

        }

    ) end


*: these languages will be automatically ran by IMM

**: these languages will NOT be automatically ran by IMM, but they will be written in a file called __ main __.EXTENSION (.c, .cpp, .s, .gleam)

*_NOTICE_*: `') end' should be at the end of these blocks exactly like that, not ')end' or ')   end)' or whatever!!`

# Moon's standard variables, functions and classes

- functions

        nop()
        # shows NO OPERATION (an unwritten rule); returns 144 as hex (0x90)

        autorun(func, *args)
        # can be used as a decorator to run the given func automatically

        bytecode(src)
        # returns the bytecode of src

        ptr(n)
        # returns the hexadecimal version of id of n

        swap(a, b)
        # a = b; b = a; swaps the values of a, b

        load(expr)
        # returns a function that executes expr, e.g.
        load('print(0)')()!

        __etype__(input_data)
        # returns the exact type of input_data, e.g.
        # __etype__("2162") -> int
        # but
        # typeof("2162") -> string

        fail(message)
        # raises RuntimeError with message

        next(obj)
        # returns the number after obj if it's a num, or returns the char after obj if it's a string

        before(obj)
        # returns the number before obj if it's a num, or returns the char before obj if it's a string

        __sum__(*n)
        # return the sum of n

        __pow__(a, b)
        # a ** b

        typeof(value)
        # return the type of value

        isinstanceof(__object, __class_or_tuple)
        # return whether an object is an instance of a class or of a subclass thereof

        messure()
        # returns the time of running the program in the end of it

        timed(func, *args)
        # can be used as a decorator which runs func with args, then returns messure function

        sizeof(obj)
        # returns the size of obj; it uses sys.getsizeof func

        lenof(obj)
        # returns the length of obj

        iota(reset=False)
        # for every call, returns a number, which starts from 0, till infinity, unless you assign reset to be True

        __clear_exec()
        # clears the mexec file
        # **

        is_falsy(__obj)
        # if __obj is '', 0, false, False, None, Nil or nil, it returns True, else False

        to_s(value)
        # returns string version of value

        to_i(value)
        # returns integer version of value

        to_f(value)
        # returns float version of value

        to_c(value)
        # returns complex version of value

        to_l(value)
        # returns list version of value

        to_t(value)
        # returns tuple version of value

        to_set(value)
        # returns the set version of value if possible

        to_bin(value)
        # returns the binary version of value

        to_b(value)
        # returns bool(value)

        to_o(value)
        # returns octal version of value

        to_d(key, value)
        # returns a dict, which has key and value
        
        to_enum(value)
        # returns enumerate(value)

        to_r(value)
        # returns the Fraction of value

        to_sym(value)
        # returns Symbol(value)

        responds_to(__obj, __name)
        # checks if __obj and any attribute named __name

        Ok(experssion)
        # evaluates expression:
        # if there is any error, it returns False and error message
        # if there isn't, it returns True

        printf(base, *values)
        # prints base % values

        byte(value)
        # uint8

        rune(value)
        # int32

        __moon__(expr)
        # gets a Python code and returns Moon version of it
        # *

        __py__(expr)
        # gets a Moon code and returns Python version of it
        # *

        append(object, to_add)
        # appends to_add to the end of object

        leq(a, b)
        # checks for loose equality

        seq(a, b)
        # checks for strict equality

        strcpy(var, value)
        # copys value in var

        chomp(__str)
        # returns __str.strip()

        make(T)
        # return T(); T is a type

        alloc(T, *args)
        # returns T(arg)
        # ======
        # retruns every arg in args with type T

        system(command)
        # runs the command with os.system

        update(__name, new_value)
        # gives new_value to __name if exists

        mexec(code)
        # executes code in Moon
        # **

        parseStmt(value)
        # returns mexec(value)

        parseInt(value)
        # returns int(value)

        parseFloat(value)
        # returns float(value)

        div(a, b)
        # a / b (b != 0)

        unreachable(msg="")
        # asserts with msg

        unimplemented()
        # raises UnimplementedError

        var_dump(*values)
        # None, Nil, nil for themselves
        # T(value)     for numbers
        # T(length) value     for the others

        deprecated(message)
        # is used as decorator for telling the user that a func is deprecated

        call(fn, *args)
        # calls fn with args

        each(arr, fn)
        # yeilds fn for every element of arr

        take(arr, n)
        # returns a list containing the Nth value of arr

        assert_equal(a, b)
        # asserts if a and b are equal

        assert_type(a, b)
        # asserts if types of a and b are the same

        retry(fn, *args, count=3)
        # runs fn with args count times

        __random__()
        # is used by IMM for generating random words (length 5)

        define_singleton_method(name, value)
        # defines 'name' with 'value' in globals

        callMain()
        # is used by IMM for calling 'main' function if exists

        countc(string, what_char)
        # returns the count of what_char in string
        
        assertTrue(a)
        # asserts if a is True
        
        assertFalse(a)
        # asserts if a is False
        
        atoi(s)
        # returns int(s)
        
        atof(s)
        # returns float(s)
        
        abort()
        # exits with code 1


        *: these functions are not completed yet!


        **: mexec writes the code you gave in a file then gives it to IMM. if the file is NOT empty, it can cause some problems, like unwanted printings or whatever YOU wrote in that file. IMM does NOT write anything automatically in that file, till you tell her to. note that you can clear the file with __clear_exec func

------------------

- variables

        nil
        # showing nothingness
        # ***

        true
        # showing trueness or 1
        # ***
        
        false
        # showing falseness or 0
        # ***
        
        maybe
        # between True and False
        # ***
        
        unknown
        # showing unknoness
        # ***
        
        HUGE_VAL
        # showing a huge value
        # ***
        
        perhaps
        # just like maybe
        # ***
        
        anything
        # showing anythingness
        # ***

        undefined
        # showing undefiningness
        # undefined is a falsy value
        # ***

        nothing
        # showing nothingness
        # length of nothing is 0
        # ***

        mystery
        # showing a mystery value!
        # NAH, just like the others
        # ***

        void
        # showing voidness
        # length of it is 0, and is a falsy value
        # ***
        
        inf
        # infinity
        
        nan
        # Not A Number
        
        zero
        one
        two
        three
        four
        five
        six
        seven
        eight
        nine
        ten
        # alpha numbers
        
        stdout
        # standard output
        
        stdin
        # standard intput
        
        stderr
        # standard error
        
        __FILE__
        # the first argument value
        
        __VERSION__
        # version of IMM
        
        __LOCALS__
        # local variables, functions, ...
        
        __GLOBALS__
        # global variables, functions, ...
        
        __NAME__
        # __name__ (Python's)
        
        FILE
        # the running Moon file

        ERR
        # if any error happened in the progrm, and if IMM passed it, it would be saved in ERR

        _
        # any result, from input giving functions in 'io' class, is saved on _

        keywords
        # a list of Moon's keywords

        RED
        GREEN
        PURPLE
        CYAN
        YELLOW
        ORANGE
        WHITE
        GRAY
        BLUE
        # colors; e.g.
        # puts f"{RED} WARNING MESSAGE FOR YA"
        
        BASE
        # normal; e.g
        # puts f"{GREEN} Hi{BASE}"
        
        UNDERLINE
        # underline
        
        BOLD
        # bolding
        
        ITALIC
        # italic font (kinda)
        
        BLINK
        # blinking text
        
        LINE
        # a line on text
        
        D_UNDERLINE
        # double underline

        PLATFORM
        # telling the platform you're on, Windows, Linux, ...

        pi
        # pi ~= 3.14

        e
        # e ~= 2.17...

        tau
        # tau = 2 * pi

        Nil
        # showing nothingness
        # ****

        NilPtr
        # the ptr function result of Nil

        NonePtr
        # the ptr function result of None (Python's)
        
        ARGC
        # argument count

        ARGV
        # argument values

        π
        # pi
        
        𝜏
        # tau

        _G
        # __GLOBALS__

        _V
        # __VERSION__


        ***: these variables are not realy restricted! using Python's are recommended! but for values like (maybe, unknown, HUGE_VAL, perhaps, anything, undefined, nothing, mystery, void) that are not available on Python (sorta), just note that they are not a real value, so use them just as a face!!


        ****: Nil vs nil
            => Nil has more power and features than nil

-----------------

- classes

    - IO

            >>      # printing to output
            <<      # getting an input
            &       # returning the ptr
            >       # returning the value

            # -----------------------------

            IO() >> "Hello"!
            IO() >> (IO() << ": ")!
            IO() &None!
            res := IO() > "Hello"


    - Stack

            push(value)     # appends value to the end of stack

            pop()           # removes the last value from stack

            top()           # returns the last value from stack

            print()         # prints and removes the last value

            get()           # prints the last value from stack

            all()           # prints the stack

            add()           # adds the last two values

            sub()           # the last value - before the last one

            mult()          # the last value * before the last one

            div()           # the last value / before the last one

            pow()           # the last value ** before the last one

            putchar(unicode_code)  # appends unicode string of unicode_code to the end of stack


    - Symbol(NO INH; arg)

            to_s(self)
            # returns string version of symbol

            next(self)
            # returns the next char in symbol

            startswith(self, with_what)
            # checks if symbol starts with with_what

            endswith(self, with_what)
            # checks if symbol ends with with_what

    Error(INH: BaseException)

    TodoError(INH: BaseException)
    
    PanicError(INH: BaseException)

    NoMethodFoundError(INH: BaseException)

    SizeError(INH: BaseException)

    UnimplementedError(INH: BaseException)

    RangeError(INH: BaseException)

    FixMeError(INH: BaseException)
    
    BehaviorConditionError(INH: BaseException)

    - Range(NO INH; start, end)

            new(self)
            # returns a range from start till end; it can be alphabets and nums

    
    - io(NO INH)

            print(*values, sep="\t")
            # prints values with seperator \t (of course you can change it !) and at the end it does not print a new line, and returns nil

            println(*values, sep="\t")
            # prints values with seperator \t (of course you can change it !) and at the end it prints a new line, and returns nil

            throw(__err, message: str = "")
            # raises the __err ( MUST be derived from BaseException ) with message message

            open(file, mode)
            # opens the file with mode mode

            freads(file)
            # reads lines from file
            # *****

            fread(file)
            # reads a line from file
            # *****

            freadc(file)
            # reads a char from file
            # *****

            fprint(file, *values)
            # puts values in file and a new line, then returns nil

            fprintf(file, base: str, *other)
            # puts base % other in file and a new line, then returns nil; it formats the base

            close(file)
            # closes the file

            status(file)
            # returns the status of the file (is opened or closed)

            read(prompt)
            # gets an input with prompt
            # *****

            fwrite(*values, file)
            # writes values in file, then returns nil

            gets()
            # gets an input string 
            # *****

            getc()
            # gets an input char
            # *****

            putc(*values)
            # prints a char
            # if any type except char is given, raises error

            printf(base: str, *values)
            # if base is not string, raises error
            # prints base % values

            sprint(value)
            # returns value
            name := io.sprint("mobin")
            # name = "mobin"

            sprintf(base: str, *values)
            # formatted sprint

            var_dump(*values)
            # prints some result about values

            system(command)
            # this will use os.system to execute command

            print_r(__value: list | dict | set | tuple)
            # prints the __values but in pretty way
            # if __value is not list or dict or set or tuple, raises error; returns nil

            exit(code: int = 0)
            # system exit with code code

            id(__obj: object)
            # returns hex format of int id of __obj
            # this is guaranteed to be unique for every object

            rand(max: int)
            # returns random.randint(0, max)
            # = 
            # returns a random number in [0, max] (math range!)

            sleep(sec: float)
            # sleeps for sec

            format(base: str, *values)
            # just like sprintf

            catch(__to_do: str, __err_type)
            # it tries: exec(__to_do)
            # excepts BaseException as e, if type of e is not the __err_type
            # returns ERR, else prints e, then returns True, and if there is no problem, returns nil
            # so
            # if there is error and __err_type is the error type, it returns True
            # but if there is error and __err_type is not the error type, it returns ERR
            # but if there is no error, it returns nil
            #
            #
            x := io.catch("io.print(hello)", NameError)
            io.print(x)!
            # True
            #
            x := io.catch("io.print(hello)", KeyError)
            io.print(x)!
            # ERR
            #
            x := io.catch("io.print('hello')", NameError)
            io.print(x)!
            # hellonil

            pprint(*values)
            # pretty print values with \n

            pprintf(base: str, *other)
            # formated pretty print with \n

            lprint(value)
            # uses for printing local variables ( my, local, native )
            # note that value must be string
            # this function does not print an '\n' at the end

            lprintln(value)
            # uses for printing local variables ( my, local, native )
            # note that value must be string
            # this function does print an '\n' at the end

            cprint(*values, sep="\t", end="\n", file=stdout)
            # uses for printing values but, customly !

            vprint(*values)
            # prints variables that are created by lit keyword
            # each value must be string

            vprintf(format, *values)
            # prints variables that are created by lit keyword but in a formatted version

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

            scanf()
            # returns the input
            # *****

            alert(value)
            # returns a warning with msg

            echo(key)
            # it will print the value of the given key in STACK dict, that you can define vars with let keyword at it
    

    - mem(NO INH)

            # a memory-like class; which has a POINTERS and STORE dict;


            &
            # is used for creating a pointer in POINTERS
            # e.g.
            #
            # zero_ptr := mem() &0
            
            *
            # is used for getting the result of a pointer
            # e.g.
            # 
            # puts mem() *zero_ptr

            imprint(self, key, value)
            # is used for creating a new space in STORE, the name is key; and the value is value

            recall(self, key)
            # is used for getting the value of the key

            forget(self, key)
            # is for poping the value of the key from STORE

            clear(self)
            # is for clearing the STORE completely

    
    - Imaginary(INH: complex);




    - Kernel(METACLASS: _KERNEL_META) ******

            # has every local and global var, func, ...



    - lazy(NO INH; func)

            # is a class that delays function evaluation until its value is accessed


            class Data:
                @lazy
                # as a decorator
                def show_my_number():
                    return 2162
            end

            obj := Data()
            # here nothing has happened yet !
            printf("%s", obj.show_my_number)!
            # BOOM


    - freezable(NO INH; arg)

            # makes a freezable object

            freeze(self)
            # freeze the object

            # e.g.
            # 
            f := freezable("arg")
            f.arg := "Hello"
            printf(f.arg)!
            f.freeze()!
            f.arg := "Bye"


    - visibility(NO INH)

            private(func)
            # can be used as a decorator; which make a function private

            # e.g.
            #
            &@visibility.private
            def whoami():
                io.print("HOW ON GOD'S GREEN PLANET COULD I GUESS?")
            end

    
    - expect(NO INH; value)

            toBeEqualTo(to)
            # returns that value == to

            toBeGreaterThan(than)
            # returns that value > than
            
            toBeLessThan(than)
            # returns that value < than
            
            toBeGreterEqualTo(to)
            # returns that value >= to
            
            toBeLessEqualTo(to)
            # returns that value <= to
            
            toBeNotEqualTo(to)
            # returns that value != to
            
            toBeIn(what)
            # returns that value in what
            
            toBeNotIn(what)
            # returns that value not in what


    - chan(NO INH)

            send(value)
            # sends the value to channel
            
            get()
            # gets the last value from channel
            
            is_empty()
            # checks if channel is empty; THIS IS NOT RELIABLE
            
            is_full()
            # checks if channel is full; THIS IS NOT RELIABLE
            
            close()
            # closes the channel FOR EVER;
            # you can NOT make any other one after closing a chan
            
            size()
            # returns the size of channel; THIS IS NOT RELIABLE


    - channel(NO INH; __type)

            >>
            # puts and item on channel

            <<
            # gets and item on channel and delets it

            >
            # puts an item on channel without blocking

            <
            # gets an item on channel and delets it without blocking
            


    - short_int(INH: int; value)

            # (-32768, 32767]
    
    - ushort_int(INH: int; value)
            
            # (0, 65535]
    
    - unsigned_int(INH: int; value)

            # (0, 4294967295]
    
    - long_int(INH: int; value)
            
            # (-2147483648, 2147483647]
    
    - ulong_int(INH: int; value)
            
            # (0, 4294967295]
    
    - long_long_int(INH: int; value)

            # (-(2**63), (2**63)]
    
    - ulong_long_int(INH: int; value)

            # (0, 18446744073709551615]
                    

    - undoable(NO INH; init_state)

            # creates an object, which you can change the values inside, and go back to the last value (undo);
            # or even 
            
            undo(self)

            redo(self)

            # e.g.
            #
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

            # {'c': 2}
            # {'c': 1}
            # {'c': 0}
            # {'c': 1}

    - _list(INH: list; iterable)

            >>
            # appends the given value to the end of iterable

            first
            # IS A PROPERTY; returns the first element of iterable

            last
            # IS A PROPERTY; returns the last element of iterable

    - natural(INH: int; value)

            # make the value to be NATURAL if possible!

    --------

            *****: they save the result in '_'

            ******: _KERNEL_META is a class which creates a frame of Python's live object and (kinda) saves them all inside of itself (YOU CAN READ THE SOURCE FILE)


> _NOTICE_ that you may see some functions, variables or even classes in __ globals __ or __ locals __ that are not told here. that's because those were only meant to be used by IMM for a certain job, result, name, or whatever


# Keywords:
    
    | True     | shows boolean true value                                                                                      |
    | False    | shows boolean false value                                                                                     |
    | nil      | a type alias of None, but you'd better use Nil not nil for showing nothing                                    |
    | Nil      | shows nothingness                                                                                             |
    | module   | creates a module                                                                                              |
    | alias    | creates a type alias                                                                                          |
    | dec      | declares a varaible                                                                                           |
    | def      | defines a new function                                                                                        |
    | if       | creates conditions                                                                                            |
    | else     | it can be used with: for, while, if, try, which executes when the other blocks are not executed               |
    | elif     | the countinue of if or when blocks                                                                            |
    | until    | do sth until condition is true                                                                                |
    | unless   | do sth if condition is false                                                                                  |
    | class    | creates a new class                                                                                           |
    | switch   | switch-case stmt that check on variables                                                                      |
    | case     | the complement of switch or match                                                                             |
    | while    | a loop which goes until condition is false                                                                    |
    | for      | a loop that usually is used for iterating over iterators                                                      |
    | try      | try block that tries the code given and catchs errors                                                         |
    | excpect  | the catch block of try block                                                                                  |
    | finally  | this block will be ran; not based on try block thta if it caught any error or not                             |
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
    | or       | or operator                                                                                                   |
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
    | addr     | returns a pointer of a object and saves it in the varible you give;                                           |
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
    | nothing  | represents nothing                                                                                            |
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
    | let      | is for making a type of variable which is saved on STACK dict                                                 | 
    | fun      | is for making a type of function which is saved on STACK dict                                                 |
    | object   | is for making an object                                                                                       |
    | of       | is for creating an instance of an object created with object                                                  |
    | co       | is for running a fuction like a thread                                                                        |
    | use      | is for importing                                                                                              |
    | affirm   | is for asserting                                                                                              |
    | whilst   | is just like while                                                                                            |
    | be       | is for making behaviors                                                                                       |
    | onlyif   | is used in behavior blocks to make a condition for it                                                         |
    | ifnot    | is used in behavior blocks to create a personal response to error                                             |

# Other Things:

    age := 16
    can_vote := age >= 18 and True or False
    # False

    puts nan == nan
    # False !!!

    mexec("if 1:\n\tio.println('hello')\nelse:\n\tio.println('bye'\nend"))

    require math
    $a = {"p" : print}
    <a["p"]("Hello, World")>
    print = math.sin
    <a["p"](print(1))>
    $sin = a["p"]
    <sin("Bye, World")>

    io.print_r([nil, True, False])!
    # print_r prints only list !
    # print_r("hello")!
    # error !!
    
    io.sprint(true)?
    # this is like a debuger
    # true
    #=> nil

    with "hello" as item:
        io.print(item)
        # h
        # e
        # l
        # l
        # o
    end

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

    with open("somefile", "r") as f:
        printf("%s", f)
        # reads the whole file
        # if i don't wanna lie, i don't know why is this reading the file !
    end

    puts hello
    if ERR is not None:
        printf(ERR)
    end

    l := _list([1, 2, 3])
    l << 4!
    puts l
    puts l.first
    puts l.last

    Kernel.printf(Kernel.io.mem() &None)!
    # just like Ruby's one