import sys
from sympy import isprime
sys.setrecursionlimit(10000000)

# ericdrome - a palindrome possibly one more than a prime
# ericprime - a prime one less than a palindrome

# returns lowest possible "ericdrome" starting with a particular digit 2, 4, or 8
def to_ericdrome(split, digit, lengthen):
    split_length = len(split) - 2 + (1 * lengthen)
    split = [digit]

    for _ in range(split_length):
        split.append(0)

    if split_length >= 0:
        split.append(digit)

    return split

# a regular array to a palindromic array - returns itself if palindromic
def to_palindrome(split):
    if len(split) == 1:
        return [split[0] + 1]

    focusindex1 = len(split) // 2 - (1 * len(split) % 2 == 0)
    focusindex2 = len(split) // 2
    new_split = split[:len(split) // 2]

    if len(split) % 2 == 0:
        new_split = new_split + new_split[::-1]
    else:
        new_split = new_split + [split[len(split) // 2]] + new_split[::-1]

    if combine(new_split) > combine(split):
        return new_split
    else:
        for i in range(len(split) // 2 + (1 * len(split) % 2 == 1)):
            if new_split[focusindex1] < 9:
                new_split[focusindex1] = new_split[focusindex1] + 1
                new_split[focusindex2] = new_split[focusindex1]
                return new_split
            else:
                if focusindex1 == 0:
                    to_next_digit(new_split)
                new_split[focusindex1] = 0
                focusindex1 = focusindex1 - 1


def to_next_digit(split):
    if (split[0] == 8) or (split[0] == 9):
        return to_ericdrome(split, 2, True)
    else:
        return to_ericdrome(split, 1 << ((split[0]).bit_length()), False)


def find_next_palindrome(split):
    if split != split[::-1]:
        raise ValueError("Not a palindrome")

    if len(split) == 1:
        return to_next_digit(split)

    focusindex1 = len(split) // 2 - (1 * len(split) % 2 == 0)
    focusindex2 = len(split) // 2

    for i in range(len(split) // 2 + (1 * len(split) % 2 == 1)):
        if focusindex1 == 0:
            return to_next_digit(split)
        elif split[focusindex1] < 9:
            split[focusindex1] = split[focusindex1] + 1
            split[focusindex2] = split[focusindex1]
            return split
        else:
            focusindex1 = focusindex1 - 1
            focusindex2 = focusindex2 + 1


def combine(split):
    return int(''.join(map(str, split)))


# calculates the age of Eric presuming he is a minimum n years old and a maximum k years old
def how_old_is_eric(n, k):
    split = [int(x) for x in str(n)] # the integer parsed into an array

    if (n >= k) & (k != -1): # if at iteration limit
        print("Done!")
    elif split != split[::-1]: # if not a palindrome
        how_old_is_eric(combine(to_palindrome(split)), k)
    elif isprime(n - 1): # if a palindrome and one more than a prime
        print("Eric could be", n, "years old!")
        how_old_is_eric(n + 2, k)
    else: # if a palindrome but not one more than a prime
        how_old_is_eric(combine(find_next_palindrome(split)), k)

how_old_is_eric(0, 10e6) # minimum age, maximum age (-1 if unlimited)