from django.shortcuts import render
from storageapp.hashfile import HashFile
from django.http import HttpResponse
import os
import json


def main(request):
    return render(request, "index.html")


def upload(request, url):
    mkdir = ''
    currentdir = os.path.abspath(os.getcwd())
    try:
        hashs = HashFile.sha1(url)
        print('hash', url)
        mkdir = HashFile.save(hashs, url)
        currentdir = os.path.abspath(os.getcwd())
        mkdir = os.path.abspath(currentdir + '/' + mkdir)
        status = True
    except:
        hashs = None
        mkdir = None
        status = False

    data = json.dumps({'status': status, 'file_path': url, 'hash': hashs, 'file_upload_path': mkdir})
    return HttpResponse(data, content_type='application/json')


def download(request, hash):
    currentdir = os.path.abspath(os.getcwd())
    filedir = HashFile.search(hash)
    if filedir != None:
        status = True
        mkdir = os.path.abspath(currentdir + '/' + filedir)
    else:
        status = False
        mkdir = None

    data = json.dumps({'status': status, 'file_download_path': mkdir, 'hash': hash})
    return HttpResponse(data, content_type='application/json')

def delete(request, hash):
    currentdir = os.path.abspath(os.getcwd())
    filedir = HashFile.search(hash)
    if filedir != None:
        status = True
        mkdir = os.path.abspath(currentdir + '/' + filedir)
        os.remove(filedir)
    else:
        status = False
        mkdir = None

    data = json.dumps({'status': status, 'file_delete_url': mkdir, 'hash': hash})
    return HttpResponse(data, content_type='application/json')

def mains(request):
    return render(request, "index.html")
