from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):
    # means the user is entering the url
    if request.method == 'GET':
        return render(request, 'AUTH/signup.html', {'form': UserCreationForm})
    else:
        # the user is submitting the form
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'AUTH/signup.html', {'form': UserCreationForm, 'error': 'that username has been already taken'})

        else:
            return render(request, 'AUTH/signup.html', {'form': UserCreationForm, 'error': 'passwords do not match'})


@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=True)

    return render(request, 'todo/currenttodos.html', {'todos': todos})


@login_required
def completedtodos(request):
    todos = Todo.objects.filter(
        user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')

    return render(request, 'todo/completedtodos.html', {'todos': todos})


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'AUTH/loginuser.html', {'form': AuthenticationForm})
    else:
        # the user is submitting the form
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'AUTH/loginuser.html', {'form': AuthenticationForm, 'error': 'username or password are incorrect'})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm})

    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm, 'error': 'bad data . Try again.'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'bad data . Try again.   '})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'POST':
        todo.dateCompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')
