### 1
def outer(x):
    def inner(y):
        print(f"{x} + {y} = {x+y}")
    return inner
###2
def get_cach(cache=None):
    if cache is None:
        cache = {}
    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum([i for i in range(n+1)])
            print(f'Hard work: {n}')
            return cache[n]
        else:
            print(f'Easy work: {n}')
            return cache[n]

    return inner


def main():
    ###1
    # adder_two = outer(2)
    # adder_two(5)
    # adder_three = outer(3)
    # adder_three(5)
    ###2 
    data = {5: 15, 3: 6}
    get_now_cach = get_cach(data)
    print(get_now_cach(5))
    print(get_now_cach(3))
    print(get_now_cach(5))
    print(get_now_cach(10))


if __name__ == '__main__':
    main()