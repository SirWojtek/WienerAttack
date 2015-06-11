#!/usr/bin/python
from fractions import Fraction
from math import sqrt

def computeSecretKey(e, n):
    continuedFractions = getContinuedFractions(e, n, 30)
    convergents = getConvergents(continuedFractions)
    eulerValues = getEulerFuncValues(convergents, e)
    print '#############################'
    primes = getPrimes(eulerValues, n)

    print 'Found p & q: %d %d' % (primes[0], primes[1])
    print 'Found d: %d' % findD(primes[0], primes[1], convergents, e)


def getContinuedFractions(a, b, steps):
    remainder = Fraction(a, b)
    result = []

    for i in range(steps):
        result.append(int(remainder))
        if remainder - result[-1] == 0:
            break
        remainder = Fraction(1, remainder - result[-1])

    return result

def getConvergents(fractionList):
    fractionList = filter(lambda a: a, fractionList)
    result = []

    for i in range(1, len(fractionList)):
        result.append(_partFraction(fractionList, 0, i))

    return result

def _partFraction(fractionList, i, n):
    if i < n:
        return Fraction(1, fractionList[i] + _partFraction(fractionList, i + 1, n))
    else:
        return Fraction(0, 1)

def getEulerFuncValues(convergents, e):
    result = []
    print 'd can be: '

    for convergent in convergents:
        print convergent.denominator
        candidate = (e * convergent.denominator - 1) / convergent.numerator
        if not (candidate % 2):
            result.append(candidate)

    return result

def getPrimes(eulerValues, n):
    for i in range(len(eulerValues)):
        p, q = resolvePolynomial(1, - n + eulerValues[i] - 1, n)

        if (p and q) and (p * q == n):
            return (p, q, i)

def resolvePolynomial(a, b, c):
    delta = pow(b, 2) - 4 * a * c

    if delta >= 0:
        sq = long(sqrt(delta))
        x1 = (-b + sq) / (2 * a)
        x2 = (-b - sq) / (2 * a)

        return (x1, x2)

    return (0, 0)

def findD(p, q, convergents, e):
    euler = (p - 1) * (q - 1)

    for convergent in convergents:
        if convergent.denominator * e % euler == 1:
            return convergent.denominator

if __name__ == "__main__":
    n = 5074772291286459206774040208059072021046562917
    e = 4223234360740816682261885795416553301541344119

    e1 = 17993
    n1 = 90581

    print '------------------------'
    computeSecretKey(e1, n1)
    print '------------------------'
    computeSecretKey(e, n)