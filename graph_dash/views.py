from django.shortcuts import render
from django.http import HttpResponse

from .models import TestResult

# Create your views here.
def index(request):
    results = TestResult.objects.all()
    nums = [10,11,12,13,14,15]
    return render(request, 'graph_dash/index.html', context={'data':results , 'line_data':nums })
