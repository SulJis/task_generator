import random

with open("source/теорія множин.txt", encoding="utf-8", mode='r') as file:
    lines = file.readlines()
    first_task = random.randint(0, len(lines)-1)
    print(lines[first_task])

with open("source/теорія границь.txt", encoding="utf-8", mode='r') as file:
    lines = file.readlines()
    second_task = random.randint(0, len(lines)-1)
    print(lines[second_task])

with open("source/Диференціальне числення.txt", encoding="utf-8", mode='r') as file:
    lines = file.readlines()
    third_task = random.randint(0, len(lines)-1)
    print(lines[third_task])

