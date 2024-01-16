from main import add


def test_add():
    assert add(1,2)==3

# Test case passed

def test_num_add():
    assert add(3,6)==9

def test_string_add():
    assert add("a","b")=="ab"

#  Group unit tests together using classes

class TestSample:

    #  Self representing instance of a class
    # the first parameter of methods is the instance the method is called on.

    # It is customary to use “self” as the first parameter in instance methods/functions of a class.

    def test_add(self):
        assert add(1, 2) == 3

    # Test case passed

    def test_num_add(self):
        assert add(3, 6) == 9

    def test_string_add(self):
        assert add("a", "b") == "ab"


class Telus:
    pass


def init():
    name="Ravi"
    age=12
    maritial= "unmarried"


class Telusko:

    def subtract_no(c,d):

        print("The given values if the number is =", c-d)

    def update(self):
        self.age=31

      subtract_no(3,4)

    #  Decalared two objects of class Telusko

    object= Telus()
    object2=Telus()

    object.name="Aniket"
    object.age= 22

    object2.name= "Aayush"
    object2.age= 23

    object2.update()


