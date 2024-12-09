from util.random_string_generator import RandomStringGenerator
import datetime

class Order(object):


    @property
    def order_id(self):
        """order_id property."""
        return self._order_id

    @property
    def pet_id(self):
        """pet_id property."""
        return self._pet_id

    @property
    def quantity(self):
        """quantity property."""
        return self._quantity

    @property
    def ship_date(self):
        """ship_date property."""
        return self._ship_date

    @property
    def status(self):
        """status property."""
        return self._status
    
    @property
    def complete(self):
        """complete property."""
        return self._complete
               
    def __init__(self):

        self._order_id = RandomStringGenerator.generate_random_number_with_n_digits(1)
        self._quantity = 1
        self._pet_id = RandomStringGenerator.generate_random_number_with_n_digits(4)
        self._ship_date = str(datetime.datetime.now())
        self._status = "COMPLETE"
        self._complete = False
        