"""
Module containing tests to validate store end point
"""
import pytest
from socks import PRINTABLE_PROXY_TYPES

from config.request_config_manager import RequestConfigManager
from config.request_constants import RequestConstants
from util.generate_data import UpdateData

HEADERS = "application/json"

@pytest.fixture
def config_manager():
    """

    steps performed before every test scenario
    :return:
    """
    requestManager = RequestConfigManager()
    requestManager.set_basic_url()
    return requestManager

@pytest.fixture
def generate_data():
    """
    :return:
    """
    return UpdateData()

@pytest.fixture
def place_order(config_manager,generate_data):
    config_manager.set_http_content_type(HEADERS)

    #set endpoint to first add user  and then get it using same id
    config_manager.set_endpoint('store/order')

    #get the data to upload
    order = generate_data.generate_test_order_data()
    config_manager.set_http_request_body_with_order_details(order)
    print(config_manager.get_http_request_body())

    #POST Http request raised
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()

    config_manager.set_post_response_full(url_temp)

    if None in config_manager.get_response_full():
        pytest.fail( "Null response received")
    #add response code
    expected_code = 200

    #check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    #print(actual_response_code)
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))

    return order


def test_get_order_byid(place_order,config_manager, generate_data):


    #precondition of adding entry of user is done by add_data fixture which returns user_data added
    #set http GET request using username
    config_manager.logger.info(f"The order entry added is {place_order.order_id}")
    config_manager.set_endpoint(f"store/order/{str(place_order.order_id)}")
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    config_manager.clear_http_request_body()
    config_manager.set_get_response_full(url_temp)

    #add response code
    expected_code = 200

    #check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))

    #check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')

    # check Response BODY contains newly added user details
    added_order_json = config_manager.get_response_full_json()
    print(added_order_json)
    assert added_order_json[RequestConstants.JSON_ID] == place_order.order_id


def test_place_order(place_order,config_manager,generate_data):

    # order added and response code checked in fixture: place_order

    #check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')



def test_delete_order(place_order,config_manager,generate_data):
    #precondition of adding entry of order is done by place order fixture which returns order added
    #set http DELETE request using pet id

    print(f"The order entry added is {place_order.order_id}")
    config_manager.set_endpoint(f"store/order/{str(place_order.order_id)}")
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    config_manager.set_delete_response_full(url_temp)

    # add response code
    expected_code = 200

    # check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))

    # check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')

    # check for deletion by trying to get the entry again
    config_manager.clear_http_request_body()
    config_manager.set_get_response_full(url_temp)

    # add response code
    expected_code = 404
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))

def test_delete_invalid_order(config_manager):
    """
    DELETE pet request using nonexisting username
    :param config_manager:
    :return:
    """


    order_id = -1
    config_manager.set_endpoint(f"store/order/{str(order_id)}")
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    config_manager.set_delete_response_full(url_temp)

    # add response code
    expected_code = 404

    # check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if  str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))


