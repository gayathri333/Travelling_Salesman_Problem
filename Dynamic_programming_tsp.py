import sys
import copy
import time

start_time = time.process_time()

matrix = [
[0,383,886,777,915,793,335,386,492,649],
[421,0,362,27,690,59,763,926,540,426],
[172,736,0,211,368,567,429,782,530,862],
[123,67,135,0,929,802,22,58,69,167],
[393,456,11,42,0,229,373,421,919,784],
[537,198,324,315,370,0,413,526,91,980],
[956,873,862,170,996,281,0,305,925,84],
[327,336,505,846,729,313,857,0,124,895],
[582,545,814,367,434,364,43,750,0,87],
[808,276,178,788,584,403,651,754,399,0]]

points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(points)
all_sets = []
g = {}
p = []

def main():
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]

    print("Distance : ",+get_minimum(1, (2,3,4,5,6,7,8,9,10)))

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('1}')
    return


def get_minimum(k, a):
    if (k, a) in g:
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()
 
end_time = time.process_time()
print("Time : ",+end_time-start_time)
