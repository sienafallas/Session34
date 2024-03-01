def greet(name):
    """
    Simple greet function, prints hello
    :param name: string
    :retun: None
    """
    print(f"Hello, {name}")


greet("Bogdan")
greet("John")
greet("Maria")
def special_op(x, y, z):
    """
    Same special operation
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of operation
    """
    return x * y + z

result = special_op(2,3,4)
print(result)
print(special_op(z=2, x=3, y=4))

greet(special_op(2,3,4))

# recursive function
def factorial(n):
    """
    Factorial of a number
    :param n: int number
    :return: the value of n!
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


