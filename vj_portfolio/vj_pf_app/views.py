from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread
import os 
import sys  # Needed for error printing
from django.utils.safestring import mark_safe

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        try:
            # ✅ Google Sheets API setup
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            creds_path = os.path.join(BASE_DIR, 'credentials', 'credentials.json')

            creds = Credentials.from_service_account_file(
                creds_path,
                scopes=["https://www.googleapis.com/auth/spreadsheets"]
            )
            client = gspread.authorize(creds)

            sheet = client.open_by_key("1Na1iFQ--hW9pZRaNYA8MM0FaXW71zYlNwQg3NbHxELA")
            worksheet = sheet.sheet1

            timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            worksheet.append_row([timestamp, name, email, mobile, message])

            # ✅ Send email to admin
            admin_subject = "New Contact Form Submission"
            admin_message = f"""
You have received a new submission from your portfolio contact form:
 
Name: {name}
Email: {email}
Mobile: {mobile}
Message: {message}
"""
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                ['vv8960727@gmail.com'],  # Admin email
                fail_silently=False
            )

            # ✅ Send thank-you email to user
            user_subject = "Thanks for Contacting Me!"
            user_message = f"""
Hi {name},

Thank you for reaching out to me through my portfolio. I’ve received your message and will get back to you as soon as possible.

-------------
Best regards,
Vijai S
Python Full Stack Developer
📧 Mail - vv8960727@gmail.com
🔗 Linkedin - https://www.linkedin.com/in/vijai1274/
💻 Github - https://github.com/Vijai1274
🌐 Portfolio - https://vijai1201.pythonanywhere.com/
"""
            send_mail(
                user_subject,
                user_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],  # User email
                fail_silently=False
            )

            
            messages.success(request, mark_safe("Thanks for your Response!...<br>Check your Email.!"))

            return redirect('/')

        except Exception as e:
            print("Error submitting form:", e, file=sys.stderr)
            return render(request, 'error.html', {"error": str(e)})
            # /rint("Error submitting form:", e, file=sys.stderr)

    return render(request, 'index.html')
