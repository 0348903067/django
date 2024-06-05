from django.shortcuts import render  # Import đúng hàm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')


