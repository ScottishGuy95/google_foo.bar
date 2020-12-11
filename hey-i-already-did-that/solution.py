# Google foo.bar 2020 Challenge
# Hey I Already Did That - Challenge 2, part 2
# When run in foo.bar, it handles testing the values

# We begin with a Random Minion ID (n).
# k = len(n)
# x = n in descending order
# y = n in ascending order
# z = x - y (plus leading 0s to make a 4-digit num)
# n = z
# repeat.

# 2 <= k <= 9                   2 <= k and k <= 9
# 2 <= b <= 10


def checkValid(n, b):
    k = len(str(n))
    if 2 <= k <= 9 and 2 <= b <= 10:
        return True
    else:
        return False


def toBase10(n, b):     # Should convert number n, to a base 10 number
    b = 10
    return 1


def toBaseN(n, b):      # Should convert number n into base b
    return 1



def solution(n, b):
    k = len(str(n))     # Used to ensure numbers are padded to the right length
    minions = []        # Stores the minions who have completed a task already
    cycle = 0           # Counts how many cycles until there was a repeated minion
    if checkValid(n, b) is False:
        return 'Invalid n or b given'
    while n not in minions:
        # Convert n into a String, then reverse the string for x, before converting back into an int
        # y is the same, but without reversing the string
        minions.append(n)
        x = int("".join(sorted(str(n), reverse=True)))
        y = int("".join(sorted(str(n))))
        if b == 10:
            # Does calculation, converts to str, adds leading zeros to match k (length of original n)
            z = str(x - y).zfill(k)
            n = z                    # Set the new value as the next minion ID to repeat the loop
        else:
            print()
            # Do base n stuff
        cycle += 1
        print(minions)
    return cycle

# Following 4 should fail
# print(solution(1211, 1))
# print(solution(1211, 11))
# print(solution(1234567890, 11))
# print(solution(0, 11))
print(solution(1211, 10))

