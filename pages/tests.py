
from django.test import TestCase
from django.urls import reverse
from .models import Category, Resource


class PageViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Programming",
            description="Programming resources"
        )

        cls.resource1 = Resource.objects.create(
            title="Python basics",
            category=cls.category,
            available=True
        )

        cls.resource2 = Resource.objects.create(
            title="Git and GitHub",
            category=cls.category,
            available=False
        )

    # Pruebas de páginas

    def test_faq_page_uses_correct_template(self):
        response = self.client.get(reverse("pages:faq"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/faq.html")

    def test_home_page_renders(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "Welcome")

    def test_resources_page_shows_example_data(self):
        response = self.client.get(reverse("pages:resources"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/resources.html")
        self.assertContains(response, "Python basics")
        self.assertContains(response, "Coming soon")

    def test_about_page_renders(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")

    def test_home_navigation_links_to_resources(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(
            response,
            f'href="{reverse("pages:resources")}"',
        )

    def test_unknown_page_returns_not_found(self):
        response = self.client.get("/not-found/")
        self.assertEqual(response.status_code, 404)

    # Pruebas de modelos y persistencia

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Programming")

    def test_resource_string_representation(self):
        self.assertEqual(str(self.resource1), "Python basics")

    def test_category_resource_relationship(self):
        self.assertEqual(self.resource1.category, self.category)
        self.assertEqual(self.category.resources.count(), 2)

    def test_resource_default_availability(self):
        resource = Resource.objects.create(
            title="Django models",
            category=self.category
        )

        self.assertTrue(resource.available)
