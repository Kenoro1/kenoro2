a = int(input('Enter number x: '))
b = int(input('Enter number y: '))




def my_f(x, y):
    print(f'{x // y}')

my_f(a, b)



name = input('Enter your name: ')
sur_name = input('Enter your surname: ')
birthday = input('Enter your birthday (DD.MM.YY): ')
city = input('Enter city where u live: ')
email = input('Enter your Email: ')
number = input('enter your number: ')


def analytics(name, surname, bd, city, em, num):
    print(f'Your name {name}, your surname {surname}, your birthday {bd}, city when u live {city}, email address {em}, and your number {num}')


analytics(name, sur_name, birthday, city, email, number)



def sums(a, b, c):
    if a > b < c:
        print(f'{a + c}')
    if a < b < c:
        print(f'{b + c}')
    if a > b > c:
        print(f'{a + b}')

sums(8, 6, 12)



def my_func(x, y):
    print(f'{x ** y}')


my_func(2, -1)




def int_func(word):
    print(word.capitalize())



int_func('hello world')


def int_func_2(word):
    return word.title()



print(int_func_2('hello world, my name Nick'))