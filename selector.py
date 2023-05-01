import random


def num_selector():
    return random.sample(range(1,46), 6)


num_selected = num_selector()


print("로또 번호:", sorted(num_selected))
