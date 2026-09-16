from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from main.forms import EducationForm
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
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education_list = [education.object for education in educations]
    institution_query = request.GET.get("institution", "").strip()
    
    if institution_query:
        education_list = [
            edu for edu in education_list
            if institution_query.lower() in edu.degree.lower()
            or institution_query.lower() in edu.institution.lower()
        ]
    
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "education_list": education_list,
        "institution_query": institution_query,
        
    }
    return render(request, "education.html", context)

def show_interest(request):
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "interest_list": Interest.objects.all(),
    }
    return render(request, "interest.html", context)


def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    education = Education.objects.all()

    if institution_query:
        education = Education.objects.filter(institution__icontains=institution_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")