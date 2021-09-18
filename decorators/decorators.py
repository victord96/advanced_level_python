from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(str(time_elapsed.total_seconds()) + " seconds have passed")
    return wrapper


def function_level(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
        n_lenghts = len(args)
        if n_lenghts == 1:
            print('It\'s an easy function')
        elif n_lenghts == 2 or n_lenghts == 3:
            print('It\'s a middle level function')
        else:
            print('It\'s a hard function')
    return wrapper        


@function_level
def division(a: int, b: int) -> int:
    return a/b
    

division(2, 2)

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b   


@function_level
@execution_time
def greeting(name='Cesar'):
    print('Hello ' + name)

# random_func()   
# greeting('Fernando') 
# sum(5, 5)
