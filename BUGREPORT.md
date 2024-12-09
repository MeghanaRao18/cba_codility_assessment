# Bug Report

## Summary
Total 3 tests in the `tests/` folder are failing due to various issues. The failures affect the functionality of the application in different ways, including incorrect outputs, exceptions, and performance problems.

## Affected Tests

### 1. Test: **`test_pet_endpoints.py::test_get_invalid_status `**

#### **Description**
This test fails when attempting to  send GET request for pet data using invalid status

#### **Steps to Reproduce**
1.  Send a GET request : https://petstore.swagger.io/v2/pet/findByStatus?status=invalid 
2.  Accepted status are : available, sold , not available and pending 
3. With the above invalid status the expectation is to receive error response code 400 : Invalid status value


#### **Expected Results**
The API request should return status code : 400

#### **Actual Results**
The API accepted the invalid request and returned  Success status code :200 

#### **Error Logs**
FAILED test_pet_endpoints.py::test_get_invalid_status - Failed: ***ERROR: unexpected error response code received: 200.         Expected : 400

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: Microsoft Windows 11
- **Testing Tool** : pytest, requests library
## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Critical
- **Priority**: High
- **Testing Tool** : pytest, requests library

**Reported By**: [Meghana Rao]  
**Date**: [2024-12-09]

---

### 2. Test: **` test_user_endpoint.py::test_login_invalid_user `**

#### **Description**
This test validates the negative scenario when non existing / invalid user tries to login 

#### **Steps to Reproduce**

Send a GET LOGIN request as https://petstore.swagger.io/v2/user/login?username=invalid&password=invalid 


#### **Expected Results**
The GET request response code is expected to  be user does not exist code: 404

#### **Actual Results**
The GET  request response code returns 200 success 

#### **Error Logs**
 FAILED test_user_endpoints.py::test_login_invalid_user - Failed: ***ERROR: Following unexpected error response code received: 200.Expected: 404

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: Microsoft Windows 11

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Major
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-12-09]

---
### 3. Test: **` test_user_endpoint.py::test_create_users_invalid_data `**

#### **Description**
This test validates the negative scenario when invalid user list is pasaed to create user API 

#### **Steps to Reproduce**

Send a POST Create user request as https://petstore.swagger.io/v2/user/createWithList with invalid user list


#### **Expected Results**
The POST request response code is expected to  invalid request  code: 400

#### **Actual Results**
The POST  request response code returns 200 success 

#### **Error Logs**
FAILED test_user_endpoints.py::test_create_users_invalid_data - Failed: ***ERROR: Following unexpected error response code received: 200Expected :400

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: Microsoft Windows 11

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Major
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-12-09]

---