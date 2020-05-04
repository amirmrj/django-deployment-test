from django.shortcuts import render
#from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import MyForm
# Create your views here.

def index(whatever):
    return render(whatever, 'AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)

def myform_view(request):
    if request.method != 'POST':
        form = MyForm()
    else:
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request) # baret migardune be homepage
    return render(request, 'AppTwo/myform.html', {'form':form})
