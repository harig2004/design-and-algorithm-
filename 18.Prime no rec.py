def is_prime(n, divisor=2):
    if n <= 2:
        return True if n == 2 else False
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)

def generate_primes(start, end):
    if start <= end:
        if is_prime(start):
            print(start)
        generate_primes(start + 1, end)

generate_primes(2, 50)
