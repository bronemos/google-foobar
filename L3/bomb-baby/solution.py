def solution(x, y):
    x = int(x)
    y = int(y)
    count = 0
    while x != 1 and y != 1:
        if x <= 0 or y <= 0:
            return "impossible"
        elif y > x:
            count += y // x
            y = y - x * (y // x)
        elif x > y:
            count += x // y
            x = x - y * (x // y)
    if x == 1:
        count += y
    elif y == 1:
        count += x
    return str(count - 1)


assert solution("4", "7") == "4"
assert solution("2", "1") == "1"
