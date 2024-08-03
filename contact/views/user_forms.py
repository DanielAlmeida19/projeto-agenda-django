from django.shortcuts import render, redirect  # type: ignore
from contact.forms import RegisterForm  # type: ignore
from django.contrib import messages  # type: ignore


def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
