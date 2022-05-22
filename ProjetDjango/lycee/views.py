import datetime

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm,PresenceForm,CallofRollForm
from django.urls import reverse

def detail_cursus(request,cursus_id):
    cursus = Cursus.objects.get(pk=cursus_id)
    result_list = cursus.student_set.all()
    context = {'liste': result_list}
    return render(request, 'lycee/cursus/detail_cursus.html',context)

def index(request):
    result_list = Cursus.objects.order_by('name')
    template = loader.get_template('lycee/index.html')
    context= {
        'liste': result_list,
    }
    return HttpResponse(template.render(context, request))

def detail_student(request,student_id):
    result_list = Student.objects.get(pk=student_id)
    context = {'liste' : result_list}
    return render(request,'lycee/student/detail_student.html',context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))

class PresenceCreateView(CreateView):
    model = Presence
    form_class = PresenceForm
    template_name = 'lycee/callofroll/create.html'

    def get_success_url(self):
        return reverse("detail_presence", args=(self.object.pk,))

def edit_student(request,student_id):
    result_list = Student.objects.get(pk=student_id)
    form = None #Creation de form vide
    if (request.method == 'POST'):
        form = StudentForm(request.POST, instance= result_list)
        if form.is_valid():
            form.save() #On sauvegarde le form en sont état actuel
            return redirect('detail_student',student_id)
    else:
        form = StudentForm(instance= result_list) #On ne change rien au niveau de la bdd
    return render(request,'lycee/student/edit.html',{'form' : form})

def cursus_call(request, cursus_id):
    if request.method == "POST":
        for student_id in request.POST.getlist('missing'): #On recupêre tous les étudiants coché isMissing
            date = request.POST.getlist('date_cursus_call') #On recupère la date selectionnée dans le form
            string_date = "".join(date) #Passe en string la date
            new_missing = Presence(
                reason="Absent during call of roll",
                isMissing=True,
                date=string_date,
                student=Student.objects.get(pk=student_id),
            )
            new_missing.save()
        return redirect('detail_presence_all')
    result_list = Student.objects.filter(cursus=cursus_id).order_by('last_name')

    context = {'liste': result_list}

    return render(request, 'lycee/callofroll/createcallofroll.html', context)

def detail_presence(request, presence_id):
    result_list = Presence.objects.get(pk=presence_id)
    context = {'liste' : result_list}
    return render(request, 'lycee/callofroll/detail_presence.html', context)

def detail_presence_all(request):
    result_list = Presence.objects.order_by('date')
    context = {'liste': result_list}
    return render(request, 'lycee/callofroll/detail_presence_all.html',context)

class CursusCallView(CreateView):
  form_class = CallofRollForm
  template_name = 'lycee/callofroll/createcallofroll.html'


