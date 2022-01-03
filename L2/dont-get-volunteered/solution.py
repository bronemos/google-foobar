moves = [2 + 1j, 2 - 1j, -2 + 1j, -2 - 1j, 1 + 2j, 1 - 2j, -1 + 2j, -1 - 2j]


def solution(src, dest):
    level = 0
    visited = set()
    src = src % 8 + src//8*1j
    dest = dest % 8 + dest//8*1j
    to_visit = [src, ]
    while dest not in to_visit:
        next_to_visit = []
        while to_visit:
            curr = to_visit.pop(0)
            visited.add(curr)
            for move in moves:
                position = curr + move
                if position in visited:
                    continue
                if position.real >= 0 and position.real < 8 and position.imag >= 0 and position.imag < 8:
                    next_to_visit.append(position)
        to_visit = next_to_visit
        level += 1
    return level
