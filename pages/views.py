from django.http import HttpResponse
from django.shortcuts import render
from .models import Resource
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
def home(request):
    context = {
        "welcome_message": "Explore learning resources and project ideas.",
    }
    return render(request, "pages/home.html", context)



def resources(request):
    resources_list = Resource.objects.select_related("category").all()

    context = {
        "resources": resources_list,
    }

    return render(request, "pages/resources.html", context)

    return render(request, "pages/resources.html", context)


def about(request):
    context = {
        "purpose": "Practice URL routing, views, and templates.",
    }
    return render(request, "pages/about.html", context)


def contact(request):
    return HttpResponse("Contact information")

def faq(request):
    context = {
        "questions": [
            {
                "question": "What is ClassroomHub?",
                "answer": "ClassroomHub is a learning portal for students."
            },
            {
                "question": "What resources can I find?",
                "answer": "You can explore programming and web development resources."
            },
        ],
    }

    return render(request, "pages/faq.html", context)

def signup(request):
    if request.user.is_authenticated:
        return redirect("pages:dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pages:login")
    else:
        form = UserCreationForm()

    return render(request, "pages/signup.html", {"form": form})


@login_required
def dashboard(request):
    visit_count = request.session.get("dashboard_visits", 0) + 1
    request.session["dashboard_visits"] = visit_count

    return render(
        request,
        "pages/dashboard.html",
        {"visit_count": visit_count},
    )