# Google foo.bar 2020 Challenge
# En Route Salute - Challenge 2, part 1
# When run in foo.bar, it handles testing the values


def solution(hallway):
    salutes = 0
    hall = list(hallway)                        # Store hall as list
    for spot in range(len(hall)):               # Loop the entire hall
        if hall[spot] == ">":                   # If the current spot has employee going right,
            for x in range(spot, len(hall)):    # Loop from here to the end of the hall
                if hall[x] == "<":              # Check if the employee meets another going left
                    salutes += 2                # If they do, add 2 for them both saluting
    return salutes


# Don't include these when submitting in foo.bar
print(solution(">----<"))
print(solution("<<>><"))

