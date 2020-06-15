import pytest

import factory

from ..factories import AccountFactory


@pytest.mark.django_db
def test_account_create(account):
    account = account

    assert account.email == f'{account.first_name}.{account.last_name}@gmail.com'.lower()
    assert account.get_first_name() == account.first_name
    assert account.get_fullname() == f'{account.last_name} {account.first_name}'
    assert account.email_user('Hey you', 'Hello Iyanu') == 1


@pytest.mark.django_db
def test_account_label():
    account = AccountFactory()

    assert account._meta.get_field('first_name').verbose_name == 'first name'
    assert account._meta.get_field('last_name').verbose_name == 'last name'
    assert account._meta.get_field('email').verbose_name == 'email address'



@pytest.mark.django_db
def test_account_max_length():
    account = AccountFactory()

    assert account._meta.get_field('first_name').max_length == 200
    assert account._meta.get_field('last_name').max_length == 200
