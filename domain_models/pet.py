from util.random_string_generator import RandomStringGenerator
from config.request_constants import RequestConstants
from domain_models.category import Category
from domain_models.tag import Tag

class Pet(object):


    @property
    def pet_id(self):
        """pet_id property."""
        return self._pet_id

    @property
    def category(self):
        """category property."""
        return self._category

    @category.setter
    def category(self, value):
        self._category.name = value

    @category.deleter
    def category(self):
        del self._category

    @property
    def tag_list(self):
        """tag_list property."""
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        self._tag_list = value

    @tag_list.deleter
    def tag_list(self):
        del self._tag_list

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
        
    @property
    def photourls(self):
        """photourls property."""
        return self._photourls

    @photourls.setter
    def photourls(self, value):
        self._photourls = value

    @photourls.deleter
    def photourls(self):
        del self._photourls        

    @property
    def status(self):
        """status property."""
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @status.deleter
    def status(self):
        del self._status 

    @property
    def photo(self):
        """photo property."""
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value

    @photo.deleter
    def photo(self):
        del self._photo
                       
    def set_pet_details(self, pet_details):
        self.name = pet_details.get(RequestConstants.JSON_NAME,self.name)
#         for pet_URLS
        self.photourls = pet_details.get(RequestConstants.JSON_PHOTOURLS,self.photourls)
        self.status  = pet_details.get(RequestConstants.JSON_STATUS,self.status)
#         for pet TAGS
        self.tag_list = pet_details.get(RequestConstants.JSON_TAGS,self.tag_list)
        self.category = pet_details.get(RequestConstants.JSON_CATEGORY)

    def __init__(self):
        '''
        Constructor
        '''
        self._pet_id = RandomStringGenerator.generate_random_number_with_n_digits(6)
        self._category = Category()
#             status_list = [RequestConstants.JSON_STATUS_AVAILABLE, RequestConstants.JSON_STATUS_PENDING, RequestConstants.JSON_STATUS_SOLD]
        tags = RandomStringGenerator.generate_random_pet_tag(3)
        self._tag_list = []
        for tag in tags:
            obj = Tag()
            obj.name = tag
            self._tag_list.append(obj.to_dict())

        self._name = RandomStringGenerator.generate_random_pet_name(5)
        self._photourls = []
        self._status = ""
        self._photo =""
#         self._logger = logging.getLogger(__name__)

        
        
        