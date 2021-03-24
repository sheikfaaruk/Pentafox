from collections import deque


def find_target(values, target):

    dq = deque(sorted([(val, idx) for idx, val in enumerate(values)]))

    while True:
        if len(dq) < 2:
            print('No match found')

        s =  dq[0][0] + dq[-1][0]

        if s > target:
            dq.pop()
        elif s < target:
            dq.popleft()  
        else:
            break
    return dq[0], dq[-1]



values = [1, 2, 3, 4, 9]
target = 8

sol = find_target(values, target)

print(sol[0][0],sol[1][0])