from django.shortcuts import render
from .forms import UploadFileForm
from django.core.mail import send_mail
from django.conf import settings
from .util import handle_uploaded_file
from .models import UploadedFile

def upload_file(request):
    summary = None
    error = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                # Validate file format
                if not (uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.csv')):
                    raise ValueError("Unsupported file type. Please upload a .xlsx or .csv file.")

                # Generate the summary report from the uploaded file
                summary = handle_uploaded_file(uploaded_file)

                # Save file info and summary to the database
                UploadedFile.objects.create(
                    file_name=uploaded_file.name,
                    summary=summary,
                )

                # Send email with the summary
                send_mail(
                    subject=f"Python Assignment - Ishan Kumar Gupta",  # Set the subject
                    message=summary,  # Email body with the generated summary
                    from_email=settings.DEFAULT_FROM_EMAIL,  # Sender email
                    recipient_list=['tech@themedius.ai'],  # Recipient email
                    fail_silently=False,
                )

            except Exception as e:
                error = f"Error processing file: {str(e)}"

    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form, 'summary': summary, 'error': error})
