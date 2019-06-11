from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello my dog</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', {'dog': dog})

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/dogs/'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age'] 

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'