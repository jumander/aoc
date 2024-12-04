from collections import defaultdict

def part1(lines):

    safeCount = 0

    for line in lines:
        levels = line.split()
        levels = [int(level) for level in levels]

        prevDiff = 0

        safe = True
        for a, b in zip(levels, levels[1:]):
            diff = b - a
            if diff == 0 or abs(diff) > 3 or (prevDiff * diff) < 0:
                safe = False
                break
            prevDiff = diff
        if safe:
            safeCount += 1

    return safeCount



def part2(lines):
    return 0


if __name__ == "__main__":

    x = open("input/2")
    lines = x.readlines()
#    lines = [
#      "7 6 4 2 1",
#      "1 2 7 8 9",
#      "9 7 6 2 1",
#      "1 3 2 4 5",
#      "8 6 4 4 1",
#      "1 3 6 7 9",
#    ]
    print(len(lines))
    print("part1", part1(lines))
    print("part2", part2(lines))


