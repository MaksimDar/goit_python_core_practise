from time import time


def args_logger(func):
    def inner(*args):
        if Debug:
            print(f"I am args logger. My args are: {args}")
        result = func(*args)
        return result
    return inner

def result_logger(func):
    def inner(*args):
        result = func(*args)
        if Debug:
            print(f'I am result {result}')
        return result
    return inner

def timer(func):
    def inner(*args):
        start = time()
        result = func(*args)
        stop = time()
        if Debug:
            print(f'I am timer. Run time: {stop - start}')
        return result
    return inner

@timer
@args_logger
@result_logger

def calc(x,y):
    result = x + y
    return result

Debug = False
# logger = args_logger(calc)

if __name__ == '__main__':
    print(calc(3,10))