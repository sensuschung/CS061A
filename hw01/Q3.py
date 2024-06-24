# Q3: Largest Factor
# Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    c = 1
    i = 2
    while i < n:
        if n % i == 0:
            c = i
        i = i + 1
    return c