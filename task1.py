from collections import defaultdict


companies = defaultdict(list)
profit_companies = defaultdict(list)

num_companies = int(input('Введите кол-во компаний: '))
sum_ = 0
for i in range(num_companies):
    name = input(f'Введите название компании {i + 1}: ')
    for j in range(4):
        companies[name].append(int(input(f'Введите прибыль за {j + 1} квартал: ')))
    sum_ += sum(companies[name])

avg = sum_ / num_companies

print(f'Средняя прибыль компаний {avg=}')

for name in companies:
    if sum(companies[name]) > avg:
        profit_companies['up'].append(name)
    elif sum(companies[name]) < avg:
        profit_companies['down'].append(name)

print('Компании с прибылью выше среднего: ')
for i in profit_companies['up']:
    print(i)

print('Компании с прибылью ниже среднего: ')
for i in profit_companies['down']:
    print(i)

