from django.shortcuts import render
from .models import Memberships
from django.views.generic import ListView
# Create your views here.
class MembershipSelectView(ListView):
    model = Memberships