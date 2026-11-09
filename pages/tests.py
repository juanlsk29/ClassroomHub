
from django.test import TestCase
from django.urls import reverse
from .models import Category, Resource
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import Client, TestCase
from django.urls import reverse


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
class AuthenticationTests(TestCase):
    def setUp(self):
        self.password = "ExampleTestPassword!2026"
        self.user = get_user_model().objects.create_user(
            username="reader",
            password=self.password,
        )

    def test_signup_page_renders(self):
        response = self.client.get(reverse("pages:signup"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/signup.html")

    def test_signup_creates_regular_user(self):
        response = self.client.post(
            reverse("pages:signup"),
            {
                "username": "new_reader",
                "password1": "NewExamplePassword!2026",
                "password2": "NewExamplePassword!2026",
            },
        )

        self.assertRedirects(response, reverse("pages:login"))
        account = get_user_model().objects.get(username="new_reader")
        self.assertFalse(account.is_staff)
        self.assertFalse(account.is_superuser)
        self.assertTrue(account.check_password("NewExamplePassword!2026"))

    def test_signup_rejects_mismatched_passwords(self):
        response = self.client.post(
            reverse("pages:signup"),
            {
                "username": "invalid_reader",
                "password1": "ExamplePassword!2026",
                "password2": "DifferentPassword!2026",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            get_user_model().objects.filter(username="invalid_reader").exists()
        )

    def test_signup_rejects_existing_username(self):
        response = self.client.post(
            reverse("pages:signup"),
            {
                "username": "reader",
                "password1": self.password,
                "password2": self.password,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            get_user_model().objects.filter(username="reader").count(),
            1,
        )

    def test_login_rejects_wrong_password(self):
        response = self.client.post(
            reverse("pages:login"),
            {"username": "reader", "password": "wrong"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("pages:login"),
            {"username": "reader", "password": self.password},
        )

        self.assertRedirects(response, reverse("pages:dashboard"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_respects_safe_next(self):
        destination = reverse("pages:resources")
        response = self.client.post(
            reverse("pages:login") + f"?next={destination}",
            {
                "username": "reader",
                "password": self.password,
                "next": destination,
            },
        )

        self.assertRedirects(response, destination)

    def test_anonymous_dashboard_redirects_to_login(self):
        response = self.client.get(reverse("pages:dashboard"))

        self.assertRedirects(
            response,
            reverse("pages:login") + "?next=/dashboard/",
        )

    def test_dashboard_session_counter_increments(self):
        self.client.force_login(self.user)

        first = self.client.get(reverse("pages:dashboard"))
        second = self.client.get(reverse("pages:dashboard"))

        self.assertEqual(first.context["visit_count"], 1)
        self.assertEqual(second.context["visit_count"], 2)

    def test_logout_get_is_not_allowed(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("pages:logout"))

        self.assertEqual(response.status_code, 405)
        self.assertIn("_auth_user_id", self.client.session)

    def test_logout_post_ends_session(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("pages:logout"))

        self.assertRedirects(response, reverse("pages:home"))
        self.assertNotIn("_auth_user_id", self.client.session)
        protected = self.client.get(reverse("pages:dashboard"))
        self.assertEqual(protected.status_code, 302)

    def test_login_post_without_csrf_is_rejected(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.get(reverse("pages:login"))

        response = csrf_client.post(
            reverse("pages:login"),
            {"username": "reader", "password": self.password},
        )

        self.assertEqual(response.status_code, 403)
class ResourceReviewPermissionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="review_candidate",
            password="ExampleTestPassword!2026",
        )
        category = Category.objects.create(name="Programming")
        Resource.objects.create(
            title="Python basics",
            category=category,
        )

        content_type = ContentType.objects.get_for_model(Resource)
        permission = Permission.objects.get(
            content_type=content_type,
            codename="view_resource",
        )
        self.reviewers = Group.objects.create(name="Catalog reviewers")
        self.reviewers.permissions.add(permission)

    def test_anonymous_review_redirects_to_login(self):
        response = self.client.get(reverse("pages:resource-review"))

        self.assertRedirects(
            response,
            reverse("pages:login") + "?next=/resources/review/",
        )

    def test_regular_user_cannot_open_review(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("pages:resource-review"))

        self.assertEqual(response.status_code, 403)

    def test_reviewer_can_open_review(self):
        self.user.groups.add(self.reviewers)
        self.client.force_login(self.user)
        response = self.client.get(reverse("pages:resource-review"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python basics")
        self.assertTemplateUsed(response, "pages/review.html")

    def test_reviewer_does_not_become_staff(self):
        self.user.groups.add(self.reviewers)
        self.user.refresh_from_db()

        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_public_catalog_remains_available(self):
        response = self.client.get(reverse("pages:resources"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python basics")

    def test_typing_review_url_cannot_bypass_permission(self):
        self.client.force_login(self.user)
        response = self.client.get("/resources/review/")

        self.assertEqual(response.status_code, 403)
    
class DashboardSummaryTests(TestCase):
    def test_anonymous_visitor_is_redirected_to_login(self):
        response = self.client.get(reverse("pages:dashboard-summary"))

        self.assertRedirects(
            response,
            reverse("pages:login") + "?next=/dashboard/summary/",
        )

    def test_regular_user_can_see_resource_counts(self):
        user = get_user_model().objects.create_user(username="summary_reader")
        category = Category.objects.create(name="Programming")
        Resource.objects.create(
            title="Python basics",
            category=category,
            available=True,
        )
        Resource.objects.create(
            title="Django basics",
            category=category,
            available=False,
        )
        self.client.force_login(user)

        response = self.client.get(reverse("pages:dashboard-summary"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Total resources: 2")
        self.assertContains(response, "Available resources: 1")