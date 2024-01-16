import pytest
import source.shapes as shapes
import math


# Example of class based tests
class TestCircle:

    #  These methods are always run when test is executed, method in argument is for each test
    def setup_method(self,method):
        print(f"Setting up {method}")
        self.circle=shapes.Circle(10)

    def teardown_method(self,method):
        print(f"Tearing down {method}")



# Beginning of test1
    def test_one(self):

        assert self.circle.area()== math.pi * self.circle.radius ** 2

    def test_perimeter(self):

        assert self.circle.perimeter()== 2 * math.pi * self.circle.radius