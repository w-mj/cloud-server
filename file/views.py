from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse
import os


def big_file_download(request, path):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, "rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
        return None

    base_path = '/home/wmj/'
    the_file_name = base_path + path
    try:
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Length'] = os.path.getsize(the_file_name)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(path)
        return response
    except FileNotFoundError:
        return HttpResponse("文件不存在")
