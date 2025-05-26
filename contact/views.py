from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            send_mail(
                'Feedback from Servexpert',
                feedback,
                'calinbantasandrei05@gmail.com',
                ['lordtwigodhimself@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Succes! Mesajul tău a fost trimis.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'main/main.html', {'form': form})