from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CandidateForm, EligibleIdForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .filters import CandidateFilter

# Create your views here.

def index(request):
    return render(request,"home/index.html")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)

            return redirect ("login")
    context = {'form':form}
    return render(request,"home/register.html", context)

def cin(request):    
    form=EligibleIdForm()
    if request.method == "POST":
        
        eligible_id = request.POST.get('id')
        try:
            ID = EligibleId.objects.get(cin=eligible_id)
            #ID_voted = EligibleId.objects.get(cin=eligible_id,voter_has_voted='True')
            if ID:
                messages.success(request, 'you are eligible to vote')
                
                
            #elif ID_voted:
            #   messages.info(request, 'you have already voted')
              #gd  
        except ObjectDoesNotExist:
            messages.warning(request, 'you are not eligible to vote')
            
              
        
    return render(request, "home/cin.html" )


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request,"home/login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')

def candidates_list(request):
    candidate = Candidate.objects.all()

    myFilter = CandidateFilter(request.GET,queryset=candidate)
    candidate=myFilter.qs
    

    context = {'candidate': candidate, 'myFilter':myFilter}
    return render(request,"home/candidatsVote.html", context)


def dashboard(request):
    candidate = Candidate.objects.all()
    voters = EligibleId.objects.all()
    total_candidates = candidate.count()
    total_voters = voters.count()
    voter_has_voted = EligibleId.objects.filter(voter_has_voted = 'True')
    voting_process = voter_has_voted.count()

    
    context = {'total_candidates':total_candidates, 'total_voters':total_voters, 'voting_process':voting_process}
    return render(request, "home/dashboard.html", context)


def createCandidate(request):
    
    form = CandidateForm()
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/candidates_list')

    context = {'form':form}
    return render(request, "home/candidate_form.html", context)

def update_Candidate(request,pk):
    candidate = Candidate.objects.get(id=pk)
    form = CandidateForm(instance=candidate)
    if request.method == "POST":
        form = CandidateForm(request.POST,instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('/candidates_list')
    context = {'form':form}
    return render(request, "home/candidate_form.html", context)

def delete(request,pk):
    candidate = Candidate.objects.get(id=pk)
    if request.method == "POST":
	    candidate.delete()
	    return redirect('/candidates_list')
    context = {'item': candidate}
    return render(request,"home/delete.html",context)

def vote(request,pknumber):
    candidate = Candidate.objects.get(id=pknumber)
    choice = Vote.objects.get(candidate_vote__votes_counter)
    form = CandidateForm(instance=candidate)
    if request.method == "POST":
        form = CandidateForm(request.POST,instance=candidate)
        candidate.votes_counter+=1
        if form.is_valid():
            form.save()
            e = Vote.objects.filter(eligibleId__voter_has_voted ='True')
        return redirect('/dashboard')
    context = {'item':candidate,} 

    
    




    return render(request, "home/vote.html", context)