import check

g_all_possible_char = "0123456789"

def generating_all_possible_pins(n_digit=4):
    for i in range(len(g_all_possible_char)**n_digit):
        guess = ""
        for j in range(n_digit):
            guess = g_all_possible_char[i % len(g_all_possible_char)] + guess
            i = i // len(g_all_possible_char)
        yield guess

def guessing(n_digit=4):
    for g in generating_all_possible_pins(4):
        print(".", end=" ")
        if check.check(g):
            return g
        