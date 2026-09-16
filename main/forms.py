from django.forms import ModelForm, NumberInput, TextInput, Textarea, URLInput

from main.models import Education

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