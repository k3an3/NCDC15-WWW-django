from django.shortcuts import render
from cgi_bin.models import BankAccount, Transaction


def index(request):
    return render(request, 'cgi_bin/index.html')
def bottom(request):
    return render(request, 'cgi_bin/bottom.html')
