import random


def get_num():
    return random.sample(range(1,46), 6)


def print_num():
    nums = get_num()
    print("로또번호:", sorted(nums))


while True:
    print_num()
    retry_key = input("새로운 로또번호를 생성하려면 'y' 또는 'Y'를 입력하세요. 종료하려면 다른 키를 누르세요: ")
    if retry_key.lower() != 'y':
        break
