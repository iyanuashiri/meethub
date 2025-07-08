from datetime import datetime

import factory

from meethub.comments.models import Comment
from meethub.accounts.factories import AccountFactory
from meethub.events.factories import EventFactory


class CommentFactory(factory.DjangoModelFactory):

    class Meta:
        model = Comment

    comment = factory.Faker('text')
    created_date = factory.LazyFunction(datetime.today())
    created_time = factory.LazyFunction(datetime.time(datetime.now()))
    event = factory.SubFactory(EventFactory)
    created_by = factory.SubFactory(AccountFactory)
    parent = factory.SubFactory('self')
