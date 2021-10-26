def input_exaption(y=int, x=int):
    while True:
        try:
            x = int(input("please enter FIRST number "))
            y = int(input("please enter Second number "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            print('Math is great! :-)')
            print(x, "+", y, "=", int(x) + int(y))
            print(x, "-", y, "=", int(x) - int(y))
            print(x, "*", y, "=", int(x) * int(y))
            print(x, "/", y, "=", int(x) / int(y))
            print(x, "**", y, "=", int(x) ** int(y))
            print(x, "//", y, "=", int(x) // int(y))
            break
