from django.http import HttpResponse,HttpResponseBadRequest
import os
from cloudX.settings import MEDIA_ROOT

def media(request,path=None, file=None):
    if not file:
        return HttpResponseBadRequest('Invalid File Path')

    with open(os.path.join(MEDIA_ROOT,path, file), 'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/doc')
        response['Content-Disposition'] = 'filename=%s' % (file.split('/')[-1])
        return response