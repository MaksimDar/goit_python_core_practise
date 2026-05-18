import pickle

def fibonacci_with_while_and_results(limit):
    try:
        with open('fibonacci.pkl', 'rb') as file:
            state = pickle.load(file)
            print('Resuming from previous calculation')
    except FileNotFoundError:
        print("Start New calculation")
        state = {'current': 0, 'next': 1, 'results': list()}

    while state['current'] < limit:
        state['results'].append(state['current'])
        new_value = state['current'] + state['next']
        state['current'],state['next'] = state['next'], new_value
        with open('fibonacci.pkl', 'wb') as file:
            pickle.dump(state,file)

    def filter_results(fib_numbers):
        return fib_numbers <= limit
    
    print('Calculation completed')
    print("Final calculation state: ", state)
    
    return list(filter(filter_results, state['results']))

print(fibonacci_with_while_and_results(3))
print(fibonacci_with_while_and_results(10))
print(fibonacci_with_while_and_results(5))
