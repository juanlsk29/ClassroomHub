from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Resource
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

class ResourceCrudTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Programming",
            description="Programming resources",
        )
        cls.resource = Resource.objects.create(
            title="Python basics",
            description="Variables and functions",
            category=cls.category,
            available=True,
        )

        User = get_user_model()

        cls.reader = User.objects.create_user(
            username="crud_reader",
            password="ExampleTestPassword!2026",
        )
        cls.editor = User.objects.create_user(
            username="crud_editor",
            password="ExampleTestPassword!2026",
        )
        cls.reviewer = User.objects.create_user(
            username="crud_reviewer",
            password="ExampleTestPassword!2026",
        )

        content_type = ContentType.objects.get_for_model(Resource)

        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                "view_resource",
                "add_resource",
                "change_resource",
                "delete_resource",
            ],
        )

        editors = Group.objects.create(name="Catalog editors")
        editors.permissions.add(*permissions)
        cls.editor.groups.add(editors)

        review_permission = Permission.objects.get(
            content_type=content_type,
            codename="view_resource",
        )

        reviewers = Group.objects.create(name="Catalog reviewers")
        reviewers.permissions.add(review_permission)
        cls.reviewer.groups.add(reviewers)

    def resource_data(self, **overrides):
        values = {
            "title": "Database testing",
            "description": "Database integration practice",
            "resource_type": "Guide",
            "category": self.category.pk,
            "available": "on",
        }
        values.update(overrides)
        return values

    def test_resource_detail_is_public(self):
        url = reverse("pages:resource-detail", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python basics")
        self.assertContains(response, "Programming")

    def test_unknown_resource_detail_returns_404(self):
        url = reverse("pages:resource-detail", args=[999999])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_public_catalog_links_to_resource_detail(self):
        response = self.client.get(reverse("pages:resources"))
        detail_url = reverse(
            "pages:resource-detail",
            args=[self.resource.pk],
        )

        self.assertContains(response, f'href="{detail_url}"')

    def test_create_redirects_anonymous_user_to_login(self):
        url = reverse("pages:resource-create")

        response = self.client.get(url)

        self.assertRedirects(
            response,
            reverse("pages:login") + f"?next={url}",
        )

    def test_create_denies_authenticated_reader(self):
        self.client.force_login(self.reader)

        response = self.client.get(reverse("pages:resource-create"))

        self.assertEqual(response.status_code, 403)

    def test_reviewer_cannot_create_resource(self):
        self.client.force_login(self.reviewer)

        response = self.client.get(reverse("pages:resource-create"))

        self.assertEqual(response.status_code, 403)

    def test_editor_can_open_create_form(self):
        self.client.force_login(self.editor)

        response = self.client.get(reverse("pages:resource-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/resource_form.html")

    def test_reader_cannot_create_resource_via_post(self):
        self.client.force_login(self.reader)
        before = Resource.objects.count()

        response = self.client.post(
            reverse("pages:resource-create"),
            self.resource_data(),
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Resource.objects.count(), before)
        self.assertFalse(
            Resource.objects.filter(title="Database testing").exists()
        )

    def test_editor_can_create_resource(self):
        self.client.force_login(self.editor)
        before = Resource.objects.count()

        response = self.client.post(
            reverse("pages:resource-create"),
            self.resource_data(),
        )

        self.assertRedirects(response, reverse("pages:resources"))
        self.assertEqual(Resource.objects.count(), before + 1)

        created = Resource.objects.get(title="Database testing")
        self.assertEqual(created.category_id, self.category.pk)
        self.assertEqual(created.resource_type, "Guide")
        self.assertTrue(created.available)

    def test_create_rejects_short_title(self):
        self.client.force_login(self.editor)
        before = Resource.objects.count()

        response = self.client.post(
            reverse("pages:resource-create"),
            self.resource_data(title="ab"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"],
            "title",
            "Title must contain at least 3 characters.",
        )
        self.assertEqual(Resource.objects.count(), before)
        self.assertFalse(Resource.objects.filter(title="ab").exists())

    def test_create_rejects_unknown_category(self):
        self.client.force_login(self.editor)
        before = Resource.objects.count()

        response = self.client.post(
            reverse("pages:resource-create"),
            self.resource_data(category=999999),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("category", response.context["form"].errors)
        self.assertEqual(Resource.objects.count(), before)

    def test_form_exposes_only_expected_fields(self):
        self.client.force_login(self.editor)

        response = self.client.get(reverse("pages:resource-create"))

        self.assertEqual(
            list(response.context["form"].fields),
            [
                "title",
                "description",
                "resource_type",
                "category",
                "available",
            ],
        )
        self.assertNotIn("created_at", response.context["form"].fields)
        self.assertNotIn("id", response.context["form"].fields)

    def test_update_redirects_anonymous_user_to_login(self):
        url = reverse("pages:resource-update", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertRedirects(
            response,
            reverse("pages:login") + f"?next={url}",
        )

    def test_update_denies_authenticated_reader(self):
        self.client.force_login(self.reader)
        url = reverse("pages:resource-update", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_reader_cannot_update_resource_via_post(self):
        self.client.force_login(self.reader)
        url = reverse("pages:resource-update", args=[self.resource.pk])

        response = self.client.post(
            url,
            self.resource_data(title="Forbidden update"),
        )

        self.assertEqual(response.status_code, 403)
        self.resource.refresh_from_db()
        self.assertEqual(self.resource.title, "Python basics")

    def test_editor_can_open_update_form(self):
        self.client.force_login(self.editor)
        url = reverse("pages:resource-update", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/resource_form.html")
        self.assertContains(response, "Python basics")

    def test_editor_can_update_existing_resource(self):
        self.client.force_login(self.editor)
        old_id = self.resource.pk
        before = Resource.objects.count()

        other_category = Category.objects.create(name="Databases")
        url = reverse("pages:resource-update", args=[old_id])

        response = self.client.post(
            url,
            self.resource_data(
                title="Updated Python resource",
                description="Updated description",
                category=other_category.pk,
                available="",
            ),
        )

        self.assertRedirects(response, reverse("pages:resources"))

        self.resource.refresh_from_db()
        self.assertEqual(self.resource.pk, old_id)
        self.assertEqual(Resource.objects.count(), before)
        self.assertEqual(self.resource.title, "Updated Python resource")
        self.assertEqual(self.resource.description, "Updated description")
        self.assertEqual(self.resource.category_id, other_category.pk)
        self.assertFalse(self.resource.available)

    def test_invalid_update_keeps_existing_values(self):
        self.client.force_login(self.editor)
        url = reverse("pages:resource-update", args=[self.resource.pk])

        response = self.client.post(
            url,
            self.resource_data(
                title="ab",
                description="This must not be saved",
                available="",
            ),
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"],
            "title",
            "Title must contain at least 3 characters.",
        )

        self.resource.refresh_from_db()
        self.assertEqual(self.resource.title, "Python basics")
        self.assertEqual(
            self.resource.description,
            "Variables and functions",
        )
        self.assertTrue(self.resource.available)

    def test_delete_redirects_anonymous_user_to_login(self):
        url = reverse("pages:resource-delete", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertRedirects(
            response,
            reverse("pages:login") + f"?next={url}",
        )

    def test_delete_denies_authenticated_reader(self):
        self.client.force_login(self.reader)
        url = reverse("pages:resource-delete", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_reviewer_cannot_delete_resource(self):
        self.client.force_login(self.reviewer)
        url = reverse("pages:resource-delete", args=[self.resource.pk])

        response = self.client.post(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Resource.objects.filter(pk=self.resource.pk).exists()
        )

    def test_delete_get_only_shows_confirmation(self):
        self.client.force_login(self.editor)
        url = reverse("pages:resource-delete", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "pages/resource_confirm_delete.html",
        )
        self.assertTrue(
            Resource.objects.filter(pk=self.resource.pk).exists()
        )

    def test_delete_post_removes_resource(self):
        self.client.force_login(self.editor)
        resource_id = self.resource.pk
        category_id = self.category.pk

        other = Resource.objects.create(
            title="Resource to preserve",
            category=self.category,
        )

        url = reverse("pages:resource-delete", args=[resource_id])

        response = self.client.post(url)

        self.assertRedirects(response, reverse("pages:resources"))
        self.assertFalse(
            Resource.objects.filter(pk=resource_id).exists()
        )
        self.assertTrue(Resource.objects.filter(pk=other.pk).exists())
        self.assertTrue(Category.objects.filter(pk=category_id).exists())

        detail = self.client.get(
            reverse("pages:resource-detail", args=[resource_id])
        )
        self.assertEqual(detail.status_code, 404)

    def test_unknown_resource_update_returns_404_for_editor(self):
        self.client.force_login(self.editor)
        url = reverse("pages:resource-update", args=[999999])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_unknown_resource_delete_returns_404_for_editor(self):
        self.client.force_login(self.editor)
        url = reverse("pages:resource-delete", args=[999999])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_reader_does_not_see_edit_or_delete_links(self):
        self.client.force_login(self.reader)
        url = reverse("pages:resource-detail", args=[self.resource.pk])

        response = self.client.get(url)

        self.assertNotContains(response, "Edit resource")
        self.assertNotContains(response, "Delete resource")

    def test_editor_can_manage_without_staff_status(self):
        self.client.force_login(self.editor)

        self.assertFalse(self.editor.is_staff)
        self.assertFalse(self.editor.is_superuser)
        self.assertTrue(self.editor.has_perm("pages.add_resource"))
        self.assertTrue(self.editor.has_perm("pages.change_resource"))
        self.assertTrue(self.editor.has_perm("pages.delete_resource"))

    def test_editor_can_still_open_review_page(self):
        self.client.force_login(self.editor)

        response = self.client.get(reverse("pages:resource-review"))

        self.assertEqual(response.status_code, 200)

    def test_public_catalog_reflects_new_resource(self):
        Resource.objects.create(
            title="New catalog resource",
            category=self.category,
        )

        response = self.client.get(reverse("pages:resources"))

        self.assertContains(response, "New catalog resource")

    def test_post_without_csrf_is_rejected(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.editor)
        before = Resource.objects.count()

        response = csrf_client.post(
            reverse("pages:resource-create"),
            self.resource_data(),
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Resource.objects.count(), before)

    def test_reviewer_cannot_update_resource(self):
        self.client.force_login(self.reviewer)
        url = reverse("pages:resource-update", args=[self.resource.pk])

        self.assertEqual(self.client.get(url).status_code, 403)

        response = self.client.post(
            url,
            self.resource_data(title="Forbidden reviewer update"),
        )

        self.assertEqual(response.status_code, 403)
        self.resource.refresh_from_db()
        self.assertEqual(self.resource.title, "Python basics")

    def test_delete_without_csrf_is_rejected(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.editor)
        url = reverse("pages:resource-delete", args=[self.resource.pk])

        response = csrf_client.post(url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Resource.objects.filter(pk=self.resource.pk).exists()
        )

    def test_add_permission_does_not_allow_update_or_delete(self):
        permission = Permission.objects.get(
            content_type=ContentType.objects.get_for_model(Resource),
            codename="add_resource",
        )
        self.reader.user_permissions.add(permission)
        self.client.force_login(self.reader)

        self.assertEqual(
            self.client.get(reverse("pages:resource-create")).status_code,
            200,
        )

        update_url = reverse(
            "pages:resource-update",
            args=[self.resource.pk],
        )
        delete_url = reverse(
            "pages:resource-delete",
            args=[self.resource.pk],
        )

        update_response = self.client.post(
            update_url,
            self.resource_data(title="Forbidden separate permission"),
        )
        delete_response = self.client.post(delete_url)

        self.assertEqual(update_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)

        self.resource.refresh_from_db()
        self.assertEqual(self.resource.title, "Python basics")

    def test_update_rejects_unknown_category_without_changes(self):
        self.client.force_login(self.editor)
        url = reverse("pages:resource-update", args=[self.resource.pk])

        response = self.client.post(
            url,
            self.resource_data(
                title="Must not be saved",
                category=999999,
            ),
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("category", response.context["form"].errors)

        self.resource.refresh_from_db()
        self.assertEqual(self.resource.title, "Python basics")
        self.assertEqual(self.resource.category_id, self.category.pk)


class ResourceSearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Search examples")

        cls.python_resource = Resource.objects.create(
            title="Python introduction",
            category=cls.category,
        )
        cls.django_resource = Resource.objects.create(
            title="Django forms",
            category=cls.category,
        )

    def test_search_with_results(self):
        before = Resource.objects.count()

        response = self.client.get(
            reverse("pages:resources"),
            {"q": "  python  "},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["query"], "python")
        self.assertQuerySetEqual(
            response.context["resources"],
            [self.python_resource.pk],
            transform=lambda resource: resource.pk,
        )
        self.assertContains(response, "Python introduction")
        self.assertNotContains(response, "Django forms")
        self.assertEqual(Resource.objects.count(), before)

    def test_search_without_results(self):
        before = Resource.objects.count()

        response = self.client.get(
            reverse("pages:resources"),
            {"q": "NoMatchingTitle987"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["resources"].count(), 0)
        self.assertContains(response, "No resources match your search.")
        self.assertEqual(Resource.objects.count(), before)

    def test_empty_search_returns_all_resources(self):
        for query in ["", "   "]:
            with self.subTest(query=query):
                response = self.client.get(
                    reverse("pages:resources"),
                    {"q": query},
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.context["query"], "")
                self.assertEqual(
                    set(
                        response.context["resources"].values_list(
                            "pk",
                            flat=True,
                        )
                    ),
                    {
                        self.python_resource.pk,
                        self.django_resource.pk,
                    },
                )