from email.mime import image
from importlib.resources import path
from django.shortcuts import render
from django.http import HttpResponse
from .certEngine import CertificatePrintingEngine
from django.core.files.storage import FileSystemStorage
import os


# Create your views here.

def form(request):
    return render(request, 'Calculator.html')

def calc(request):
    n1 = int(request.GET["num1"])
    n2 = int(request.GET["num2"])
    res = n1+n2
    return render(request, 'result.html', {'Result': res})

def formCert(request):
    return render(request, 'CertifiacteForm.html')

def returnCert(request):
    first = request.GET["first"]
    last = request.GET["last"]
    date = request.GET["date"]
    inFile = request.GET["inFile"]
    xtext = int(request.GET["xtext"])
    ytext = int(request.GET["ytext"])
    xdate = int(request.GET["xdate"])
    ydate = int(request.GET["ydate"])
    tFont  = request.GET["tFont"]
    sizeText = int(request.GET["sizeText"])
    dFont  = request.GET["dFont"]
    sizeDate = int(request.GET["sizeDate"])
    RED = int(request.GET["RED"])
    GREEN = int(request.GET["GREEN"])
    BLUE = int(request.GET["BLUE"])

    cpe = CertificatePrintingEngine()
    name = cpe.setName(first,last)
    cpe.setInputFile(inFile)
    cpe.setTextColor(RED,GREEN,BLUE)
    cpe.setTextFont(tFont,sizeText)
    cpe.setTextPosition(xtext,ytext)
    cpe.setDatePosition(xdate,ydate)
    cpe.setDateFont(dFont,sizeDate)
    outFile = cpe.setOutputFile(name,date)
    cwd= print(os.getcwd())
    cpe.Print(name,str(date),outFile)
    return render(request, 'Output.html', {'Result': outFile})

    
def printCert(request):
    if request.method == 'POST' and request.FILES['inFile']:
        myfile = request.FILES['inFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        first = request.POST["first"]
        last = request.POST["last"]
        date = request.POST["date"]
        xtext = int(request.POST["xtext"])
        ytext = int(request.POST["ytext"])
        xdate = int(request.POST["xdate"])
        ydate = int(request.POST["ydate"])
        tFont  = request.POST["tFont"]
        sizeText = int(request.POST["sizeText"])
        dFont  = request.POST["dFont"]
        sizeDate = int(request.POST["sizeDate"])
        color = request.POST['textcolor']
        # RED = int(request.POST["RED"])
        # GREEN = int(request.POST["GREEN"])
        # BLUE = int(request.POST["BLUE"])

        cpe = CertificatePrintingEngine()
        name = cpe.setName(first,last)
        cpe.setInputFile(myfile)
        cpe.setTextColor(color)
        cpe.setTextFont(tFont,sizeText)
        cpe.setTextPosition(xtext,ytext)
        cpe.setDatePosition(xdate,ydate)
        cpe.setDateFont(dFont,sizeDate)
        outFile = cpe.setOutputFile(name,date)
        cpe.Print(name,str(date),outFile)
        uploaded_file_url = fs.url(outFile)
        return render(request, 'PrintCertificate.html', {
            'Outfile': uploaded_file_url
        })

    return render(request, 'PrintCertificate.html')



