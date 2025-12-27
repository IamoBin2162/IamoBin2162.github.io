# <measure()>
# # calling 'measure' function to get the execution time

# class Car:
# 	# Object-Oriented Programming
# 	def __init__(self, name, year):
# 		# initializing the name and year of the Car
# 		self.name = name
# 		self.year = year
# end
# # 'end' is nessecery for ending classes
# BMW := Car("BMW", 2024)
# # creating a instance of Car to BMW object
# <print(BMW.name, BMW.year)>
# # you can use <> for calling function
# # printing the name and year of the BMW

# def test():
# 	# Creating the function, using 'def' keyword
# 	print("hello")
# 	print("bye")
# 	# do sth at function, 'test'
# end
# # 'end' is nessecery for ending function
# <test()>
# # calling test function

# name = "mobin"
# # creating variable name
# switch name:
# # using switch-case for name variable
# # as same as if name == ...: ...
# 	case "mobin":
# 		# if name == "mobin": ...
# 		println("Hi Admin")
# 	case _:
# 		# in case of a switch, _ means else !
# 		# else: ...
# 		println("Hi User")
# end
# # 'end' is nessecery for ending switch-case

# num = 0
# # defining num variable
# while num < 100:
# 	# while CONDITION is true: ...
# 	num += 1
# else :
# 	# if CONDITION is not true: ...
# 	println("finished")
# end
# # 'end' is nessecery for ending while

# for n in range(10):
# 	# for loop
# 	# until 10
# 	# 0 1 2 3 4 5 6 7 8 9 (not the 10)
# 	println(n)
# end
# # 'end' is nessecery for ending for

# double = lambda num: num * 2
# # creating lambda function
# <println(double(7)>

# <println(math.acos(-1))>
# # using math module functions

# $name = "Mobin"
# # global variables with '$'
# <println(name)>

# x = 0
# # defining x variable to 0
# until x != 10:
# 	# while COND is true: ...
# 	println(x)
# 	x += 1
# 	# print x then increse the x by 1
# end
# # 'end' is nessecery for ending until

# unless x == 10:
# 	# while not COND is true: ...
# 	# or
# 	# while COND is false: ...
# 	println(x)
# 	x += 1
# 	# print x then increse the x by 1
# end

# # declaring name variable
# # imm is gonna give nil value for this variable
# dec name
# <println(typeof(name))>
# # <type 'nil'>

# dec name
# # declaring the name
# name = fgets()
# # getting a value from stdin

# if name == "":
# 	# if name is ""
# 	println("bad")
# 	# print "bad"
# elif name == "nil":
# 	# or if name is "nil"
# 	println("50 50")
# 	# print "50 50"
# else :
# 	# otherwise
# 	println("good")
# 	# good
# end

# def sayHi(name):
# 	# creating function called sayHi with a name param
# 	println(f"Hello {name}")
# 	# printing message
# end

# sayHi->"Mobin"
# # calling the function with ->
# # but -> prints the result
# # Hello Mobin
# # None

# # ** usage of -> in variables for calling functions are not allowed !! **

# def math(a, b, func):
# 	# a function to the func with a and b
# 	return func(a, b)
# end

# def add(a, b):
# 	# to use with math
# 	return a + b
# end

# <println(math(5, 7, add))>
# # a way to call the math
# math->5, 7, add
# # another way

# math->10, 5, lambda x, y: x * y

# as same as:

# SOME_NAME = lambda x, y: x * y
# <println(math(10, 5, SOME_NAME))>
# math->10, 5, SOME_NAME

# or

# def SOME_NAME2(x, y):
#    return x * y
# end
# <println(math(10, 5, SOME_NAME2))>
# math->10, 5, SOME_NAME2

# num = 0
# until num < 100:
# 	println(num ** 10)
# 	num += 10
# else:
#   # use of else with until loop
#   # that means when the COND is false this block (else) will be executed
# 	println("finished process")
# end

# func = (a, b) -> a + b
# # lambda functions using ->
# func->7, 8
# # -> for calling functions and -> for creating lambda functions are diffrent !!

# myNone = () -> None
# # returning None
# # () means no params !
# myNone->
# # calling a function with -> without any param

# $greet = (name) -> f"Oh, Hi {name}"
# # -> function, in $ (global) variables
# greet->"Mobin"
# # calling 'greet'

# $numbers = {"1": iota(), "2": iota(), "3": iota()}
# # after each usage of iota()
# # it increases the value.
# # it starts from 0
# println->numbers
# # if you use -> for calling println or etc. that prints sth to stdout,
# # you will get 'None' at the end

# # but:
# sprint->numbers
# # sprint return the value you give
# # but no need to use it in functions

# # for example:
# Name = sprint("John Doe")
# # here, sprint returns ( or we can say gives ) the "John Doe" to Name
# sprint->Name
# # not to get None !

# module person:
# 	# creating module
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def show_result(self):
# 		return f"{self.name} is {self.age} years old"
# end
# # 'end' is neccessery for ending module

# $me = person("mobin", 16)
# # instace of person
# sprint->me.show_result()
# # as i said ,
# # not to get None

# <io.debug(nil)>
# # calling with <>
# io.debug->nil
# # calling with ->

# nil |> io.debug
# # calling function with |> (pipeline)
# # imm exchanges this code to:
# # io.debug(nil)

# nil |> typeof |> io.debug
# # imm exchanges this code to:
# # io.debug(typeof(nil))

# $test = io.println("Hello")
# test == nil |> println
# test is nil |> println
# # because io.println return 'nil' at the end
# # test == nil

# f = io.open("main.txt", "r")
# # opening file with mode 'r' only for reading
# <io.println(io.freads(f))>
# # readlines, returns a list
# f |> io.close
# # close file
# <io.println(io.status(f))>
# # is file closed or not ?

# age = 14
# canVoteOrNot = age >= 18 and true or false
# # means:
# # if age >= 18:
# 	# return true
# # else:
# 	# return false
# <io.write(tostring(canVoteOrNot))>

# alias myNone = None
# # new alias type
# <io.println(myNone)>

# if both(True, True):
# 	# both must be True
# 	io.println("Hi")
# end

# if either(True, True):
# 	# one of them must be True or both
# 	io.println("Hello")
# end

# if neither(False, False):
# 	# non of them must be True
# 	io.println("Bye")
# end

# if xor(True, False):
# 	# one of them must be True
# 	io.println("Boobooli")
# end

# "if" |> typeof |> io.println
# # <type 'keyword'>

# # moon has alaphabet's number,
# # like one, two, ...
# # but to ten
# # but we can make higher than ten
# eleven = int(tostring(one) + tostring(one))
# # getting the string of one ('1') twice
# # and put them together
# # and change the type of '11' to a int
# # '11' -> 11
# io.sprint -> eleven + eleven
# # 22

# mexec("name = 'mobin'")
# # mexec => moon execute
# # how it works?
# # first it gets the code you give
# # then writes it into a file called '__exec__.txt'
# # then runs it with 'moon' in command line
# # so if e.g you create a variable called 'name' with mexec,
# # there wont be a variable called 'name' in this file !

# # puts is added as a keyword, like print (but print is function)
# # but the diffrence between 'puts' and other printing functions is
# # 'puts' uses pretty printer to print sth
# # so e.g. a list or dict or ... will be printed pretty :)
# # puts ...
# puts keywords

# global x = (a) -> a
# # global x
# # as same as $x = ...
# puts x(7)

# with open("__exec__.txt", "r") as f:
#   # as same as: f = open(...)
#   # but with 'with' keyword this is going to close it auto !
# 	io.println(f)
# end

# puts [x for x in range(1, 100)]
# # as same as:
# # for x in range(1, 100):
# #    puts x
# # end

# $x = %s[hello, world]
# # a way to create a string
# $y = %(hello, world)
# # another way to create string
# $z = ?a
# # another way to create string, but this way (?) accepts only char
# # that means a string with length 1

# y = (7..8)
# # just 7 not 8
# y = (7..8+1)
# # 7, 8
# y = (7..9)
# # 7, 8
# # making range with '..'

# puts nan == nan
# # False

# never test = 8
# variables with 'never' wont be used
# #puts test
# # error: test is not defined

# mexec("if 1:\n\tio.println('hello')\nelse:\n\tio.println('bye')\nend")

# require "math"
# # if there is problem, raises Error
# include "math"
# # if there is problem, prints Warning

# a = 8
# do :
# 	io.println("hello")
# 	# first prints "hello"
# 	# then if COND is true
# 	# prints "hello" in loop
# while a > 7
# end

# def say_hi():
#   return "hello"
# end
# # if function doesnt take any param, you can use '<-' to call it
# say_hi <-
# # as same as:
# # print(say_hi())

# measure <-
# $result = 0
# for k in Range(1_000_000):
#   result += ~k
# end
# io.sprint -> result

# require('math')
# $a = {"p" : print}
# <a["p"]("Hello, World")>
# print = math.sin
# <a["p"](print(1))>
# $sin = a["p"]
# <sin("Bye, World")>
# # playing with name, but this is dangerous !

# <io.new("x", void)>

# def y(a: int, b: int) -> int:
#   # type annotations
#   io.print(a + b)
# end

# include('Int')
# $odd_or_even = (number) -> "even" if Int.is_even(number) else "odd"
# io.sprint -> odd_or_even(70)
# <io.print_r([nil, true, false])>

# include('List')
# <List.print_r(["hello"])>

# puts to_s(7)
# # to string
# puts to_i(7)
# # to int
# puts to_f(7)
# # to float
# puts to_c(7)
# # to complex
# puts to_l('7')
# # to list
# puts to_t('7')
# # to tuple
# puts to_set('7')
# # to set
# puts to_bin(7)
# # to binary
# puts to_b(7)
# # to bool
# puts to_o(7)
# # to octal
# puts to_n(7)
# # to nil
# puts to_d(0, '7')
# # to dict
# puts to_enum([1, 2])
# # to enumerate
# puts to_z('hi')
# # to zero
# puts to_r(0.1)
# # to rational

# class Test:
#   def test(): ...
# end
# puts responds_to(Test, 'test')

# <io.throw(SyntaxError, "hello")>

# io.print => "hello"

# io.putc => 'c'

# require('Math')
# io.print => Math.pi

# include('File')
# $f = File.fopen("main.txt", "r")
# io.print => File.freadc(f)
# io.print => File.freads(f)
# io.print => File.fread(f)
# File.close => f
# io.print => File.closed(f), File.name(f), File.mode(f)
# $f = File.fopen("main.txt", "a")
# io.print => File.fwrite("\nbye, world", f)

# include('Random')
# <Random.new_seed(10)>
# io.print => Random.rand()
# io.print => Random.randi(0, 10)

# switch 70:
#   case range(1, 50):
#     io.print("low")
#   case range(51, 75):
#     io.print("medium")
#   case range(76, 100):
#     io.print("high")
#   case _:
#     io.print("very high")
# end

# io.print => Range("a", "e").new()
# for idx in range(len(Range("a", "c").new())):
#   io.print(f"{idx}: {Range('a', 'c').new()[idx]}")
# end

# include('Time')
# io.print => Time.now

# system => 'echo hello'

# require 'Int'!
# include 'List'!
# List.print_r [Int.is_even(8)]!

# io.sprint -> "hello %s" % "world"
# io.sprintf -> "hello %s", "world"

# io.sprint(true)?

# with "hello" as item:
#   io.print(item)
# end

# class Person:
#   def __init__(self, name: str, age: int, id: int) -> None:
#     self.name = name
#     self.age = age
#     self.__id = id
# end
# $mobin = Person("mobin", 16, 122333)
# io.print(mobin.name, mobin.age, mobin._Person__id)!

# <boobooli = "@">
# io.print(boobooli)!

# io.printf("%.80f", .1 + .2)!
# io.printf("💀")!

# io.printf("%s", _)!
# io.gets()!
# io.printf("%s", _)!
# io.read("")!
# io.printf("%s", _)!
# io.getc()!
# io.printf("%s", _)!

# $result = ""
# for count in range(5+1):
#   result += to_s(io.rand(1))
# end
# io.printf(result)!

# $x = io.catch("io.printf(hello)", NameError)
# io.printf("%s", x == True)!
# # error, True

# $x = io.catch("io.printf(hello)", KeyError)
# io.printf("%s", x == ERR)!
# # True

# $x = io.catch("io.printf('hello')", NameError)
# io.printf("%s", x == nil)!
# # 'hello', True

# io.printf("%d", argc)!

# io.printf(chomp("hello\n\n"))!
# io.printf(chop("hello"))!

# io.open("main.txt", "r") do |file|:
#   io.printf("%s", io.freads(file))
# end

# io.printf("%s", is_zero(0))!

# $a = Char('*')

# `cls`

# puts self

# include('typing')
# @typing.final
# class Test:
#   ...
# end

# $Func = (a, b) -> a + b
# puts Func(2, 2)
# $Func = (a, b) -> a - b
# puts Func(2, 2)

# $value = 0
# puts value
# update('value', 7)!
# puts value
# # 7

# update('value', 8)!
# # err

# try:
#   io.puts(0 / 0)
# except:
#   io.puts(ERR)
# end
# io.puts(ERR)
# raise KeyError(nil)!
# io.puts(ERR)

# puts _
# # nil
# $x = io.read(">>> ")
# puts x == _
# # True

# puts ERR
# nil

# io.throw(TypeError, "Mooooon")!
# puts ERR
# #<TypeError: Mooooon>

# $result1 = stdin.readline()
# puts result1
# # getting input with stdin
# # note that, there is no 's' at the end of readline !

# $result2 = stdin.readlines()
# # note that, there is a 's' at the end of readlines !
# # infinitly getting input
# # because when you are reading stdin, with readlines, this is going to read the lines till the end, but the end for stdin is ^C (i think this is only in Windows), so your program will not finish until ^C
# puts result2

# $pointers = {}
# class io:

#     def cout(*values):
#         for value in values:
#             print(value)

#     def cin(prompt):
#         return input(prompt)

#     def __rshift__(self, value):
#         return io.cout(value)

#     def __lshift__(self, prompt):
#         return io.cin(prompt)

#     def __and__(self, value):
#         pointers[hex(id(value))] = value
#         return hex(id(value))

#     def __mul__(self, pointer):
#         try:
#             return pointers[pointer]
#         except KeyError:
#             print(f"ERR: {pointer} is not defined or not a pointer")
# end

# $_ = io()
# _ >> "hello"!
# _ >> (_ << ">>> ")!
# _ >> (_ &7)!
# _ >> (_ * (_ &7))!
# $p = _ &'hello'
# _ >> p!
# _ >> (_ *p)!
# _ >> f"{p} -> {_ *p}"!
# _ >> (_ &(_ << ">>> "))!

# $fname = 'Mobin';
# $full_name = strcpy(fname) + ' Shibafar';
# puts full_name

# `moon main.moon`

# def prime():
#   io.printf("Starting...")
#   result = 0
#   for num in range(0, 10):
#     if num > 1:
#       for i in range(2, num):
#         if num % i == 0:
#           break
#       else :
#         io.printf("%d", num)
#         result += num
#   io.printf("-- %d --", result)
# end
# prime()!

# # i added async funcs

# match 5:
#   case 5:
#     printf("%s", "yep")
#   case _:
#     printf("%s", "nop")
# end
# # you can use match as like switch

# printf("Hello") <=
# # calls itself without args

# printf => "Hello"
# # calls itself with args

# io.sprintf -> "Hello"
# # prints itself with args

# io.sprintf("Hello") <-
# # prints itself without args

# <printf("Hello")>
# # call the function

# printf("Hello")!
# # calls the function

# local name = "Mobin"
# puts name

# todo as "I haven't completed it yet"
# panic as "Oh shoot"

# io.throw(Error, 'Oh')!

# 5 add 7 add 8 add 8
# 28 sub 8 sub 10
# 2 mult 8 mult 2
# 81 div 9 div 3
# 2 pow 2 pow 2
# 15 mod 5
# True xor False
# 1 shr 5
# 1 shl 5

# addr nil as nil_ptr
# puts nil_ptr

# __clear_exec__ <=
# parseStmt("puts 'Hello'")!

# $name = 'Mobin'
# when name == "Mobin":
#   printf("Admin")
# else:
#   printf("User")
# end

# $list = [0, 1, 2]
# foreach elem as list:
#   printf("%d", elem)
# end

# $list = Range('d', 'f').new()
# foreach elem as list:
#   printf(elem)
# end

# io.printf("%.2f", 22 / 7)!

# printf(DidYouMean.correction2("returm io.printf"))!
# printf(DidYouMean.correction("put"))!

# printf(each([1, 2, 3]))!

# printf(next("a9b"))!
# printf("%s", next("12"))!

# fail("This is RuntimeError")!

# print(Symbol("done"))!

# type Z = dict[int]
# $num: Z = 5
# puts num

# alias Z int
# $num: Z = 5
# # i hate type annotations. but anyway ...
# puts num

# struct Student:
#     name: str
#     age: int
#     grade: str
# end
# $Ali = Student()
# $Ali.name = "Ali"
# $Ali.age = 15
# $Ali.grade = 'A'
# puts Ali.name

# enum week {"Sunday": iota()+1, "Monday": iota()+1, "Tuesday": iota()+1, "Wednesday": iota()+1, "Thursday": iota()+1, "Friday": iota()+1, "Saturday": iota()+1}
# enum today week = 'Sunday'
# puts today

# say "Hello, world"

# 8 neq 9
# 8 eq 8
# 8 gt 5
# 8 lt 9
# 8 ge 8
# 8 le 8

# my grade = 17
# io.lprint("grade")!

# our name = "Mobin"
# puts name

# num := 2162
# puts num

# until (message := io.gets()) != "mobin":
#     printf("Oh")
# end

# my num = 2162
# io.lprint('num')!
# discard num
# io.lprint('num')!

# io.cprint("Hello")!

# puts Imaginary(7, 8)

# END {
#     printf("%d", 8 * 8)
# }
# defer printf("Bye World")

# mut user = "Mobin"
# puts user

# package moon

# module File:
#     NA = 6.02 * (10 ** 23)
# end
# require("File")!
# puts File.NA

# auto array = Range(0, 10).new()

# define("n", 0)!
# puts n

# require("fmt")!

# loop:
#     fmt.Println("Hello")
# end

# puts Ok("print")

# lit $n = 0
# io.vprintln('$n')!

# IO >> (IO << "-> ")

# set n to 8
# puts n

# define __my_macro(a, b) a if a < b else b
# puts __my_macro(8, 6)

# define magic_number 2162
# puts

# macro __my(a, b) a if a < b else b
# puts __my(4, 8)

# macro number 0xaa
# puts number

# a := 0
# b := 1
# consume a to b
# puts a
# puts b

# deprecated("This is old, use new one")
# def old():
#     printf("Old")
# end
# def new():
#     printf("New")
# end
# old <=

# printf("%s", maybe, undefined, unknown, true, false, True, False, nil, None, inf, nan, ok, ERR, HUGE_VAL, Nil)!

# n := make(bool)
# printf("%s", n)!

# static n = 5
# puts n

# forever:
#     printf("Hi")
# end

# RB (

#     p "Hello, World"

# ) end

# LUA (

#     print("Hello")

# ) end

# ZIG (
#     const std = @import("std");

#     pub fn main() void {
#         std.debug.print("Hello", .{});
#     }

# ) end

# C (
#     #include <stdio.h>

#     int main() {
#         printf("Hello, World");

#         return 0;
#     }

# ) end

# ASM (

#     section .data

# ) end

# Go (
#     package main
#     import "fmt"

#     func main() {
#         fmt.Println("Hello")
#     }

# ) end

# GLEAM (

#     import gleam/io

#     pub fn main() {

# 	io.print("Hello, World")

# 	Nil

#     }

# ) end

# CPP (
#     #include <iostream>

#     int main() {
#         std::cout << "Hello, World";

#         return 0;
#     }

# ) end

# puts Nil, NilPtr, NonePtr

# unreachable()!
# panic as "Not hereeeeee!"
# todo as "Complete here"

# &print(
#     "hi",
#     "bye"
# ) end

# lit 5 = 6
# putv 5

# while 1:

#     io.print("moon> ")
#     __input = input()

#     if __input == "cls":
#         system("cls")

#     elif __input == "exit":
#         break

#     else:
#         mexec(__input)

# end

# printf("%s", type(div(8, 0)))!

# typeof ~> Nil

# num := 1.5

# var res = typeof ~> Nil
# var func = fn (name) -> printf(f"Hello {name}")
# var call = print => "Hello"
# var call = int <=
# var name = "Mobin"
# var a = 5 add 5
# var s = 5 sub 5
# var m = 5 mult 5
# var d = 5 div 5
# var p = 5 pow 5
# var m2 = 5 mod 5
# var x = 5 xor 5
# var s2 = 5 shr 5
# var s3 = 5 shl 5
# var e = 5 eq 5
# var n = 6 neq 5
# var g = 6 gt 5
# var g_e = 6 ge 6
# var l = 5 lt 6
# var l_e = 5 le 5
# var i_n = Nil isnot Nil
# var i_i = Nil is Nil
# var new_val = cast[int](num)
# var n_i = "h" notin "bye"
# var p = Nil |> io.sprint
# var compar = 5.4 ~= 5
# var compar2 = num === 1.5
# var s = sin pi
# var c = cos pi
# var t = tan pi
# var c = cot pi
# var sq = sqrt 4
# var cb = cbrt 8
# var l = log 10
# var nl = ln e
# var c = 4 <=> 5
# var short_hand = 5 < 4 ? True : False
# var d = printf("Hello") ?? "Error"
# var block = do
# 	name = "Mobin"
# 	printf("Hello")
# 	printf(f"Hello {name}")
# 	printf("Bye")
# end
# var a = await 2 printf("Hello")
# var r = 0 through 10
# var ar = 'a' through 'e'
# var contains = [0, 1] has 2
# var contains2 = [0, 1] lacks 2
# var abs = |-5|
# var fact = 5!
# var conv = 5_f
# var conv2 = 1.5_i
# var conv3 = 0_b
# var conv4 = 7895_s
# var sh = "Moon & Python":split("&")
# var cond = if True:
#         Nil
#     else:
#         nil
#     end
# var area = (r = 2; __pi = 3.14; __pi * r * r)

# with [2, 6, 1, 2] as num:
#     printf(to_s(num))
# end

# with open("fmt.py", "r") as f:
#     printf("%s", f)
# end

# puts mystery

# var m = mystery
# puts m

# f := freezable("arg")
# f.arg := "Hello"
# printf(f.arg)!
# f.freeze()!
# f.arg := "Bye"

# printf("%s", Nil) also print(nil)

# printf("%s", Nil) after print(nil)

# printf("%s", Nil) before print(nil)

# puts perhaps

# d := {0, 1}
# mirror d to new_d
# puts new_d

# sleep 5
# wait 5

# num := 5
# inc num
# puts num
# decr num
# puts num

# io.warn("A Warning")!
# io.error(NameError, "An error")!

# puts append("Hello", ", World")

# puts leq(2.4, 2)
# puts leq(pi, 3)
# puts leq(pi, 3.14)

# puts seq(pi, 3.14)

# lable here:
# 	printf("Hello")
# end
# goto here

# puts bytecode("num = 0")

# lit 💀 = 5
# lit 🖤 = 0
# io.vprintln('💀')!
# io.vprintln('🖤')!

# var_dump(i + 1)!

# require("this")!

# from icecream import ic!
# ic("Hello")!

# puts __code__
# hello()!
# puts __code__
# puts ERR

# var divByZero = 1 / 0
# var ByZero = 1 div 0
# puts divByZero, ByZero

# puts INFO

# var V = {}
# var value = "Mobin"
# V[ptr(value)] = value!
# puts V

# &values = {
# 	0,
# 	1,
# 	2,
# } end
# puts values

# main := freezable("main")
# main.freeze()!
# main.value = Nil!

# &def person(
#         name: str,
#         age: int,
#         city: str,
# ) -> str:
#         return f"{name} is {age} years old that lives in {city}"
# end

# puts person("mobin", 17, "Urmia")

# class pub_and_priv:
# 	def pub(self):
# 		return "pub"

# 	@visibility.private
# 	def priv(self):
# 		return "priv"
# end
# $pp = pub_and_priv()
# puts pp.pub()
# # puts pp.priv()
# # error

# @deprecated("use new function")
# def old():
#     print("old")
# end
# def new():
#     print("new")
# end
# old()!

# 'printf "Hello"

# chan.send("Hello, World")!
# chan.send("Hello")!
# chan.send("Bye")!
# print(chan.is_empty())!
# print(chan.size())!
# print(chan.get())!
# print(chan.size())!
# print(chan.get())!
# print(chan.get())!
# print(chan.size())!
# print(chan.is_empty())!
# print(chan.is_full())!
# chan.close()!

# @name = "Mobin"
# puts __main__.name

# namespace block:
# 	def greet():
# 		print("Hello")
# end
# b = block!
# b.greet()!

# interface animal:
# 	sound: None
# end
# class cat(animal):
# 	def sound():
# 		return "meow"
# end
# my_pet = cat!
# puts my_pet.sound()

# si := short_int(32767)
# usi := ushort_int(65535)
# ui := unsigned_int(4294967295)
# li := long_int(2147483647)
# uli := ulong_int(4294967295)
# lli := long_long_int(2**63)
# ulli := ulong_long_int(18446744073709551615)

# state := undoable({"c": 0})
# state["c"] = 1!
# state["c"] = 2!
# print(state)!
# state.undo()!
# print(state)!
# state.undo()!
# print(state)!
# state.redo()!
# print(state)!

# var r = (lambda: Nil)()
# puts r

# proc hi(name) = f"Hi {name}"
# puts hi("mobin")

# puts "hi"
# again

# block b:
# 	printf("Hello")
# end
# does b

# puts hello
# if ERR is not None:
# 	printf(ERR)
# end
# if not ok:
# 	printf(ERR)
# end

# require t
# include t

# for elem in each([0, 1, 2], io.sprint):
#     print(elem)
# end

# call(print, "Hello", "World")!

# print(take([x for x in Range(0, 2).new()], len))!
# print(take([0, 1], 2))!
# print(take([0, 1], 5))!

# assert_equal(0, 1)!

# assert_type(4, 10.0)!

# retry(print, 0, count=3)!

# 2 awaitfor printf("Hello")

# ensure False

# unimplemented()!

# fixme as "This code needs your fix to be ran"

# IO >> (IO & Nil)

# STDOUT >> (STDIN << ">>> ")

# IO >> (IO > 0)

# puts hex(3735929054)
# 0xdeadc0de

# puts hex(12648430)
# 0xc0ffee

# puts hex(195936478)
# 0xbadc0de

# puts hex(2976579765)
# 0xb16b00b5

# puts hex(4276215469)
# 0xfee1dead

# puts hex(3131961357)
# 0xbaadf00d

# puts hex(2953575118)
# 0xb00bface

# puts hex(267262893)
# 0xfee1bad

# puts hex(49374)
# 0xc0de

# puts hex(53261)
# 0xd00d

# puts hex(57007)
# 0xdeaf

# puts hex(3221344269)
# 0xc001d00d

# puts hex(2645)
# 0xa55

# puts hex(3053)
# 0xbed

# puts chr(72) + chr(101) + chr(108) + chr(108) + chr(111) + chr(32) + chr(119) + chr(111) + chr(114) + chr(108) + chr(100)

# Stack.push("Hello, World")!
# Stack.putchar(72)!
# Stack.putchar(101)!
# Stack.putchar(108)!
# Stack.putchar(108)!
# Stack.putchar(111)!
# Stack.putchar(32)!
# Stack.putchar(119)!
# Stack.putchar(111)!
# Stack.putchar(114)!
# Stack.putchar(108)!
# Stack.putchar(100)!
# Stack.all()!
# Stack.print()!
# Stack.get()!

# var main = do
#     printf("Hello")
# end

# puts Number("Hello")

# native num = 2162
# io.lprint("num")!

# proc main() = printf("Hello, World")
# main()!

# puts PLATFORM

# puts append(list(), 0)

# puts io.putchar(72)

# puts io.putchars(72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100)

# puts INFO
# puts 0
# puts Hello
# # ERROR
# puts INFO

# printf("%s", io.countc("Hello", "l"))!

# io.assertEqual(5, 7)!
# io.assertTrue("")!
# io.assertFalse("H")!

# &Stack.push(5)
# Stack.push(5)
# Stack.add()
# printf("%d", Stack.top())
# end

# define_singleton_method("shit", 2162)!
# puts shit

# class __main__:
#     def __init__(self, value):
#         self.__value = value
#     @property
#     @visibility.private
#     def sth(self):
#         return self.__value
# end
# printf(__main__(5).sth)!

# let 🌑 = "Moon"
# io.echo("🌑")!

# fun hello():
#     print("Hello, World")
# end
# %hello(void)

# object person:
#     name, age
# end
# me = object of person {"Mobin", 16}
# puts me.name

# io.scanf ->

# name := "Moon & Python"
# name:split("&")

# {0, 1, 2}:pop()

# ☃ = 0!
# puts ☃

# puts _G["_G"] == _G

# l := _list([1, 2, 3])
# l << 4!
# puts l
# puts l.first
# puts l.last
# s := _str("Hell")
# printf(s << "o")!

# def main():
#     printf("Hello, World")
#     return 0
# end

# def download():
#     printf("%d", 1)
#     io.sleep(2)
#     printf("%d", 2)
# end
# co download()
# printf("here")!

# p := io.mem() &Nil
# printf("%s", io.mem() *p)!
# io.mem().imprint("User.name", "Mobin")!
# puts io.mem().recall("User.name")

# puts io.getenv("SHIT")

# shit := "Mobin"
# if let shit as name:
#     printf(name)
# end
# # if shit is not None:
# #     name = shit
# #     printf(name)

# use sys.getsizeof
# puts getsizeof("cls")
# use os.*
# puts cpu_count()

# print(make(int))!
# print(make(float))!
# print(make(complex))!
# print(make(str))!
# print(make(list))!
# print(make(tuple))!
# print(make(dict))!
# print(make(set))!
# print(make(frozenset))!
# print(make(range))!
# print(make(Range))!
# print(make(bool))!
# print(make(bytes))!
# print(make(bytearray))!
# print(make(memoryview))!
# print(make(None))!
# print(make(Nil))!

# idx := 0
# whilst idx < 5:
#     printf("%d", idx)
#     idx += 1
# end

# affirm False, ""

# printf("%s", Symbol(":MyMoon🌑"))!

# print(to_sym("🌑"))

# puts Symbol(":10").next()

# raise RuntimeError(void)

# puts False and "yes" or "no"

# load('print(0)')()!

# puts _V

# Kernel.printf(Kernel.io.mem() &None)!

# $a = () -> Nil
# $b = ?h
# $c = %s[Hello]
# $d = %(Hello)
# $e = (0..10)
# $f = !True

# c := channel(str)
# c >> "Hello, World"!
# c > "Bye, World"!
# print(c << void)!
# print(c < void)!

# num := natural("-10")
# print(num)!

# print("Hi") orelse printf("Damn")

# puts hash(pi)

# include std
# std.core.io.printf("Hello, World")!

# puts alloc(int, "2162")

# print(np.array([1, 2, 3]))!

# be over(a, b), [onlyif b != 0] => a / b
# be over2(a, b), [onlyif b != 0; ifnot: raise ZeroDivisionError("Nah")] => a / b
# puts over2(5, 0)

# nop <=

# &@timed
# def hi():
#     printf("Hello")
# end

# &@autorun
# def hi():
#     printf("Hello")
# end

# def sum(a, b):
#     return a + b
# end
# par sum10 = sum(10, ?)
# puts sum10(5)

# def some(a, b, c):
#     return a + b - c
# end
# par some2 = some(1, ?, ?)
# puts some2(2, 3)
