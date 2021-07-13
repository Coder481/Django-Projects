from django.urls import include
from BRMapp import views
from django.conf.urls import url
urlpatterns=[
    url('view-books',views.viewBooks),
    url('edit-book',views.editBook),
    url('delete-book',views.deleteBook),
    url('new-book',views.newBook),
    url('add',views.add),
    url('search',views.search),
    url('edit',views.edit),
    url('search-book',views.searchBook),
]
