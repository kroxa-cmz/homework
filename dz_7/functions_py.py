import time
#Ex.1
# def action_decorator(func):
#     def inner(value):
#         print(func.__name__, 'is canceled!')
#     return inner


#Ex.2
# def action_decorator(func):
#     def inner(value):
#         start = time.time()
#         func(value)
#         print(time.time() - start, ' sec - exec time')
#     return inner

#Ex.3
# counter=[]
# def action_decorator(func):
#     def inner(value):
#         func(value)
#         counter.append(1)
#         print(len(counter), 'time exec func')
#     return inner


#Ex.4
# def action_decorator(func):
#     print('Create decorator')
#     def inner(value):
#         print('Begin of exec func')
#         func(value)
#         print('End of exec func')
#     return inner

#Ex.5
# def action_decorator(func):
#     def inner(value):
#         try:
#             func(value)
#         except Exception as e:
#             print(e)
#     return inner


#@action_decorator
def long(value):
    time.sleep(5)  # delays for 5 seconds
    return 'long ' + str(value)


def short(string_param):
    print('Speed!', string_param)
    return 'short'


def medium(value, *modificators):
    result = value
    for m in modificators:
        result *= m

    return result


def change_sign(num, check_sign=True):
    if check_sign and num > 0:
        raise ValueError('num > 0!')
    return -num


#map/filter/reduce

arr=[1,4,5,30,99]

print(list(map(lambda x: x%5, arr)))

arr = [3, 4, 90, -2]

print(list(map(lambda x: str(x),arr)))

arr = ['some', 1, 'v', 40, '3a', str]

print(list(filter(lambda x: type(x) != type(''),arr)))

from functools import reduce

arr = ['some', 'other', 'value']

print(len(reduce(lambda a,x: a + x,arr)))