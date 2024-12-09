# Petstore API Test

This project contains an automation test framework to validate https://petstore.swagger.io/#/ rest API  using pytest and request

## Prerequisites

- Python 3.x installed
- python pytest and request libraries
- Chrome/firefox web browser

## Setup

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:pip install -r requirements.txt
3. Activate the virtual environment: source .env/bin/activate  # On Windows: .\.env\Scripts\activate
4. Navigate to petstore_api_tests/tests folder to run the tests.
5. Update the paths in pytest.ini for test reports html and log files.


## Test Scenarios

The various test scenarios covering critical features of the web application are as below: 
### PET Endpoint
1.  Add pet data. 
2. Get pet data using pet_id.
3. Delete pet data using valid id.
4. Delete pet data using invalid id.
5. Update pet data.
5. Get ped data using invalid id.
6. Get pet data by status.
7. Get pet data by invalid status.
8. Upload pet image.

### STORE/ORDER Endpoint
1. place order.
2. Get order by order id
3. Delete order by order id.
4. Update order.
5. Delete invalid order id.

### USER Endpoint
1.  Add User/create user.
2. Login valid user.
3. Login invalid user.
4. Logout
5. Update user data
6. Get user by username. 
7. Delete user by invalid username. 
8. Delete user by username.
9. Create user with List.
10. Create user with invalid list.
11. Create user with empty list.

## Running all the Tests
 pytest 

## Running individual Test
 pytest <test_name.py>

- The test will be executed with the random test data generated. 
- Entire test results are store in reports/ directory