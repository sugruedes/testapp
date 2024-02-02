from django.shortcuts import render
from projects.models import Project


def __str__(self):
        # view of the model in admin pannel
        return 

#def save(self, *args, **kwargs):
        # logic before you save you model object
        
#        super().save(*args, **kwargs)

class Meta:
        # for naming you table
        db_table = ""

# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }    
    return render(request, "projects/details.html", context)