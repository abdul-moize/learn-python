"""Generators.

@see: https://www.learnpython.org/en/Generators

Generators are used to create iterators, but with a different approach. Generators are simple
functions which return an iterable set of items, one at a time, in a special way.

When an iteration over a set of item starts using the for statement, the generator is run. Once the
generator's function code reaches a "yield" statement, the generator yields its execution back to
the for loop, returning a new value from the set. The generator function can generate as many
values (possibly infinite) as it wants, yielding each one in its turn.
"""

import random


def lottery():
    """Generator function example.

    Here is a simple example of a generator function which returns random integers.
    This function decides how to generate the random numbers on its own, and executes the yield
    statements one at a time, pausing in between to yield execution back to the main for loop.
    """
    # returns first 3 random numbers between 1 and 10
    # pylint: disable=unused-variable
    for i in range(3):
        yield random.randint(1, 10)

    # returns a 4th number between 10 and 20
    yield random.randint(10, 20)


def test_generators():
    """Yield statement"""
    xyz = enumerate(lottery())
    for number_index, random_number in xyz:
        if number_index < 3:
            assert 0 <= random_number <= 10
        else:
            assert 10 <= random_number <= 20

    def my_gen():
        n = 1
        yield n
        n += 1
        yield n
        n += 1
        yield n
    # manually access
    numbers = my_gen()
    assert next(numbers) == 1
    assert next(numbers) == 2
    assert next(numbers) == 3

    #loop access
    count = 1
    for i in my_gen():
        assert i == count
        count += 1


