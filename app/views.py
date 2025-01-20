import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
import qtconsole
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='login')

def HomePage(request):
   return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       password=request.POST.get('password')
       con_password =request.POST.get('confirm_password')
       if password!=con_password:
          return HttpResponse("Password and Confirm password not same!")
       else:
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
       

    return render(request,'signup.html')


@csrf_exempt
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home.html',{"status": "success", "message": "Login successful!"})
        else:
            return render(request, 'login.html',{"status": "error", "message": "Username or Password is incorrect!"}, status=401)

    return render(request, 'login.html',{"status": "error", "message": "Only POST requests are allowed."}, status=405)
     

#    return render(request,'MONALI)

def LogoutPage(request):
    logout(request)
    return redirect('login')


def DashBoard(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'login.html', {'service_requests': service_requests})


def Help(request):
    return render(request, 'help.html')

# @login_required
# def track_my_account(request):
#     # profile = request.user.profile  # Access the profile data
#     return render(request, 'track_my_account.html')

# views.py


@login_required
def TrackMyAccount(request):
    # profile = request.user.profile
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES, instance=profile)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = ProfileForm(instance=profile)
    return render(request, 'track_my_account.html')




# List all service requests
# def service_request_list(request):
#     requests = ServiceRequest.objects.all()
#     return render(request, 'service_requests/list.html', {'requests': requests})

# # View details of a single service request
# def service_request_detail(request, pk):
#     service_request = get_object_or_404(ServiceRequest, pk=pk)
#     return render(request, 'service_requests/detail.html', {'service_request': service_request})

# # Create a new service request
# def service_request_create(request):
#     if request.method == 'POST':
#         form = ServiceRequestForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('service_request_list')
#     else:
#         form = ServiceRequestForm()
#     return render(request, 'service_requests/create.html', {'form': form})

# Update an existing service request
# def service_request_update(request, pk):
#     service_request = get_object_or_404(ServiceRequest, pk=pk)
#     if request.method == 'POST':
#         form = ServiceRequestForm(request.POST, request.FILES, instance=service_request)
#         if form.is_valid():
#             form.save()
#             return redirect('service_request_detail', pk=service_request.pk)
#     else:
#         form = ServiceRequestForm(instance=service_request)
#     return render(request, 'service_requests/update.html', {'form': form, 'service_request': service_request})
# app/views.py


# def service_request_create(request):
#     # If the form is submitted via POST
#     if request.method == 'POST':
#         form = ServiceRequestForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new service request to the database
#             return redirect('home')  # Redirect to the home page after successful submission
#     else:
#         form = ServiceRequestForm()  # Empty form for GET request

#     return render(request, 'home.html', {'form': form})


from django.shortcuts import render, redirect
from .models import ServiceRequest

# def service_request_create(request):
#     if request.method == 'POST':
#         service_type = request.POST.get('service_type')
#         description = request.POST.get('description')
#         # attachment = request.FILES.get('attachment')
#         # status = request.POST.get('status')

#         # Save data to the database
#         service_request = ServiceRequest(
#             service_type=service_type,
#             description=description,
#             # attachment=attachment,
#             # status=status
#         )
#         service_request.save()

#         # Redirect after saving
#         #return redirect('')  # Replace 'success_page' with your URL name

#     return render(request, 'home.html')

@csrf_exempt
def service_request_create(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            # data = json.loads(request.body)
            service_type = request.POST.get('service_type')
            description = request.POST.get('description')
            status = request.POST.get('status', 'Pending')  # Default status is 'Pending'

            # Validate required fields
            if not service_type or not description:
                return JsonResponse({"status": "error", "message": "All fields are required."}, status=400)

            # Save the data to the database
            service_request = ServiceRequest(
                service_type=service_type,
                description=description,
                status=status
            )
            service_request.save()

            return render(request, 'home.html', {
                "message": "Service request submitted successfully!",
                "service_request": {
                    "id": service_request.id,
                    "service_type": service_request.service_type,
                    "description": service_request.description,
                    "status": service_request.status
                }
            })

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"An error occurred: {e}"}, status=500)

    return JsonResponse({"status": "error", "message": "Only POST requests are allowed."}, status=405)
