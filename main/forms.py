from django.forms import DateTimeInput, ModelForm, NumberInput, Select, TextInput, Textarea, URLInput

from main.models import Education, Experience, Interest

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "study_program",
            "start_year",
            "end_year",
        ]

        labels = {
            "institution": "Nama institut",
            "degree": "Gelar",
            "study_program": "Program study",
            "start_year": "Tahun mulai",
            "end_year": "Tahun selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "S1",
                    "maxlength": 255,
                }
            ),
             "study_program": TextInput(
                attrs={
                    "placeholder": "Ilmu Komputer",
                    "maxlength": 255,
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2025",
                    "min": 1900,
                    "max": 2100,
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "Sekarang / 2029",
                    "min": 1900,
                    "max": 2100,
                }
            ),
        }
        
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            # "started_at",
            "ended_at",
        ]
        
        widgets = {
            "tittle": TextInput(
                attrs={
                    "placeholder": "Pengalaman",
                    "maxlenght": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                    "style": "width:100%; padding:0.75rem; font-size:1rem;",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://.............",
                }
            ),
            # "started_at": DateTimeInput(
            #     attrs={
            #         "type": "datetime-local"
            #     }
            # ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local"
                }
            ),
        }
        
class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = [
            "nama"
        ]
        widgets = {
            "nama": TextInput(
                attrs={
                    "placeholder": "Ketertarikan",
                    "max_lenght": 255,
                }
            ),
        }