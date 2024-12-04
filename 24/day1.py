from collections import defaultdict

def day1(lines):
    left = []
    right = []

    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    diffSum = 0
    for l, r in zip(left, right):
        diffSum += abs(l - r)

    return diffSum



def day2(lines):
    left = defaultdict(int)
    right = defaultdict(int)


    for line in lines:
        l, r = line.split()
        left[int(l)] += 1
        right[int(r)] += 1


    similarity = 0
    for l, count in left.items():
        similarity += count * l * right[l]

    return similarity


if __name__ == "__main__":
    x = open("input/1")
    lines = x.readlines()
    print("day1", day1(lines))
    print("day2", day2(lines))


