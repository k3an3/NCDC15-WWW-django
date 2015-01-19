from django.shortcuts import render, get_object_or_404
from cgi_bin.models import BankUser, Transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def index(request):
    return render(request, 'cgi_bin/index.html')

def bottom(request):
    return render(request, 'cgi_bin/bottom.html')

def bottom2(request):
    return render(request, 'cgi_bin/bottom2.html')

def branches(request):
    return render(request, 'cgi_bin/branches.html')

def landing(request):
    return render(request, 'cgi_bin/welcome.html')

def make_payment(request):
    if request.user.is_authenticated():
        user = request.user.bankuser
        if request.REQUEST['other_party'] and request.REQUEST['amount']:
            dest_user = get_object_or_404(User, username=request.REQUEST['other_party'])
            amount = int(request.REQUEST['amount'])
            if dest_user:
                if user.balance - amount >= 0:
                    user.balance -= amount
                    dest_user.bankuser.balance += amount
                    user.save()
                    dest_user.bankuser.save()
                    return HttpResponse(dest_user.bankuser.balance)
                else:
                    return HttpResponse("You do not have enough money to complete this transfer.")
            else:
                return HttpResponse("The target user was not found.")
        return HttpResponse("Losing")
       # request.user.save()
        #return HttpResponseRedirect(reverse('issues:detail', args=(issue.id,)))
    else:
        return HttpResponse("You are not logged in.")
