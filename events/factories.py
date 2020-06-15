from datetime import datetime

import factory

from accounts.factories import AccountFactory
from .models import Event, Category


class CategoryFactory(factory.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Faker('name')
    description = factory.Faker('sentence')


class EventFactory(factory.DjangoModelFactory):

    class Meta:
        model = Event

    name = factory.Faker('name')
    details = factory.Faker('sentence')
    venue = factory.Faker('address')
    date = factory.LazyFunction(datetime.today())
    time = factory.LazyFunction(datetime.time(datetime.now()))
    category = factory.SubFactory(CategoryFactory)
    creator = factory.SubFactory(AccountFactory)
    num_of_attendees = 1

    @factory.post_generation
    def attendees(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for attendee in extracted:
                self.attendees.add(attendee)




