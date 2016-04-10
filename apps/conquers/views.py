from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, ActivityForm
from .models import UserProfile, Activity

from django.http import HttpResponse


def valida(username):
    u = User.objects.get(username=username)
    up = UserProfile.objects.get(nickname=u)
    if up.type_user == 2:
        usu = 1
        return usu
    else:
        usu = 2
        return usu


def index(request):
    username = request.user.username
    if username == '':
        return render(request, 'conquers/index.html')
    else:
        usu = valida(username)
        print(usu)
        return render(request, 'conquers/index.html', {'tipo':usu })


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.nickname = user
            profile.save()
            registered = True

            return redirect('conquers:index')
        else:
            print("hay error")

    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'conquers/admin/registro.html', {'user': user_form,
                                                         'profile': profile_form, 'registrado': registered})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return redirect('conquers:index')
            else:
                return HttpResponse("tu cuenta esta desactivada")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("login invalido")
    else:
        return render(request, 'conquers/admin/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('conquers:index')


@login_required()
def envio_actividad(request):
    if request.method == 'POST':
        acty_form = ActivityForm(request.POST, request.FILES)
        if acty_form.is_valid():
            acty_form.save()

            return redirect('conquers:index')
        else:
            print("hay error")

    else:
        acty_form = ActivityForm()
    return render(request, 'conquers/admin/actividad.html', {'form':acty_form})