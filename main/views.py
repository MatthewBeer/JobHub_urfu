from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.template import loader
from main.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentForm
def style(request):
    template = loader.get_template('main/css/style.css')
    return HttpResponse(template.render(), content_type='text/css')
def index(request):
    return render(request, 'main/index.html', )


def submit_company_registration(request):
    return render(request, 'main/registration_company_registration.html')


def submit_student_registration(request):
    return render(request, 'main/submit_student_registration.html')
def recomendation(request):
    students = Student.objects.all().order_by('-id')[:4]
    return render(request, 'main/recomendations.html', {'students': students})

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена/<h1>')
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id={post_id}")
def recomendationcompanies(request):
    return render(request, 'main/recomendations_comp.html')
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'main/ready_profil.html', {'student': student})
def innovatech(request):
    return render(request, 'main/ready_profil_comp.html', )
def digitallabs(request):
    return render(request, 'main/ready_profil_comp11.html', )
def itbox(request):
    return render(request, 'main/ready_profil_comp1.html', )
def unit(request):
    return render(request, 'main/ready_profil_comp2.html', )
def addpage(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после сохранения
    else:
        form = StudentForm()

    return render(request, 'main/profil.html', {'form': form})