"""FOR statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or
giving the user the ability to define both the iteration step and halting condition (as C),
Python’s for statement iterates over the items of any sequence (a list or a string), in the
order that they appear in the sequence. For example (no pun intended):
"""


def get_result():
    name = ['amk', 'ali', 'hamza']
    marks = [100, 9, 10]
    result = {}
    for i, j in zip(name, marks):
        result[i] = j
    return result


def get_combinations():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    combinations = []
    for question, answer in zip(questions, answers):
        combinations.append('What is your {0}?  It is {1}.'.format(question, answer))
    return combinations
# pylint: disable=too-many-locals


def get_inds_vals():
    inds = []
    vals = []
    for ind, val in enumerate(range(5)):
        inds.append(ind)
        vals.append(val)
    return inds, vals


def get_knights():
    kn = []
    kp = []
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        kn.append(key)
        kp.append(value)
    return kn, kp


def get_indices():
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)
    return indices, values


def get_combined_names():
    names = ['amk', 'hamza', 'ali']
    last_names = ['arif', 'khizar', 'fareed']
    combined_names = []
    for i, j in zip(names, last_names):
        combined_names.append(i + ' ' + j)
    return combined_names


def test_for_statement():
    """FOR statement"""

    # Measure some strings:
    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    # "cat" length is 3
    # "window" length is 6
    # "defenestrate" length is 12
    assert words_length == (3 + 6 + 12)
    words_length = 0
    for i in range(len(words)):
        words_length += len(words[i])
    assert words_length == (3 + 6 + 12)
    combined_names = get_combined_names()
    assert combined_names == ['amk arif', 'hamza khizar', 'ali fareed']
    # If you need to modify the sequence you are iterating over while inside the loop
    # (for example to duplicate selected items), it is recommended that you first make a copy.
    # Iterating over a sequence does not implicitly make a copy. The slice notation makes this
    # especially convenient:
    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)

    # Otherwise with for w in words:, the example would attempt to create an infinite list,
    # inserting defenestrate over and over again.

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']
    words = ['cat', 'window', 'defenestrate']

    # If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    # handy. It generates arithmetic progressions:
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    inds, vals = get_inds_vals()
    assert inds == vals
    # To iterate over the indices of a sequence, you can combine range() and len() as follows:
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '
    numbers = [5, 4, 3, 2, 1]
    reverse_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reverse_numbers.append(numbers[i])
    assert reverse_numbers == [1, 2, 3, 4, 5]

    # Or simply use enumerate().
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # When looping through dictionaries, the key and corresponding value can be retrieved at the
    # same time using the items() method.
    knights_names, knights_properties = get_knights()
    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # When looping through a sequence, the position index and corresponding value can be retrieved
    # at the same time using the enumerate() function
    indices, values = get_indices()
    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # To loop over two or more sequences at the same time, the entries can be paired with
    # the zip() function.
    combinations = get_combinations()

    assert combinations == [
        'What is your name?  It is lancelot.',
        'What is your quest?  It is the holy grail.',
        'What is your favorite color?  It is blue.',
    ]
    result = get_result()
    assert result == {'amk': 100, 'ali': 9, 'hamza': 10}


def test_range_function():
    """Range function

    If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    handy. It generates arithmetic progressions.

    In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
    It is an object which returns the successive items of the desired sequence when you iterate
    over it, but it doesn’t really make the list, thus saving space.

    We say such an object is iterable, that is, suitable as a target for functions and constructs
    that expect something from which they can obtain successive items until the supply is exhausted.
    We have seen that the for statement is such an iterator. The function list() is another; it
    creates lists from iterables:
    """

    assert list(range(5)) == [0, 1, 2, 3, 4]

    # The given end point is never part of the generated sequence; range(10) generates 10 values,
    # the legal indices for items of a sequence of length 10. It is possible to let the range start
    # at another number, or to specify a different increment (even negative; sometimes this is
    # called the ‘step’):

    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
    assert list(range(5, 0, -1)) == [5, 4, 3, 2, 1]
