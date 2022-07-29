from ctypes import sizeof
from unittest import result

# g(i, S) = min_k_in_S(C_ik + g(k, S - k))
def dynamic_method(start, S, cost_map):
    if len(S) == 0:
        print(cost_map[start][1])
        return cost_map[start][1]

    res = []
    for _ in range(len(S)):
        k = S.pop()
        res.append(cost_map[start][k] + dynamic_method(k, S, cost_map))
        S.insert(0, k)
        

    print("-----------------------------")
    if len(res) == 0:
        return 0

    return min(res)

def min_path(n, roads):
    cost_map = [[0 for x in range(n+1)] for x in range(n+1)]

    for road in roads:
        print(road)
        cost_map[road[0]][road[1]]  = road[2]
        cost_map[road[1]][road[0]]  = road[2]

    res = 0
    S = [x for x in range(2, n+1)]

    return dynamic_method(1, S, cost_map)


if __name__ == '__main__':
    # n = 3
    # tuple = [[1,2,1],[2,3,2],[1,3,3]]
    # result = min_path(n, tuple)
    # print(result)

    n = 4
    tuple = [ [0,0,0,0,0],
              [0,0,10,15,20], 
              [0,5,0,9,10], 
              [0,6,13,0,12], 
              [0,8,8,9,0] 
              ]
    S = [2,3,4]
    print(dynamic_method(1, S, tuple))

    # x = [1,2,3]
    # y = x.pop()
    # x.insert(0, y)
    # print(x)
    # x.append(1)
    # x.pop()
    # if len(x) == 0:
    #     print("Kha")