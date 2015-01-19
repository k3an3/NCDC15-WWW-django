from django.shortcuts import render, get_object_or_404
from cgi_bin.models import BankUser, Transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.files import File
from django.contrib.auth import authenticate


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
            if amount > 0:
                if dest_user:
                    if user.balance - amount >= 0:
                        user.balance -= amount
                        user.save()
                        t1 = Transaction(user=user, debit=amount, typeof=dest_user, balance=user.balance)
                        t1.save()
                        dest_user.bankuser.balance += amount
                        dest_user.bankuser.save()
                        t2 = Transaction(user=dest_user.bankuser, credit=amount, typeof=user, balance=dest_user.bankuser.balance)
                        t2.save()
                        return HttpResponseRedirect('../show_user')
                    else:
                        return HttpResponse("You do not have enough money to complete this transfer.")
                else:
                    return HttpResponse("The target user was not found.")
            else:
                return HttpResponse("You cannot request this kind of transfer.")
    else:
        return HttpResponse("You are not logged in.")

def show_user(request):
    transaction_history = Transaction.objects.filter(user=request.user.bankuser).order_by('pk')
    context = {'transaction_history': transaction_history}
    return render(request, 'cgi_bin/show-user.html', context)

def admintoken(request):
    if not request.user.is_authenticated():
        attempt = request.GET['password']
        f = open( '/usr/lib/db/pass_Administrator', 'r' )
        passwd = f.readline().rstrip()
        f.close()
        if passwd == attempt:
            user = authenticate(username='admin', password='admin')
            return HttpResponse("access_token=" + request.COOKIES.get('sessionid'))
        else:
            return HttpResponse("Fail")
    else:
        return HttpResponse("access_token=" + request.COOKIES.get('sessionid'))



