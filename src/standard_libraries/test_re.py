"""String Pattern Matching.

@see: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:
"""

import re


def test_re():
    """String Pattern Matching"""

    assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
        'foot',
        'fell',
        'fastest'
    ]

    assert re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') == 'cat in the hat'

    # When only simple capabilities are needed, string methods are preferred because they are
    # easier to read and debug:
    assert 'tea for too'.replace('too', 'two') == 'tea for two'
    regex = '''
        \\b[a-z0-9]+       # must start with at least one lower case letter or digit
        [a-zA-Z0-9.-_]*    # followed by 0 or more digits, '.', '-', '_' 
        @                  # followed by at the rate sign '@' 
        [a-z]+             # followed by at least one lowercase letter        
        [0-9-_]*           # followed by 0 or more digits, '-', '_'
        \\.                # followed by '.'
        [a-z]{2,3}\\b      # followed by 2 to 3 lowercase characers
        '''
    assert re.match(regex, 'abdul.moize@arbisoft.com', re.VERBOSE)
    emails = ['ankitrai326@gmail.com', 'my.ownsite@ourearth.org', 'ankitrai326.com']
    assert re.match(regex, emails[0], re.VERBOSE)
    assert re.match(regex, emails[1], re.VERBOSE)
    assert not re.match(regex, emails[2], re.VERBOSE)
    card_regex = '''
        \\b\\d{2}   # must start with 2 digits
        -           # followed by '-'
        \\d{5}      # followed by 5 digits
        -           # followed by '-'
        44          # followed by '44'
        -           # followed by '-'
        \\d{2}\\b   # must end with 2 digits
        '''
    card_numbers = ['12-12345-44-10', 'ab-12345-44-20', '23-45678-12-12', '21_32198_44_90']
    assert re.match(card_regex, card_numbers[0], re.VERBOSE)
    assert not re.match(card_regex, card_numbers[1], re.VERBOSE)
    assert not re.match(card_regex, card_numbers[2], re.VERBOSE)
    assert not re.match(card_regex, card_numbers[3], re.VERBOSE)
