import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied        

# Create your views here.
from main.forms import EducationForm, ExperienceForm, InterestForm
from main.models import Experience, Mahasiswa, Education, Interest


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Muhammad Taufiq Ramadhan",
        "username": "Taufiq",
        "npm": "2506536143",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia. Learning, building, and figuring things out along the way."
        ),
        "last_login": last_login,
        "mahasiswa" : Mahasiswa.objects.all()
    }
    
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)
    
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience_list = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "experience_list": experience_list,
        "title_query": title_query
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
    json_response = get_interest_json(request)
    
    interests = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    interest_list = [interest.object for interest in interests]
    nama_query = request.GET.get("nama", "").strip()
    
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "interest_list": interest_list,
        "nama_query": nama_query
    }
    return render(request, "interest.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    
    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")    
def create_interest(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = InterestForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Minat baru berhasil ditambahkan!")
        return redirect("main:show_interest")
    
    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
    }
    return render(request, "interest_form.html", context)

def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    education = Education.objects.all()

    if institution_query:
        education = Education.objects.filter(institution__icontains=institution_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()
    
    if title_query:
        experience = Experience.objects.filter(title_icontains=title_query)
        
    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def get_interest_json(request):
    nama_query = request.GET.get("nama", "").strip()
    interest = Interest.objects.all()
    
    if nama_query:
        interest = Interest.objects.filter(nama_icontains=nama_query)
        
    interest_json = serializers.serialize("json", interest)
    return HttpResponse(interest_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def delete_interest(request, interest_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    interest = get_object_or_404(Interest, pk=interest_id)
    
    if request.method == "POST":
        interest.delete()
        messages.success(request, "Minat berhasil dihapus!")
        return redirect("main:show_interest")
    
    return redirect("main:show_interest")

@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
        "education": education,
    }
    return render(request, "education_update_form.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_update_form.html", context)

@login_required(login_url="/login/")
def update_interest(request, interest_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    interest = get_object_or_404(Interest, pk=interest_id)
    form = InterestForm(request.POST or None, instance=interest)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Minat berhasil diperbarui!")
        return redirect("main:show_interest")

    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
        "interest": interest,
    }
    return render(request, "interest_update_form.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "username": "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response






