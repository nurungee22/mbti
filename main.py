from MBTI_list import *
from rand_num import *
from hello import say_hello

score=dict()

say_hello()
#적으면 0, 
#for g in arr_list['I']:
#    print(mbti['I'][rand_nums['0']])
#    user_input = input("숫자를 입력하세요: ")
#    score_i += user_input
#    print(mbti['I'][rand_nums['1']])
#    user_input_2 = input('숫자를 입력하세요: ')
#    score_i 


for a in MBTI:
    score[a]=0
    for n in rand_num_list(4,2):
        print(MBTI[a][n])
        user_input = int(input("0~5점 사이의 값을 입력하세요: "))
        if user_input <0:
            user_input =0
        elif user_input > 5:
            user_input = 5
        score[a] += user_input

if score['I'] > score['E']:
    print('I', end='')
else:
    print('E', end='')

if score['S'] > score['N']:
    print('S', end='')
else:
    print('N', end='')

if score['F'] > score['T']:
    print('F', end='')
else:
    print('T', end='')

if score['P'] > score['J']:
    print('P', end='')
else:
    print('J', end='')
