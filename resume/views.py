from django.shortcuts import render

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