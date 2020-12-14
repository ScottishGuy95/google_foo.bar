# Google foo.bar 2020 Challenge
# Hey I Already Did That - Challenge 2, part 2
# When run in foo.bar, it handles testing the values


def checkValid(n, b):
    """
    Checks if the given minionID and given base value are within the expected range
    :param n: The minion ID length should be within 2 to 9
    :param b: Only allowed a base of 2 to 10
    :return: Boolean on whether the result is valid or not
    """
    k = len(str(n))
    if 2 <= k <= 9 and 2 <= b <= 10:
        return True
    else:
        return False


def baseN(n10, b):
    # Converts a number to given base
    x = int(n10)                        # Convert the string to a int
    values = []                         # Stores the number during conversion
    while x >= b:                       # Loop until the number is less than the base
        remainder = x % b               # Get the remainder
        values.append(str(remainder))   # Add the remainder to the list
        x = (x - remainder) // b        # Divide the number and the base, ignoring the remainder
    values.append(str(x))               # Add the final number to the list
    return ''.join(values[::-1])        # Return a String version of the list, in reverse


def base10(nb, b):
    # Converts a non-base 10 number, to base 10
    x = list(nb[::-1])                  # A reversed list version of the number to convert
    y = 0                               # Handles the final value
    for i, j in enumerate(x):           # Loops through the indexed list
        y += int(j) * (int(b) ** i)
    return str(y)                       # Converts the final value to a String


def solution(n, b):
    k = len(n)     # Used to ensure numbers are padded to the right length
    minions = []        # Stores the minions who have completed a task already
    if checkValid(n, b) is False:
        return 'Invalid n or b given'
    while n not in minions:
        minions.append(n)
        x = "".join(sorted(n, reverse=True))    # Sorts and reverses ID (descending)
        y = "".join(sorted(n))                  # Sorts ID (ascending)
        if b == 10:                             # Handles base 10
            z = int(x) - int(y)
            n = str(z)                   # Set the new value as the next minion ID to repeat the loop
        else:                                   # Handles all other bases
            # Converts x/y to base b
            z = int(base10(x, b)) - int(base10(y, b))
            z = baseN(str(z), b)
            n = z
        n = (k - len(n)) * '0' + n              # Adds the required zeros to the start of the ID
    return len(minions) - minions.index(n)      # Takes the length of all IDs, and the repeated ID position


# Don't submit this part inside of foo.bar
print('Part 1 - ', str(solution('1211', 10)))   # Should return 1
print('Part 2 - ', str(solution('210022', 3)))  # Should return 3


