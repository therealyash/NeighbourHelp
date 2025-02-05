from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

class HomePageView(TemplateView):
    template_name = "pages/index.html"

# def create_task(request):
#     return render(request, 'pages/createtask.html')

def about(request):
    return render(request, 'pages/about.html')

def userDash(request):
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'pages/userDash.html', {'tasks': tasks})

def volDash(request):
    tasks = Task.objects.all()
    return render(request, 'pages/volunteerDash.html', {'tasks': tasks})


def signup_view(request):
    return render(request, 'signup.html')  

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task


# Create a task view (with form submission)
@login_required
def createtask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        work_description = request.POST.get('work_description')  # Correct field name from the form
        pincode = request.POST.get('pincode')
        task_type = request.POST.get('task_type')

        # Validate user authentication
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to submit a task.")
            return redirect('login')  # Redirect to login page if user is not authenticated

        # Create and save the new task in the database
        task = Task.objects.create(
            title=title,
            work_description=work_description,
            pincode=pincode,
            task_type=task_type,
            user=request.user
        )

        # Show a success message and redirect to task submission page
        messages.success(request, "Task created successfully!")
        return redirect('pages:index')  # Redirect to home page or another page after submission

    return render(request, 'pages/createtask.html')


def accept_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task by ID
    if task.status == 'pending':  # If the task is pending, accept it
        task.status = 'accepted'
        task.save()
    if task.status == 'declined':  # If the task is pending, accept it
        task.status = 'accepted'
        task.save()
    return redirect('pages:volDash')  # Redirect to the dashboard after accepting

# Function to handle task decline
def decline_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task by ID
    if task.status == 'accepted':  # If the task is accepted, decline it
        task.status = 'declined'
        task.save()
    return redirect('pages:volDash')  


# def accept_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     if task.status == 'pending':  # Only allow accepting if the task is pending
#         task.status = 'accepted'
#         task.save()
#     return redirect('pages:volDash')  # Redirect to volunteer dashboard after accepting

# # Decline the task (Change status to 'pending')
# def decline_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     if task.status == 'accepted':  # Only allow declining if the task is accepted
#         task.status = 'pending'  # Change status back to 'pending'
#         task.save()
#     return redirect('pages:volDash')  


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
    return redirect('pages:userDash')