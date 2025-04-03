while 1:

    io.print("moon> ")
    __input = input()

    if __input == "cls":
        system("cls")

    elif __input == "exit":
        break

    elif __input == "clear":
        __clear_exec__()

    else:
        mexec(__input)

end