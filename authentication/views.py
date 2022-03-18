from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render

from . import forms


def signup_page(request):
    form = forms.SignupForm()

    if request.method == "POST":
        form = forms.SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Enregistrement réussi")
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "authentication/signup.html", context={"form": form})


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Vous avez été déconnecté")
        return super().dispatch(request, *args, **kwargs)
