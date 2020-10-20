from book.models import Book

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10_000):
            try:
                Book.objects.create(
                    author=fake.name(),
                    title=fake.paragraph(nb_sentences=1),
                )
            except ImportError:
                pass
