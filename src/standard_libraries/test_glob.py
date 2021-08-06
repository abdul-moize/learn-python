"""File Wildcards.

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

The glob module provides a function for making file lists from directory wildcard searches:
"""

import glob


def test_glob():
    """File Wildcards."""

    # == operator for lists relies on the order of elements in the list.
    # In some cases (like on Linux Mint, python3.6) the glob() function returns list
    # in reverse order then  it might be expected. Thus lets sort both lists before comparison
    # using sorted() built-in function.

    filenames = ['names.txt', 'cars.txt', 'cars.json', 'some.csv', 'data1.txt', 'data2.txt', 'data9.txt']
    path = 'src/standard_libraries/glob_files'
    for i in filenames:
        open(path+i, 'w').close()
    assert sorted(glob.glob(path + '/*.csv')) == sorted([path + '/some.csv'])
    assert sorted(glob.glob(path + '/data[0-2].txt')) == sorted([path + '/data1.txt', path + '/data2.txt'])


