from django.contrib import admin
from .models import HostTab,ProjectTab,UserProfile,IDCTab,TaskTab,TaskLogDetailTab,SysTypeTab
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('email', 'name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserProfile
        fields = ('email', 'password', 'name', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserProfileAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('绑定项目组', {'fields': ('project_tab',)}),
        ('Permissions', {'fields': ('is_admin','user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('user_permissions','project_tab')


class HostTabAdmin(admin.ModelAdmin):
    list_display = ('ip_addr','port','login_user','login_pwd','sys_type_tab','project_tab','idc_tab')


class ProjectTabAdmin(admin.ModelAdmin):
    list_display = ('name','pro_type')


class IDCTabAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SysTypeTabAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TaskTabAdmin(admin.ModelAdmin):
    list_display = ('user','pid','host_tab','task_read','status','date')


class TaskLogDetailTabAdmin(admin.ModelAdmin):
    list_display = ('task','result','start_date','end_date')
# Now register the new UserAdmin...
admin.site.register(UserProfile, UserProfileAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
# Register your models here.

admin.site.register(IDCTab,IDCTabAdmin)
admin.site.register(HostTab,HostTabAdmin)
admin.site.register(ProjectTab,ProjectTabAdmin)
admin.site.register(SysTypeTab,SysTypeTabAdmin)
admin.site.register(TaskTab,TaskTabAdmin)
admin.site.register(TaskLogDetailTab,TaskLogDetailTabAdmin)