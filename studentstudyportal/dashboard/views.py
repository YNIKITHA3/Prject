from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.views import generic
from django.core.checks import messages
from django.forms.widgets import FileInput
from . forms import *
from django.contrib import messages
from youtubesearchpython import VideosSearch
from youtubesearchpython import VideosSearch 

from django.shortcuts import get_object_or_404, redirect
from .models import Notes
#from .forms import HomeworkForm
#from .models import Homework
#from .models import HomeworkForm
from .models import Homework
from .models import Todo
from .forms import TodoForm

from . forms import *
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')


def notes(request):
    if request.method=="POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username} succesfully")
    else:
        form=NotesForm()
        notes = Notes.objects.filter(user=request.user)

    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

def delete_note(request, id):
    note = get_object_or_404(Notes, id=id)
    note.delete()
    return redirect('notes')

'''def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")'''
    
class NotesDetailView(generic.DetailView):
    model=Notes
    


def homework(request):
    homeworks = Homework.objects.filter(user=request.user)
    homeworks = Homework.objects.all()
    context={"homeworks":homeworks}
    return render(request,'dashboard/homework.html',context)

'''def homework(request):
    if request.method == "POST":
        form = HomeWorkForm(request.POST)
        if form.is_valid():
            # Retrieve the form data
            finished = request.POST.get('is_finished', 'off') == 'on'
            homeworks = Homework(
                user=request.user,
                subject=form.cleaned_data['subject'],
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                due=form.cleaned_data['due'],
                is_finished=finished
            )
            homeworks.save()
            messages.success(request, f'Homework added successfully by {request.user.username}!')
            return redirect('homework')  # Redirect to avoid form resubmission on refresh
            
    else:
        form = HomeWorkForm()

    # Retrieve all homeworks for the current user
    homeworks = Homework.objects.filter(user=request.user)
    homework_done = not homeworks.exists()  # Simplified check

    context = {
        'form': form,
        'homeworks': homeworks,
        'homeworks_done': homework_done
    }
    return render(request, 'dashboard/homework.html', context)




def update_homework(request,pk=None):
    homework=Homework.objects.get(pk=id)
    if homework.is_finished==True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()
    return redirect('homework')'''



def youtube(request):
    if request.method=="POST":
        form=DashboardForm(request.POST)
        text=request.POST['text']
        video=VideosSearch(text,limit=10)
        result_list=[]
        for i in video.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
            }
            desc=' '
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc+=j['text']
            result_dict['description']=desc
            result_list.append(result_dict)
            context={
                'form':form,
                'results':result_list
            }
        return render(request,'dashboard/youtube.html')
    else:
        form=DashboardForm()
    context={'form':form}
    return render(request,"dashboard/youtube.html ",context)






def todo(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST["is_finished"]
                if finished=="ON":
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            todos=Todo(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            todos.save()
            messages.success(request,f"Todo added from {request.user.username}!!")
    else:
        form=TodoForm()
    todos = Todo.objects.all()
    todos_count = len(todos)
    if todos_count==0:
        todos_done=True
    else:
        todos_done=False
    context={
        "form":form,
        "todos":todos,
        "todos_done":todos_done
    }
    return render(request,"dashboard/todo.html",context)


def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()
    return redirect('todo')


def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")

'''def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')  # Adjust this to your URL pattern name for the todo list
    return render(request, 'delete_todo.html', {'todo': todo})


def delete_todo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    if 'profile' in request.META['HTTP_REFERER']:
        return redirect('profile')
    return redirect('todo')'''