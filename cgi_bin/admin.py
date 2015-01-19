from django.contrib import admin
from cgi_bin.models import BankUser, Transaction

admin.site.register(BankUser)
admin.site.register(Transaction)
