from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date, parse_time
from datetime import date, datetime
from .forms import  VisitorForm, DepartmentForm, BookingForm, VisitorLoginForm, EmployeeForm, ArtifactForm, ArtistForm, FeedbackForm
from .models import Visitor, Employee, Artifact, Artist, Booking, Department, Feedback
from django.db import IntegrityError
from django.http import JsonResponse
import json
import requests
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
# Utility functions for validation
def check_text(s):
    return s.isalpha()

def check_number(s):
    return s.isdigit()

def check_dob(s):
    try:
        date = datetime.strptime(s, "%Y-%m-%d")
        return date < datetime.now()
    except ValueError:
        return False

def check_time(s):
    try:
        datetime.strptime(s, "%H:%M:%S")
        return True
    except ValueError:
        return False

def check_dob_fwd(s):
    try:
        date = datetime.strptime(s, "%Y-%m-%d")
        return date > datetime.now()
    except ValueError:
        return False

# General Views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def explore(request):
    return render(request, 'explore.html')

# User Authentication Views
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # Use Django's built-in authentication function
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            # User is authenticated and is a superuser
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard or any other admin page
        else:
            # Invalid login
            messages.error(request, 'Invalid username or password')

    return render(request, 'login_form.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with this username exists
        user = User.objects.filter(username=username).first()
        
        if user is not None:
            # Authenticate the user
            auth_user = authenticate(username=username, password=password)
            
            if auth_user is not None:
                # Login the authenticated user
                login(request, auth_user)
                return redirect('visitor_dashboard')
            else:
                # Invalid password
                messages.error(request, 'Invalid username or password.')
        else:
            # User does not exist, create an account with a default password
            new_user = User.objects.create_user(username=username, password='defaultpassword')
            login(request, new_user)
            messages.info(request, 'Account created successfully. You are now logged in.')
            return redirect('visitor_dashboard')

    return render(request, 'loginform.html')
@login_required
def profile(request):
    user = request.user
    
    context = {
        'user': user,
        
    }
    return render(request, 'admin_dashboard.html', context)

def success_view(request):
    return render(request, 'sucess.html')

def success(request):
    return render(request, 'sucess2.html')

@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been logged out successfully.")
        return redirect('admin_dashboard')  

    return redirect('home')  

def visitor_reg(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_dashboard')  # Redirect to the visitor dashboard after successful registration
    else:
        form = VisitorForm()
    return render(request, 'reg_visitor.html', {'form': form})

def admin_dashboard(request):
    employees = Employee.objects.all()
    artists = Artist.objects.all()
    artifacts = Artifact.objects.all()
    departments = Department.objects.all()

    context = {
        'employees': employees,
        'artists': artists,
        'artifacts': artifacts,
        'departments': departments,
    }

    return render(request, 'admin_dashboard.html', context)

@login_required
def emp_reg(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = EmployeeForm()

    return render(request, 'reg_employee.html', {'form': form})
        
@login_required
def artist_reg(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = ArtistForm()

    return render(request, 'reg_artist.html', {'form': form})


@login_required
def artifact_reg(request):
    if request.method == 'POST':
        form = ArtifactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_success_url')
    else:
        form = ArtifactForm()
    
    # Fetch all departments
    departments = Department.objects.all()

    return render(request, 'reg_artifact.html', {'form': form, 'departments': departments})

@login_required
def department_reg(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
            # Redirect or render success page
    else:
        form = DepartmentForm()  
    
    return render(request, 'reg_department.html', {'form': form})
@login_required
def visitorpage(request):
    if not request.user.is_superuser:
        return render(request, 'visitorpage.html')
    else:
        return HttpResponse("Unauthorized access")

# Content Display Views
def show(request):
    context = {}
    if request.method == 'POST':
        type_ = request.POST.get('type')

        if type_ == "Artifacts":
            return redirect('artifacts')
        elif type_ == "Artifacts by Artist":
            return redirect('artist_artifact')
        elif type_ == "Artifacts by Department":
            return redirect('department_artifact')
        elif type_ == "None":
            context['error'] = "Please select a valid option"
        else:
            context['error'] = "Invalid option selected"

    return render(request, 'show.html', context)

def artifacts(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Name FROM ARTIFACT")
        rows = cursor.fetchall()
    
    context = {'result': rows}
    return render(request, "show_artifacts.html", context)

def artist_artifact(request):
    if request.method == "POST":
        Artist = request.POST.get("artist")
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT a.Name FROM ARTIFACT a JOIN ARTIFACTARTIST aa ON a.Artifact_ID = aa.Artifact_ID JOIN ARTIST ar ON aa.Artist_ID = ar.Artist_ID WHERE ar.Name = %s",
                [Artist]
            )
            rows = cursor.fetchall()
        
        context = {'result': rows}
        return render(request, "show_artifacts_artist.html", context)
    
    return render(request, "show_artists.html")

def department_artifact(request):
    if request.method == "POST":
        Department = request.POST.get("department")
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT a.Name FROM ARTIFACT a JOIN DEPARTMENT d ON a.Dept_ID = d.Dept_ID WHERE d.Name = %s",
                [Department]
            )
            rows = cursor.fetchall()
        
        context = {'result': rows}
        return render(request, "show_artifacts_department.html", context)
    
    return render(request, "show_departments.html")

def visitor_details(request):
    visitor = Visitor.objects.all()
    paginator = Paginator(visitor, 10)  # Show 10 visitors per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'visitor_details.html', {'page_obj': page_obj})

def view_booking(request):
    booking = Booking.objects.all()
    paginator = Paginator(booking, 10)  # Show 10 bookings per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_booking.html', {'page_obj': page_obj})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    
    if request.method == 'POST':
        # Process form submission for editing booking
        # Example: Update booking details based on form input
        # booking.name = request.POST['name']
        # booking.phone = request.POST['phone']
        # booking.email = request.POST['email']
        # booking.amount = request.POST['amount']
        # booking.ticket_type = request.POST['ticket_type']
        # booking.quantity = request.POST['quantity']
        # booking.date = request.POST['date']
        # booking.save()
        
        # Redirect back to booking list or detail page
        return redirect('booking_list')
    
    # Render edit booking form with initial data
    context = {
        'booking': booking
    }
    return render(request, 'edit_booking.html', context)


@require_POST
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.delete()
    
    # Return success response
    return JsonResponse({'message': 'Booking deleted successfully.'})

# Visitor Interaction Views
@login_required
def visitor_dashboard(request):
    booked_tickets = Booking.objects.filter(visitor_name=request.user)
    return render(request, 'visitor_dashboard.html', {'booked_tickets': booked_tickets})


def stkpush(request):
    if request.method == 'POST':
        name = request.POST['name']
        phn = int(request.POST['phone'])
        countryCode = '254'
        phone = countryCode + str(phn)
        amount = request.POST['amount']
        print(f'Name: {name}, Phone number: {phone}, Amount: {amount}')
        
        data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": int(phone),
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": int(phone),
            "CallBackURL": "https://project.my-market.co.ke/Callback_main/callbackurl_prjct.php",
            "AccountReference": "Nairobi National Museum",
            "TransactionDesc": "Testing stk push"
        }
        response = lipa_na_mpesa_online(data)
        return render(request, 'sucess.html', {'message': response})
    return render(request, 'book_ticket.html')

def lipa_na_mpesa_online(data):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    res = requests.post(api_url, json=data, headers=headers).json()
    print(json.dumps(res, indent=4))
    try:
        return res["ResponseDescription"]
    except:
        return res["errorMessage"]


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('feedback_thank_you')  # Redirect to thank you page after submission
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_thank_you(request):
    return render(request, 'feedback_thankyou.html')

def admin_feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'admin_feedback.html', {'feedbacks': feedbacks})

@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        return render(request, 'visitor_profile.html')
    else:
        return HttpResponse("Unauthorized access")

# Helper functions to get IDs
def get_dept_id(name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Dept_ID FROM DEPARTMENT WHERE Name = %s", [name])
        return cursor.fetchone()[0]

def get_artist_id(name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Artist_ID FROM ARTIST WHERE Name = %s", [name])
        return cursor.fetchone()[0]

def get_emp_ID(name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Employee_ID FROM EMPLOYEE WHERE Name = %s", [name])
        return cursor.fetchone()[0]
