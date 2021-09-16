def is_prime(number: int) -> bool:
    for x in range(number):
        if x != 0 and x != 1 and x != number:
            if number % x == 0:
                return 0    
    return 1

def run():
    print(is_prime(10))


if __name__ == '__main__':
    run()