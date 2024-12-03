from builtins import str
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest
import uuid

# Tests for UserBase
def test_user_base_valid(user_base_data):
    # Test if nickname provided
    user_base_data['nickname'] = 'j_doe'
    user = UserBase(**user_base_data)
    assert user.nickname == 'j_doe'
    assert user.email == user_base_data["email"]

    # Test if nickname not provided
    user_base_data.pop('nickname', None)
    user= UserBase(**user_base_data)
    assert user.nickname is None
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    # Test if nickname not provided 
    user_create_data['nickname'] = 'j_doe'
    user = UserCreate(**user_create_data)
    assert user.nickname == 'j_doe'
    assert user.password == user_create_data["password"]

    # Test if nickname not provided
    user_create_data.pop('nickname', None)
    user = UserCreate(**user_create_data)
    assert user.nickname is None
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    # Test if first name provided
    user_update_data['first_name'] = 'John'
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == "John"

    # Test if first name not provided
    user_update_data.pop('first_name', None)
    user_update = UserUpdate(**user_update_data)
    assert user_update.first_name is None

def test_user_response_valid(user_response_data):
    # Create a fixed UUID for the test
    fixed_uuid = uuid.uuid4()
    user_response_data["id"] = fixed_uuid  # Assign the fixed UUID directly

    # Create the UserResponse instance
    user = UserResponse(**user_response_data)

    # Assertions
    assert user.id == fixed_uuid  # Compare with the fixed UUID
    assert user.email == user_response_data["email"]
    assert user.nickname == user_response_data.get("nickname")


# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    # Checks that email is included in data
    login_request_data = {
        "email": "john.doe@example.com",
        "password": "Secure*1234"
    }
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Tests for UserBase
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        user = UserBase(**user_base_data_invalid)
    
    assert "value is not a valid email address" in str(exc_info.value)
    assert "john.doe.example.com" in str(exc_info.value)