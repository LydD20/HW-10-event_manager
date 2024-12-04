# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment


## Issues Found

1. **Issue #1**: The first issue I found was with pytest errors, specifically found in the tests folder including test/test_schemas/test_user_schemas.py,  tests/test_email.py/test_send_markdown_email. I also found errors referencing “nickname”. To fix this issue, I had to add edit conftest and test_user_schemas to match inputs and also added the missing nickname field to test data and schemas. 

### Issue 1 Link: 

2. **Issue #2**: The second issue I found was with UserResponse when running pytest. To fix this issue, I updated test_user_schemas to include the needed uuid field, which helped ensure compatibility with the expected schema.

### Issue 2 Link: 

3. **Issue #3**: Another issue I found was in the functionality of the code. There was no default admin user so wanted to add admin credentials for testing with admin user as user in API. To fix this issue, a default admin user is automatically added to the postgres database with credentials defined in config.py. With the admin_email and admin_password found in config.py, we can authorize the current session in the fastAPI and perform all CRUD tests with ADMIN privileges.

### Issue 3 Link:

4. **Issue #4**: The fourth issue I found was with a 401 error, which was raised if the email is not verified. I decided to add a warning of verification step to code. To fix this, a new warning was added so that if a user without email verification tries to login, the API returns a 400 code. This code is a BadRequest HTTP response code and states “Complete email verification to login." so users know to fill in email verification to login.

### Issue 4 Link: 

5. **Issue #5**: The main and most time-consuming issue I found was in tests/test_api. When I ran pytest, I got errors with the following:
test_users_api.py::test_login_unverified_user - assert 401 == 400
test_users_api.py::test_create_user_access_denied
test_users_api.py::test_retrieve_user_access_denied
test_users_api.py::test_retrieve_user_access_allowed
test_users_api.py::test_retrieve_user_access_allowed
test_users_api.py::test_update_user_email_access_denied
test_users_api.py::test_update_user_email_access_allowed
test_users_api.py::test_delete_user
test_users_api.py::test_delete_user_does_not_exist
test_users_api.py::test_update_user_github
test_users_api.py::test_update_user_linkedin
test_users_api.py::test_list_users_as_admin
test_users_api.py::test_list_users_as_manager
Test_users_api.py::test_list_users_unauthorized

To fix this issue, I had to create a login function in conftest, import decode_token, and edit the jwt service file. I also fixed the docker.compose file by getting rid of the version and creating a .env file with secret token and admin information.  

### Issue #5 Link:

## Docker Image
<img width="831" alt="Screenshot 2024-12-03 at 5 02 45 PM" src="https://github.com/user-attachments/assets/74eba59d-4a9e-4371-95cf-bb29fa681ce6">

## Reflection
This assignment was definitely one of the toughest assignments I've had this semester across all of my classes. It required me to ensure my back-end logic and front-end interactions were properly connected and functioning as expected. The biggest takeaway from this assignment was definitely the importance of debugging and testing APIs. Without this element, results can be incorrect, and it can create confusion for front-end users. Although this is kind of known by every professional software engineer, this homework also reinforced just how collaborative Git is. It introduced me to GitHub issues and showed just how easy it is to communicate and collaborate with fellow developers or co-workers. 

From working with pytest to identify and handle certain components, such as the login_request_data located in the conftest.py, really demonstrated the value of systematic testing. These tests allowed me to verify tokens and ensure the application was ready for deployment in Docker. Docker was another key component of this assignment, as it required careful management of secret keys and SMTP keys to ensure seamless operation in a cloud environment. Overall, this assignment provided immense insight into the day-to-day work of a QA analyst/developer. It highlighted the strength of FastAPI applications, OOP Principles, and structure development methodologies. It greatly improved my technical capabilities and also left me with a bigger appreciation for the partnership that exists between an individual developer and a team collaboration in building robust applications.
