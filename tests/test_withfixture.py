import pytest
import source.shapes as shapes


# Created since we have to initialize the object again and again
@pytest.fixture()
def my_rectangle():
    return shapes.Rectangle(10, 20)


# This is showing error since it has self in it
def test_area(self):
    # Why we have to use super class name to call method of  a sub-class in a test case
    rectangle = shapes.Rectangle(4, 3)
    assert self.rectangle.area() == self.length * self.width


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20
