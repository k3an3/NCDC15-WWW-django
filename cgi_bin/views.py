from django.shortcuts import render, get_object_or_404
from cgi_bin.models import BankAccount, Transaction


def index(request):
    return render(request, 'cgi_bin/index.html')

def bottom(request):
    return render(request, 'cgi_bin/bottom.html')

def bottom2(request):
    return render(request, 'cgi_bin/bottom2.html')

def branches(request):
    return render(request, 'cgi_bin/branches.html')

def account(request):
    balance = get_object_or_404(BankAccount, user=request.user)
    return render(request, 'cgi_bin/welcome.html', {'question': question})
