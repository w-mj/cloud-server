import hashlib
from django.http import HttpResponse
from .secret import secret

def checksignature(request):
    if request.method != 'GET':
        return HttpResponse('only get method is available for check signature')
    # print(request.GET)
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    echostr = request.GET.get('echostr')
    nonce = request.GET.get('nonce')
    if signature and timestamp and echostr:
        l = [secret['check_signature_token'], nonce, timestamp]
        l.sort()
        s = ''.join(l)
        s = hashlib.sha1(s.encode('utf-8')).hexdigest()
        print(s)
        if s == signature:
            return HttpResponse(echostr)
    return HttpResponse('Fail')
