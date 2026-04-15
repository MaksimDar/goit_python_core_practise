####### Counter

# from collections import Counter


# def num_counter(filename, n):
#     with open(filename, 'r', encoding='utf-8') as fh:
#         data = fh.read()
#         data_updated = [int(i) for i in data.split(',')]
#     # print(data)
#     # print(type(data_updated[0]), data_updated)
#     counter = Counter(data_updated)
#     order = counter.most_common(len(counter))
#     # return [i for i in order[:n]], [i for i in order[-n:]]
#     return order[:n], order[-n:]

# most,least = num_counter('numbers.txt', 5)
# print(most)
# print(least)

######## namedtuple

# from collections import namedtuple

# cat_info = namedtuple('Cat', ['nickname', 'age', 'owner'])

# bobs_cat = cat_info('Bob',9,'Mak')
# print(bobs_cat.nickname, bobs_cat.age, bobs_cat.owner)

# from collections import namedtuple

# rgb = namedtuple('RGB', ['red', 'green', 'blue'])

# ocean_wave= rgb(244,9,53)
# indigo = rgb(22,8,123)
# print(indigo.red)
# print(ocean_wave.green)


########### defaultdict

# from collections import defaultdict

# phone_numbers = ['0508588594', '067839393934', '0960157201', '063778221', '0678965436', '0508432594', '095835533934', '0950154501', '063558221']

# phone_operators = defaultdict(list)

# for phone in phone_numbers:
#     if phone.startswith('050') or phone.startswith('095'):
#         phone_operators['Vodafone'].append(phone)
#     if phone.startswith('063') or phone.startswith('096'):
#         phone_operators['KyivStar'].append(phone)

#     if phone.startswith('067'):
#         phone_operators['LifeCell'].append(phone)
# print(phone_operators)