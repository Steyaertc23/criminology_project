from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Criminal, Crime
from .forms import AddCharge, AddMisdomeanor, AddFelon

# Create your views here.
# @login_required(login_url='/login')
def home(request):
    return render(request, 'crimdb/home.html')

# @login_required(login_url='/login')
def search(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        if name:
            # case insensitive
            criminals = Criminal.objects.filter(full_name__icontains=name)

            return render(request, 'crimdb/search.html', {'criminals':criminals})
    return render(request, 'crimdb/search.html',{'criminals':None})

def getMisdomeanorsOnly(criminals):
    misdoms = []
    for criminal in criminals:
        try:
            criminal.crime_set.filter(degree__icontains='fel')
        except Exception():
            misdoms.append(criminal)
    
    return misdoms

def getFelonsOnly(criminals):
    felons = []
    for criminal in criminals:
        try:
            criminal.crime_set.filter(degree__icontains='fel')
            felons.append(criminal)
        except Exception():
            continue



# @login_required(login_url='/login')
def showAllCriminals(request):
    criminals = Criminal.objects.all()

    felons = getFelonsOnly(criminals)
    misdoms=getMisdomeanorsOnly(criminals)

    return render(request, 'crimdb/criminals.html', {'felons':felons, 'misdoms':misdoms})


# @login_required(login_url='/login')
def addFelon(request):
    if request.method == 'POST':
        form = AddFelon(request.POST)

        if form.is_valid():
            first = form.cleaned_data.get('first_name')
            last = form.cleaned_data.get('last_name')
            crime_committed = form.cleaned_data.get('crime_committed')
            class_s = form.cleaned_data.get('class_s')

            criminal = Criminal.objects.create(first_name=first, last_name=last)
            criminal.crime_set.create(class_s=class_s, committed=crime_committed, degree=Crime.Degree.FEL)
            criminal.save()
            return HttpResponseRedirect('/')
        else:
            form = AddFelon()

        return render(request,'crimdb/addCriminal.html', {'form':form})

# @login_required(login_url='/login')
def addMisdomeanor(request):
    if request.method == 'POST':
        form = AddMisdomeanor(request.POST)

        if form.is_valid():
            first = form.cleaned_data.get('first_name')
            last = form.cleaned_data.get('last_name')
            crime_committed = form.cleaned_data.get('crime_committed')
            class_s = form.cleaned_data.get('class_s')

            criminal = Criminal.objects.create(first_name=first, last_name=last)
            criminal.crime_set.create(class_s=class_s, committed=crime_committed, degree=Crime.Degree.MISD)
            criminal.save()
            return HttpResponseRedirect('/')
        else:
            form = AddMisdomeanor()

        return render(request,'crimdb/addCriminal.html', {'form':form})

# @login_required(login_url='/login')
def addCrimeToFelon(request):
    if request.method == 'GET':
        criminals = Criminal.objects.all()
        felons = getFelonsOnly(criminals)
        return render(request, 'crimdb/getCriminals.html', {'criminals':felons})

# @login_required(login_url='/login')
def addCrimeToMisdomeanor(request):
    if request.method == 'GET':
        criminals = Criminal.objects.all()
        misdoms = getMisdomeanorsOnly(criminals)
        return render(request, 'crimdb/getCriminals.html', {'criminals':misdoms})

# @login_required(login_url='/login')
def addMisdom(request, criminal_name:str):
    if request.method == 'POST':
        form = AddCharge(request.POST)
        if form.is_valid():
            crime_committed = form.cleaned_data.get('crime_committed')
            class_s = form.cleaned_data.get('class_s')
            
            criminal:Criminal = Criminal.objects.filter(full_name__icontains=criminal_name)
            criminal.crime_set.create(class_s=class_s, committed=crime_committed, degree=Crime.Degree.MISD)
            criminal.save()
            return HttpResponseRedirect('/')
        else:
            form = AddCharge()
    return render(request, 'crimdb/addCrime.html', {'form':form})

# @login_required(login_url='/login')
def addFelony(request, criminal_name:str):
    if request.method == 'POST':
        form = AddCharge(request.POST)
        if form.is_valid():
            crime_committed = form.cleaned_data.get('crime_committed')
            class_s = form.cleaned_data.get('class_s')

            criminal:Criminal = Criminal.objects.filter(full_name__icontains=criminal_name)
            criminal.crime_set.create(class_s=class_s, committed=crime_committed, degree=Crime.Degree.FEL)
            criminal.save()

            return HttpResponseRedirect('/')
        else:
            form = AddCharge()
    return render(request, 'crimdb/addCrime.html', {'form':form})




# @login_required(login_url='/login')
def showCriminal(request, criminal_name):
    criminal = Criminal.objects.filter(full_name__icontains=criminal_name)

