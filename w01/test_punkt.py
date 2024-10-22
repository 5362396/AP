from punkt import Punkt


if __name__ == "__main__":
    p = Punkt(1, 2)
    r = Punkt(2, 1)
    p.x = 2

    print(p)
    print(type(p))
    print(p.__repr__())

    print(p == r)
    print(p != r)
    print(p.y < r.y)
    print(p.y > r.y)
    print(r.x <= p.x)
    print(r.y >= p.y)

    try:
        del p.x
    except AttributeError as e:
        print(e)
