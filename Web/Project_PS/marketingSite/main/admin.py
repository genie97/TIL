from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form=UserCreationForm

    list_display = ('email', 'is_active', 'date_joined')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'feilds':('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email')
    ordering = ('-date_joined',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
