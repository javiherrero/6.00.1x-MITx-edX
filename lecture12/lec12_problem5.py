# Desc: Lec 12, Problem 5.
# Author: Javier Herrero Arnanz.

def genPrimes():
    """Generates the sequence of prime numbers"""
    primes = [] # List of prime numbers.
    i = 2 # Candidate.
    while (True):
        # A candidate number x is prime if (x % p) != 0 for all earlier primes p.
        isPrime = True
        for prime in primes:
            if ((i % prime) == 0):
                isPrime = False
                break
        # Show the prime number and add it to the list.        
        if (isPrime):
            primes.append(i)
            yield i
        # Generate another candidate.
        i += 1
        
