from my_package.maincode import my_sum
import pytest
""" Using pytest for testing code """


def test_list_int():
    """ Tests that it can sum a list of integers """
    data = [4, 5, 6]
    result = my_sum(data)
    assert result == 16, "It should be 15"

def test_list_float():
    """ Tests that it can sum a list of floats """
    data = [4.0, 5.0, 6.0]
    result = my_sum(data)
    assert result == 15, "It should be 15"

def test_tuple_int():
    """ Tests that it can sum a tuple of integers """
    data = (4, 5, 6)
    result = my_sum(data)
    assert result == 15, "It should be 15"

def test_tuple_float():
    """ Tests that it can sum a tuple of floats """
    data = (4.0, 5.0, 6.0)
    result = my_sum(data)
    assert result == 15, "It should be 15"

def collections_equals_fifteen(data):
    """ receives some collection data """
    function_result = my_sum(data)
    expected_value = 15
    message = "It should be 15"
    assert function_result == expected_value, message
    # assert function_result == 14, message
    # assert function_result == 13, message

def test_collections_equals_fifteen():
    """ tests different collections if they sum to fifteen """
    collections_equals_fifteen((4, 5, 6))
    collections_equals_fifteen([4, 5, 6])
    collections_equals_fifteen({4, 5, 6})
    collections_equals_fifteen((4.0, 5.0, 6.0))
    collections_equals_fifteen([4.0, 5.0, 6.0])
    collections_equals_fifteen({4.0, 5.0, 6.0})

@pytest.mark.xfail
def test_expected_failing_test():
    assert 4 == 5, "yeah... four is five"
