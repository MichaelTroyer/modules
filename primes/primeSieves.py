# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 17:08:18 2017

# http://stackoverflow.com/questions/2068372

"""


def rwh_primes1(n=1000000):

    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in xrange(1, n // 2) if sieve[i]]
