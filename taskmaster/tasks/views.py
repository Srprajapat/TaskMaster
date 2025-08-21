from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.contrib import messages



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

def homepage(request):
    return render(request, 'homepage.html')

@login_required
def task_list(request):
    tasks = Task.objects.all() if request.user.is_superuser else Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            if not request.user.is_staff:
                task.assigned_to = request.user
            task.save()
            form.save_m2m()
            return redirect('task_list')
    else:
        form = TaskForm()
        if not request.user.is_staff:
            form.fields['assigned_to'].queryset = User.objects.filter(id=request.user.id)
            form.fields['assigned_to'].initial = request.user
            form.fields['assigned_to'].widget.attrs['readonly'] = True

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.assigned_to and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit this task.")

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if not request.user.is_staff:
            # Force the field value to remain the same for non-admins
            form.data = form.data.copy()
            form.data['assigned_to'] = task.assigned_to.id

        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)

        if not request.user.is_staff:
            form.fields['assigned_to'].queryset = User.objects.filter(id=request.user.id)
            form.fields['assigned_to'].initial = request.user
            form.fields['assigned_to'].disabled = True

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.assigned_to and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete this task.")

    task.delete()
    return redirect('task_list')

@login_required
@require_POST
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.assigned_to and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to mark this task as completed.")

    task.status = 'Completed'
    task.save()
    messages.success(request, f"Task '{task.title}' marked as completed.")
    return redirect('task_list')



@csrf_exempt
def custom_logout_view(request):
    logout(request)
    return redirect('/')
