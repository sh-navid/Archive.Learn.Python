# method-wrapper ??
# slot wrapper   ??
# bound-method              # removed in python 3

# [Function]
def my_function():
    print("This is from my function")


# [Lambda]
my_lambda = lambda num: print(f"This is from my lambda {num}")

my_function()
print(type(my_function))
my_lambda(12)
print(type(my_lambda))


class MyClass:
    variable_of_class = 12  # For class and all instances

    # __init__ is Constructor
    # __init__ also is a [Magic Method] (have double underscores: dunder)
    def __init__(self, argument) -> None:
        self.variable_of_instance = argument
        print("Dunder    Method")

    @staticmethod
    def my_static_method():
        print(f"Static   Method")

    @classmethod
    def my_class_method(cls):
        print(
            f"Class    Method of [{cls.__name__}], class_variable=[{cls.variable_of_class}]"
        )

    # [Instance Method]
    def my_instance_method(self):
        print(
            f"Instance Method of [{self.__class__.__name__}], class_variable=[{self.variable_of_class}], instance_variable=[{self.variable_of_instance}]"
        )


MyClass.my_static_method()
MyClass.my_class_method()


instance1 = MyClass(1)
instance2 = MyClass(2)


MyClass.variable_of_class = 14  # Work on both
print(MyClass.variable_of_class is instance1.variable_of_class)  # True
instance1.variable_of_class = 16
# Just working on instance1; Is this shadowed?? or is the same variable?
print(MyClass.variable_of_class is instance1.variable_of_class)  # False


instance1.my_static_method()
instance1.my_class_method()
instance1.my_instance_method()


instance2.my_static_method()
instance2.my_class_method()
instance2.my_instance_method()
