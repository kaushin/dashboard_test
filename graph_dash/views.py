from django.shortcuts import render
from django.http import HttpResponse

from .models import TestResult
import datetime
import json
# Create your views here.
def index(request):
    results = TestResult.objects.all()
    test_dict = {}
    for i in results:
        if i.result == True:
            try:
                test_dict[i.date.strftime('%m/%d/%Y')] += 1
            except KeyError:
                test_dict[i.date.strftime('%m/%d/%Y')] = 1

    lst= [(k,v) for k, v in test_dict.items()]
    lst.sort(key= lambda x : x[0])

    dates = [x[0] for x in lst]
    values = [x[1] for x in lst]
    print(lst)

    return render(request, 'graph_dash/index.html', context={'data':results , 'line_data':dates, 'counts':values })
