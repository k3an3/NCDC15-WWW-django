from django.contrib import admin
from cgi_bin.models import BankUser, Transaction, AdminSession

admin.site.register(BankUser)
admin.site.register(Transaction)
admin.site.register(AdminSession)
