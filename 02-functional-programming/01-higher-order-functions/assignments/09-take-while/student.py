def take_while(xs, condition):
    first = []
    second = []

    for i in range(len(xs)):
        if not condition(xs[i]):
            first = xs[:i]
            second = xs[i:]
            return (first, second)
    
    return (xs, [])

