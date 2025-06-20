from datetime import datetime
from django.db import models
from author.models import Author
from django.utils import timezone

class Book(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField(Author, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    # Нові поля
    publication_year = models.IntegerField(null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)

    def __str__(self):
        authors_ids = [author.id for author in self.authors.all()]
        return f"'id': {self.id}, 'name': '{self.name}', 'description': '{self.description}', 'count': {self.count}, 'authors': {authors_ids}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(book_id):
        book = Book.get_by_id(book_id)
        if book:
            book.delete()
            return True
        return False

    @staticmethod
    def create(name, description, count=10, authors=None, publication_year=None, issue_date=None):
        if len(name) > 128:
            return None
        book = Book(name=name, description=description, count=count,
                    publication_year=publication_year, issue_date=issue_date)
        book.save()
        if authors:
            book.authors.set(authors)
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.id for author in self.authors.all()],
            'publication_year': self.publication_year,
            'issue_date': self.issue_date,
        }

    def update(self, name=None, description=None, count=None, publication_year=None, issue_date=None):
        if name is not None:
            if len(name) <= 128:
                self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if publication_year is not None:
            self.publication_year = publication_year
        if issue_date is not None:
            self.issue_date = issue_date
        self.save()

    def add_authors(self, authors):
        for author in authors:
            self.authors.add(author)
        self.save()

    def remove_authors(self, authors):
        for author in authors:
            self.authors.remove(author)
        self.save()

    @staticmethod
    def get_all():
        return list(Book.objects.all())
