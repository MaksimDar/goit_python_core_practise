def filter_lines(keyword):
    print(f'Looking for {keyword}')
    try:
        while True:
            line = yield
            if keyword in line:
                yield f"Line accepted:{line}"
            else:
                yield None
    except GeneratorExit:
        print('Generator is being closed')

if __name__ == '__main__':
    gen = filter_lines('Maksym')
    next(gen)
    lines_list = [' Hello Maksym', ' How are you?', ' How is life, Maksym?', ' What do you like, Maksym?', ' What time is it?']
    maksym_list = []
    for line in lines_list:
        result = gen.send(line)
        if result:
            maksym_list.append(result)
        next(gen)
    gen.close()
    print(maksym_list)


