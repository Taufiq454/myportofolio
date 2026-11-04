from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("experience/", api_views.experience_list, name="experience-list"),
    path("interest/", api_views.interest_list, name="interest-list"),
    path("education/", api_views.education_list, name="education-list"),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("education/<uuid:education_id>/", api_views.education_detail, name="education-detail"),
    path("interest/<uuid:interest_id>/", api_views.interest_detail, name="interest-detail"),
    path("education/<uuid:education_id>/star/", api_views.education_star, name="education-star"),
    path("experience/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),
    path("interest/<uuid:interest_id>/star/", api_views.interest_star, name="interest-star"),

]