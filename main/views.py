from django.shortcuts import render

# Create your views here.
from main.models import Experience, Mahasiswa, Education, Interest


def show_main(request):
    context = {
        "name": "Muhammad Taufiq Ramadhan",
        "username": "Taufiq",
        "npm": "2506536143",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia. Learning, building, and figuring things out along the way."
        ),
        "mahasiswa" : Mahasiswa.objects.all()
    }
    
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_interest(request):
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "interest_list": Interest.objects.all(),
    }
    return render(request, "interest.html", context)
# from main.models import Mahasiswa

# def show_mahasiswa(request):
    

#     return render(request, 'index.html', {
#         'mahasiswa': mahasiswa
#     })
