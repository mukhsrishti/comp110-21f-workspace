"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.
def all(list, n):
    for i in list:
        if i != n:
            return False
        else:
            return True

def is_equal(first: list[int], second: list[int]):
    if (len(first) != len(second)):
        return False
    if is_equal == is_equal(first, second):
        print (is_equal)


def max(i: list[int]):
    largest_number = 0
    length_of_list = len(i)
    if length_of_list == 0:
        raise ValueError("max() arg is an empty List")
    for items in i:
        if i[items] > largest_number:
            largest_number = i[items]

    return largest_number




        