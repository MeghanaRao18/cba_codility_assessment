from util.random_string_generator import RandomStringGenerator
from domain_models.base import Base

class Tag(Base):
    '''
    classdocs
    '''


    @property
    def id(self):
        """id property."""
        return self._id

    @property
    def name(self):
        """name property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name
        

                
    def __init__(self):
        '''
        Constructor
        '''
        self._id = RandomStringGenerator.generate_random_number_with_n_digits(6)
        self._name = ""
