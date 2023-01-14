#!/usr/bin/env python3
"""Example of a class with an attribute and a method.

Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
"""


class MyClass:
    """Example class.

    Note the difference between class attributes and instance attributes.
    """

    # This attribute will be common to **all** instances of the class.
    class_attribute = "world"

    def my_method(self, param1: str) -> None:
        print(f"\nHello {param1}")
        print(f"The object that called this method is: {self}")

        # This attribute is being added only to the instance of the class on
        # which my_method() is being called.
        self.instance_attribute = param1


def main():
    instance_1 = MyClass()
    instance_2 = MyClass()

    print()
    print()
    print(f"id(instance_1) = {id(instance_1)}")
    print(f"id(instance_2) = {id(instance_2)}")

    print("output of dir(instance_1):")
    print(dir(instance_1))
    print()
    print("output of dir(instance_2):")
    print(dir(instance_2))

    instance_2.my_method("CS162")  # adds the instance_attribute
    print(f"instance_2 has new attribute with value: {instance_2.instance_attribute}")
    print()

    print("output of dir(instance_1):")
    print(dir(instance_1))
    print()
    print("output of dir(instance_2):")
    print(dir(instance_2))


if __name__ == "__main__":
    main()
