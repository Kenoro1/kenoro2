from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

count = 0
for item in cycle([True, 'Hello', 1, 12.213, {23, 10}, (2, 6, 8), {'car':False}]):
    if count > 10:
        break
    print(item)
    count += 1
