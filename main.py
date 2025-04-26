"""
One day, a middle-school mathematics teacher named Eric posted a question on social media,
professing a mathematical riddle. His age was a palindrome one more than a prime. My first
thought was 8, though I figured he could not have aged *that* badly. Eric had turned 44 that
day if I recall correctly.

At this point, I thought that either this question had more solutions, or I was about to make
an interesting discovery concerning some bizarre relation between primes and palindromes. To
no surprise it was the former. By manually looking at a list of prime numbers, I replied:

"i’m not sure! presuming that you’re a youthful sub-6000 years old, you could be any of the
following ages: 3, 4, 6, 8, 44, 212, 242, 272, 434, 444, 464, 828, 858, 878, 888, 2112, 2222,
2442, 2552, 4004, 4664, and 4994."

With a cheshire grin, I went to bed, and woke up pleasantly to some media traction on my reply.
I knew, however, that I could do better, and that I had the programming knowledge to fulfil this
curiousity.

In the undertaking that proceeded, I not only aimed to fulfil an infinite
generation of solutions to Eric's problem, but to optimise the task as best I could.
I will avoid tedious detail, but I had noticed that all multi-digit solutions began with a
2, 4, or 8, and deduced that it would be far quicker to generate palindromes and check for
primes than to generate primes and check for palindromes. The resulting solution is primarily
a unique palindrome fetcher with an isprime() called somewhere.

Though it was my first completely novel coding experience, I hope you can appreciate the effort
more-so than its flaws. The following code, though short and simple, will forever exist as a fixed
point of my mind, as it beholds all rationality behind my passion for computer programming.
Eric Numbers is a program of algorithmic creativity and mathematical leveraging ultimately designed
for fun and laughs as the reader wonders just how much I must have had to go and make this.

I wrote this code in the earliest four hours of September 26, 2024.
Eric's original post appears to be deleted, but my original two replies are still online.

- Zachary Brownjohn"""

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