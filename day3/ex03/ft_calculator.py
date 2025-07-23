def auto_print(method):
    """Just to show how to make my own decorator"""
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        print(self.data)
    return wrapper

class calculator:
    """My calculator class"""
    def __init__(self, data: list):
        self.data = data
    
    @auto_print
    def __add__(self, object) -> None:
        """Method to add a scalar to vector"""
        self.data = [i + object for i in self.data]

    @auto_print
    def __mul__(self, object) -> None:
        """Method to multiply a vector by a scalar"""
        self.data = [i * object for i in self.data]

    @auto_print
    def __sub__(self, object) -> None:
        """Method to substract a scalar to a vector"""
        # for i, n in enumerate(self.data):
        #     self.data[i] = n - object
        self.data = [i - object for i in self.data]

    @auto_print
    def __truediv__(self, object) -> None:
        """Method to divide a vector by a scalar, doesn't work with zero"""
        if object == 0:
            raise ZeroDivisionError("trying to divide by zero")
        self.data = [i / object for i in self.data]

