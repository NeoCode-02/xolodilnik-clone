from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, View

from users.forms import LoginForm, ProfileUpdateForm, RegisterForm
from users.models import User


class RegisterUserView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login-template")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterForm()

        return context

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")

        if email and User.objects.filter(email=email).exists():
            self.add_error("email", "Email already exists")
            return self.form_invalid(form)

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")
            return self.form_invalid(form)

        return super().form_valid(form)


class LoginUserView(FormView):
    template_name = "auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid email or password")  # Non-field error
            return self.form_invalid(form)


class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy("home"))


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "auth/profile.html"
    success_url = reverse_lazy("profile-template")

    def get_object(self, queryset=None):
        return self.request.user
