def greet():
    '''Return a friendly greeting'''
    return 'Hello'

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
