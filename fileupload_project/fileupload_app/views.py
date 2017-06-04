from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Document,Teacher
from .forms import DocumentForm
import csv,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def list(request):
    if request.method == 'POST':
        #Check if the form is valid then 
        #save the documentform file in the document model
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            csvimport(newdoc.docfile)

            #Redirect to list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        #If there are any documents already uploaded then show them and show them the form
        form = DocumentForm()
    documents = Document.objects.all()
    return render( 
        request,
        'list.html',
        {'form':form,
        'documents':documents}
    )

def csvimport(file):
    fpath = file.url
    #THIS IS DONE BECAUSE file.url gives a 
    #path which has forward slashes
    #and system I am using is windows
    #and it's directory uses backward slash

    fpath = fpath.replace('/','\\')
    #REMOVE ABOVE LINE IF YOU ARE WORKING IN LINUX

    path = BASE_DIR + fpath
    f = open(path,'rt')
    reader = csv.reader(f)
    for row in reader:
        _, created = Teacher.objects.get_or_create(
        first_name=row[0],
        last_name=row[1],
        middle_name=row[2],
        )
