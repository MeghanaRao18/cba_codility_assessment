

import domain_models.pet as pet
import domain_models.user as user
import domain_models.order as order
from config.request_constants import RequestConstants
from config.request_config_manager import RequestConfigManager
class UpdateData(object):
    """
    Class to create and  store pet, order and user data object parameters
    """
    def __init__(self):
        self.pet_data = None
        self.user_data = None
        self.order_data = None

    def generate_test_pet_data(self, status=""):
        """Generate test pet data"""
        self.pet_data = pet.Pet()
        pet_detail = {}
        pet_detail[RequestConstants.JSON_STATUS] = status
        self.pet_data.set_pet_details(pet_detail)
        return self.pet_data

    def generate_test_user_data(self):
        self.user_data = user.User()
        user_detail = {}

        user_detail[RequestConstants.JSON_USER_FIRST_NAME]="meg"
        user_detail[RequestConstants.JSON_USER_FIRST_NAME] = "rao"
        user_detail[RequestConstants.JSON_USER_EMAIL] = "mvmeghana@gmail.com"
        user_detail[RequestConstants.JSON_USER_PASSWORD] = "1111"
        user_detail[RequestConstants.JSON_USER_PHONE] = "00000"
        user_detail[RequestConstants.JSON_USER_STATUS] = 0

        user_list = [
        {
            "id": 1,
            "username": "user1",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        },
        {
            "id": 2,
            "username": "user2",
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane.smith@example.com",
            "password": "password456",
            "phone": "0987654321",
            "userStatus": 1
        }
        ]
        self.user_data.set_user_details(user_detail,user_list)

        return self.user_data

    def generate_test_order_data(self):
        self.order_data = order.Order()
        return self.order_data





