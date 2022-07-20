from django.shortcuts import render
from django.http import HttpResponse
from .models import vids
from django.core import serializers
from .forms import uploadvideo  
from moviepy.editor import VideoFileClip
import uuid
from pathlib import Path
from os import remove

def index(request):
    return render(request,'index.html')

def list(request):
    videos = vids.objects.all()
    return HttpResponse(serializers.serialize("json", videos))
    
def show(request):
    videos = vids.objects.all()
    return render(request,'list.html',{"videos":videos}) 

def upload(request):
    if request.method == 'POST':  
        video = uploadvideo(request.POST, request.FILES) 
        if video.is_valid():  
            filename = str(uuid.uuid4())
            extension=Path(request.FILES['file'].name).suffix[1:].lower()
            filesize= request.FILES['file'].size   
            filepath='upload/media/'+filename+'.'+extension
            with open(filepath, 'wb+') as destination:  
                for chunk in request.FILES['file'].chunks():  
                    destination.write(chunk)  
            with VideoFileClip(filepath) as clip:
                filetime=float(clip.duration)
            if filetime>600:
                remove(filepath)
                return render(request,"upload.html",{'form':video,'msg':'Video can\'t be longer than 10 minutes'}) 
            else:
                vids(filename=filename,filesize=filesize,duration=filetime,filetype=extension).save() 
                return render(request,"upload.html",{'form':video,'msg':'File uploaded successfuly!'})  
        return render(request,"upload.html",{'form':video,'msg':''})  
    else:  
        video = uploadvideo()  
        return render(request,"upload.html",{'form':video,'msg':''})  
  
def fee(request):
    if request.GET and request.GET['size'] and request.GET['duration'] and request.GET['type']:
        vtype=request.GET['type']
        try:
            vtime=float(request.GET['duration'])
            vsize=float(request.GET['size'])
        except:
            return HttpResponse("{'error':'The values are expected to be numbers'}", status=403)
        if vtype!= 'mp4' and vtype!= 'mkv':
            return HttpResponse("{'error':'Invalid file type!'}", status=403)
        if 0>vsize or vsize>1000000:
            return HttpResponse("{'error':'Video size cannot be more than 1GB!'}", status=403)
        if 0>vtime or vtime>600000:
            return HttpResponse("{'error':'Video duration cannot be more than 10 minutes!'}", status=403)
        price=0.0
        if vsize<=500000:
            price+=5.0
        else:
            price+=12.5
        if vtime<=370800:
            price+=12.5  
        else:
            price+=20
        return HttpResponse("{'fee':'"+str(price)+"'}")        
    else:
        return HttpResponse("{'error':'Not enough parmeters provided!'}", status=405)
        
