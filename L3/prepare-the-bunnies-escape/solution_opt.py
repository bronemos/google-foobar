from collections import deque
import time

moves = (1, -1, 1j, -1j)


def solution(maze):
    moves = (1, -1, 1j, -1j)
    w, h = len(maze[0]) - 1, len(maze) - 1

    start = 0 + 0j
    goal = w + h*1j

    fwd_queue = deque([start, ])
    bwd_queue = deque([goal, ])

    fwd_dist = dict()
    fwd_dist[start] = 1
    bwd_dist = dict()
    bwd_dist[goal] = 1
    while fwd_queue or bwd_queue:
        if fwd_queue:
            curr_fwd = fwd_queue.popleft()

            for move in moves:
                pos_fwd = curr_fwd + move

                if pos_fwd in fwd_dist:
                    continue
                elif 0 <= pos_fwd.real <= w and 0 <= pos_fwd.imag <= h:
                    fwd_dist[pos_fwd] = fwd_dist[curr_fwd] + 1
                    if pos_fwd in bwd_dist:
                        return fwd_dist[pos_fwd] + bwd_dist[pos_fwd] - 1
                    if maze[int(pos_fwd.imag)][int(pos_fwd.real)] == 0:
                        fwd_queue.append(pos_fwd)

        if bwd_queue:
            curr_bwd = bwd_queue.popleft()

            for move in moves:
                pos_bwd = curr_bwd + move

                if pos_bwd in bwd_dist:
                    continue
                elif 0 <= pos_bwd.real <= w and 0 <= pos_bwd.imag <= h:
                    bwd_dist[pos_bwd] = bwd_dist[curr_bwd] + 1
                    if pos_bwd in fwd_dist:
                        return fwd_dist[pos_bwd] + bwd_dist[pos_bwd] - 1
                    if maze[int(pos_bwd.imag)][int(pos_bwd.real)] == 0:
                        bwd_queue.append(pos_bwd)


start_time = time.time()
assert solution([[0, 0, 0],
                 [1, 1, 0],
                 [1, 1, 1]]) == 5
assert solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7
assert solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
                0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11
assert solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 39
assert solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [
                0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 21
print(time.time() - start_time)
