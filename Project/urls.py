from dateutil.parser import parser
from django.contrib import admin
from django.urls import path

from filmApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloApi.as_view()),
    path('aktyorlar/', AktyorlarApi.as_view()),
    path('aktyorlar/<int:pk>/', AktyorApi.as_view()),
    path('tariflar/',TarifApi.as_view()),
    path('tarif/<int:pk>/',TarifEditApi.as_view()),
    path('tariflar/<int:pk>/delete/',TarifDeleteApi.as_view()),
]
