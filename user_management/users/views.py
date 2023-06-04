import random
import string
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from flask_login import login_required
from .models import Customer
from django.conf import settings
import re


def generate_user_id():
    # Generate a random alphanumeric user ID
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


@csrf_exempt
def create_customer(request):
    if request.method == 'POST':
        # Retrieve the form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')

        # Check if required fields are not empty
        if not username or not password or not email:
            return JsonResponse({'error': 'Please provide a username, password, and email'})

        # Validate the email format
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'error': 'Please provide a valid email address'})

        # Validate the username format (alphabet characters only)
        if not re.match(r'^[A-Za-z]+$', username):
            return JsonResponse({'error': 'Username should consist of alphabet characters only'})

        # Validate the mobile number format (integer with length 10)
        if not re.match(r'^\d{10}$', mobile):
            return JsonResponse({'error': 'Please provide a 10-digit mobile number'})

        # Validate the password format (alphanumeric with special characters)
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            return JsonResponse({'error': 'Password should contain at least 8 characters, including letters, numbers, and special characters'})


        user_id = generate_user_id()
        # Create or update the customer
        customer, created = Customer.objects.update_or_create(
            email=email,
            defaults={
                'username': username,
                'password': password,
                'mobile': mobile,
                'name': name,
                'address': address
            }
        )

        if created:
            # Send a welcome email to the user
            email_subject = 'Welcome to Our Website'
            email_message = f'Thank you for joining us! Your user ID is: {user_id}'
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            # Customer is created
            return JsonResponse({'message': 'Customer created successfully'})
        else:
            # Customer is updated
            return JsonResponse({'message': 'Customer updated successfully'})


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    print(username, password, request)
    if user is not None:
        login(request, user)
        response = {
            'message': 'Login successful',
            'token': 'abcdef123456'  # Example token
        }
        return JsonResponse(response)
    else:
        response = {
            'message': 'Login failed',
        }
        return JsonResponse(response, status=401)


def select_all_customers(request):
    customers = Customer.objects.all().values()
    return JsonResponse({'customers': list(customers)}, status=200)
