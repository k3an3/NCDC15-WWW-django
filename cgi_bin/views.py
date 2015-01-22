from django.shortcuts import render, get_object_or_404
from cgi_bin.models import BankUser, Transaction, AdminSession
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.files import File
from django.contrib.auth import authenticate
from datetime import datetime


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
        redir = '../show/show-user'
    elif has_admin_token(request) and User.objects.filter(username=request.GET['user_name']).exists():
        user = BankUser.objects.get(user=User.objects.get(username=request.GET['user_name']))
        redir = '../show/show-user?user_name=' + user.user.username
    else:
        return HttpResponseRedirect('../login')
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
                    return HttpResponseRedirect(redir)
                else:
                    return HttpResponse("You do not have enough money to complete this transfer.")
            else:
                return HttpResponse("The target user was not found.")
        else:
            return HttpResponse("You cannot request this kind of transfer.")

def show_user(request):
    if has_admin_token(request) or request.user.is_authenticated():
        if has_admin_token(request) and request.GET['user_name']:
            result = BankUser.objects.get(user=User.objects.get(username=request.GET['user_name']))
        elif request.user.is_authenticated():
            result = request.user.bankuser
        transaction_history = Transaction.objects.filter(user=result).order_by('pk')
        context = {'transaction_history': transaction_history, 'user' : result}
        return render(request, 'cgi_bin/show-user.html', context)
    return HttpResponseRedirect('../login')

# TODO: Only allow the RDP server to connect
def admintoken(request):
    if True: # request.meta['REMOTE_ADDR'] == '192.168.1.4':
        attempt = request.GET['password']
        f = open( '/usr/lib/db/pass_Administrator', 'r' )
        passwd = f.readline().rstrip()
        f.close()
        if passwd == attempt:
            try:
                token = hex(AdminSession.objects.all().reverse()[0].pk + 314758926 * int((datetime.now()-datetime(1970,1,1)).total_seconds()))[2:]
            except IndexError:
                token = hex(314758926 * int((datetime.now()-datetime(1970,1,1)).total_seconds()))[2:]
            session = AdminSession(access_token=token)
            session.save()
            response = HttpResponse()
            response.set_cookie('access_token', token)
            return response
        else:
            return HttpResponse("Wrong!")

def has_admin_token(request):
    try:
        return AdminSession.objects.filter(access_token=request.COOKIES['access_token']).exists()
    except KeyError:
        return False

def find_user(request):
   if has_admin_token(request):
       user = User.objects.get(username=request.GET['user_name'])
       if user:
           return HttpResponse(user.bankuser.balance)
       else:
           return HttpResponse("User not found!")

def create_user(request):
   if has_admin_token(request):
       newuser = User(username=request.POST['name'], password=request.POST['password'])
       newuser.save()
       newbankuser = BankUser(user=newuser)
       newbankuser.save()
       return HttpResponseRedirect("cgi-bin/show/show-user?user_name=" + newuser.username)

def delete_user(request):
   if has_admin_token(request):
       deluser = User(username=request.POST['user_name'])
       if deluser:
           delbankusesr = BankUser(user=deluser)
           delbankuser.delete()
           deluser.delete()
           return HttpResponse("User " + request.POST['user_name'] + " deleted!")
       else:
           return HttpResponse("User " + request.POST['user_name'] + " not found!")

def make_deposit(request):
    if has_admin_token(request) and request.GET['user_name'] and request.GET['amount']:
        user = get_object_or_404(User, username=request.REQUEST['user_name'])
        amount = int(request.GET['amount'])
        if amount > 0:
            user.bankuser.balance += amount
            user.bankuser.save()
            transaction = Transsaction(user=user.bankuser, typeof="Deposit", balance=user.bankuser.balance, credit=amount)
            transaction.save()
            return HttpResponseRedirect("../show/show-user?user_name=" + user.username)

def make_withdrawal(request):
    if has_admin_token(request) and request.GET['user_name'] and request.GET['amount']:
        user = get_object_or_404(User, username=request.REQUEST['user_name'])
        amount = int(request.GET['amount'])
        if amount > 0 and user.bankuser.balance - amount >= 0:
            user.bankuser.balance -= amount
            user.bankuser.save()
            transaction = Transaction(user=user.bankuser, typeof="Withdrawal", balance=user.bankuser.balance, debit=amount)
            transaction.save()
            return HttpResponseRedirect("../show/show-user?user_name=" + user.username)
