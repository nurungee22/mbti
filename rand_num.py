import itertools
from random import randint as rand

#0~(n-1) 중 m개의 숫자를 랜덤으로 뽑아서 정렬된 리스트를 반환
def rand_num_list(n, m):
    arr = [i for i in range(0, n)]
    arr_list = list(itertools.permutations(arr, m))
    index = rand(0, len(arr_list) - 1)
    return sorted(list(arr_list[index]))
