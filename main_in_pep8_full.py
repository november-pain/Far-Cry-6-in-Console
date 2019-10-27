#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math
import os
print(os.name)

if os.name == 'nt':
    systema = 'cls'
elif os.name == 'posix':
    systema = 'clear'
else:
    systema = 'clear'


def downloading(systema):
    '''
    fun function to make short animation 
    '''
    os.system(systema)
    print('Initialization   \\')
    os.system(systema)
    print('Initialization   \\')
    os.system(systema)
    print('Initialization   |')
    os.system(systema)
    print('Initialization   |')
    os.system(systema)
    print('Initialization   /')
    os.system(systema)
    print('Initialization   /')
    os.system(systema)
    print('Initialization   â')
    os.system(systema)
    print('Initialization   â')
   

def possible_numbers(U, P, H):
    '''
    
    '''
    set_of_alltypes = set(U + H + P)
    set_of_alltypes = list(set_of_alltypes)
    set_of_alltypes.sort()
    print('All numbers that is Ulama or Prime or Happy: \n')
    x = 0
    while x + 20 < len(set_of_alltypes):
        print(set_of_alltypes[x:x + 15])
        x += 15


def type_of_number(number):
    """
    this function returns list of number`s type
    """

    type_of_number = []
    if number in Happy:
        type_of_number.append('H')
    if number in Prime:
        type_of_number.append('P')
    if number in Ulama:
        type_of_number.append('U')

    return type_of_number


def def_to_check(a, b):
    """
    this function checks if two numbers have any types in common
    """

    type_of_a = type_of_number(a)
    type_of_b = type_of_number(b)
    common_types = list(set(type_of_a).intersection(type_of_b))
    if len(common_types) > 0:
        return True
    elif a == 0 or b == 0:
        return True
    elif len(type_of_a) == 0 and len(type_of_b) == 0:
        return True
    else:
        return False


def list_digits_of_num(num):
    """
    this function makes a list of digits of given number
    this function is neccesary for generating happy numbers
    """

    if num == 0:
        return [1]
    else:
        num_lenght = int(math.log10(num)) + 1
        digits_of_num = []
        m = 0
        while m < num_lenght:
            m += 1
            digits_of_num.append(0)

        for k in range(num_lenght):
            digit = num // 10 ** k % 10
            digits_of_num[num_lenght - (k + 1)] = digit
        return digits_of_num


def generate_happy(max):
    """
    this function generates list of happy numbers
    """

    happy = []
    for i in range(1, max):
        checker = 0
        a = len(list_digits_of_num(i))
        lap = 0
        m = i
        while lap < 100:
            lap += 1

            for k in range(a):
                checker += list_digits_of_num(m)[k] ** 2

            m = checker
            a = len(list_digits_of_num(m))

            if checker == 1:
                happy.append(i)
                break
            else:
                checker = 0
    return happy


def ulan_generator(max):
    """
    this function generates list of Ulam numbers
    """

    arr = [1, 2, 3]
    for i in range(4, max):
        sum_counter = 0
        for k in range(0, len(arr)):
            if i - arr[k] in arr and arr[k] * 2 != i:
                sum_counter += 1
            if sum_counter > 2:
                break
        if sum_counter == 2:
            arr.append(i)
    return arr


def generate_prime(max):
    """
    this function generates list of prime numbers
    """

    prime_list = [2]
    for i in range(3, max):
        div_count = 0
        for k in range(2, i + 1):
            if i % k == 0:
                div_count += 1
            if div_count >= 2:
                break
        if div_count == 1:
            prime_list.append(i)
    return prime_list


def shift_num_right(lst):
    """
    this function shifts number right if the folowing number is 0
    >>> [0, 0, 1, 0]
    [0, 0, 0, 1]
    """

    for i in range(len(lst)):
        for k in range(3):
            if lst[i][k] != 0:
                while lst[i][k + 1] == 0:
                    lst[i][k + 1] = lst[i][k]
                    lst[i][k] = 0
    return lst


def add_right(lst):
    """
    this function add neighbour numbers that have at least one type in common
    and shift the result to the right
    >>> [[1, 0, 1, 0], [7, 1, 1, 0], [7, 0, 1, 0], [0, 7, 1, 0]]
    [[0, 0, 0, 2], [0, 0, 7, 2], [0, 0, 0, 8], [0, 0, 0, 8]]
    """

    # shifts to right sde

    for i in range(4):
        lst = shift_num_right(lst)

    for i in range(4):
        for j in range(3):
            if def_to_check(lst[i][2 - j], lst[i][3 - j]):
                lst[i][3 - j] = lst[i][2 - j] + lst[i][3 - j]
                global score
                if lst[i][3 - j] in Happy and lst[i][3 - j] \
                    not in opened_happy:
                    opened_happy.append(lst[i][3 - j])
                    score = score + lst[i][3 - j]
                if lst[i][3 - j] in Prime and lst[i][3 - j] \
                    not in opened_prime:
                    opened_prime.append(lst[i][3 - j])
                    score = score + lst[i][3 - j]
                if lst[i][3 - j] in Ulama and lst[i][3 - j] \
                    not in opened_ulam:
                    opened_ulam.append(lst[i][3 - j])
                    score = score + lst[i][3 - j]
                lst[i][2 - j] = 0
                for k in range(2):
                    lst = shift_num_right(lst)
    return lst


def add_left(lst):
    """
    this function add neighbour numbers that have at least one type in common
    and shift the result to the left
    >>> [[1, 0, 1, 0], [7, 1, 1, 0], [7, 0, 1, 0], [0, 7, 1, 0]]
    [[2, 0, 0, 0], [8, 1, 0, 0], [8, 0, 0, 0], [8, 0, 0, 0]]
    """

    lst_reversed = []
    for i in range(len(lst)):
        lst_reversed.append(list(reversed(lst[i])))

    add_right(lst_reversed)

    lst_reversed_back = []
    for i in range(len(lst)):
        lst_reversed_back.append(list(reversed(lst_reversed[i])))

    return lst_reversed_back


def rotate_table(lst):
    """
    this function rotates table in order to make possible adding up or down
    """

    lst = lst[::-1]
    rotated_lst = []
    for k in range(len(lst)):
        column = []
        for i in range(len(lst)):
            column.append(lst[i][k])
        rotated_lst.append(column)

    return rotated_lst


def add_up(lst):
    """
    this function adds all possible numbers up
    """

    lst = add_right(rotate_table(lst))
    for i in range(3):
        lst = rotate_table(lst)
    return lst


def add_down(lst):
    """
    this function adds all possible numbers down
    """

    lst = add_left(rotate_table(lst))
    for i in range(3):
        lst = rotate_table(lst)
    return lst


def choose_number(U, P, H):
    """
    lst, lst, lst -> int

    chooses random number from Ulama orr Prime or Happy
    """

    gen_U = U[0:4]
    gen_P = P[0:4]
    gen_H = H[0:4]

    gn = random.randint(1, 3)
    if gn == 1:
        return random.choice(gen_U)
    elif gn == 2:
        return random.choice(gen_P)
    else:
        return random.choice(gen_H)

def check_for_zeros(lst):
    zeros_in_lines = []
    for i in range(len(lst)):
        count = 0
        for k in range(len(lst[i])):
            if lst[i][k] == 0:
                count += 1
        zeros_in_lines.append(count)
    return zeros_in_lines


def spawn_number(array, max_pos):
    """
    checks if can spawn in loop and adds 1 number to array
    index
    """
    spawner = True
    while spawner:
        a = random.randint(0, max_pos)
        b = random.randint(0, max_pos)

        if array[a][b] != 0:
            a = random.randint(0, max_pos)
            b = random.randint(0, max_pos)

        if array[a][b] == 0:
            array[a][b] = choose_number(Ulama, Prime, Happy)
            if array[a][b] in Happy and array[a][b] not in opened_happy:
                opened_happy.append(array[a][b])
            if array[a][b] in Prime and array[a][b] not in opened_prime:
                opened_prime.append(array[a][b])
            if array[a][b] in Ulama and array[a][b] not in opened_ulam:
                opened_ulam.append(array[a][b])
            return array
        if sum(check_for_zeros(array)) == 0:
            spawner = False

def key_get():
    """
    gets key to make a move soon
    """

    k = input('\33[35m' + 'make your turn: ' + '\033[0m')
    k = k.lower()
    sett = ['w', 's', 'a', 'd']
    for i in sett:
        if k == i:
            global key_pressed
            key_pressed = k
            return True

    print("wrong key pressed. Click 'w', 's', 'a', 'd'")
    return False


# our table

def size_of_table(height, width):
    '''
    this fuction creates table with given height and width
    '''

    num_list = []
    for i in range(height):
        line = []
        for k in range(width):
            line.append(0)
        num_list.append(line)
    return num_list


def int_to_str(
    lst,
    U,
    P,
    H,
    ):
    '''
    complition for table function
    '''

    str_list = []

    for k in range(len(lst)):
        list_of_line = []
        for i in range(4):
            color = '\033[0m'
            rm_space = len(list_digits_of_num(lst[k][i])) - 1

            # gets the color of number. If no such color
            # than this number has none of these three types

            if lst[k][i] in U and lst[k][i] in P:
                color = '\33[1;33m'  # YELLOW = RED + GREEN
            elif lst[k][i] in U and lst[k][i] in H:

                color = '\33[1;35m'  # Magenta = RED + BLUE
            elif lst[k][i] in H and lst[k][i] in P:

                color = '\33[1;36m'  # CYAN = GREEN + BLUE
            elif lst[k][i] in U:

                color = '\33[31m'  # RED
            elif lst[k][i] in P:

                color = '\33[32m'  # GREEN
            elif lst[k][i] in H:

                color = '\33[34m'  # BLUE

            if lst[k][i] in U and lst[k][i] in P and lst[k][i] in H:
                color = '\33[0;30;46m'  # CYAN BACKGROUND AND BLACK FORE

            list_of_line.append(color + str(lst[k][i]) + '\033[0m' + ' '
                                 * (8 - rm_space))

        str_list.append(list_of_line)

    return str_list


def show_score(score):
    score_to_print = str(score)
    score_to_print = score_to_print.upper()
    print('\nSCORE: ')
    print(score_to_print)


def output(grid):
    '''
    outputs table 4x4 into screen
    '''

    grid = int_to_str(grid, Ulama, Prime, Happy)
    print('\n')

    for i in range(len(grid)):
        res = '\t\t'

        # for j in 4

        for j in range(len(grid[i])):
            for x in range(17 - len(grid[i][j])):
                res += ' '
            res += grid[i][j] + ' '

        print(res)
        print('\n')
    return 0


def colour_description():
    print('Number types:\33[31m RED\33[0m - Ulam,\33[32m GREEN\33[0m - Prime,\33[34m BLUE\33[0m - Happy')
    print('Combinations of types:\33[1;33m YELLOW\33[0m - U and P,\33[1;35m MAGENTA\33[0m - U and H,\33[1;36m CYAN\33[0m -H and P,\33[0;30;46mCYANbg\33[0m - U, P and H')

def check_for_lose(lst):
    if sum(check_for_zeros(lst)) == 0:
        return True

# launch program

if __name__ == '__main__':
    x = 0
    while x < 20:
        x += 1
        #print('Initialization... ')
        downloading(systema)


    # DATA

    limit_for_num = 999

    Ulama = ulan_generator(limit_for_num)
    Prime = generate_prime(limit_for_num)
    Happy = generate_happy(limit_for_num)

    # -----------------------------------------------------------------|

    # Settings
    # global variables:

    global opened_ulam
    opened_ulam = []
    global opened_happy
    opened_happy = []
    global opened_prime
    opened_prime = []
    global score
    score = 0

    # --------------------

    # one of possible moves

    key_pressed = ''

    # initialization of game

    game_is_playing = True
    all_numbers = size_of_table(4, 4)
    a = len(all_numbers[0]) - 1
    spawn_number(all_numbers, a)
    spawn_number(all_numbers, a)

    # initialization finished
    os.system(systema)
    print('Initialization finished')
    input('Press any key to cintinue... ')
    print('Now you are ready to start')
    input()
    os.system(systema)
    print()
    print("in old days... ")
    input()
    os.system(systema)
    print('\n\t\t\n')
    print("old \33[30mblack mage\33[0m cursed the world")
    input()
    print('And \33[31mNOW\33[0m')
    print('\n\t\33[34mYOU\33[0m must save the world')
    input()
    os.system(systema)
    print('''
    Game rule is very simple if you know what is 
    Ulama, Prime or Happy numbers.

    Don't you?

    Then try and learn, save \33[34mWORLD\33[37m from dAngEr!!!




    *** The world is corrupted if all fields of numbers are filled =( ***
    ''')
    input("  Yes, I'm in (press 'yes' \n  No, I'm in (press any key) ")

    # main loop of the program

    while game_is_playing:


        # show table of numbers
        output(all_numbers)
        
        if check_for_lose(all_numbers):
            print('Evil wins, you are loser')
            break

        # show colour description
        colour_description()

        # show list of opened numbers

        print('\33[31mList of  Ulam numbers, you have opened:' \
            + str(sorted(opened_ulam)))
        print('\33[32mList of Prime numbers, you have opened:' \
            + str(sorted(opened_prime)))
        print('\33[34mList of Happy numbers, you have opened:' \
            + str(sorted(opened_happy)))

        # show score

        show_score(score)

        # gets move from player

        x = 0
        while not key_get():
            x += 1
            key_get()

            # if cant make a move: break

            if x > 10:
                print('You lost, try again :(')
                break

        print('game is going ... ')

        # making game physics - add to side

        if key_pressed == 'w':
            all_numbers = add_up(all_numbers)
        elif key_pressed == 's':
            all_numbers = add_down(all_numbers)
        elif key_pressed == 'a':
            all_numbers = add_left(all_numbers)
        elif key_pressed == 'd':
            all_numbers = add_right(all_numbers)

        # generate new numbers

        spawn_number(all_numbers, a)
        spawn_number(all_numbers, a)
        os.system(systema)
