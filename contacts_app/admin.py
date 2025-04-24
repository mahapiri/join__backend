from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ValidationError
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Contact

# Register your models here.# Custom UserCreationForm mit Pflicht für first_name und last_name
class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

# Custom UserChangeForm mit Validierung
class MyUserChangeForm(UserChangeForm):
    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            raise ValidationError("First name is required.")
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]

# Angepasster UserAdmin
class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    # Diese Felder erscheinen beim "Benutzer hinzufügen"
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(Contact)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)