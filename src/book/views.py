# from django.shortcuts import render
from book.models import Book

from django.http import HttpResponse

from faker import Faker


# Create your views here.r
def books_list(request):
    books = Book.objects.all()
    results = ''
    for book in books:
        results += f' id: {book.id} title: {book.title} author: {book.author},'
    return HttpResponse(results)


def books_create(request):
    fake = Faker()
    book = Book.objects.create(
        author=fake.name(),
        title=fake.paragraph(nb_sentences=1)
    )
    return HttpResponse(f"Book created!  |  Title: {book.title}  |  Author: {book.author}")
