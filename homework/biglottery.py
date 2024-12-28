import random

min = 1
max = 49


set1 = set()
while(True):
    target = random.randint(min, max)
    set1.add(target)
    if len(set1) == 7:
        print('本期大樂透電腦選號號碼如下:\n')
        for i in list(set1):
            print(i, end=" ")
        print(f'\n\n特別號:{list(set1)[-1]}')
        break
