

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SendMailForm
# Register your models here.
from .models import Contact


# Register your models here.


admin.site.register(Contact)

# 4.189391136169434
# 2.2064855098724365
