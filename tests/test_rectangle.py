import pytest
import source.shapes as shapes


#  EXAMPLE OF PYTEST WITH FUNCTIONAL BASED TEST

@pytest.fixture()
def my_rectangle():
    return shapes.Rectangle(10,20)

# This is showing error since it has self in it
def test_area(self):
    # Why we have to use super class name to call method of  a sub-class in a test case
    rectangle = shapes.Rectangle(4, 3)
    assert self.rectangle.area() == self.length * self.width


def test_area():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.area() == 10 * 20
