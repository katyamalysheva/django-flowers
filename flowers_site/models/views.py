from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser, Lot, LotsReview, SellerReview, Deal
from django.db.models import Count, Sum

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def seller():
    sellers = {}
    seller_list = CustomUser.objects.filter(user_type = 'S')
    for sel in seller_list:
        deals = Deal.objects.filter(lot__in =  Lot.objects.filter(flower_seller = sel)).values('customer').annotate(customer_sum_checks=Sum('total_check')).order_by()
        sellers[sel] = [deals]
    print(sellers)

seller()