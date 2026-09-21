from django.urls import path

from main.views import create_education, create_experience,create_interest, delete_education, delete_experience, delete_interest, get_education_json, get_experience_json, get_interest_json, show_main, show_experience, show_education, show_interest, update_education, update_experience, update_interest
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
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/experience", get_experience_json, name="get_experience_json"),
    path("api/interest", get_interest_json, name="get_interest_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("interest/<uuid:interest_id>/delete/", delete_interest, name="delete_interest"),
    path("education/update/<uuid:education_id>/", update_education, name="update_education"),
    path("experience/update/<uuid:experience_id>/", update_experience, name="update_experience"),
    path("interest/update/<uuid:interest_id>/", update_interest, name="update_interest"),
    # path('', views.show_mahasiswa, name='show_mahasiswa'),
]
