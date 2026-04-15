class MyContextManager():
    def __enter__(self):
        print('You are entered')
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print('Exit block')
        if exc_type:
            print(f'Error detected {exc_type}')

        return False
    
with MyContextManager() as context:
    print('Raise Exception')
    raise Exception('Something went wrong!')