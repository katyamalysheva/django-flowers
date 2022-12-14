from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Lot, LotsReview, SellerReview, Deal

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'user_type']
    fieldsets = (
        (('User'), {'fields': ('username', 'email','is_staff', 'user_type')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Lot)
admin.site.register(LotsReview)
admin.site.register(SellerReview)
admin.site.register(Deal)
