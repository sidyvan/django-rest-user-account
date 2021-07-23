from django.contrib import admin
from django.urls import path

from account.api.viewsets import UserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserView.as_view()),

]
