from week5_day1.src.fixture_login import UserAuth
import pytest
@pytest.fixture
def user_auth():
    return UserAuth()

@pytest.fixture(
    params=[("user1", "password123", "email@example.com"),
            ("user2", "password123", "user2@example.com")]
)
def register_user(request, user_auth):
    username, password, email = request.param
    user_auth.register(username, password, email)
    return user_auth, username, password

class TestUserAuth:

    def test_login(self, register_user):
        '''
        测试注册
        '''
        user_auth, username, password = register_user
        assert user_auth.login(username, password) == "Login successful"

    def test_change_password(self, register_user):
        '''
        测试更改密码
        '''
        user_auth, username, password = register_user
        user_auth.change_password(username, password, "newpassword123")
        assert user_auth.login(username, "newpassword123") == "Login successful"

    def test_invalid_login(self, user_auth):
        '''
        测试注册异常场景
        '''
        with pytest.raises(ValueError):
            user_auth.login("noexistuser", "password")