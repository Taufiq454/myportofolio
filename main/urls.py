from django.urls import path

from main.views import show_main, show_experience, show_education, show_interest
from . import views

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("intrest/", show_interest, name="show_interest"),
    # path('', views.show_mahasiswa, name='show_mahasiswa'),
]
