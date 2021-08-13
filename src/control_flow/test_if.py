"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = -20
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
        if number > -10:
            conclusion += ' and greater than negative ten'
        if number > -100:
            conclusion += ' and greater than negative hundred'

    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number is less than zero and greater than negative hundred'
