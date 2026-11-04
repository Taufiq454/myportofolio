from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Sekretaris UKM",
            description="Membuat berkas-berkas",
            category="part-time",
        )
            
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="S1",
            study_program="Ilmu Komputer",
            start_year=2025,
            end_year=None
        )
        

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Sekretaris UKM")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:experience-list"))
        api = self.client.get(reverse("api:experience-list"))
        ids = [item["id"] for item in api.data]
        self.assertIn(str(self.experience.id), ids)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")
        self.assertEqual(self.client.get(reverse("api:experience-list")).data, [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        api = self.client.get(reverse("api:experience-list"))
        item = next(i for i in api.data if i["id"] == str(self.experience.id))
        self.assertFalse(item["is_ongoing"])

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:education-list"))
        api = self.client.get(reverse("api:education-list"))
        item = next(i for i in api.data if i["id"] == str(self.education.id))
        self.assertEqual(item["degree"], self.education.degree)

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))
        self.assertContains(response, "Belum ada riwayat pendidikan yang ditambahkan atau ditemukan.")
        self.assertEqual(self.client.get(reverse("api:education-list")).data, [])
