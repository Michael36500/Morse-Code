# gets input
input = input()

# here you can set different characters for dot, line, etc...
c_dot = "."
c_line = "-"
c_let = "/"
c_word = "//"

# main loop, takes letter from input, and find equvivalent in morse code
for a in input:
    # if a = a, then it print desired characters
    if a == "a":
        print(c_dot, c_line, end = "")
    if a == "b":
        print(c_line, c_dot, c_dot, c_dot, end = "")
    if a == "c":
        print(c_line, c_dot, c_line, c_dot, end = "")
    if a == "d":
        print(c_line, c_dot, c_dot, end = "")
    if a == "e":
        print(c_dot, end = "")
    if a == "f":
        print(c_dot, c_dot, c_line, c_dot, end = "")
    if a == "g":
        print(c_line, c_line, c_dot, end = "")
    if a == "h":
        print(c_dot, c_dot, c_dot, c_dot, end = "")
    if a == "i":
        print(c_dot, c_dot, end = "")
    if a == "j":
        print(c_dot, c_line, c_line, c_line, end = "")
    if a == "k":
        print(c_line, c_dot, c_line, end = "")
    if a == "l":
        print(c_dot, c_line, c_dot, c_dot, end = "")
    if a == "m":
        print(c_line, c_line, end = "")
    if a == "n":
        print(c_line, c_dot, end = "")
    if a == "o":
        print(c_line, c_line, c_line, end = "")
    if a == "p":
        print(c_dot, c_line, c_line, c_dot, end = "")
    if a == "q":
        print(c_line, c_line, c_dot, c_line, end = "")
    if a == "r":
        print(c_dot, c_line, c_dot, end = "")
    if a == "s":
        print(c_dot, c_dot, c_dot, end = "")
    if a == "t":
        print(c_line, end = "")
    if a == "u":
        print(c_dot, c_dot, c_line, end = "")
    if a == "v":
        print(c_dot, c_dot, c_dot, c_line, end = "")
    if a == "w":
        print(c_dot, c_line, c_line, end = "")
    if a == "x":
        print(c_line, c_dot, c_dot, c_line, end = "")
    if a == "y":
        print(c_line, c_dot, c_line, c_line, end = "")
    if a == "z":
        print(c_line, c_line, c_dot, c_dot, end = "")
    if a == " ":
        print(c_word, end = "")
    else:
        print(c_let, end = "")
