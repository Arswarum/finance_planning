from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def project_list(request):
    # return available projects view
    return render(request, 'budget/project-list.html')

@login_required(login_url='login')
def project_detail(request, project_slug):
    # return curent project view
    return render(request, 'budget/project-detail.html')