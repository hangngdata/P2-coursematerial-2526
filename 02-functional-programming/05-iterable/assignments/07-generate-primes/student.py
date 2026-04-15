def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2

def primes():
    current = 2
    while True:
        if is_prime(current):
            yield current
        current += 1
