from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}), label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Confirm Password",
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if email and User.objects.filter(email=email).exists():
            self.add_error("email", "Email already exists")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")

        return cleaned_data

    def save(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user = User.objects._create_user(email=email, password=password)
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}), label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password and not User.objects.filter(email=email).exists():
            self.add_error("email", "User does not exist")

        return cleaned_data


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "avatar"]

    def __init__(self, *args, **kwargs):
        user_instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)
        if user_instance:
            self.fields["first_name"].initial = user_instance.first_name
            self.fields["last_name"].initial = user_instance.last_name
            self.fields["phone_number"].initial = user_instance.phone_number
            self.fields["avatar"].initial = user_instance.avatar
