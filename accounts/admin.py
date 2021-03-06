from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserAdminCreationForm, UserAdminChangeForm

# Register your models here.


User = get_user_model()



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin','Agent')
    list_filter = ('status','admin', 'Agent','is_active')
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password','status','profile_pic')}),
        ('Full name', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'Agent','staff', 'is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','status','profile_pic')}
        ),
        ('Permissions', {'fields': ('admin', 'Agent','staff', 'is_active',)}),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
=======

# Register your models here.
>>>>>>> de971c457c57b32399128ec0900d27bd168bb331
