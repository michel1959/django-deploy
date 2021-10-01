from django.shortcuts import render
from contact.models import Contact
from .forms import ContactForm
from django.contrib import messages #import messages


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your inquiry. Your contact information and message was successfully submitted.")
            return render(request, 'application/index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request,'application/index.html',context)

