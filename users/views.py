from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'账号创建成功！欢迎 {username}')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
