# Exercise: Testing REST APIs of petstore web application

## Objective

The goal of this exercise is to set up a automation test framework for rest API validation of https://petstore.swagger.io/#/

## Prerequisites
- Python 3.x installed
- python pytest and request libraries
- Chrome/firefox web browser

## Setup

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:pip install -r requirements.txt
3. Activate the virtual environment: source .env/bin/activate  # On Windows: .env\Scripts\activate
4. Navigate to petstore_api_tests/tests folder to run the tests.
5. Update the paths in pytest.ini for test reports html and log files.

## Test Coverage

### 1. Pet Endpoint
#### Test: test_get_pet_by_id
- **Objective:** Create GET API request with appropriate payload and send the request to  using pet id.
- **Expected Result:** Successful request response code 200 with expected pet data.

#### Test: test_add_pet
- **Objective:** Create POST API request with appropriate payload and send the request to  add pet data.
- **Expected Result:** Successful request response code 200 with expected pet data.

#### Test: test_update_pet
- **Objective:** Create PUT API request with appropriate payload and send the request to  update pet data.
- **Expected Result:** Successful request response code 200 with expected pet data.

#### Test: test_delete_pet
- **Objective:** Create DELETE API request with appropriate payload and send the request to  delete pet data using pet id.
- **Expected Result:** Successful request response code 200 with expected pet data.

#### Test:test_get_by_status
- **Objective:** Create GET API request with appropriate payload and send the request to  get pet data by Status.
- **Expected Result:** Successful request response code 200 with expected pet status.

#### Test:test_get_invalid_status
- **Objective:** Create GET API request with appropriate payload having invalid status and send the request to  get pet data by status.
- **Expected Result:** Error request response code 400.

#### Test:test_delete_invalid_petid
- **Objective:** Create DELETE API request  with appropriate payload having invalid pet id and send the request to  delete pet data using pet id.
- **Expected Result:** Error request response code 404.

#### Test:test_upload_pet_image
- **Objective:** Create POST upload image API request  with appropriate payload and image file and send the request to  upload pet photo.
- **Expected Result:** Successful upload with success response code 200.

### 2. User Endpoint
#### Test: test_get_user_name
- **Objective:** Create GET API request with appropriate payload and send the request to  get user dat aby username.
- **Expected Result:** Successful request response code 200 with expected user data.

#### Test: test_add_user
- **Objective:** Create POST API request with appropriate payload and send the request to  add user data.
- **Expected Result:** Successful request response code 200 with expected user data.

#### Test: test_update_user
- **Objective:** Create PUT API request with appropriate payload and send the request to  update user data.
- **Expected Result:** Successful request response code 200 with expected user data.

#### Test: test_delete_user
- **Objective:** Create DELETE API request with appropriate payload and send the request to  delete user data using username.
- **Expected Result:** Successful request response code 200 with expected user data.

#### Test:test_user_login
- **Objective:** Create GET LOGIN API request with appropriate payload and send the request to login with uname and password.
- **Expected Result:** Successful request response code 200 with expected user data.

#### Test:test_login_invalid_user
- **Objective:** Create GET LOGIN API request with appropriate payload having invalid username, password and send the request to  login.
- **Expected Result:** Error request response code 404.

#### Test:test_delete_invalid_user
- **Objective:** Create DELETE API with appropriate payload having invalid username and send the request to  delete user data.
- **Expected Result:** Error request response code 404.

#### Test:test_user_logout
- **Objective:** Create GET LOGOUT API request  with appropriate payload  send the request to  logout the user session.
- **Expected Result:** Successful logout with success response code 200.

#### Test:test_create_users_with_list
- **Objective:** Create POST create user API request  with appropriate payload with users list send the request to  create the user session.
- **Expected Result:** Successful creation of users with success response code 200.

#### Test:test_create_users_invalid_data
- **Objective:** Create POST create user API request with appropriate payload with users list invalid fields send the request to  create the user session.
- **Expected Result:** Error response code 400.

#### Test:test_create_users_empty_data
- **Objective:**  Create POST create user API request with appropriate payload with users list empty send the request to  create the user session.
- **Expected Result:** Successful user creation with success response code 200.

### 3. Store Endpoint 
#### Test: test_get_order_byid
- **Objective:** Create GET API request with appropriate payload and send the request to  get order data by id.
- **Expected Result:** Successful request response code 200 with expected order data.

#### Test: test_place_order
- **Objective:** Create POST API request with appropriate payload and send the request to place order.
- **Expected Result:** Successful request response code 200 with expected order data.

#### Test:test_delete_order
- **Objective:** Create DELETE  API request with appropriate payload and send the request to delete an order by ID.
- **Expected Result:** Successful request response code 200 with expected user data.

#### Test:test_delete_invalid_order
- **Objective:** Create DELETE  API request with appropriate payload having invalid order id and send the request to delete.
- **Expected Result:** Error request response code 404.


## Analyzing Test Results

### Review Test Output
- **Check the Status Code:**
Ensure that the status code returned by the API matches the expected result (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).
Example: If the test expected 200 OK but received 500 Internal Server Error, there’s likely an issue with the server-side logic or configuration.

- **Inspect Response Body:**
Verify if the response body contains the expected data or error messages.

- **Verify Headers:**
Ensure that necessary headers (e.g., Content-Type, Authorization) are correctly set in the request and that the response headers match expectations.
Example: Missing Authorization headers might result in authentication errors.

### Review Test Logs
- **Check Logs for Errors:**
Examine logs for detailed error messages or stack traces. This often provides insights into what went wrong.

- **Compare with Expected Behavior:**
Compare the actual log output with the expected behavior. Look for discrepancies or errors that deviate from the expected outcomes.

## Troubleshooting
- Identify common issues like authentication errors, invalid payloads, server errors, and endpoint problems.
- Provide detailed information in the bug report for accurate diagnosis and resolution.

## Submission
- **After completing the exercise:** Ensure that all tests pass or document any failed tests with details on the issues encountered.
Submit a summary report of your findings, including any problems or observations.

## Additional Notes
- **Environment:** Make sure your test environment mirrors the application’s expected configuration as closely as possible.
- **Support:** Reach out if you encounter any issues or have questions regarding the test setup or execution. [mvmeghana@gmail.com](mvmeghana@gmail.com)

## Running all the Tests to log into console
 pytest -v

## Running all the Tests with html report 
pytest --html=/reports/report.html
Open report.html in your web browser to view a detailed report of the test results.

## Running individual Test
 pytest <test_name.py>

