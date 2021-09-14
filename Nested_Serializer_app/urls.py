from django.urls import path

from Nested_Serializer_app import views

urlpatterns = [
    path('author_list/',views.AuthorListView.as_view()),
    path('author_detail/<int:pk>',views.AuthorDetailView.as_view()),

    path('book_list/',views.BookListView.as_view()),
    path('book_detail/<int:pk>',views.BookDetailView.as_view())
]