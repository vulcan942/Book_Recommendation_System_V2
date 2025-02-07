import json
import os
from django.core.management.base import BaseCommand
from api.v1.books.models import Author, Book, Genre  # Updated import


class Command(BaseCommand):
    help = "Populates the database with book data from a JSON file"

    def handle(self, *args, **kwargs):
        # Get the absolute path of the project root
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        )
        file_path = os.path.join(base_dir, "books.json")

        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR(f"Error: File not found at {file_path}"))
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for genre_name, books in data.items():
                try:
                    genre, _ = Genre.objects.get_or_create(name=genre_name)
                except Exception as e:
                    self.stderr.write(
                        self.style.ERROR(f"Error creating genre '{genre_name}': {e}")
                    )
                    continue

                for entry in books:
                    try:
                        title = entry.get("title", "").strip()
                        if not title:
                            raise ValueError("Missing or empty title")

                        author_name = entry.get("author", "").strip()
                        if not author_name:
                            raise ValueError(
                                f"Missing or empty author for book '{title}'"
                            )

                        description = entry.get("description", "").strip()
                        if not description:
                            self.stderr.write(
                                self.style.WARNING(
                                    f"Warning: Missing description for book '{title}'"
                                )
                            )

                        image_url = entry.get("image", "").strip()
                        if not image_url:
                            self.stderr.write(
                                self.style.WARNING(
                                    f"Warning: Missing image URL for book '{title}'"
                                )
                            )
                        rating = entry.get("rating", 0.0)

                        author, _ = Author.objects.get_or_create(name=author_name)
                        book, created = Book.objects.get_or_create(
                            title=title,
                            author=author,
                            description=description,
                            rating=(
                                0.0
                                if not isinstance(rating, (int, float))
                                else float(rating)
                            ),
                            image_url=image_url,
                        )

                        if created:
                            book.genres.add(genre)
                            self.stdout.write(
                                self.style.SUCCESS(f"Added book: {title}")
                            )

                    except Exception as e:
                        self.stderr.write(
                            self.style.ERROR(
                                f"Error processing book '{entry.get('title', 'Unknown Title')}': {e}"
                            )
                        )

            self.stdout.write(self.style.SUCCESS("Database population complete."))

        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f"JSON Decode Error: {e}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Unexpected Error: {e}"))
