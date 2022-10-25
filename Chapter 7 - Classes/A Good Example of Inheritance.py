### An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

# Create an Abstract Base Classes.

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open!')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed!')
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print('Reading data from a file...')

class NetworkStream(Stream):
    def read(self):
        print('Reading data from a network...')

class MemoryStream(Stream):
    def read(self):
        print('Reading data from a memory stram...')

stream = MemoryStream()
stream.open()