# Welcome Message
print("*" * 30)
print("   TERMINAL TIC TAC TOE")
print("*" * 30)

player = 1
symbol = "X"
a, b, c, d, e, f, g, h, i = ".", ".", ".", ".", ".", ".", ".", ".", "."

def set_var_from_choice(choice):
    choice = choice.upper()
    if (choice == "1A" or choice == "A1"):
        global a 
        a = symbol
    elif (choice == "1B" or choice == "B1"):
        global b
        b = symbol
    elif (choice == "1C" or choice == "C1"):
        global c 
        c = symbol
    elif (choice == "2A" or choice == "A2"):
        global d 
        d = symbol
    elif (choice == "2B" or choice == "B2"):
        global e 
        e = symbol
    elif (choice == "2C" or choice == "C2"):
        global f 
        f = symbol
    elif (choice == "3A" or choice == "A3"):
        global g 
        g = symbol
    elif (choice == "3B" or choice == "B3"):
        global h 
        h = symbol
    elif (choice == "3C" or choice == "C3"):
        global i 
        i = symbol
    else:
        pass
    
def get_var_from_choice(choice):
    choice = choice.upper()
    if (choice == "1A" or choice == "A1"):
        return a
    elif (choice == "1B" or choice == "B1"):
        return b
    elif (choice == "1C" or choice == "C1"):
        return c
    elif (choice == "2A" or choice == "A2"):
        return d
    elif (choice == "2B" or choice == "B2"):
        return e
    elif (choice == "2C" or choice == "C2"):
        return f
    elif (choice == "3A" or choice == "A3"):
        return g
    elif (choice == "3B" or choice == "B3"):
        return h
    elif (choice == "3C" or choice == "C3"):
        return i
    else:
        return "invalid"

def taken(choice):
    var = get_var_from_choice(choice)
    if var != ".":
        return True
    else:
        return False
    
def winner():
    if a == b and b == c and c != ".":
        return True
    elif a == d and d == g and g != ".":
        return True
    elif a == e and e == i and i != ".":
        return True
    elif d == e and e == f and f != ".":
        return True
    elif g == h and h == i and i != ".":
        return True
    elif b == e and e == h and h != ".":
        return True
    elif c == f and f == i and i != ".":
        return True
    elif c == e and e == g and g != ".":
        return True
    else:
        return False
    
def reset():
    global a, b, c, d, e, f, g, h, i, player, symbol
    a, b, c, d, e, f, g, h, i = ".", ".", ".", ".", ".", ".", ".", ".", "."
    player = 1
    symbol = "X"

    
def update(choice):
    global player,symbol
    set_var_from_choice(choice)
    if winner():
        print_board()
        print(f"\nPlayer {player} wins!")
        again = input(f"\nWould you like to play again? (y/n) Default n: ")
        if again == "y" or again == "Y":
            reset()
            return False
        elif again == "n" or again == "N":
            print("\nBye! Come again!")
            return True
        else:
            print("\nBye! Come again!")
            return True
    temp = symbol
    if temp == "X":
        symbol = "O"
        player = 2
    if temp == "O":
        symbol = "X"
        player = 1
    return False

def print_board():
    print(f"""
             A      B      C
          _____________________
          |      |      |      |
       1      {a}      {b}      {c} 
          |______|______|______|
          |      |      |      |
       2      {d}      {e}      {f} 
          |______|______|______|
          |      |      |      |
       3      {g}      {h}      {i}    
          |______|______|______|

          """)

while True:
    print_board()
    
    choice = input(f"\nPayer {player}'s turn: ")

    while get_var_from_choice(choice) == "invalid":
        print(f"\nInvalid choice: {choice}")
        choice = input(f"\nPayer {player}'s turn: ")

    if taken(choice):
        while taken(choice):
            print(f"\nAlready taken. Pick another.")
            choice = input(f"\nPayer {player}'s turn: ")
        if update(choice):
            break
    else:
        if update(choice):
            break


        
