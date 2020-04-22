import math

from decimal import *


def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def another_way_to_try_prime(n):
    return n in {
        num
        for num in range(1, n+1)
        if num != 1 and not any([num % div == 0 for div in range(2, math.ceil(math.sqrt(num)))])
    }


def solution():
    # uses e = 3652840521386397770775930229533596171296167783910904555909 / 5085525453460186301777867529962655859538011626631066055111

    import random
    getcontext().prec = 1000

    def primesbelow(N):
        # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        # """ Input N>=6, Returns a list of primes, 2 <= p < N """
        correction = N % 6 > 1
        N = {0: N, 1: N - 1, 2: N + 4, 3: N + 3, 4: N + 2, 5: N + 1}[N % 6]
        sieve = [True] * (N // 3)
        sieve[0] = False
        for i in range(int(N ** .5) // 3 + 1):
            if sieve[i]:
                k = (3 * i + 1) | 1
                sieve[k * k // 3::2 * k] = [False] * ((N // 6 - (k * k) // 6 - 1) // k + 1)
                sieve[(k * k + 4 * k - 2 * k * (i % 2)) // 3::2 * k] = [False] * (
                            (N // 6 - (k * k + 4 * k - 2 * k * (i % 2)) // 6 - 1) // k + 1)
        return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N // 3 - correction) if sieve[i]]

    smallprimeset = set(primesbelow(100000))
    _smallprimeset = 100000

    def isprime(n, precision=7):
        # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
        if n == 1 or n % 2 == 0:
            return False
        elif n < 1:
            raise ValueError("Out of bounds, first argument must be > 0")
        elif n < _smallprimeset:
            return n in smallprimeset

        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        for repeat in range(precision):
            a = random.randrange(2, n - 2)
            x = pow(a, d, n)

            if x == 1 or x == n - 1: continue

            for r in range(s - 1):
                x = pow(x, 2, n)
                if x == 1: return False
                if x == n - 1: break
            else:
                return False

        return True

    a, b, n = 0, 1, 100
    while n:
        if n % 3 == 2:
            m = (n + 1) / 3 * 2
        else:
            m = 1
        a, b, n = b, a + m * b, n - 1

    e = str(Decimal(a) / Decimal(b))
    n = 1
    while True:
        n += 1
        Number = e[n: n + 10]
        if isprime(int(Number)):
            print(Number)
            break


def run():
    print(another_way_to_try_prime(37))
    print(another_way_to_try_prime(2))
    print(another_way_to_try_prime(8))

    mult = 10 ** 9
    e = math.e * mult
    i = 1
    print(format(math.e, '.120g'))
    print(len('2718281828459045090795598298427648842334747314453125'))
    while True:
        e = int(str('2718281828459045090795598298427648842334747314453125')[i:10 + i])
        print('current e: {}'.format(e))
        if is_prime(math.floor(e)):
            print(e)
            break
        i += 1

    solution()