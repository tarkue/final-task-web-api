import abc


class SingletonMeta(type):
    """
    Singleton metaclass for classes without parameters on constructor,
    for compatibility with FastApi Depends() function.
    """
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonABCMeta(SingletonMeta, abc.ABCMeta):
    """Metaclass that combines SingletonMeta and ABCMeta"""
    pass