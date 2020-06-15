from pytest_factoryboy import register
import pytest
from rest_framework.test import APIClient

from accounts.factories import AccountFactory


register(AccountFactory, 'account')


@pytest.fixture
def authenticated_user(client, account):
    """Create an authenticated user for a test"""
    # user = G(User, email='test@gmail.com')
    account.email = 'test@gmail.com'
    account.set_password('my_password123')
    account.save()
    client.login(email='test@gmail.com', password='my_password123')
    return account


@pytest.fixture
def authenticated():
    client = APIClient()
    client.post('http://127.0.0.1:8000/auth/users/', data={"first_name": "iyanu",
                                                           "last_name": "ajao",
                                                           "email": "iyanu@example.com",
                                                           "password": "decagon1234"})

    response = client.post('http://127.0.0.1:8000/auth/token/login/', data={"password": "decagon1234",
                                                                            "email": "iyanu@example.com"})
    auth_token = response.data['auth_token']
    client.credentials(HTTP_AUTHORIZATION='Token ' + auth_token)
    return client
