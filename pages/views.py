from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "welcome_message": "Explore learning resources and project ideas.",
    }
    return render(request, "pages/home.html", context)



def resources(request):
    context = {
        "resources": [
            {
                "title": "Python basics",
                "category": "Programming",
                "available": True,
            },
            {
                "title": "Git and GitHub",
                "category": "Collaboration",
                "available": False,
            },
            {
                "title": "Django models",
                "category": "Web development",
                "available": False,
            },
            {
                "title": "HTML and CSS",
                "category": "Web development",
                "available": True,
            },
            {
                "title": "JavaScript fundamentals",
                "category": "Programming",
                "available": True,
            },
        ],
    }

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