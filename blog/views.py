from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_page(request):
    return HttpResponse('this is main page\r\n\r\nTEST OK!!\r\n\r\nCOMING SOON')


def forbid_zhihu(request):
    return render(request, 'forbidden_zhihu.html')