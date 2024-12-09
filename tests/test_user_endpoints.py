"""
Module containing tests to validate user end point
"""
import pytest
from socks import PRINTABLE_PROXY_TYPES

from config.request_config_manager import RequestConfigManager
from config.request_constants import RequestConstants
from tests.test_pet_endpoints import add_data
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
def add_user(config_manager,generate_data):
    config_manager.set_http_content_type(HEADERS)

    #set endpoint to first add user  and then get it using same id
    config_manager.set_endpoint('user')

    #get the data to upload
    add_user = generate_data.generate_test_user_data()
    config_manager.set_http_request_body_with_user_details(add_user)
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


    return add_user


def test_get_user_name(add_user,config_manager, generate_data):


    #precondition of adding entry of user is done by add_data fixture which returns user_data added
    #set http GET request using username
    config_manager.logger.info(f"The username entry added is {add_user.username}")
    config_manager.set_endpoint(f"user/{str(add_user.username)}")
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
    added_user_json = config_manager.get_response_full_json()
    print(added_user_json)
    assert added_user_json[RequestConstants.JSON_USER_NAME] == add_user.username


def test_add_user(add_user,config_manager,generate_data):

    # user added and response code checked in fixture: add_user

    #check response HEADER content type
    config_manager.set_expected_response_content_type(HEADERS)
    actual_response_content_type = config_manager.get_response_full_content_type()
    if HEADERS not in actual_response_content_type:
        pytest.fail( '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)

    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')



def test_update_user(add_user,config_manager,generate_data):

    #set header content type
    config_manager.set_http_content_type(HEADERS)

    # entry added in the fixture add_data
    config_manager.set_endpoint(f"user/{str(add_user.username)}")
    #now using this user name update the status
    add_user.user_status = 1
    config_manager.set_http_request_body_with_user_details(add_user)

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

    # check by getting the user  date to see if new status value is updated
    config_manager.set_endpoint(f"user/{str(add_user.username)}")
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    config_manager.clear_http_request_body()
    config_manager.set_get_response_full(url_temp)
    expected_code = 200
    #check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code))
    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')

    # check Response BODY contains newly added user details
    added_user_json = config_manager.get_response_full_json()
    print(added_user_json)
    assert added_user_json[RequestConstants.JSON_USER_STATUS] == add_user.user_status


def test_delete_user(add_user,config_manager,generate_data):
    #precondition of adding entry of pet is done by add_data fixture which returns pet_data added
    #set http DELETE request using pet id

    print(f"The username entry added is {add_user.username}")
    config_manager.set_endpoint(f"user/{str(add_user.username)}")
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

def test_user_login(add_user,config_manager):
    """
    Scenario Outline: GET pet request using pet status
    :param config_manager:
    :param generate_data:
    :return:
    """


    config_manager.set_http_accept_type(HEADERS)

    config_manager.set_endpoint("user/login")

    #use the already added user details
    config_manager.set_http_request_url_query_param(add_user)
    # GET Login HTTP request is raised
    config_manager.set_http_request_body_with_user_details(add_user)
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    config_manager.clear_http_request_body()
    config_manager.set_get_user_login_response_full(url_temp)
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

    response_text = config_manager.get_response_full_text()
    try:
        response = tuple(response_text.split(':'))
        session_number = response[1]
        print('session number : ' + session_number)
    except:
        print('User is not logged')

def test_delete_invalid_user(config_manager):
    """
    DELETE pet request using nonexisting username
    :param config_manager:
    :return:
    """


    username = -1
    config_manager.set_endpoint(f"user/{str(username)}")
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

def test_login_invalid_user(config_manager,add_user):
    config_manager.set_http_accept_type(HEADERS)

    config_manager.set_endpoint("user/login")
    add_user.username = "invalid"
    add_user.password = "invalid"
    config_manager.set_http_request_url_query_param(add_user)
    # GET Login HTTP request is raised
    config_manager.set_http_request_body_with_user_details(add_user)
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
    #config_manager.clear_http_request_body()
    config_manager.set_get_user_login_response_full(url_temp)
    print (config_manager.get_http_request_body())

    # add response code user does not exist
    expected_code = 404
    # check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    print (actual_response_code)
    if  str(actual_response_code) not in str(expected_code):
        pytest.fail( f'***ERROR: Following unexpected error response code received: {str(actual_response_code)}.'
                     f'Expected: {str(expected_code)}')

def test_user_logout(config_manager):

    config_manager.set_http_content_type(HEADERS)

    config_manager.set_endpoint("user/logout")


    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()
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


def test_create_user_with_list(config_manager,generate_data):

    """
    Test to validate POST adding users with a list of users
    """
    config_manager.set_http_content_type(HEADERS)

    #set endpoint to first add user  and then get it using same id
    config_manager.set_endpoint('user/createWithList')


    #get the data to upload
    add_user = generate_data.generate_test_user_data()
    config_manager.set_http_request_body_with_user_list(add_user)
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


    # check http response body is not null
    if None in config_manager.get_response_full():
        pytest.fail( '***ERROR:  Null or none response body received')


def test_create_users_invalid_data(config_manager,generate_data):

    """
    Test to validate POST with invalid user field list
    """

    config_manager.set_http_content_type(HEADERS)

    #set endpoint to first add user  and then get it using same id
    config_manager.set_endpoint('user/createWithList')


    #get the data to upload
    add_user = generate_data.generate_test_user_data()
    add_user.user_list = [{"username":""}] #Missing fields
    config_manager.set_http_request_body_with_user_list(add_user)
    print(config_manager.get_http_request_body())

    #POST Http request raised
    url_temp = config_manager.get_basic_url()
    url_temp += config_manager.get_endpoint()

    config_manager.set_post_response_full(url_temp)

    if None in config_manager.get_response_full():
        pytest.fail( "Null response received")
    #add response code
    expected_code = 400

        #check http response code
    config_manager.set_expected_response_code(expected_code)
    actual_response_code = config_manager.get_response_full_status_code()
    #print(actual_response_code)
    if str(actual_response_code) not in str(expected_code):
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)+\
                    'Expected :'+str(expected_code))


def test_create_users_empty_data(config_manager,generate_data):

    """
    Test to validate POST with empty user  list
    """

    config_manager.set_http_content_type(HEADERS)

    #set endpoint to first add user  and then get it using same id
    config_manager.set_endpoint('user/createWithList')


    #get the data to upload
    add_user = generate_data.generate_test_user_data()
    add_user.user_list = [] #empty list 
    config_manager.set_http_request_body_with_user_list(add_user)
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
        pytest.fail( '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)+\
                    'Expected : '+str(expected_code))