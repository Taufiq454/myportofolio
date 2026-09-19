from django.urls import path

from main.views import create_education, create_experience,create_interest, delete_education, get_education_json, show_main, show_experience, show_education, show_interest
from . import views

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("interest/", show_interest, name="show_interest"),
    path("education/add/", create_education, name="create_education"),
    path("experience/add/", create_experience, name="create_experience"),
    path("interest/add/", create_interest, name="create_interest"),
    path("api/projects/", get_education_json, name="get_projects_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    # path('', views.show_mahasiswa, name='show_mahasiswa'),
]
