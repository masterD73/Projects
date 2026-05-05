# Reviewer: Ran
class Property(object):

    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, obj, objtype=None):
        return self.fget(obj)

    def __set__(self, obj, value):
        self.fset(obj, value)

    def __delete__(self, obj):
        self.fdel(obj)

    def Setter(self, fset):
        self.fset = fset
        return self

    def Deleter(self, fdel):
        self.fdel = fdel
        return self


class X(object):
    """Example class"""

    def __init__(self, val):
        """init function for class X"""
        self.__x = int(val)

    @Property
    def x(self):
        return self.__x

    @x.Setter
    def x(self, val):
        self.__x = int(val)

    @x.Deleter
    def x(self):
        del self.__x


a = X(0)
print(a.x)
a.x = 1
del a.x
