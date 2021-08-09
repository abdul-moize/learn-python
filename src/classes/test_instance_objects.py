"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#instance-objects
"""


def test_instance_objects():
    """Instance Objects.

    Now what can we do with instance objects? The only operations understood by instance objects
    are attribute references. There are two kinds of valid attribute names:
    - data attributes
    - methods.
    """

    # DATA ATTRIBUTES need not be declared; like local variables, they spring into existence when
    # they are first assigned to. For example, if x is the instance of MyCounter created above,
    # the following piece of code will print the value 16, without leaving a trace.

    # pylint: disable=too-few-public-methods
    class DummyClass:
        """Dummy class"""
        pass

    dummy_instance = DummyClass()
    assert dummy_instance.__doc__ == 'Dummy class'
    # pylint: disable=attribute-defined-outside-init
    dummy_instance.temporary_attribute = 1
    assert dummy_instance.temporary_attribute == 1
    del dummy_instance.temporary_attribute
    dummy_instance.name = "amk"
    assert dummy_instance.name == "amk"
    dummy_instance.data = {'name': 'ali', 'age': '10'}
    assert dummy_instance.data == {'name': 'ali', 'age': '10'}
    del dummy_instance.data
    try:
        dummy_instance.data is None
        error = ''
    except AttributeError:
        error = "attribute data does not exist"
    assert error == "attribute data does not exist"
