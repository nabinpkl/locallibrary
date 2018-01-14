from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('books/',views.BookListView.as_view(),name='books'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name='book-detail'),
    path('mybooks/',views.LoanedBooksByUserListView.as_view(),name='my-borrowed'),
    path('borrowed/',views.LibrarianView.as_view(),name='borrowed'),
    path('book/<uuid:pk>/renew/',views.renew_book_librarian,name='renew-book-librarian')
]