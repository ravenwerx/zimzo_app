from django.shortcuts import render
from zimzo_app import forms
from .models import BusinessModel
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'zimzo_app/index.html')


@login_required
def add_business(request):
    form = forms.BusinessModelForm()

    if request.method == 'POST':
        form = forms.BusinessModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.BusinessModelForm()

    return render(request, 'zimzo_app/add_business.html', {'form': form})


def list_business(request):
    business = BusinessModel.objects.order_by('business_name')
    business_dict = {'business_info': business}
    return render(request, 'zimzo_app/list_business.html', context=business_dict)


def user_login(request):
    return render(request, 'zimzo_app/user_login.html')
