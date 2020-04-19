from django.shortcuts import render
from django.utils import timezone
from .models import ToDo, Info
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy


def display(request):
    todo_items = list(ToDo.objects.all().order_by("-added_date"))
    return render(request, 'index.html', {"todo_items": todo_items[0:3]})


def display_older_posts(request):
    todo_items = list(ToDo.objects.all().order_by("-added_date"))
    return render(request, 'index.html', {"todo_items": todo_items[3:len(todo_items)]})


def add_todo(request):
    current_addeddate = timezone.now()
    content = request.POST["content"].capitalize()
    description1 = request.POST["desp"]
    print(request.POST)
    created_obj = ToDo.objects.create(added_date=current_addeddate, text=content, description=description1)
    return HttpResponseRedirect("/")


def delete(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


def post(request):
    return render(request, 'post.html')


def contact(request):
    return render(request, 'contact.html')


def contact1(request):
    name = request.POST["name"]
    email = request.POST["email"]
    phone_no = request.POST["phone_no"]
    message = request.POST["message"]
    Info.objects.create(name=name, email=email, phone_no=phone_no, message=message)
    return HttpResponseRedirect("/")


def about(request):
    return render(request, 'about.html')


class Detail(DetailView):
    model = ToDo
    template_name = 'detail.html'
    context_object_name = 'rex'


class Update(UpdateView):
    model = ToDo
    template_name = 'update.html'
    fields = ['text', 'description']
    success_url = reverse_lazy('display')
