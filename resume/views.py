from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request, "portfolio/home.html")

def about(request):
    return render (request, "portfolio/about.html")

def projects(request):
    projects_show = [
        {
            "title": "Portfolio",
            "path": "images/portfolio.png",
        },
        {
            "title": "Dual Examinner Marking System",
            "path": "images/image-20160824-30252-j527k8.avif",
        },
        {
            "title": "Traveller Blog",
            "path": "images/DI_5-Steps-To-Designing-An-Eye-Catching-Travel-Blog_Banner_828x300.jpg",
        },
        {
            "title": "School Attendence System",
            "path": "images/stdasms.jpg",
        },
    ]
    return render (request, "portfolio/projects.html", {"projects": projects_show})

def experience(request):
    experiences = [
        {
            "company_name": "Innoweb Limited",
            "position": "Software Engineer",
        },
        {
            "company_name": "Innoweb Limited",
            "position": "Software Engineer Inetrn",
        }
    ]
    return render (request, "portfolio/experience.html", {"experiences": experiences})


def contact(request):
    return render (request, "portfolio/contact.html")


def resume(request):
    resume_path = "files/NasimulHasanCV.pdf"
    resume_path = staticfiles_storage.path(resume_path)

    if staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="NasimulHasanCV.pdf"'
            return response
    else:
        return HttpResponseNotFound('Resume not found')