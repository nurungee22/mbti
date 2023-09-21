from MBTI_list import *
from rand_num import *
from hello import say_hello

score_i = 0
score_e = 0
score_n = 0
score_s = 0
score_f = 0
score_t = 0
score_p = 0
score_j = 0

say_hello()
#적으면 0, 
#for g in arr_list['I']:
#    print(mbti['I'][rand_nums['0']])
#    user_input = input("숫자를 입력하세요: ")
#    score_i += user_input
#    print(mbti['I'][rand_nums['1']])
#    user_input_2 = input('숫자를 입력하세요: ')
#    score_i 




for n in rand_num_list(4,2):
    print(MBTI['I'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_i += user_input

for n in rand_num_list(4,2):
    print(MBTI['E'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_e += user_input



for n in rand_num_list(4,2):
    print(MBTI['S'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_s += user_input


for n in rand_num_list(4,2):
    print(MBTI['N'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_n += user_input



for n in rand_num_list(4,2):
    print(MBTI['F'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_f += user_input

for n in rand_num_list(4,2):
    print(MBTI['T'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_t += user_input


for n in rand_num_list(4,2):
    print(MBTI['P'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_p += user_input

for n in rand_num_list(4,2):
    print(MBTI['J'][n])
    user_input = int(input("0~5점 사이의 값을 입력하세요: "))
    if user_input <0:
        user_input =0
    elif user_input > 5:
        user_input = 5
    score_j += user_input



