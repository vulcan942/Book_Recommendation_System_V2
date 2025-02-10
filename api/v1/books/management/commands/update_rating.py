from django.core.management.base import BaseCommand
from api.v1.books.models import Book


class Command(BaseCommand):
    help = "Set book rating to 2.5 if it is 0 or NULL"

    def handle(self, *args, **kwargs):
        updated_count = Book.objects.filter(rating__lte=0).update(rating=2.5)

        if updated_count == 0:
            self.stdout.write(self.style.SUCCESS("No books needed updating."))
        else:
            self.stdout.write(
                self.style.SUCCESS(f"Updated {updated_count} books to a rating of 2.5")
            )
