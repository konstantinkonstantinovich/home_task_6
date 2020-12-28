from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arg', nargs='+', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        num = options['arg'][0]
        for _ in range(num):
            user = fake.name().replace(' ', '_').replace("'", '')
            email_s = fake.ascii_email()
            pass_word = fake.password()

        User.objects.create_user(username=user, email=email_s,
                                 password=pass_word)
