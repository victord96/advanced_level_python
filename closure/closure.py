
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Only strings, please'
        return string * n
    return repeater


def make_division_by(n):
    def division(x):
        return x/n
    return division    


def run():
    # repeat_5 = make_repeater_of(5)
    # repeat_10 = make_repeater_of(10)

    # print(repeat_5('Hello'))
    # print(repeat_10('Platzi'))

    make_division_by_5 = make_division_by(5)

    print(make_division_by_5(2))


if __name__ == '__main__':
    run()