def fizzbuzz():
    x = 1
    while True:
        if x % 3 == 0 and x % 5 == 0:
            yield "fizzbuzz"
        elif x % 3 == 0:
            yield "fizz"
        elif x % 5 == 0:
            yield "buzz"
        else:
            yield str(x)
        x += 1