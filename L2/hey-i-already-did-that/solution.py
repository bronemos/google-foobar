def subtract(x, y, b):
    difference = []
    carry = 0

    for minuend, subtrahend in zip(x, y):
        result = minuend - subtrahend + carry
        if result < 0:
            carry = -1
            result = b + result
        else:
            carry = 0
        difference.append(result)
    difference.reverse()
    return "".join(map(str, difference))


def solution(n, b):
    index = 0
    visited = dict()

    while n not in visited.keys():
        visited[n] = index
        index += 1
        x = [int(char) for char in n]
        x.sort()
        y = [int(char) for char in reversed(x)]
        print(n)
        n = subtract(x, y, b)

    return index - visited[n]
