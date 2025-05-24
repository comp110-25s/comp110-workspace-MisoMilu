"""Document for code written on May 22"""


def factorial(n: int) -> int:
    """Calculates factorial"""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case   (dont need to include else below, but can)
    elif n > 1:
        return n * factorial(n-1)
    else:
        return -1


print(factorial(n=100))
