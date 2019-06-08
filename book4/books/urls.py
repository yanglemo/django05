from django.conf.urls import url

from books.views import index,HomeView,detail
from django.conf import settings
urlpatterns=[
    url(r'index/$',index),
    url(r'home/$',HomeView.as_view()),
    url(r'detail/$',detail)
]

