"""
Module covering pet data end point test cases
"""

import requests,os,re
import pytest
from socks import PRINTABLE_PROXY_TYPES


from  config.request_config_manager import RequestConfigManager
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
def add_data(config_manager,generate_data):
    config_manager.set_http_content_type(HEADERS)

    #set endpoint to first add pet  and then get it using same id
    config_manager.set_endpoint('pet')

    #get the data to upload
    pet_data = generate_data.generate_test_pet_data(status=RequestConstants.JSON_STATUS_AVAILABLE)
    config_manager.set_http_request_body_with_pet_details(pet_data)
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
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))

    # check Response BODY contains newly added pet details
    added_pet_json = config_manager.get_response_full_json()
    assert added_pet_json[RequestConstants.JSON_ID] == pet_data.pet_id
    return pet_data


def test_get_pet_by_id(add_data,config_manager, generate_data):


    #precondition of adding entry of pet is done by add_data fixture which returns pet_data added
    #set http GET request using pet id
    config_manager.logger.info(f"The pet_id entry added is {add_data.pet_id}")
    config_manager.set_endpoint(f"pet/{str(add_data.pet_id)}")
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

    # check Response BODY contains newly added pet details
    added_pet_json = config_manager.get_response_full_json()

    assert added_pet_json[RequestConstants.JSON_STATUS] == add_data.status
    assert added_pet_json[RequestConstants.JSON_NAME] == add_data.name
    assert added_pet_json[RequestConstants.JSON_ID] == add_data.pet_id
    assert added_pet_json[RequestConstants.JSON_PHOTOURLS] == add_data.photourls

def test_add_pet(add_data,config_manager,generate_data):

    # pet added and response code checked in fixture: add_data

    #check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')

    # check Response BODY contains newly added pet details
    added_pet_json = config_manager.get_response_full_json()

    assert added_pet_json[RequestConstants.JSON_STATUS] == add_data.status
    assert added_pet_json[RequestConstants.JSON_NAME] == add_data.name
    assert added_pet_json[RequestConstants.JSON_ID] == add_data.pet_id
    assert added_pet_json[RequestConstants.JSON_PHOTOURLS] == add_data.photourls


def test_update_pet(add_data,config_manager,generate_data):

    #set header content type
    config_manager.set_http_content_type(HEADERS)

    # entry added in the fixture add_data

    #now using this pet_id update the status
    add_data.status = RequestConstants.JSON_STATUS_SOLD
    config_manager.set_http_request_body_with_pet_details(add_data)

    #PUT Http request raised
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()

    config_manager.set_put_response_full(url_temp)
    if None in config_manager.get_response_full():
        pytest.fail( "Null response received")

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

    # check Response BODY contains newly added pet status
    added_pet_json = config_manager.get_response_full_json()

    assert added_pet_json[RequestConstants.JSON_STATUS] == add_data.status


def test_delete_pet(add_data,config_manager,generate_data):
    #precondition of adding entry of pet is done by add_data fixture which returns pet_data added
    #set http DELETE request using pet id

    print(f"The pet_id entry added is {add_data.pet_id}")
    config_manager.set_endpoint(f"pet/{str(add_data.pet_id)}")
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

def test_get_by_status(config_manager):
    """
    Scenario Outline: GET pet request using pet status
    :param config_manager:
    :param generate_data:
    :return:
    """
    status = RequestConstants.JSON_STATUS_AVAILABLE

    config_manager.set_http_content_type(HEADERS)

    # GET FINDBYSTATUS api pet request endpoint is set as "pet/findByStatus"
    config_manager.set_endpoint("pet/findByStatus" +RequestConstants.JSON_REQUEST_STATUS)

    # GET FINDBYSTATUS HTTP request is raised
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint() + str(status)
    config_manager.clear_http_request_body()
    config_manager.set_get_response_full(url_temp)
    print (url_temp)

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

    # check Response BODY contains newly added pet details
    added_pet_json = config_manager.get_response_full_json()
    #print(added_pet_json)

    #assert added_pet_json[RequestConstants.JSON_STATUS] == status

def test_get_invalid_status(config_manager):
    """
    Scenario: GET pet request using invalid pet status
    :param config_manager:
    :return:
    """
    config_manager.set_http_content_type(HEADERS)

    # GET FINDBYSTATUS api pet request endpoint is set as "pet/findByStatus"
    config_manager.set_endpoint("pet/findByStatus" +RequestConstants.JSON_REQUEST_STATUS)

    # GET FINDBYSTATUS HTTP request is raised
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint() + str("invalid")
    config_manager.clear_http_request_body()
    config_manager.set_get_response_full(url_temp)
    print (url_temp)

    # add response code
    expected_code = 400

    # check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( f'***ERROR: unexpected error response code received: {str(actual_response_code)}. \
        Expected : {str(expected_code)}')

    # check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http text have invalid status value

    expected_response_text = "Invalid status value"
    actual_response_text = config_manager.get_response_full_text()
    if actual_response_text not in expected_response_text:
        pytest.fail( '***ERROR: Following unexpected error response text received: ' + actual_response_text)

def test_delete_invalid_petid(config_manager):
    """
    DELETE pet request using nonexisting pet ID
    :param config_manager:
    :return:
    """
    pet_id = -1
    config_manager.set_endpoint(f"pet/{str(pet_id)}")
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

def test_upload_pet_image(add_data,config_manager,generate_data):
    """
    Scenario: UPLOAD pet photo/image POST request using pet ID
    :param add_data:
    :param config_manager:
    :param generate_data:
    :return:
    """

    print(f"The pet_id entry added is {add_data.pet_id}")
    # POST UPLOADIMAGE api pet request endpoint is set as "pet"
    config_manager.set_endpoint("pet"+ "/" + str(add_data.pet_id) + "/" + RequestConstants.JSON_UPLOAD_IMAGE)
    current_dir = os.path.dirname(__file__)
    image_path = os.path.abspath(os.path.join(current_dir, "..", "config", "img1.jpg"))
    assert os.path.exists(image_path)
    add_data.photo =image_path
    config_manager.set_http_request_body_with_pet_photo(add_data)
    #add_data.photourls = [r"https://media.istockphoto.com/id/1359095204/photo/beagle-puppy-sitting-on-chair.jpg?s=1024x1024&w=is&k=20&c=qjXIcCj8jW35JetE77ZkWTJFeSexvR8jgsuf3b7JrPA="]
    config_manager.set_http_request_body_with_pet_details(add_data)
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    config_manager.set_post_uploadimage_response_full(url_temp)
    print (url_temp)
    # add response code
    expected_code = 200

    # check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if not ( str(actual_response_code) == str(expected_code)):
        pytest.fail(f"***ERROR:  unexpected error response code received {str(actual_response_code)}. \
        Expected: {str(expected_code)}")


    # check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')
    # check Response BODY contains newly added pet details
    response_data = config_manager.get_response_full_json()
    assert "File uploaded to" in response_data["message"]  # Confirm file path in the message
    assert "bytes" in response_data["message"]  # Confirm file size in the message
