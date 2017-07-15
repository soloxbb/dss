from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect 

from .models import Consequence, MissingInfo, Likelihood, Severity, ManualComments, ManualAddInfo

from django.utils import timezone

from .forms import ManuallyAcceptForm, AddingDataForm

def index(request):
    consequence_list = Consequence.objects.all()
    context = {'consequence_list': consequence_list}
    return render(request, 'results/index.html', context)


def consequencelist(request):   
    consequence_list = Consequence.objects.all()
    context = {'consequence_list': consequence_list}
    return render(request, 'results/consequencelist.html', context) 


def mitigationindex(request):   
    consequence_list = Consequence.objects.all()
    context = {'consequence_list': consequence_list}
    return render(request, 'results/mitigationindex.html', context) 


def mitigation(request, consequence_id):   
    consequence = get_object_or_404(Consequence, pk=consequence_id)
    context = {'consequence': consequence}
    return render(request, 'results/mitigation.html', context) 


def detail(request, consequence_id):   
    consequence = get_object_or_404(Consequence, pk=consequence_id)
    context = {'consequence': consequence}
    return render(request, 'results/detail.html', context) 


def context(request, consequence_id):    
    consequence = get_object_or_404(Consequence, pk=consequence_id)
    context = {'consequence': consequence}
    return render(request, 'results/context.html', context) 


def missingdetail(request, missinginfo_id):
    missinginfo = get_object_or_404(MissingInfo, pk=missinginfo_id)
    context = {'missinginfo': missinginfo}
    return render(request, 'results/missingdetail.html', context)  


def manuallyaccept(request, missinginfo_id):
    missingData = get_object_or_404(MissingInfo, pk=missinginfo_id)
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ManuallyAcceptForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): #processing
            # update ManualComments in Database 
            formcontent = form.cleaned_data
            for q in Consequence.objects.all():
                c = q.missinginfo_set.filter(missinginfo_text=missingData)
                # add manual comment, delete missing info
                if c:
                    print(c)
                    q.manualcomments_set.create(missinginfo_id = missinginfo_id, missinginfo_text=missingData, comments_text=formcontent['comments'], operator=formcontent['operator'], email=formcontent['email'], mod_date=timezone.now())
                    q.save()                    
                    # remove MissingInfo in Database
                    c.delete()
                    print (q)             
            #print(formcontent['comments']) 
            
            # redirect to a new URL:
            return HttpResponseRedirect('/results/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ManuallyAcceptForm()
 
    return render(request, 'results/manuallyaccept.html', {'form': form, 'missinginfo': missingData, 'method':request.method})



# to check the detail of manually accepted comments
def manualcommentsdetail(request, missinginfo_id):
    manualcomments = get_object_or_404(ManualComments, pk=missinginfo_id)
    context = {'manualcomments': manualcomments}
    return render(request, 'results/manualcommentsdetail.html', context) 


def addingdata(request, missinginfo_id):
    missingData = get_object_or_404(MissingInfo, pk=missinginfo_id) 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddingDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): 
            # update ManualAddInfo in Database 
            formcontent = form.cleaned_data
            for q in Consequence.objects.all():
                c = q.missinginfo_set.filter(missinginfo_text=missingData)
                # add manual comment, delete missing info
                if c:
                    print(c)
                    q.manualaddinfo_set.create(missinginfo_id = missinginfo_id, missinginfo_text=missingData, data=formcontent['data'], operator=formcontent['operator'], email=formcontent['email'], mod_date=timezone.now())
                    q.save()                    
                    # remove MissingInfo in Database
                    c.delete()
                    print (q)             
            # redirect to a new URL:
            return HttpResponseRedirect('/results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddingDataForm()
 
    return render(request, 'results/addingdata.html', {'form': form, 'missinginfo': missingData})
 

# to check the details of manually added missing data
def manualaddeddetail(request, missinginfo_id):
    print(missinginfo_id)
    manualaddeddata = get_object_or_404(ManualAddInfo, pk=missinginfo_id)
    context = {'manualaddeddata': manualaddeddata}
    return render(request, 'results/manualaddeddetail.html', context)  

