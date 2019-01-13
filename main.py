import random

task_list = ["source/множества.txt", "source/отношения, отношения эквивалентности, отображения.txt", "source/отношения порядка.txt", "source/теория графов.txt", "source/мощность множеств"]

for file in task_list:
    with open(file, encoding="utf-8", mode='r') as file:
        lines = file.readlines()
        task = random.randint(0, len(lines)-1)
        print(lines[task])



