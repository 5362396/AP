def mult(arg):
    result = 1
    for i in arg:
        result *= i
    return result


def mult_ints(arg):
    result = 1
    for i in arg:
        if isinstance(i, int):
            result *= i
    return result


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def multiply_ints(*args):
    result = 1
    for arg in args:
        if isinstance(arg, int):
            result *= arg
    return result


def make_car(firma, model, **kwargs):
    car = {
        "firma": firma,
        "model": model
    }
    car.update(kwargs)
    return car


def main():
    print(mult([3, 5, 7]))
    print(mult(range(3, 8, 2)))  # (2, 8, 2) zwraca 48 (2*4*6) nie 105 (3*5*7)

    print(mult_ints([3, 3.14, 5, "abc", 7]))

    print(multiply(3, 5, 7))

    print(multiply_ints(3, 3.14, 5, "abc", 7))

    car1 = make_car("Kia", "Picanto", kolor="cafe mocca", poj_silnika=900)
    car2 = make_car("Volvo", "V50", kolor="czarny", poj_silnika=1600)
    car3 = make_car("Skoda", "Citigo", kolor="biały", pol_silnika=1000)
    [print(car) for car in [car1, car2, car3]]


if __name__ == '__main__':
    main()
