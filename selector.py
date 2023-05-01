import random


def num_selector():
    return random.sample(range(1,46), 6)


def print_num_selected():
    num_selected = num_selector()
    print("로또번호:", sorted(num_selected))


while True:
    print_num_selected()
    press_y = input("새로운 로또번호를 생성하려면 'y' 또는 'Y'를 입력하세요. 종료하려면 다른 키를 누르세요: ")
    if press_y.lower() != 'y':
        break
