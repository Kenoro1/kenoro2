water = open('text.txt', 'w', encoding='utf-8')
water.write('Hello world\nHi\n7\n')


content = open('text_1.txt', 'r', encoding='utf-8')

for el, ef in enumerate(content, start=1):
    print(el, ef, end=(''))





with open(r'firm_.txt', 'r', encoding='utf-8') as my_file:
        sum_1 = []
        sec = []
        line = my_file.read().split("\n")
        for i in line:
            i = i.split()
            if float(i[1]) < 20000:
                sec.append(i[0])
            sum_1.append(i[1])

print(f'Зарплата меньше 20 000 {sec}. Average salary - {sum(map(float, sum)) / len(sum_1)}')









four = open('four.txt', 'r', encoding='utf-8')
four_2 = open('four_2.txt', 'w', encoding='utf-8')

dict_ = {
       'One':'Один',
       'Two':'Два',
       'Three':'Три',
       'Four':'Четыре'
   }
for line in four:
    for key, value in dict_.items():
        line = line.replace(key, value)
    four_2.write(line)

from random import randint

sum_el = 0
with open('text_5.txt', 'w', encoding='utf-8') as file_1:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        file_1.write(str(el) + " ")

print(f'Сумма элементов - {sum_el}')







dict_ = {}
with open('text_6.txt', encoding='utf-8') as file:
    for line in file:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        dict_[name] = name_sum

    print(f'{dict_}')