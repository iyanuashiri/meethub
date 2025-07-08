from datetime import datetime

import factory

from meethub.accounts.models import Account


class AccountFactory(factory.DjangoModelFactory):

    class Meta:
        model = Account

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda a: f'{a.first_name}.{a.last_name}@gmail.com'.lower())
    date_joined = factory.LazyFunction(datetime.now)
    is_staff = False
    is_active = True
