import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied      
from django.views.decorators.http import require_POST  

# Create your views here.
from main.forms import EducationForm, ExperienceForm, InterestForm
from main.models import Experience, Mahasiswa, Education, Interest

def is_editor(user):
    return user.groups.filter(name="Editor").exists()


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
        "mahasiswa" : Mahasiswa.objects.all(),
        "is_editor" : is_editor(request.user),
    }
    
    return render(request, "index.html", context)


def show_experience(request):
    # json_response = get_experience_json(request)
    
    # experiences = serializers.deserialize(
    #     "json",
    #     json_response.content.decode("utf-8"),
    # )
    # experience_list = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        # "experience_list": experience_list,
        "title_query": title_query,
        "is_editor" : is_editor(request.user),
    }
    return render(request, "experience.html", context)

def show_education(request):
    institution_query = request.GET.get("institution", "").strip()
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        # "education_list": education_list,
        "institution_query": institution_query,
        "is_editor" : is_editor(request.user),
        "form": EducationForm(),
        
    }
    return render(request, "education.html", context)

def show_interest(request):
    # json_response = get_interest_json(request)
    
    # interests = serializers.deserialize(
    #     "json",
    #     json_response.content.decode("utf-8"),
    # )
    # interest_list = [interest.object for interest in interests]
    nama_query = request.GET.get("nama", "").strip()
    
    context = {
        "username" : "Taufiq",
        "name": "Muhammad Taufiq Ramadhan",
        # "interest_list": interest_list,
        "nama_query": nama_query,
        "is_editor" : is_editor(request.user),
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
    educations = Education.objects.prefetch_related('starred_by').all()

    if institution_query:
        educations = Education.objects.filter(institution__icontains=institution_query)
        
    data =[]
    for education in educations:
        starred_users = education.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(education.id),
            "fields": {
                "id": education.id,
                "institution": education.institution,
                "degree": education.degree,
                "study_program": education.study_program,
                "start_year": education.start_year,
                "end_year": education.end_year,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    # education_json = serializers.serialize(
    #     "json", education, use_natural_foreign_keys=True)
    # return HttpResponse(education_json, content_type="application/json")
    return JsonResponse(data, safe=False)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()
    
    if title_query:
        experiences = Experience.objects.filter(title_icontains=title_query)
        
    data =[]
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "started_at": experience.started_at,
                "ended+at": experience.ended_at,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })        
        
    # experience_json = serializers.serialize(
    #     "json", experience, use_natural_foreign_keys=True)
    # return HttpResponse(experience_json, content_type="application/json")
    return JsonResponse(data, safe=False)

def get_interest_json(request):
    nama_query = request.GET.get("nama", "").strip()
    interests = Interest.objects.prefetch_related('starred_by').all()
    
    if nama_query:
        interests = Interest.objects.filter(nama_icontains=nama_query)
        
    data =[]
    for interest in interests:
        starred_users = interest.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(interest.id),
            "fields": {
                "nama": interest.nama,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    # interest_json = serializers.serialize(
    #     "json", interest, use_natural_foreign_keys=True)
    # return HttpResponse(interest_json, content_type="application/json")
    return JsonResponse(data, safe=False)

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
    if not (request.user.is_superuser or is_editor(request.user)):
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
        "is_editor": is_editor(request.user),
    }
    return render(request, "education_update_form.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request.user)):
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
        "is_editor": is_editor(request.user),
    }
    return render(request, "experience_update_form.html", context)

@login_required(login_url="/login/")
def update_interest(request, interest_id):
    if not (request.user.is_superuser or is_editor(request.user)):
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
        "is_editor": is_editor(request.user),
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

@login_required(login_url="/login/")
def toggle_star_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_interest(request, interest_id):
    interest = get_object_or_404(Interest, pk=interest_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in interest.starred_by.all():
            interest.starred_by.remove(request.user)
        else:
            interest.starred_by.add(request.user)

    return redirect("main:show_interest")


...

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Riwayat pendidikan berhasil ditambahkan.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)






