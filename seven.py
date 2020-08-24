def fact_x(x):
    start = 1
    fact = 1
    while start <= 5:
        yield fact
        start = start + 1
        fact = fact * start


func = fact_x(5)
for i in func:
    print(i)