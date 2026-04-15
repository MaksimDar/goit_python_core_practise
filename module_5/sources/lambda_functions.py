##### first example

# import math

# def get_length(d):
#     result = d * math.pi
#     return result

# get_lambda_lenth =  lambda d: d*math.pi

# if __name__ == '__main__':
#     length_1 = get_length(10)
#     length_2 = get_lambda_lenth(10)
#     print(length_1)
#     print(length_2)


import math

def get_ost(data):
    result = []

    for i in data:
        ost = i % 2
        result.append(ost)
    return result

def check_num(data):
    result = []

    for i in data:
        ost = i % 2
        if ost:
            result.append(i)
    return result

if __name__ == '__main__':
    data = [1,2,3,4,5,6]
    ost_1 = get_ost(data)
    ost_2 = map(lambda i: i % 2, data)
    # print(*ost_1)
    print(*ost_2)

    check = check_num(data)
    print(check)

    check_data = list(filter(lambda i: i % 2, data))
    print(check_data)
    
